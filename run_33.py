"""Run training format: /trainings/{training_id}/tasks/{task_id}."""
import json
import re
import time
import traceback
from pathlib import Path

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from api_submit import (
    finish_training,
    start_training,
    submit_answer_training,
    submit_answer_training_code,
    submit_answer_training_drag,
    submit_answer_training_raw,
)
from browser import make_session, refresh_session_from_driver
from config import ANSWER_SIMILARITY_THRESHOLD, BASE_URL, EXCEL_3_3
from excel_loader import load_3_3
from page_parser import get_csrf_from_page, parse_question_page
from similarity import best_match, best_matches_multiple

FORM_SELECTOR = "input[name^='questions[']"
FORM_OR_TASKFORM = "form#taskForm"
FORM_WAIT_MAIN = 2.0


def _is_training_task_already_answered(html: str) -> bool:
    """
    Более строгая проверка solved для training-задач.
    Не используем общий эвристический детектор, чтобы не получать ложные skip.
    """
    if not html:
        return False
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find("form", id="taskForm")
    if not form:
        return False
    # Если есть кнопка "Ответить" внутри формы — задача точно не завершена.
    submit_btn = form.find("button", string=re.compile(r"Ответить"))
    if submit_btn is not None and submit_btn.get("disabled") is None:
        return False
    # Иначе считаем solved только при явных признаках solved-состояния.
    html_low = html.lower()
    if "actions_solved" in html_low or "tasksolved" in html_low or "alreadysolved" in html_low:
        return True
    # Если кнопки "Ответить" в taskForm нет, чаще всего это solved-экран.
    return submit_btn is None


def _extract_training_and_task_from_form_action(html: str) -> tuple[int | None, int | None]:
    """Extract canonical ids from form action /trainings/<id>/tasks/<id>."""
    if not html:
        return None, None
    try:
        soup = BeautifulSoup(html, "html.parser")
        form = soup.find("form", id="taskForm")
        if not form:
            return None, None
        action = (form.get("action") or "").strip()
        m = re.search(r"/trainings/(\d+)/tasks/(\d+)", action)
        if not m:
            return None, None
        return int(m.group(1)), int(m.group(2))
    except Exception:
        return None, None


def _parse_drag_payload(answer_text: str) -> tuple[int | None, list[tuple[int, int]]]:
    """
    Parse drag payload copied from curl in Excel.
    Supports both plain:
      name="questions[1207774][10162110]"
    and escaped-with-caret form:
      name=^\^"questions^[1207774^]^[10162110^]^\^"^
    """
    if not answer_text:
        return None, []
    lines = answer_text.splitlines()
    qid = None
    mappings: list[tuple[int, int]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].replace("^", "")
        m = re.search(r"questions\[(\d+)\]\[(\d+)\]", line)
        if not m:
            i += 1
            continue
        cur_qid = int(m.group(1))
        from_id = int(m.group(2))
        if qid is None:
            qid = cur_qid
        j = i + 1
        to_id = None
        while j < n:
            candidate = lines[j].replace("^", "").strip()
            j += 1
            if not candidate:
                continue
            m_num = re.search(r"^\d+$", candidate)
            if m_num:
                to_id = int(candidate)
            break
        if to_id is not None:
            mappings.append((from_id, to_id))
        i = j
    if qid is None or not mappings:
        return None, []
    return qid, mappings


