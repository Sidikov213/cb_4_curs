"""Run format 3.2: lessons. Submit each answer via API (no video). Load question page in browser to get form HTML."""
import json
import time
import traceback
from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from api_submit import (
    submit_answer_3_2,
    submit_answer_3_2_code,
    submit_answer_3_2_multiple,
    submit_answer_3_2_drag,
    submit_code_test_execution,
)
from browser import make_session, refresh_session_from_driver
from config import BASE_URL, EXCEL_3_2, ANSWER_SIMILARITY_THRESHOLD
from excel_loader import load_3_2
from page_parser import get_csrf_from_page, is_task_already_answered, parse_question_page
from similarity import best_match, best_matches_multiple
import re

FORM_SELECTOR = "input[name^='questions[']"
# Code task pages use form#taskForm and CodeMirror, no standard input initially
FORM_OR_TASKFORM = "form#taskForm"
FORM_WAIT_MAIN = 1.8

_JS_GET_CODE_IDS = """
var inputs = document.querySelectorAll('input[name*="questions["]');
var result = { code_question_id: null, test_case_execution_id: null };
for (var i = 0; i < inputs.length; i++) {
  var n = inputs[i].name || '';
  var v = inputs[i].value || '';
  if (n.indexOf('][][') !== -1) {
    var match = n.match(/questions\\[(\\d+)\\]/);
    if (match) result.code_question_id = parseInt(match[1], 10);
    if (n.indexOf('test_case_execution_id') !== -1) result.test_case_execution_id = v;
  }
}
return result;
"""


def _normalize_answer(answer) -> str:
    """
    Нормализует ответ из Excel.

    Для drag-and-drop типа (3.2) ответы записаны в формате:
      [item] -> [item]
    по одному соответствию на строку.
    Нам оттуда важна правая часть (то, что реально «выбрано»),
    поэтому превращаем такой текст в список правых элементов,
    разделённых переводами строк.
    Для остальных случаев возвращаем строку как есть.
    """
    if answer is None:
        return ""
    text = str(answer)
    if "->" not in text:
        return text
    lines = []
    for raw_line in str(text).splitlines():
        if "->" not in raw_line:
            continue
        left, right = raw_line.split("->", 1)
        right = right.strip()
        # убираем возможные квадратные скобки вокруг элемента
        if right.startswith("[") and right.endswith("]"):
            right = right[1:-1].strip()
        if right:
            lines.append(right)
    # если в итоге ничего не разобрали — вернём исходный текст,
    # чтобы не ломать поведение в неожиданных форматах
    return "\n".join(lines) if lines else text


