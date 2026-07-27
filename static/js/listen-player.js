/* listen-player.js — progressive enhancement for the field-guide narration player.
 *
 * Play / pause and seek-to-any-position are already provided by the native
 * <audio controls> element. This adds the one control the native player hides
 * (or omits, depending on the browser): a visible playback-speed selector.
 *
 * Self-contained: injects its own styles, no-ops on pages without a
 * .listen-player, and remembers the chosen speed across sections and pages.
 */
(function () {
  "use strict";

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
    if (document.getElementById("lp-speed-styles")) return;
    var css =
      ".lp-speed{display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin-top:12px;}" +
      ".lp-speed-label{font-size:0.8em;font-weight:600;color:#6a8470;margin-right:2px;}" +
      ".lp-speed-btn{font:inherit;font-size:0.8em;line-height:1;cursor:pointer;" +
      "padding:6px 10px;min-height:32px;border-radius:999px;border:1px solid #cdddce;" +
      "background:#ffffff;color:#4a6b52;transition:background .15s,color .15s,border-color .15s;}" +
      ".lp-speed-btn:hover{background:rgba(74,107,82,0.10);}" +
      ".lp-speed-btn:focus-visible{outline:2px solid #4a6b52;outline-offset:2px;}" +
      ".lp-speed-btn.is-active{background:#4a6b52;color:#f2f5f2;border-color:#4a6b52;}";
    var s = document.createElement("style");
    s.id = "lp-speed-styles";
    s.textContent = css;
    document.head.appendChild(s);
  }

  function enhance(player) {
    if (player.dataset.speedReady) return;
    var audio = player.querySelector("audio");
    if (!audio) return;
    player.dataset.speedReady = "1";

    var rate = savedRate();
    audio.playbackRate = rate;

    var row = document.createElement("div");
    row.className = "lp-speed";
    row.setAttribute("role", "group");
    row.setAttribute("aria-label", "Playback speed");

    var label = document.createElement("span");
    label.className = "lp-speed-label";
    label.textContent = "Speed";
    row.appendChild(label);

    var btns = [];
    function setActive(r) {
      btns.forEach(function (o) {
        var on = o.r === r;
        o.el.classList.toggle("is-active", on);
        o.el.setAttribute("aria-pressed", on ? "true" : "false");
      });
    }

    RATES.forEach(function (r) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "lp-speed-btn";
      b.textContent = r + "×"; // 0.75×, 1×, 1.25×, 1.5×, 2×
      b.setAttribute("aria-label", "Play at " + r + " times speed");
      b.addEventListener("click", function () {
        audio.playbackRate = r;
        rate = r;
        saveRate(r);
        setActive(r);
      });
      row.appendChild(b);
      btns.push({ r: r, el: b });
    });
    setActive(rate);

    // If the browser's own speed menu changes the rate, keep our buttons honest.
    audio.addEventListener("ratechange", function () {
      if (audio.playbackRate !== rate) {
        rate = audio.playbackRate;
        setActive(rate);
      }
    });

    player.appendChild(row);
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
