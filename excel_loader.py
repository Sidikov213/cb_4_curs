"""Load task/answer data from Excel (no headers)."""
from pathlib import Path
from typing import Any

import openpyxl


def _cell_value(v: Any) -> str | int | float:
    if v is None:
        return ""
    if isinstance(v, (int, float)):
        return v if isinstance(v, int) else (int(v) if v == int(v) else v)
    return str(v).strip()


def load_excel(path: str | Path) -> list[tuple[Any, Any, Any]]:
    """Load rows as (col0, col1, col2). No header row. Returns list of (id1, id2, answer)."""
    path = Path(path)
    if not path.exists():
        return []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows = []
    for row in ws.iter_rows(values_only=True):
        if not row or (row[0] is None and row[1] is None):
            continue
        c0, c1, c2 = (row[0], row[1], row[2] if len(row) > 2 else None)
        rows.append((_cell_value(c0), _cell_value(c1), _cell_value(c2)))
    wb.close()
    return rows


def group_by_first(rows: list[tuple[Any, Any, Any]]) -> dict[Any, list[tuple[Any, Any]]]:
    """Group rows by first column. Value per group: list of (col1, answer)."""
    groups: dict[Any, list[tuple[Any, Any]]] = {}
    for col0, col1, answer in rows:
        if col0 not in groups:
            groups[col0] = []
        groups[col0].append((col1, answer))
    return groups


def load_3_1(path: str | Path) -> dict[Any, list[tuple[Any, Any]]]:
    """Load test1.xlsx for format 3.1. Groups by classwork_id. Each row: (question_id, answer)."""
    return group_by_first(load_excel(path))


def load_3_2(path: str | Path) -> dict[Any, list[tuple[Any, Any]]]:
    """Load test2.xlsx for format 3.2. Groups by lesson_id (taskId). Each row: (task_id, answer)."""
    return group_by_first(load_excel(path))


def load_3_3(path: str | Path) -> dict[Any, list[tuple[Any, Any]]]:
    """Load test3.xlsx for format trainings. Groups by training_id. Each row: (task_id, answer)."""
    return group_by_first(load_excel(path))
