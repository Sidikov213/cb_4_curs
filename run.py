"""Main entry: open Chrome, wait for login, open video URLs in new tabs; optional 2x on HTML5 video (no seek)."""
import sys
import threading
import time
import traceback
from pathlib import Path

from selenium.webdriver.common.by import By

from browser import create_driver, wait_for_login
from config import (
    VIDEO_AUTOPLAY,
    VIDEO_AUTOPLAY_MUTED,
    VIDEO_DETAILED_TAB_COUNT,
    VIDEO_FAST_IFRAME_DEPTH,
    VIDEO_FAST_OVERLAY_WAIT_SEC,
    VIDEO_FAST_RATE_SCAN_INTERVAL_SEC,
    VIDEO_FAST_RATE_SCAN_PASSES,
    VIDEO_LINKS_FILE,
    VIDEO_OPEN_SETTLE_SEC,
    VIDEO_OPEN_TAB_DELAY_SEC,
    VIDEO_OVERLAY_WAIT_SEC,
    VIDEO_PAUSE_CHECK_INTERVAL_SEC,
    VIDEO_PLAYBACK_RATE,
    VIDEO_RATE_KEEPALIVE_MS,
    VIDEO_RELOAD_ON_OVERLAY,
    VIDEO_RATE_SCAN_INTERVAL_SEC,
    VIDEO_RATE_SCAN_PASSES,
)

# Error-style banners on kb (transient CDN/player); we wait briefly, then keep re-applying 2x anyway.
_OVERLAY_MARKERS = (
    "технические шоколадки",
    "не отключайтесь",
    "что-то сломалось",
    "technical chocolates",  # if ever localized
)

# Walk Shadow DOM in the current document, set playbackRate/defaultPlaybackRate, optionally play(), keep re-applying.
# Selenium separately switches into iframes, including cross-origin frames when WebDriver permits it.
_JS_PLAYBACK_RATE_KEEPALIVE = """
(function(rate, durationMs, autoplay, muted) {
  function walkEl(el) {
    var n = 0;
    function w(x) {
      if (!x) return 0;
      var c = 0;
      if (x.nodeName === 'VIDEO') {
        try {
          x.defaultPlaybackRate = rate;
          x.playbackRate = rate;
          if (autoplay) {
            x.muted = muted;
            x.play().catch(function() {});
          }
          c++;
        } catch (e) {}
      }
      if (x.shadowRoot) c += w(x.shadowRoot);
      for (var y = x.firstElementChild; y; y = y.nextElementSibling) c += w(y);
      return c;
    }
    return w(el);
  }
  function applyAll() {
    return walkEl(document.documentElement);
  }
  var first = applyAll();
  var id = setInterval(applyAll, 450);
  setTimeout(function() { clearInterval(id); }, durationMs);
  return first;
})(arguments[0], arguments[1], arguments[2], arguments[3]);
"""

_JS_RESUME_PAUSED_VIDEOS = """
(function(rate, muted) {
  var stats = { videos: 0, paused: 0, resumed: 0 };
  function w(x) {
    if (!x) return;
    if (x.nodeName === 'VIDEO') {
      stats.videos++;
      try {
        if (rate > 0) {
          x.defaultPlaybackRate = rate;
          x.playbackRate = rate;
        }
        if (!x.ended && x.paused) {
          stats.paused++;
          x.muted = muted;
          var p = x.play();
          if (p && p.catch) p.catch(function() {});
          stats.resumed++;
        }
      } catch (e) {}
    }
    if (x.shadowRoot) w(x.shadowRoot);
    for (var y = x.firstElementChild; y; y = y.nextElementSibling) w(y);
  }
  w(document.documentElement);
  return stats;
})(arguments[0], arguments[1]);
"""


