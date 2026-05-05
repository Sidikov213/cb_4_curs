"""Parse question page HTML to get form question id and radio options (text -> value).

Supports HTML formats from requirements.md:
- 3.1 radio: form#taskForm action="/classworks/.../tasks/...", input name="questions[ID]"
  type="radio", label in next sibling div with span.MathContent_content__2a8XE.
- 3.2 radio: form#taskForm action="/teacher/lessons/.../tasks/...", same input + div + span
  structure (see requirements.md ANSWER ATTEMPT html FOR RADIO 3.2).
"""
import re
from typing import Any

from bs4 import BeautifulSoup


def _radio_label_text(inp, soup) -> str:
    """Get option label for a radio input. 3.1/3.2: label in next sibling div or span.MathContent_content__2a8XE."""
    label_text = ""
    inp_id = inp.get("id")
    if inp_id:
        label = soup.find("label", attrs={"for": inp_id})
        if label:
            label_text = label.get_text(strip=True)
    if not label_text:
        parent = inp.find_parent("label")
        if parent:
            label_text = parent.get_text(strip=True)
    if not label_text:
        next_el = inp.find_next_sibling()
        if next_el:
            label_text = next_el.get_text(strip=True)
            if not label_text:
                span = next_el.find(class_=re.compile(r"MathContent_content"))
                if span:
                    label_text = span.get_text(strip=True)
    return label_text or ""


def parse_question_page(html: str) -> dict[str, Any]:
    """
    Returns:
      - question_form_key: 'questions[123]' or 'questions[123][]'
      - question_id: numeric id used in form (e.g. 1248193)
      - is_text_input: True if text/textarea (use questions[id][]), False if radio
      - options: for radio, list of (label_text, value); for text, []
    """
    soup = BeautifulSoup(html, "html.parser")
    result = {
        "question_form_key": None,
        "question_id": None,
        "is_text_input": False,
        "is_code": False,
        "is_multiple_choice": False,
        "is_drag": False,
        "code_question_id": None,
        "test_case_execution_id": None,
        "options": [],
    }

    # 3.2 code type: questions[ID][][language], questions[ID][][source_code], questions[ID][][test_case_execution_id]
    # (Code task page may use form#taskForm + CodeMirror; hidden inputs can be added by JS.)
    code_name_re = re.compile(r"^questions\[(\d+)\]\[\]\[(?:language|source_code|test_case_execution_id)\]$")
    code_inputs = soup.find_all(attrs={"name": code_name_re})
    if not code_inputs:
        def _code_name(n):
            if not n:
                return False
            return "questions[" in n and "][][" in n and any(x in n for x in ("language", "source_code", "test_case_execution_id"))
        code_inputs = soup.find_all(attrs={"name": _code_name})
    if code_inputs:
        first_name = code_inputs[0].get("name") or ""
        m = re.search(r"questions\[(\d+)\]", first_name)
        if m:
            result["is_code"] = True
            result["code_question_id"] = int(m.group(1))
            result["question_form_key"] = f"questions[{m.group(1)}][]"
            for tag in code_inputs:
                name = tag.get("name") or ""
                if "test_case_execution_id" in name:
                    val = tag.get("value")
                    if val is not None:
                        result["test_case_execution_id"] = str(val).strip()
                    break
            return result

    # Multiple choice (3.2): input type="checkbox" name="questions[ID][]", same label structure as radio
    checkboxes = soup.find_all(
        name="input",
        attrs={"type": "checkbox", "name": re.compile(r"^questions\[\d+\]\[\]$")},
    )
    if checkboxes:
        first = checkboxes[0]
        name = first.get("name")
        if name:
            result["question_form_key"] = name
            result["is_multiple_choice"] = True
            m = re.search(r"questions\[(\d+)\]", name)
            if m:
                result["question_id"] = int(m.group(1))
        for inp in checkboxes:
            value = inp.get("value")
            if value is None:
                continue
            label_text = _radio_label_text(inp, soup)
            result["options"].append((label_text, value))
        return result

    # Radio: 3.1 and 3.2 use same structure — input name="questions[ID]" type="radio", label in next sibling div
    radios = soup.find_all(name="input", attrs={"type": "radio", "name": re.compile(r"^questions\[\d+\]$")})
    if radios:
        first = radios[0]
        name = first.get("name")
        if name:
            result["question_form_key"] = name
            m = re.search(r"questions\[(\d+)\]", name)
            if m:
                result["question_id"] = int(m.group(1))
        for inp in radios:
            value = inp.get("value")
            if value is None:
                continue
            label_text = _radio_label_text(inp, soup)
            result["options"].append((label_text, value))
        return result

    # Drag-and-drop (LinkTask) detection: нет обычных input[name="questions[...]"],
    # но есть специфичные классы LinkTask_root/LinkTask_optionsPanel.
    if "LinkTask_root__" in html or "LinkTask_optionsPanel__" in html:
        result["is_drag"] = True
        # Для drag-типа числовые id ответов есть только в payload curl, а не в HTML,
        # поэтому form_key определить нельзя.
        return result

    # Text/textarea: name like questions[1248194][]
    text_inputs = soup.find_all(
        name="input",
        attrs={"type": re.compile(r"text|number"), "name": re.compile(r"^questions\[\d+\]\[\]$")},
    ) + soup.find_all(name="textarea", attrs={"name": re.compile(r"^questions\[\d+\]\[\]$")})
    if text_inputs:
        first = text_inputs[0]
        name = first.get("name")
        if name:
            result["question_form_key"] = name
            result["is_text_input"] = True
            m = re.search(r"questions\[(\d+)\]", name)
            if m:
                result["question_id"] = int(m.group(1))
        return result

    # Fallback: any input/textarea with name questions[...]
    any_q = soup.find_all(attrs={"name": re.compile(r"^questions\[\d+\](\[\])?$")})
    for tag in any_q:
        name = tag.get("name")
        if not name:
            continue
        result["question_form_key"] = name
        m = re.search(r"questions\[(\d+)\]", name)
        if m:
            result["question_id"] = int(m.group(1))
        if "[]" in name:
            result["is_text_input"] = True
        else:
            # Radio (same 3.1/3.2 structure)
            for inp in soup.find_all(name="input", attrs={"type": "radio", "name": name}):
                value = inp.get("value")
                if value is None:
                    continue
                label_text = _radio_label_text(inp, soup)
                result["options"].append((label_text, value))
        break

    return result