def _parse_drag_payload(answer_text: str) -> tuple[int | None, list[tuple[int, int]]]:
    """
    Разбирает текст из Excel, если он содержит payload в стиле curl для drag-and-drop.

    Ищет блоки вида:
      Content-Disposition: form-data; name="questions[1207774][10162110]"

    <пустые строки>
    10162111

    Возвращает (question_id, [(from_id, to_id), ...]).
    Если ничего похожего не найдено — (None, []).
    """
    if not answer_text:
        return None, []
    lines = answer_text.splitlines()
    pattern = re.compile(r'name="questions\[(\d+)\]\[(\d+)\]"')
    question_id: int | None = None
    mappings: list[tuple[int, int]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = pattern.search(line)
        if not m:
            i += 1
            continue
        qid = int(m.group(1))
        from_id = int(m.group(2))
        if question_id is None:
            question_id = qid
        # Пропускаем до первой непустой строки с числом — это to_id
        j = i + 1
        to_id: int | None = None
        while j < n:
            val_line = lines[j].strip()
            j += 1
            if not val_line:
                continue
            if val_line.isdigit():
                to_id = int(val_line)
            break
        if to_id is not None:
            mappings.append((from_id, to_id))
        i = j
    if question_id is None or not mappings:
        return None, []
    return question_id, mappings


def _get_code_ids_from_browser(driver: WebDriver) -> dict | None:
    """Run in page context: find code task hidden inputs, return code_question_id and test_case_execution_id."""
    try:
        r = driver.execute_script(_JS_GET_CODE_IDS)
        if r and r.get("code_question_id") and r.get("test_case_execution_id"):
            return r
        if r and r.get("code_question_id"):
            return r
        return None
    except Exception:
        return None


def _get_code_ids_from_api(session, lesson_id, task_id) -> dict | None:
    """Try GET task API JSON and extract code_question_id and test_case_execution_id."""
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}"
    try:
        resp = session.get(url, headers={"Accept": "application/json"}, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json() if getattr(resp, "json", None) else json.loads(resp.text)
        qid = None
        tceid = None
        if isinstance(data, dict):
            task = data.get("task") or data
            qid = data.get("question_id") or data.get("id") or task.get("question_id") or task.get("id")
            tceid = data.get("test_case_execution_id") or task.get("test_case_execution_id")
            if not tceid and isinstance(data.get("test_case_executions"), list) and data["test_case_executions"]:
                tceid = data["test_case_executions"][0].get("id") if isinstance(data["test_case_executions"][0], dict) else data["test_case_executions"][0]
            if (qid is None or tceid is None) and isinstance(task.get("questions"), list):
                for q in task["questions"]:
                    if isinstance(q, dict) and (q.get("test_case_execution_id") or q.get("id")):
                        if qid is None:
                            qid = q.get("question_id") or q.get("id") or qid
                        if tceid is None:
                            tceid = q.get("test_case_execution_id") or q.get("id")
                        break
        if qid is not None:
            return {
                "code_question_id": int(qid) if not isinstance(qid, int) else qid,
                "test_case_execution_id": str(tceid) if tceid is not None else None,
            }
        return None
    except Exception:
        return None


def _get_page_html(driver: WebDriver, page_url: str) -> tuple[str | None, bool]:
    """Load page, wait for form or detect already-answered. Returns (html, already_answered)."""
    try:
        driver.set_page_load_timeout(20)
        driver.get(page_url)
        # Quick check: already answered -> skip
        try:
            html = driver.page_source
            if is_task_already_answered(html):
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
                if is_task_already_answered(d.page_source):
                    return True
            except Exception:
                pass
            return False

        try:
            WebDriverWait(driver, FORM_WAIT_MAIN).until(form_or_solved)
        except Exception:
            pass
        page_html = driver.page_source
        # If we timed out but HTML has form, use it anyway and try to submit
        if not page_html:
            return (None, False)
        try:
            if is_task_already_answered(page_html):
                return (None, True)
        except Exception:
            pass
        if "taskForm" in page_html and "cm-editor" in page_html:
            time.sleep(0.7)
            page_html = driver.page_source
        return (page_html, False)
    except Exception:
        return (None, False)
    finally:
        try:
            driver.switch_to.default_content()
            driver.set_page_load_timeout(300)
        except Exception:
            pass


def run_3_2(driver: WebDriver) -> None:
    path_32 = Path(EXCEL_3_2)
    if not path_32.exists():
        print(f"[3.2] File not found: {path_32} (place test2.xlsx next to the script/exe)")
        return
    data = load_3_2(path_32)
    if not data:
        print(f"[3.2] No data in {EXCEL_3_2} (file exists but no rows; expect 3 columns, no header row)")
        return

    for lesson_id, rows in data.items():
        if not rows:
            continue
        print(f"[3.2] Lesson {lesson_id}: submitting {len(rows)} answers")
        try:
            session = make_session(driver)
        except Exception:
            traceback.print_exc()
            continue
        for task_id, answer in rows:
            # Приводим ответ из Excel к удобному текстовому виду
            # (в том числе вытаскиваем правые части пар для drag-and-drop).
            normalized_answer = _normalize_answer(answer)

            # Особый случай: в ячейке лежит payload для drag-and-drop (скопирован из curl).
            drag_question_id, drag_mappings = _parse_drag_payload(str(answer))
            if drag_question_id is not None and drag_mappings:
                print(
                    f"[3.2] Task {task_id}: using explicit drag-and-drop payload from Excel "
                    f"(question_id={drag_question_id}, {len(drag_mappings)} mapping(s))"
                )
                try:
                    resp = submit_answer_3_2_drag(
                        session,
                        lesson_id,
                        task_id,
                        drag_question_id,
                        drag_mappings,
                    )
                except Exception:
                    print(f"[3.2] Submit drag-and-drop task {task_id} failed:")
                    traceback.print_exc()
                    continue
                if resp.status_code in (200, 201, 204):
                    preview = (resp.text or "")[:200].replace("\n", " ")
                    print(f"[3.2] Submit lesson={lesson_id} task={task_id} -> {resp.status_code} {preview}")
                else:
                    body = (resp.text or (resp.content.decode(errors="replace") if resp.content else ""))[:500]
                    print(f"[3.2] Submit lesson={lesson_id} task={task_id} -> err {resp.status_code}: {body}")
                # payload уже отправлен — дальше обычная логика не нужна
                continue

            resp = None
            print(f"[3.2] Task {task_id} ...", flush=True)
            page_url = f"{BASE_URL}/lessons/{lesson_id}/tasks/{task_id}"
            page_html, already_answered = _get_page_html(driver, page_url)
            if already_answered:
                print(f"[3.2] Task {task_id} already answered, skip.")
                continue
            if not page_html or ("questions[" not in page_html and "taskForm" not in page_html):
                print(f"[3.2] Could not load form for task {task_id}")
                continue
            refresh_session_from_driver(driver, session)
            page_csrf = get_csrf_from_page(page_html)
            if page_csrf:
                session.headers["X-CSRF-Token"] = page_csrf
            parsed = parse_question_page(page_html)
            form_key = parsed.get("question_form_key")
            if not form_key and "taskForm" in page_html and "cm-editor" in page_html:
                code_ids = _get_code_ids_from_api(session, lesson_id, task_id)
                if not code_ids or not code_ids.get("code_question_id"):
                    code_ids = None
                    for _ in range(2):
                        time.sleep(0.3)
                        code_ids = _get_code_ids_from_browser(driver)
                        if code_ids and code_ids.get("code_question_id"):
                            break
                    if not code_ids or not code_ids.get("code_question_id"):
                        code_ids = _get_code_ids_from_api(session, lesson_id, task_id)
                if code_ids:
                    parsed["is_code"] = True
                    parsed["question_form_key"] = f"questions[{code_ids['code_question_id']}][]"
                    parsed["code_question_id"] = code_ids["code_question_id"]
                    parsed["test_case_execution_id"] = code_ids.get("test_case_execution_id")
                    form_key = parsed["question_form_key"]
            if not form_key:
                # Drag-and-drop задачи (LinkTask) не имеют стандартного form_key в HTML.
                if parsed.get("is_drag"):
                    print(f"[3.2] Task {task_id}: detected drag-and-drop type without form key (requires explicit payload).")
                    continue
                print(f"[3.2] Could not find form question key for task {task_id}")
                continue
            if parsed.get("is_code"):
                code_id = parsed.get("code_question_id")
                if not code_id:
                    print(f"[3.2] Code task {task_id}: missing code_question_id")
                    continue
                source_code = (normalized_answer if isinstance(normalized_answer, str) else str(normalized_answer or "")).strip()
                if not source_code:
                    print(f"[3.2] Code task {task_id}: empty code in Excel, skip.")
                    continue
                # Сначала запускаем тесты через /api/wk/test_case_executions
                try:
                    ids_for_tests = _get_code_ids_from_api(session, lesson_id, task_id)
                    test_question_id = ids_for_tests.get("code_question_id") if ids_for_tests else None
                except Exception:
                    test_question_id = None
                if test_question_id:
                    try:
                        resp_test = submit_code_test_execution(
                            session,
                            test_question_id,
                            language="python3",
                            source_code=source_code,
                            lesson_id=lesson_id,
                            task_id=task_id,
                        )
                        print(
                            f"[3.2] Code task {task_id}: test execution -> "
                            f"{resp_test.status_code} {(resp_test.text or '')[:120].replace(chr(10), ' ')}"
                        )
                    except Exception:
                        print(f"[3.2] Code task {task_id}: test execution request failed:")
                        traceback.print_exc()
                # Даём бэкенду секунду, чтобы зафиксировать запуск тестов
                time.sleep(1.0)
                try:
                    resp = submit_answer_3_2_code(
                        session,
                        lesson_id,
                        task_id,
                        code_id,
                        language="python3",
                        source_code=source_code,
                    )
                except Exception:
                    print(f"[3.2] Submit code task {task_id} failed:")
                    traceback.print_exc()
                    continue
            elif parsed.get("is_text_input"):
                answer_value = str(normalized_answer).strip() if normalized_answer is not None else ""
                try:
                    resp = submit_answer_3_2(session, lesson_id, task_id, form_key, answer_value)
                except Exception:
                    print(f"[3.2] Submit task {task_id} failed:")
                    traceback.print_exc()
                    continue
            elif parsed.get("is_multiple_choice"):
                options = parsed.get("options") or []
                answer_values = best_matches_multiple(
                    normalized_answer, options, threshold=ANSWER_SIMILARITY_THRESHOLD
                )
                if not answer_values:
                    print(f"[3.2] No matching option(s) for answer '{answer}' (task {task_id}), skip.")
                    continue
                try:
                    resp = submit_answer_3_2_multiple(
                        session, lesson_id, task_id, form_key, answer_values
                    )
                except Exception:
                    print(f"[3.2] Submit task {task_id} failed:")
                    traceback.print_exc()
                    continue
            else:
                options = parsed.get("options") or []
                answer_value = best_match(normalized_answer, options, threshold=ANSWER_SIMILARITY_THRESHOLD)
                if answer_value is None:
                    print(f"[3.2] No matching option for answer '{answer}' (task {task_id}), skip.")
                    continue
                try:
                    resp = submit_answer_3_2(session, lesson_id, task_id, form_key, answer_value)
                except Exception:
                    print(f"[3.2] Submit task {task_id} failed:")
                    traceback.print_exc()
                    continue
            if resp.status_code in (200, 201, 204):
                preview = (resp.text or "")[:200].replace("\n", " ")
                print(f"[3.2] Submit lesson={lesson_id} task={task_id} -> {resp.status_code} {preview}")
            else:
                body = (resp.text or (resp.content.decode(errors="replace") if resp.content else ""))[:500]
                print(f"[3.2] Submit lesson={lesson_id} task={task_id} -> err {resp.status_code}: {body}")