def _parse_multipart_fields_from_payload(answer_text: str) -> list[tuple[str, str]]:
    """
    Parse generic multipart-like payload copied from curl and return [(field_name, value), ...].
    Supports normal and caret-escaped Windows-curl snippets.
    """
    if not answer_text:
        return []
    lines = [ln.replace("^", "") for ln in answer_text.splitlines()]
    fields: list[tuple[str, str]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = re.search(r'name="([^"]+)"', line)
        if not m:
            i += 1
            continue
        field_name = m.group(1).strip()

        # Move to payload body: after header line and optional blank separators.
        j = i + 1
        while j < n and lines[j].strip() == "":
            j += 1

        # Collect all body lines until multipart boundary.
        value_lines: list[str] = []
        while j < n:
            raw = lines[j]
            stripped = raw.strip()
            if stripped.startswith("------WebKitFormBoundary") or stripped.startswith("--"):
                break
            value_lines.append(raw.rstrip("\r"))
            j += 1

        # Keep exact text body, but trim only trailing empty lines.
        while value_lines and value_lines[-1].strip() == "":
            value_lines.pop()
        value = "\n".join(value_lines)
        fields.append((field_name, value))
        i = j
    return fields


def _get_training_code_ids_from_api(session, training_id, task_id) -> dict | None:
    """Try GET training task API JSON and extract code_question_id and test_case_execution_id."""
    url = f"{BASE_URL}/api/trainings/{training_id}/tasks/{task_id}"
    try:
        resp = session.get(url, headers={"Accept": "application/json"}, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json() if getattr(resp, "json", None) else json.loads(resp.text)
        qid = None
        tceid = None
        if isinstance(data, dict):
            task = data.get("task") or data
            qid = data.get("question_id") or data.get("id") or task.get("question_id")
            tceid = data.get("test_case_execution_id") or task.get("test_case_execution_id")
            if isinstance(task.get("questions"), list):
                for q in task["questions"]:
                    if not isinstance(q, dict):
                        continue
                    if qid is None:
                        qid = q.get("question_id") or q.get("id")
                    if tceid is None:
                        tceid = q.get("test_case_execution_id")
            if tceid is None and isinstance(data.get("test_case_executions"), list) and data["test_case_executions"]:
                first = data["test_case_executions"][0]
                tceid = first.get("id") if isinstance(first, dict) else first
        if qid is None:
            return None
        return {
            "code_question_id": int(qid) if not isinstance(qid, int) else qid,
            "test_case_execution_id": str(tceid) if tceid is not None else None,
        }
    except Exception:
        return None


def _get_page_html(driver: WebDriver, page_url: str) -> tuple[str | None, bool]:
    """Load page, wait for form or detect already-answered. Returns (html, already_answered)."""
    try:
        driver.set_page_load_timeout(20)
        driver.get(page_url)
        try:
            html = driver.page_source
            if _is_training_task_already_answered(html):
                return (None, True)
        except Exception:
            pass

        def form_or_solved(d):
            try:
                d.find_element(By.CSS_SELECTOR, FORM_SELECTOR)
                return True
            except Exception:
                pass
            try:
                d.find_element(By.CSS_SELECTOR, FORM_OR_TASKFORM)
                return True
            except Exception:
                pass
            try:
                if _is_training_task_already_answered(d.page_source):
                    return True
            except Exception:
                pass
            return False

        try:
            WebDriverWait(driver, FORM_WAIT_MAIN).until(form_or_solved)
        except Exception:
            pass
        page_html = driver.page_source
        if not page_html:
            return (None, False)
        try:
            if _is_training_task_already_answered(page_html):
                return (None, True)
        except Exception:
            pass
        return (page_html, False)
    except Exception:
        return (None, False)
    finally:
        try:
            driver.switch_to.default_content()
            driver.set_page_load_timeout(300)
        except Exception:
            pass


def run_3_3(driver: WebDriver) -> None:
    path = Path(EXCEL_3_3)
    if not path.exists():
        print(f"[3.3] File not found: {path} (place test3.xlsx next to the script/exe)")
        return
    data = load_3_3(path)
    if not data:
        print(f"[3.3] No data in {EXCEL_3_3} (expect 3 columns: training_id, task_id, answer)")
        return

    for training_id, rows in data.items():
        if not rows:
            continue
        print(f"[3.3] Training {training_id}: submitting {len(rows)} answers")
        try:
            session = make_session(driver)
        except Exception:
            traceback.print_exc()
            continue

        # Start training before submitting attempts (per requirements curl)
        try:
            training_page_url = f"{BASE_URL}/trainings/{training_id}"
            page_html, already_answered = _get_page_html(driver, training_page_url)
            if page_html:
                refresh_session_from_driver(driver, session)
                page_csrf = get_csrf_from_page(page_html)
                if page_csrf:
                    session.headers["X-CSRF-Token"] = page_csrf
            start_resp = start_training(session, training_id)
            if start_resp.status_code in (200, 201, 204):
                preview = (start_resp.text or "")[:200].replace("\n", " ")
                print(f"[3.3] Start training={training_id} -> {start_resp.status_code} {preview}")
            else:
                body = (start_resp.text or (start_resp.content.decode(errors="replace") if start_resp.content else ""))[:500]
                print(f"[3.3] Start training={training_id} -> err {start_resp.status_code}: {body}")
        except Exception:
            print(f"[3.3] Start training {training_id} failed:")
            traceback.print_exc()

        for task_id, answer in rows:
            print(f"[3.3] Task {task_id} ...", flush=True)
            page_url = f"{BASE_URL}/trainings/{training_id}/tasks/{task_id}"
            page_html, already_answered = _get_page_html(driver, page_url)
            if already_answered:
                print(f"[3.3] Task {task_id} already answered, skip.")
                continue
            if not page_html:
                print(f"[3.3] Could not load page for task {task_id}")
                continue

            refresh_session_from_driver(driver, session)
            page_csrf = get_csrf_from_page(page_html)
            if page_csrf:
                session.headers["X-CSRF-Token"] = page_csrf

            actual_training_id, actual_task_id = _extract_training_and_task_from_form_action(page_html)
            submit_training_id = actual_training_id if actual_training_id is not None else training_id
            submit_task_id = actual_task_id if actual_task_id is not None else task_id
            if str(submit_training_id) != str(training_id) or str(submit_task_id) != str(task_id):
                print(
                    f"[3.3] Task {task_id}: canonical ids from page "
                    f"training={submit_training_id}, task={submit_task_id}"
                )

            parsed = parse_question_page(page_html)
            form_key = parsed.get("question_form_key")

            # Универсальный обходной путь: если в Excel в ответе лежит payload (curl multipart),
            # отправляем его как есть (подходит для text/radio/drag/code-like полей).
            raw_fields = _parse_multipart_fields_from_payload(str(answer))
            if raw_fields:
                try:
                    resp = submit_answer_training_raw(
                        session,
                        submit_training_id,
                        submit_task_id,
                        raw_fields,
                    )
                except Exception:
                    print(f"[3.3] Submit task {task_id} with raw payload failed:")
                    traceback.print_exc()
                    continue
                if resp.status_code in (200, 201, 204):
                    preview = (resp.text or "")[:200].replace("\n", " ")
                    print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> {resp.status_code} {preview}")
                else:
                    body = (resp.text or (resp.content.decode(errors="replace") if resp.content else ""))[:500]
                    print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> err {resp.status_code}: {body}")
                time.sleep(0.2)
                continue

            # Drag-and-drop in trainings: use explicit payload from Excel.
            if parsed.get("is_drag"):
                drag_qid, drag_mappings = _parse_drag_payload(str(answer))
                if drag_qid is None or not drag_mappings:
                    print(f"[3.3] Drag task {task_id}: payload not found in Excel answer, skip.")
                    continue
                try:
                    resp = submit_answer_training_drag(
                        session,
                        submit_training_id,
                        submit_task_id,
                        drag_qid,
                        drag_mappings,
                    )
                except Exception:
                    print(f"[3.3] Submit drag task {task_id} failed:")
                    traceback.print_exc()
                    continue
                if resp.status_code in (200, 201, 204):
                    preview = (resp.text or "")[:200].replace("\n", " ")
                    print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> {resp.status_code} {preview}")
                else:
                    body = (resp.text or (resp.content.decode(errors="replace") if resp.content else ""))[:500]
                    print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> err {resp.status_code}: {body}")
                time.sleep(0.2)
                continue

            if not form_key and parsed.get("is_code"):
                ids = _get_training_code_ids_from_api(session, submit_training_id, submit_task_id)
                if ids:
                    parsed["code_question_id"] = ids.get("code_question_id")
                    parsed["test_case_execution_id"] = ids.get("test_case_execution_id")
                    parsed["is_code"] = True

            if parsed.get("is_code"):
                code_id = parsed.get("code_question_id")
                if not code_id:
                    print(f"[3.3] Code task {task_id}: missing code question id, skip.")
                    continue
                source_code = str(answer or "").strip()
                if not source_code:
                    print(f"[3.3] Code task {task_id}: empty code in Excel, skip.")
                    continue
                try:
                    resp = submit_answer_training_code(
                        session,
                        submit_training_id,
                        submit_task_id,
                        code_id,
                        language="python3",
                        source_code=source_code,
                        test_case_execution_id=parsed.get("test_case_execution_id"),
                    )
                except Exception:
                    print(f"[3.3] Submit code task {task_id} failed:")
                    traceback.print_exc()
                    continue
            else:
                if not form_key:
                    print(f"[3.3] Could not find form question key for task {task_id}")
                    continue
                if parsed.get("is_text_input"):
                    answer_value = str(answer).strip() if answer is not None else ""
                elif parsed.get("is_multiple_choice"):
                    options = parsed.get("options") or []
                    answer_values = best_matches_multiple(
                        answer, options, threshold=ANSWER_SIMILARITY_THRESHOLD
                    )
                    if not answer_values:
                        print(f"[3.3] No matching option(s) for answer '{answer}' (task {task_id}), skip.")
                        continue
                    # trainings multiple choice uses repeated key like lessons
                    try:
                        files = [(form_key, (None, str(v))) for v in answer_values]
                        url = f"{BASE_URL}/api/trainings/{submit_training_id}/tasks/{submit_task_id}/answer_attempts"
                        resp = session.post(url, files=files)
                    except Exception:
                        print(f"[3.3] Submit task {task_id} failed:")
                        traceback.print_exc()
                        continue
                else:
                    options = parsed.get("options") or []
                    answer_value = best_match(answer, options, threshold=ANSWER_SIMILARITY_THRESHOLD)
                    if answer_value is None:
                        print(f"[3.3] No matching option for answer '{answer}' (task {task_id}), skip.")
                        continue
                    try:
                        resp = submit_answer_training(
                            session, submit_training_id, submit_task_id, form_key, answer_value
                        )
                    except Exception:
                        print(f"[3.3] Submit task {task_id} failed:")
                        traceback.print_exc()
                        continue

            if resp.status_code in (200, 201, 204):
                preview = (resp.text or "")[:200].replace("\n", " ")
                print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> {resp.status_code} {preview}")
            else:
                body = (resp.text or (resp.content.decode(errors="replace") if resp.content else ""))[:500]
                print(f"[3.3] Submit training={submit_training_id} task={submit_task_id} -> err {resp.status_code}: {body}")

            time.sleep(0.2)

        try:
            finish_resp = finish_training(session, training_id)
            if finish_resp.status_code in (200, 201, 204):
                preview = (finish_resp.text or "")[:200].replace("\n", " ")
                print(f"[3.3] Finish training={training_id} -> {finish_resp.status_code} {preview}")
            else:
                body = (finish_resp.text or (finish_resp.content.decode(errors="replace") if finish_resp.content else ""))[:500]
                print(f"[3.3] Finish training={training_id} -> err {finish_resp.status_code}: {body}")
        except Exception:
            print(f"[3.3] Finish training {training_id} failed:")
            traceback.print_exc()