def is_task_already_answered(html: str) -> bool:
    """True if the task page shows an already-solved state (no need to wait for form or submit).
    Avoids long timeouts when the page no longer has an answer form.
    """
    if not html or "taskForm" not in html and "questions[" not in html:
        # Page might be a different view (e.g. result only)
        if any(m in html for m in ("Решено", "Принято", "Верно", "балл", "Ответ засчитан")):
            return True
        return False
    soup = BeautifulSoup(html, "html.parser")
    # Submit button "Ответить" is typically removed or hidden when task is already answered
    form = soup.find("form", id="taskForm")
    if form:
        submit_btn = form.find("button", string=re.compile(r"Ответить"))
        if not submit_btn or submit_btn.get("disabled") is not None:
            return True
    # Class that indicates solved state (e.g. no longer "noSolved")
    if re.search(r"actions_solved|alreadySolved|taskSolved", html, re.I):
        return True
    return False


def get_csrf_from_page(html: str) -> str | None:
    """Extract CSRF token from <meta name="csrf-token" content="...">."""
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"name": "csrf-token"})
    if meta and meta.get("content"):
        return meta["content"].strip()
    return None


def find_video_and_task_links(html: str, base_url: str) -> tuple[str | None, str | None]:
    """Find first link to /groups/ (video) and first to teacher/courses/.../lessons/ (task page). Returns (video_url, task_page_url)."""
    soup = BeautifulSoup(html, "html.parser")
    video_url = None
    task_page_url = None
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if "/groups/" in href:
            if not video_url:
                video_url = href if href.startswith("http") else (base_url.rstrip("/") + ("/" + href.lstrip("/")))
        if "/teacher/courses/" in href and "/lessons/" in href:
            if not task_page_url:
                task_page_url = href if href.startswith("http") else (base_url.rstrip("/") + ("/" + href.lstrip("/")))
    return video_url, task_page_url
