"""Answer text similarity for matching Excel answer to HTML option (radio / multiple choice)."""
import re
from difflib import SequenceMatcher


def similarity(a: str, b: str) -> float:
    """0..1 ratio; 1 = identical."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    a, b = a.strip().lower(), b.strip().lower()
    return SequenceMatcher(None, a, b).ratio()


def best_match(
    answer: str | int | float,
    options: list[tuple[str, str]],
    threshold: float = 0.7,
) -> str | None:
    """
    Find option whose text best matches answer. options = [(display_text, value), ...].
    Returns value for the best match if ratio >= threshold, else None.
    """
    answer_str = str(answer).strip() if answer is not None else ""
    if not answer_str:
        return None
    best_ratio = 0.0
    best_value = None
    for text, value in options:
        r = similarity(answer_str, str(text).strip())
        if r >= threshold and r > best_ratio:
            best_ratio = r
            best_value = value
    return best_value


def best_matches_multiple(
    answer: str | int | float,
    options: list[tuple[str, str]],
    threshold: float = 0.7,
) -> list[str]:
    """
    Split answer by comma/semicolon/pipe/newline, match each part to options, return list of option values.
    options = [(display_text, value), ...]. Used for multiple-choice (checkbox) tasks.
    Keeps order of first occurrence; skips parts that don't match any option.
    """
    answer_str = str(answer).strip() if answer is not None else ""
    if not answer_str:
        return []
    parts = [s.strip() for s in re.split(r"[,;\|\n]+", answer_str) if s.strip()]
    seen = set()
    result = []
    for part in parts:
        val = best_match(part, options, threshold=threshold)
        if val is not None and val not in seen:
            seen.add(val)
            result.append(val)
    return result
