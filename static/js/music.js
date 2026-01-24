(() => {
  const audio = document.getElementById("bgm");
  const btn = document.getElementById("musicToggle");

  // If audio or button isn't on the page, safely do nothing
  if (!audio || !btn) return;

  const KEY_ON = "music:on";
  const KEY_TIME = "music:time";

  // ---------- Enable music once when arriving from Enter ----------
  const params = new URLSearchParams(window.location.search);
  if (params.get("music") === "1") {
    localStorage.setItem(KEY_ON, "true");

    // Remove ?music=1 so it doesn't keep forcing on refresh
    params.delete("music");
    const newUrl =
      window.location.pathname +
      (params.toString() ? `?${params}` : "") +
      window.location.hash;
    history.replaceState({}, "", newUrl);
  }

  // ---------- Helpers ----------
  function setUI(on) {
    btn.setAttribute("aria-pressed", String(on));
    btn.textContent = on ? "🔊" : "🔇";
  }

  function isEnabled() {
    return localStorage.getItem(KEY_ON) === "true";
  }

  // Start with stored preference
  let on = isEnabled();
  setUI(on);

  // ---------- Restore playback position ----------
  const savedTime = sessionStorage.getItem(KEY_TIME);
  if (savedTime) {
    const t = Number(savedTime);
    if (!Number.isNaN(t) && t > 0) {
      // currentTime may fail until metadata is loaded
      audio.addEventListener(
        "loadedmetadata",
        () => {
          audio.currentTime = Math.min(t, audio.duration || t);
        },
        { once: true }
      );
    }
  }

  // Keep saving time so navigation doesn't restart
  function saveTime() {
    sessionStorage.setItem(KEY_TIME, String(audio.currentTime || 0));
  }

  audio.addEventListener("timeupdate", () => {
    // save periodically (cheap)
    saveTime();
  });

  window.addEventListener("beforeunload", saveTime);

  // ---------- Play logic ----------
  async function tryPlay() {
    // Keep state ON visually even if autoplay is blocked
    localStorage.setItem(KEY_ON, "true");
    on = true;
    setUI(true);

    try {
      await audio.play();
      return true;
    } catch (e) {
      // Autoplay blocked: this is normal.
      // DO NOT flip to OFF. We'll start on the next user gesture.
      return false;
    }
  }

  function pauseMusic() {
    audio.pause();
    saveTime();
    localStorage.setItem(KEY_ON, "false");
    on = false;
    setUI(false);
  }

  // If it should be on, attempt to play immediately (may be blocked)
  if (on) {
    tryPlay();
  }

  // Unlock playback on first user gesture if music is enabled
  function unlockOnGesture() {
    if (isEnabled()) {
      tryPlay();
    }
  }

  window.addEventListener("pointerdown", unlockOnGesture, { once: true });
  window.addEventListener("keydown", unlockOnGesture, { once: true });

  // ---------- Toggle button ----------
  btn.addEventListener("click", async () => {
    if (on) {
      pauseMusic();
    } else {
      await tryPlay();
    }
  });
})();
