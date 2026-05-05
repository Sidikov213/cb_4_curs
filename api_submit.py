"""Submit answer attempt via API (multipart/form-data)."""
from typing import Any

import requests

from config import BASE_URL


def submit_answer_3_1(
    session: requests.Session,
    classwork_id: int | str,
    question_id: int | str,
    form_question_key: str,
    answer_value: str | int,
    referer_path: str | None = None,
) -> requests.Response:
    """POST to /api/homeworks/{classwork_id}/tasks/{question_id}/answer_attempts."""
    url = f"{BASE_URL}/api/homeworks/{classwork_id}/tasks/{question_id}/answer_attempts"
    referer_path = referer_path or f"/classworks/{classwork_id}/tasks/{question_id}?page=1"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    # multipart form: one field name=form_question_key, value=answer_value
    files = {}
    data = {form_question_key: (None, str(answer_value))}
    # requests will build multipart; we need to send as form data with one key
    # Actually the API expects multipart with Content-Disposition: form-data; name="questions[123]"
    payload = {form_question_key: str(answer_value)}
    resp = session.post(url, files=[(k, (None, v)) for k, v in payload.items()])
    return resp


def submit_answer_3_2(
    session: requests.Session,
    lesson_id: int | str,
    task_id: int | str,
    form_question_key: str,
    answer_value: str | int,
    referer_path: str | None = None,
) -> requests.Response:
    """POST to /api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts."""
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/teacher/lessons/{lesson_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    payload = {form_question_key: str(answer_value)}
    resp = session.post(url, files=[(k, (None, v)) for k, v in payload.items()])
    return resp


def submit_answer_3_2_multiple(
    session: requests.Session,
    lesson_id: int | str,
    task_id: int | str,
    form_question_key: str,
    answer_values: list[str | int],
    referer_path: str | None = None,
) -> requests.Response:
    """POST to /api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts with multiple values for one key (checkboxes).
    Payload: one form-data part per selected value, all with name=form_question_key (e.g. questions[1207768][]).
    """
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/lessons/{lesson_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    payload = [(form_question_key, (None, str(v))) for v in answer_values]
    resp = session.post(url, files=payload)
    return resp


def submit_answer_3_2_code(
    session: requests.Session,
    lesson_id: int | str,
    task_id: int | str,
    code_question_id: int | str,
    language: str,
    source_code: str,
    test_case_execution_id: str | int | None = None,
    referer_path: str | None = None,
) -> requests.Response:
    """POST to /api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts with code-type payload (3.2).
    Payload per requirements.md: only questions[id][][language] and questions[id][][source_code].
    """
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/lessons/{lesson_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    base = f"questions[{code_question_id}][]"
    source_code_bytes = (source_code or "").encode("utf-8")
    payload = [
        (f"{base}[language]", (None, language)),
        (f"{base}[source_code]", (None, source_code_bytes, "text/plain; charset=utf-8")),
    ]
    resp = session.post(url, files=payload)
    return resp


def submit_code_test_execution(
    session: requests.Session,
    question_id: int | str,
    language: str,
    source_code: str,
    lesson_id: int | str,
    task_id: int | str,
    referer_path: str | None = None,
) -> requests.Response:
    """
    Запускает проверку кода для задачи 3.2.
    POST /api/wk/test_case_executions с JSON:
      { "question_id": ..., "language": "...", "source_code": "..." }
    """
    url = f"{BASE_URL}/api/wk/test_case_executions"
    referer_path = referer_path or f"/lessons/{lesson_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    payload_json = {
        "question_id": int(question_id) if not isinstance(question_id, int) else question_id,
        "language": language,
        "source_code": source_code,
    }
    resp = session.post(url, json=payload_json)
    return resp


def submit_answer_3_2_drag(
    session: requests.Session,
    lesson_id: int | str,
    task_id: int | str,
    question_id: int | str,
    mappings: list[tuple[int | str, int | str]],
    referer_path: str | None = None,
) -> requests.Response:
    """
    Отправка drag-and-drop (LinkTask, формат 3.2) по заранее известным соответствиям.

    mappings: список пар (from_id, to_id), по которым нужно собрать поля:
      questions[question_id][from_id] = to_id
    """
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/teacher/lessons/{lesson_id}/tasks"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    files_payload: list[tuple[str, tuple[None, str]]] = []
    base = f"questions[{question_id}]"
    for from_id, to_id in mappings:
        name = f"{base}[{from_id}]"
        files_payload.append((name, (None, str(to_id))))

    resp = session.post(url, files=files_payload)
    return resp


def submit_answer_training(
    session: requests.Session,
    training_id: int | str,
    task_id: int | str,
    form_question_key: str,
    answer_value: str | int,
    referer_path: str | None = None,
) -> requests.Response:
    """POST to /api/trainings/{training_id}/tasks/{task_id}/answer_attempts."""
    url = f"{BASE_URL}/api/trainings/{training_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/trainings/{training_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    payload = {form_question_key: str(answer_value)}
    return session.post(url, files=[(k, (None, v)) for k, v in payload.items()])


def submit_answer_training_code(
    session: requests.Session,
    training_id: int | str,
    task_id: int | str,
    code_question_id: int | str,
    language: str,
    source_code: str,
    test_case_execution_id: str | int | None = None,
    referer_path: str | None = None,
) -> requests.Response:
    """POST code answer to /api/trainings/{training_id}/tasks/{task_id}/answer_attempts."""
    url = f"{BASE_URL}/api/trainings/{training_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/trainings/{training_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    base = f"questions[{code_question_id}][]"
    source_code_bytes = (source_code or "").encode("utf-8")
    payload = [
        (f"{base}[language]", (None, language)),
        (f"{base}[source_code]", (None, source_code_bytes, "text/plain; charset=utf-8")),
    ]
    if test_case_execution_id is not None:
        payload.append((f"{base}[test_case_execution_id]", (None, str(test_case_execution_id))))
    return session.post(url, files=payload)


def submit_answer_training_drag(
    session: requests.Session,
    training_id: int | str,
    task_id: int | str,
    question_id: int | str,
    mappings: list[tuple[int | str, int | str]],
    referer_path: str | None = None,
) -> requests.Response:
    """POST drag-and-drop answer for trainings."""
    url = f"{BASE_URL}/api/trainings/{training_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/trainings/{training_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    files_payload: list[tuple[str, tuple[None, str]]] = []
    base = f"questions[{question_id}]"
    for from_id, to_id in mappings:
        files_payload.append((f"{base}[{from_id}]", (None, str(to_id))))
    return session.post(url, files=files_payload)


def submit_answer_training_raw(
    session: requests.Session,
    training_id: int | str,
    task_id: int | str,
    fields: list[tuple[str, str]],
    referer_path: str | None = None,
) -> requests.Response:
    """POST raw multipart fields for trainings answer_attempts."""
    url = f"{BASE_URL}/api/trainings/{training_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/trainings/{training_id}/tasks/{task_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer
    files_payload = [(k, (None, str(v))) for k, v in fields]
    return session.post(url, files=files_payload)


def finish_training(
    session: requests.Session,
    training_id: int | str,
    referer_path: str | None = None,
) -> requests.Response:
    """POST /api/trainings/{training_id}/finish after all attempts."""
    url = f"{BASE_URL}/api/trainings/{training_id}/finish"
    referer_path = referer_path or f"/trainings/{training_id}/finish"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer
    return session.post(url)


def start_training(
    session: requests.Session,
    training_id: int | str,
    referer_path: str | None = None,
) -> requests.Response:
    """POST /api/trainings/{training_id}/start before answer_attempts."""
    url = f"{BASE_URL}/api/trainings/{training_id}/start"
    referer_path = referer_path or f"/trainings/{training_id}"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer
    return session.post(url)


def submit_answer_3_2_drag(
    session: requests.Session,
    lesson_id: int | str,
    task_id: int | str,
    question_id: int | str,
    mappings: list[tuple[int | str, int | str]],
    referer_path: str | None = None,
) -> requests.Response:
    """
    Отправка drag-and-drop (LinkTask, формат 3.2) по заранее известным соответствиям.

    mappings: список пар (from_id, to_id), по которым нужно собрать поля:
      questions[question_id][from_id] = to_id
    """
    url = f"{BASE_URL}/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts"
    referer_path = referer_path or f"/teacher/lessons/{lesson_id}/tasks"
    referer = f"{BASE_URL}{referer_path}"
    session.headers["Referer"] = referer
    session.headers["X-Referer"] = referer

    files_payload: list[tuple[str, tuple[None, str]]] = []
    base = f"questions[{question_id}]"
    for from_id, to_id in mappings:
        name = f"{base}[{from_id}]"
        files_payload.append((name, (None, str(to_id))))

    resp = session.post(url, files=files_payload)
    return resp
