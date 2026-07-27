/* listen-player.js — progressive enhancement for the field-guide narration player.
 *
 * Play / pause and seek-to-any-position are already provided by the native
 * <audio controls> element. This adds the controls the native player hides or
 * omits (varies by browser):
 *   - skip back / forward 15 seconds
 *   - a visible playback-speed selector (0.75×–2×)
 *
 * Self-contained: injects its own styles, no-ops on pages without a
 * .listen-player, and remembers the chosen speed across sections and pages.
 */
(function () {
  "use strict";

  var SKIP = 15; // seconds
  var RATES = [0.75, 1, 1.25, 1.5, 2];
  var STORE_KEY = "cfm-narration-rate";

  function savedRate() {
    try {
      var v = parseFloat(localStorage.getItem(STORE_KEY));
      return RATES.indexOf(v) >= 0 ? v : 1;
    } catch (_) { return 1; }
  }
  function saveRate(r) {
    try { localStorage.setItem(STORE_KEY, String(r)); } catch (_) {}
  }

  function injectStyles() {
    if (document.getElementById("lp-controls-styles")) return;
    var css =
      ".lp-controls{display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin-top:12px;}" +
      ".lp-controls + .lp-controls{margin-top:8px;}" +
      ".lp-label{font-size:0.8em;font-weight:600;color:#6a8470;margin-right:2px;}" +
      ".lp-btn{display:inline-flex;align-items:center;gap:4px;font:inherit;font-size:0.8em;" +
      "line-height:1;cursor:pointer;padding:6px 11px;min-height:32px;border-radius:999px;" +
      "border:1px solid #cdddce;background:#ffffff;color:#4a6b52;" +
      "transition:background .15s,color .15s,border-color .15s;}" +
      ".lp-btn:hover{background:rgba(74,107,82,0.10);}" +
      ".lp-btn:focus-visible{outline:2px solid #4a6b52;outline-offset:2px;}" +
      ".lp-btn.is-active{background:#4a6b52;color:#f2f5f2;border-color:#4a6b52;}" +
      ".lp-btn svg{width:15px;height:15px;flex:0 0 auto;}";
    var s = document.createElement("style");
    s.id = "lp-controls-styles";
    s.textContent = css;
    document.head.appendChild(s);
  }

  // A circular replay arrow with a jump tick; mirrored for the "back" direction.
  function skipIcon(forward) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' +
      (forward ? '' : ' style="transform:scaleX(-1)"') + '>' +
      '<path d="M21 12a9 9 0 1 1-3.5-7.1"></path>' +
      '<polyline points="21 3 21 8 16 8"></polyline></svg>';
  }

  function makeBtn(html, aria) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "lp-btn";
    b.innerHTML = html;
    b.setAttribute("aria-label", aria);
    return b;
  }

  function enhance(player) {
    if (player.dataset.controlsReady) return;
    var audio = player.querySelector("audio");
    if (!audio) return;
    player.dataset.controlsReady = "1";

    /* ---- jog row: skip back / forward 15s ---- */
    var jog = document.createElement("div");
    jog.className = "lp-controls";
    jog.setAttribute("role", "group");
    jog.setAttribute("aria-label", "Skip");

    var back = makeBtn(skipIcon(false) + "<span>" + SKIP + "s</span>", "Skip back " + SKIP + " seconds");
    back.addEventListener("click", function () {
      audio.currentTime = Math.max(0, audio.currentTime - SKIP);
    });
    var fwd = makeBtn("<span>" + SKIP + "s</span>" + skipIcon(true), "Skip forward " + SKIP + " seconds");
    fwd.addEventListener("click", function () {
      var end = isFinite(audio.duration) ? audio.duration : Infinity;
      audio.currentTime = Math.min(end, audio.currentTime + SKIP);
    });
    jog.appendChild(back);
    jog.appendChild(fwd);
    player.appendChild(jog);

    /* ---- speed row ---- */
    var rate = savedRate();
    audio.playbackRate = rate;

    var speed = document.createElement("div");
    speed.className = "lp-controls";
    speed.setAttribute("role", "group");
    speed.setAttribute("aria-label", "Playback speed");

    var label = document.createElement("span");
    label.className = "lp-label";
    label.textContent = "Speed";
    speed.appendChild(label);

    var btns = [];
    function setActive(r) {
      btns.forEach(function (o) {
        var on = o.r === r;
        o.el.classList.toggle("is-active", on);
        o.el.setAttribute("aria-pressed", on ? "true" : "false");
      });
    }
    RATES.forEach(function (r) {
      var b = makeBtn(r + "×", "Play at " + r + " times speed"); // 0.75×, 1×, …
      b.addEventListener("click", function () {
        audio.playbackRate = r;
        rate = r;
        saveRate(r);
        setActive(r);
      });
      speed.appendChild(b);
      btns.push({ r: r, el: b });
    });
    setActive(rate);

    audio.addEventListener("ratechange", function () {
      if (audio.playbackRate !== rate) { rate = audio.playbackRate; setActive(rate); }
    });

    player.appendChild(speed);
  }

  function init() {
    var players = document.querySelectorAll(".listen-player");
    if (!players.length) return;
    injectStyles();
    for (var i = 0; i < players.length; i++) enhance(players[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
