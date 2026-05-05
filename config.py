"""Configuration. Override via environment or edit defaults."""
import os
import sys
from pathlib import Path

# Data files location:
# - in script mode: project folder (next to .py files)
# - in .exe mode: folder where .exe is located (so user can replace xlsx/txt without rebuild)
def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent

_BASE = _base_dir()

BASE_URL = os.environ.get("KBC_BASE_URL", "https://kb.cifrium.ru")

# Paths to Excel files (3.1 = classworks/homeworks, 3.2 = lessons)
EXCEL_3_1 = os.environ.get("KBC_EXCEL_31", str(_BASE / "test1.xlsx"))
EXCEL_3_2 = os.environ.get("KBC_EXCEL_32", str(_BASE / "test2.xlsx"))
EXCEL_3_3 = os.environ.get("KBC_EXCEL_33", str(_BASE / "test3.xlsx"))

# Optional: course_id for building teacher task page URL for 3.1 (if needed)
COURSE_ID = os.environ.get("KBC_COURSE_ID", "")

# Selenium
HEADLESS = os.environ.get("KBC_HEADLESS", "").lower() in ("1", "true", "yes")
IMPLICIT_WAIT_SEC = 10
# Pause after opening browser so user can log in
LOGIN_WAIT_SEC = int(os.environ.get("KBC_LOGIN_WAIT_SEC", "60"))

# Answer matching: min ratio (0..1) to accept Excel answer as match for radio option text
ANSWER_SIMILARITY_THRESHOLD = float(os.environ.get("KBC_ANSWER_SIMILARITY", "0.7"))

# Optional: X-Device-Id header (from browser DevTools). If empty, a random one is used.
X_DEVICE_ID = os.environ.get("KBC_X_DEVICE_ID", "")

# Video links: one URL per line; opened in new tabs (videos-only run in run.py).
VIDEO_LINKS_FILE = os.environ.get("KBC_VIDEO_LINKS_FILE", str(_BASE / "videos.txt"))
# HTML5 <video> playbackRate (2 = 2x). Set to 0 to leave the browser default (no script change).
VIDEO_PLAYBACK_RATE = float(os.environ.get("KBC_VIDEO_PLAYBACK_RATE", "2"))
# After opening video tabs: wait before touching the player (slow pages / "шоколадки" overlay).
VIDEO_OPEN_SETTLE_SEC = float(os.environ.get("KBC_VIDEO_OPEN_SETTLE_SEC", "5"))
# Delay between opening video tabs; opening many at once can trigger player/CDN "technical chocolates".
VIDEO_OPEN_TAB_DELAY_SEC = float(os.environ.get("KBC_VIDEO_OPEN_TAB_DELAY_SEC", "0.7"))
# Keep re-applying playbackRate in each tab for this long (ms); some players reset rate after load.
VIDEO_RATE_KEEPALIVE_MS = int(os.environ.get("KBC_VIDEO_RATE_KEEPALIVE_MS", "120000"))
# How many times to rescan each tab/frame after opening; players may inject iframe/video late.
VIDEO_RATE_SCAN_PASSES = int(os.environ.get("KBC_VIDEO_RATE_SCAN_PASSES", "2"))
# Seconds between rescans while looking for late-loaded players.
VIDEO_RATE_SCAN_INTERVAL_SEC = float(os.environ.get("KBC_VIDEO_RATE_SCAN_INTERVAL_SEC", "0.8"))
# Max seconds per tab to wait for the "technical difficulties" banner; keep low because there may be many tabs.
VIDEO_OVERLAY_WAIT_SEC = float(os.environ.get("KBC_VIDEO_OVERLAY_WAIT_SEC", "1"))
# Only these first tabs use the slower full scan; the rest use the fast scan settings below.
VIDEO_DETAILED_TAB_COUNT = int(os.environ.get("KBC_VIDEO_DETAILED_TAB_COUNT", "2"))
# Fast scan settings for the remaining tabs.
VIDEO_FAST_OVERLAY_WAIT_SEC = float(os.environ.get("KBC_VIDEO_FAST_OVERLAY_WAIT_SEC", "0"))
VIDEO_FAST_RATE_SCAN_PASSES = int(os.environ.get("KBC_VIDEO_FAST_RATE_SCAN_PASSES", "1"))
VIDEO_FAST_RATE_SCAN_INTERVAL_SEC = float(os.environ.get("KBC_VIDEO_FAST_RATE_SCAN_INTERVAL_SEC", "0.1"))
VIDEO_FAST_IFRAME_DEPTH = int(os.environ.get("KBC_VIDEO_FAST_IFRAME_DEPTH", "1"))
# Reload a tab once when the "technical difficulties" banner is visible.
VIDEO_RELOAD_ON_OVERLAY = os.environ.get("KBC_VIDEO_RELOAD_ON_OVERLAY", "1").lower() in ("1", "true", "yes")
# Try to start HTML5 videos automatically. Muted autoplay is much more reliable in Chrome.
VIDEO_AUTOPLAY = os.environ.get("KBC_VIDEO_AUTOPLAY", "1").lower() in ("1", "true", "yes")
VIDEO_AUTOPLAY_MUTED = os.environ.get("KBC_VIDEO_AUTOPLAY_MUTED", "1").lower() in ("1", "true", "yes")
# Periodic anti-pause check after the initial video setup. Set 0 to disable.
VIDEO_PAUSE_CHECK_INTERVAL_SEC = float(os.environ.get("KBC_VIDEO_PAUSE_CHECK_INTERVAL_SEC", "1200"))