def _read_video_links(path: str) -> list[str]:
    """Read video URLs: one per line, skip empty and # comments."""
    p = Path(path)
    if not p.exists():
        return []
    return [
        line.strip() for line in p.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def _has_technical_overlay(driver) -> bool:
    try:
        src = driver.page_source.lower()
    except Exception:
        return False
    return any(m.lower() in src for m in _OVERLAY_MARKERS)


def _wait_for_overlay_or_timeout(driver, max_sec: float) -> None:
    """Wait while the 'technical difficulties' style banner is present (up to max_sec)."""
    deadline = time.time() + max_sec
    while time.time() < deadline and _has_technical_overlay(driver):
        time.sleep(1.2)
    if _has_technical_overlay(driver):
        print(
            "[video] На странице всё ещё сообщение про сбой/«шоколадки» — "
            "пробуем выставить скорость всё равно (часто помогает обновить вкладку F5)."
        )


def _reload_once_if_overlay(driver) -> bool:
    """Reload current tab once if the transient error banner is visible."""
    if not VIDEO_RELOAD_ON_OVERLAY or not _has_technical_overlay(driver):
        return False
    try:
        print("[video] Видно «технические шоколадки» — обновляю вкладку один раз...")
        driver.refresh()
        time.sleep(2.5)
        return True
    except Exception:
        return False


def _install_playback_keepalive_on_tab(driver, rate: float, duration_ms: int) -> int:
    """Inject keepalive in the current tab; returns count of <video> nodes found on first pass."""
    try:
        return int(
            driver.execute_script(
                _JS_PLAYBACK_RATE_KEEPALIVE,
                rate,
                duration_ms,
                VIDEO_AUTOPLAY,
                VIDEO_AUTOPLAY_MUTED,
            )
            or 0
        )
    except Exception:
        return 0


def _install_playback_keepalive_in_frame_tree(
    driver,
    rate: float,
    duration_ms: int,
    depth: int = 0,
    max_depth: int = 5,
) -> int:
    """Inject keepalive into the current document and recursively into reachable iframes."""
    total = _install_playback_keepalive_on_tab(driver, rate, duration_ms)
    if depth >= max_depth:
        return total

    try:
        frames = driver.find_elements(By.TAG_NAME, "iframe")
    except Exception:
        return total

    for frame in frames:
        switched = False
        try:
            driver.switch_to.frame(frame)
            switched = True
            total += _install_playback_keepalive_in_frame_tree(
                driver, rate, duration_ms, depth=depth + 1, max_depth=max_depth
            )
        except Exception:
            pass
        finally:
            if switched:
                try:
                    driver.switch_to.parent_frame()
                except Exception:
                    try:
                        driver.switch_to.default_content()
                    except Exception:
                        pass
    return total


def _resume_paused_videos_on_tab(driver, rate: float) -> tuple[int, int, int]:
    """Resume paused HTML5 videos in the current document."""
    try:
        stats = driver.execute_script(_JS_RESUME_PAUSED_VIDEOS, rate, VIDEO_AUTOPLAY_MUTED) or {}
        return (
            int(stats.get("videos") or 0),
            int(stats.get("paused") or 0),
            int(stats.get("resumed") or 0),
        )
    except Exception:
        return 0, 0, 0


def _resume_paused_videos_in_frame_tree(
    driver,
    rate: float,
    depth: int = 0,
    max_depth: int = 5,
) -> tuple[int, int, int]:
    """Resume paused videos in the current document and reachable iframes."""
    videos, paused, resumed = _resume_paused_videos_on_tab(driver, rate)
    if depth >= max_depth:
        return videos, paused, resumed

    try:
        frames = driver.find_elements(By.TAG_NAME, "iframe")
    except Exception:
        return videos, paused, resumed

    for frame in frames:
        switched = False
        try:
            driver.switch_to.frame(frame)
            switched = True
            fv, fp, fr = _resume_paused_videos_in_frame_tree(
                driver, rate, depth=depth + 1, max_depth=max_depth
            )
            videos += fv
            paused += fp
            resumed += fr
        except Exception:
            pass
        finally:
            if switched:
                try:
                    driver.switch_to.parent_frame()
                except Exception:
                    try:
                        driver.switch_to.default_content()
                    except Exception:
                        pass
    return videos, paused, resumed


def _resume_paused_videos_all_tabs(driver, rate: float) -> tuple[int, int, int]:
    """Resume paused videos across all open tabs."""
    handles = list(driver.window_handles)
    if not handles:
        return 0, 0, 0
    current = driver.current_window_handle
    total_videos = 0
    total_paused = 0
    total_resumed = 0
    for h in handles:
        try:
            driver.switch_to.window(h)
            driver.switch_to.default_content()
            videos, paused, resumed = _resume_paused_videos_in_frame_tree(driver, rate)
            total_videos += videos
            total_paused += paused
            total_resumed += resumed
        except Exception:
            pass
    try:
        driver.switch_to.window(current if current in handles else handles[0])
    except Exception:
        pass
    return total_videos, total_paused, total_resumed


def _start_pause_watchdog(driver, stop_event: threading.Event) -> threading.Thread | None:
    """Every N seconds, resume paused HTML5 videos while the browser is open."""
    if VIDEO_PAUSE_CHECK_INTERVAL_SEC <= 0:
        return None

    def _loop() -> None:
        rate = VIDEO_PLAYBACK_RATE if VIDEO_PLAYBACK_RATE > 0 else 1.0
        while not stop_event.wait(VIDEO_PAUSE_CHECK_INTERVAL_SEC):
            try:
                videos, paused, resumed = _resume_paused_videos_all_tabs(driver, rate)
                print(
                    f"[video] Анти-пауза: найдено <video>: {videos}, "
                    f"на паузе: {paused}, запущено: {resumed}."
                )
            except Exception:
                if not stop_event.is_set():
                    print("[video] Анти-пауза: не удалось проверить вкладки.")

    thread = threading.Thread(target=_loop, name="video-pause-watchdog", daemon=True)
    thread.start()
    return thread


def _apply_playback_rate_all_tabs(driver, rate: float, duration_ms: int) -> tuple[int, int]:
    """
    Each tab: optional overlay wait, then inject JS timer in top page and iframe tree.
    Returns (peak_videos_single_pass, tabs_with_any_video).
    """
    handles = list(driver.window_handles)
    if not handles:
        return 0, 0
    current = driver.current_window_handle
    peak = 0
    tabs_hit = 0
    for idx, h in enumerate(handles, start=1):
        try:
            driver.switch_to.window(h)
            driver.switch_to.default_content()
            detailed = idx <= max(0, VIDEO_DETAILED_TAB_COUNT)
            mode = "full" if detailed else "fast"
            print(f"[video] Проверяю вкладку {idx}/{len(handles)} ({mode})...")
            overlay_wait = VIDEO_OVERLAY_WAIT_SEC if detailed else VIDEO_FAST_OVERLAY_WAIT_SEC
            scan_passes = VIDEO_RATE_SCAN_PASSES if detailed else VIDEO_FAST_RATE_SCAN_PASSES
            scan_interval = VIDEO_RATE_SCAN_INTERVAL_SEC if detailed else VIDEO_FAST_RATE_SCAN_INTERVAL_SEC
            max_frame_depth = 5 if detailed else max(0, VIDEO_FAST_IFRAME_DEPTH)
            if overlay_wait > 0:
                _wait_for_overlay_or_timeout(driver, overlay_wait)
            if detailed and _reload_once_if_overlay(driver):
                _wait_for_overlay_or_timeout(driver, overlay_wait)
            time.sleep(0.25 if detailed else 0.05)
            tab_peak = 0
            for scan_no in range(max(1, scan_passes)):
                try:
                    driver.switch_to.default_content()
                except Exception:
                    pass
                n = _install_playback_keepalive_in_frame_tree(
                    driver, rate, duration_ms, max_depth=max_frame_depth
                )
                tab_peak = max(tab_peak, n)
                if scan_no + 1 < scan_passes:
                    time.sleep(scan_interval)
            if tab_peak > 0:
                tabs_hit += 1
            peak = max(peak, tab_peak)
        except Exception:
            pass
    try:
        driver.switch_to.window(current if current in handles else handles[0])
    except Exception:
        pass
    return peak, tabs_hit


def main() -> None:
    speed_hint = (
        f"{VIDEO_PLAYBACK_RATE:g}x HTML5 where supported"
        if VIDEO_PLAYBACK_RATE > 0
        else "default speed (no script)"
    )
    print(
        "Starting Chrome. Log in when the page opens, then press Enter — "
        f"links from videos.txt open in new tabs ({speed_hint}; no seek)."
    )
    driver = create_driver()
    pause_watch_stop = threading.Event()
    pause_watch_thread = None
    try:
        wait_for_login(driver)
        video_links = _read_video_links(VIDEO_LINKS_FILE)
        if not video_links:
            print(f"[video] No links in {VIDEO_LINKS_FILE} (one URL per line). Nothing to open.")
        else:
            print(f"[video] Opening {len(video_links)} link(s) in new tabs...")
            for url in video_links:
                if url:
                    driver.execute_script("window.open(arguments[0], '_blank');", url)
                    if VIDEO_OPEN_TAB_DELAY_SEC > 0:
                        time.sleep(VIDEO_OPEN_TAB_DELAY_SEC)
            print(
                f"[video] Пауза {VIDEO_OPEN_SETTLE_SEC:g} с перед настройкой плеера "
                f"(подгрузка, «шоколадки», overlay)..."
            )
            time.sleep(VIDEO_OPEN_SETTLE_SEC)

            if VIDEO_PLAYBACK_RATE > 0:
                peak, tabs_with_video = _apply_playback_rate_all_tabs(
                    driver, VIDEO_PLAYBACK_RATE, VIDEO_RATE_KEEPALIVE_MS
                )
                print(
                    f"[video] Установлен режим повторной установки скорости ~{VIDEO_PLAYBACK_RATE:g}x "
                    f"на {VIDEO_RATE_KEEPALIVE_MS // 1000} с "
                    f"(Shadow DOM + Selenium iframe scan x{VIDEO_RATE_SCAN_PASSES}, "
                    "плеер иногда сбрасывает rate)."
                )
                if peak == 0:
                    print(
                        "[video] Элементов <video> не найдено — сайт может использовать свой плеер без HTML5, "
                        "или видео в другом домене (iframe). Поставь скорость вручную в UI или обнови вкладку (F5)."
                    )
                else:
                    print(
                        f"[video] За первый проход затронуто до {peak} <video> на одной вкладке; "
                        f"вкладок с видео: {tabs_with_video}."
                    )
            pause_watch_thread = _start_pause_watchdog(driver, pause_watch_stop)
            if pause_watch_thread:
                print(
                    f"[video] Анти-пауза включена: проверка каждые "
                    f"{VIDEO_PAUSE_CHECK_INTERVAL_SEC / 60:g} мин."
                )
        print("Done (videos only).")
    except Exception:
        traceback.print_exc()
    finally:
        input("Press Enter to close the browser...")
        pause_watch_stop.set()
        if pause_watch_thread and pause_watch_thread.is_alive():
            pause_watch_thread.join(timeout=2)
        driver.quit()


if __name__ == "__main__":
    main()
    sys.exit(0)
