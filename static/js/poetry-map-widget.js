/* Poetry Map Widget — interactive Hebrew poetic-form mapper.
   Renders any .poetry-map-widget[data-set] container from POEM_SETS below.
   Forms taxonomy adapted from the Translation Hub "Hebrew Poetic Forms"
   framework (attested forms only; Lowth-standard parallelism + poetics).
   Text: KJV. */
(function () {
  "use strict";

  var POEM_SETS = {
    psalms: [
      {
        tab: "Psalm 1:6", tabsub: "Antithetic",
        form: "Antithetic Parallelism", meta: "Bicolon · Psalm 1:6",
        blurb: "Two lines set in contrast. One phrase — “the way of” — leads to opposite destinies, drawing the moral boundary the whole Psalter opens upon.",
        lines: [
          { g: "A", role: "frame", ref: "1:6a", html: 'For the LORD knoweth <span class="pmw-kw">the way of</span> the righteous:' },
          { g: "B", role: "frame", ref: "1:6b", html: 'but <span class="pmw-kw">the way of</span> the ungodly shall <span class="pmw-ct">perish</span>.' }
        ],
        notation: "A &nbsp;&lt; &gt;&nbsp; B",
        a: { Relation: "Two destinies contrasted through one repeated phrase, “the way of.”", Key: "righteous ⟷ ungodly · knoweth ⟷ perish", Function: "Sets the two ways as the choice the whole book of Psalms opens upon.", Claim: "strong", Caution: "“Knoweth” means covenant care, not mere awareness — God keeps one way and lets the other perish." }
      },
      {
        tab: "Psalm 19:1", tabsub: "Synonymous",
        form: "Synonymous Parallelism", meta: "Two bicola · Psalm 19:1–2",
        blurb: "The second line restates the first with fresh images — not repetition but a deepening. Creation is given a voice that never stops speaking.",
        lines: [
          { g: "A", role: "frame", ref: "19:1a", html: 'The heavens declare the glory of God;' },
          { g: "A′", role: "frame", ref: "19:1b", html: 'and the firmament sheweth his handywork.' },
          { g: "B", role: "pair2", ref: "19:2a", html: 'Day unto day uttereth speech,' },
          { g: "B′", role: "pair2", ref: "19:2b", html: 'and night unto night sheweth knowledge.' }
        ],
        notation: "A // A′ &nbsp;·&nbsp; B // B′",
        a: { Relation: "Each pair says one thing twice, matching term for term.", Key: "heavens // firmament · declare // sheweth · day // night", Function: "Doubles the witness of creation so it feels continuous and total.", Claim: "strong", Caution: "The second colon is never filler; “firmament / handywork” adds a new image to “heavens / glory.”" }
      },
      {
        tab: "Psalm 19:7", tabsub: "Grammatical",
        form: "Grammatical Parallelism", meta: "Quatrain · Psalm 19:7–8",
        blurb: "Four lines share one exact grammatical shape: “The ___ of the LORD is ___, ___ing the ___.” Six names for the Torah, each with a quality and an effect.",
        lines: [
          { g: "A", role: "frame", ref: "19:7a", html: 'The <span class="pmw-kw">law</span> of the LORD is perfect, converting the soul:' },
          { g: "A", role: "frame", ref: "19:7b", html: 'the <span class="pmw-kw">testimony</span> of the LORD is sure, making wise the simple.' },
          { g: "A", role: "frame", ref: "19:8a", html: 'The <span class="pmw-kw">statutes</span> of the LORD are right, rejoicing the heart:' },
          { g: "A", role: "frame", ref: "19:8b", html: 'the <span class="pmw-kw">commandment</span> of the LORD is pure, enlightening the eyes.' }
        ],
        notation: "A // A // A // A &nbsp;(identical grammar)",
        a: { Relation: "One template repeats four times: [name] of the LORD · [quality] · [effect].", Key: "law · testimony · statutes · commandment — synonyms for the Torah", Function: "The drumbeat of matching clauses makes the law feel whole and life-giving.", Claim: "strong", Caution: "The parallel is grammatical as well as thematic — every clause shares subject-, verb-, and object-shape." }
      },
      {
        tab: "Psalm 29:1", tabsub: "Staircase",
        form: "Staircase / Climactic Progression", meta: "Tricolon · Psalm 29:1–2",
        blurb: "Each line repeats a phrase and adds to it, climbing like a stair. The summons “Give unto the LORD” mounts three times toward its climax.",
        lines: [
          { g: "A", role: "frame", ref: "29:1a", html: '<span class="pmw-kw">Give unto the LORD</span>, O ye mighty,' },
          { g: "A+", role: "frame", ref: "29:1b", html: '<span class="pmw-kw">give unto the LORD</span> <span class="pmw-pr">glory and strength</span>.' },
          { g: "A++", role: "frame", ref: "29:2a", html: '<span class="pmw-kw">Give unto the LORD</span> <span class="pmw-pr">the glory due unto his name</span>;' }
        ],
        notation: "A &nbsp;&gt;&nbsp; A+ &nbsp;&gt;&nbsp; A++",
        a: { Relation: "A repeated summons is extended and intensified with each step.", Key: "“Give unto the LORD” × 3 · glory → glory due unto his name", Function: "Builds momentum and a chant-like pressure toward worship.", Claim: "strong", Caution: "A true staircase needs repetition plus advancement — here the phrase repeats and the object grows." }
      },
      {
        tab: "Psalm 2", tabsub: "Chiasm",
        form: "Chiasm", meta: "Concentric · Psalm 2:1–12",
        blurb: "A mirrored structure that turns on its center. The raging kings on the outside frame God’s answer within — and at the very heart stands the enthroned Son on Zion.",
        lines: [
          { g: "A", role: "frame", ref: "2:1–3", html: 'Why do the heathen rage… the kings of the earth set themselves… <span class="pmw-ct">against the LORD, and against his anointed</span>… Let us break their bands asunder.' },
          { g: "B", role: "pair2", ref: "2:4–5", html: 'He that sitteth in the heavens shall laugh… Then shall he speak unto them in his wrath.' },
          { g: "X", role: "center", ref: "2:6–7", html: 'Yet have I set my king upon my holy hill of Zion… the LORD hath said unto me, <span class="pmw-kw">Thou art my Son</span>; this day have I begotten thee.' },
          { g: "B′", role: "pair2", ref: "2:8–9", html: 'Ask of me, and I shall give thee the heathen for thine inheritance… Thou shalt break them with a rod of iron.' },
          { g: "A′", role: "frame", ref: "2:10–12", html: 'Be wise now therefore, O ye kings… <span class="pmw-ct">Kiss the Son</span>, lest he be angry… Blessed are all they that put their trust in him.' }
        ],
        notation: "A – B – X – B′ – A′",
        a: { Relation: "The kings of the earth frame the psalm (A / A′); God’s power answers within (B / B′); the enthroned Son is the center (X).", Key: "A/A′ the raging → warned kings · B/B′ wrath → iron rod · X “Thou art my Son” on Zion", Function: "The mirror throws all the weight onto the center — the Anointed King installed on Zion.", Claim: "moderate", Caution: "A stanza-level concentric reading: claimed on the mirrored themes and the clear Zion/Sonship pivot, not word-for-word symmetry." }
      },
      {
        tab: "Psalm 8:1,9", tabsub: "Inclusio",
        form: "Inclusio", meta: "Frame · Psalm 8:1 & 8:9",
        blurb: "The very same line opens and closes the psalm, sealing everything between it inside a single frame — and naming its theme: the LORD’s excellent name.",
        lines: [
          { g: "A", role: "frame", ref: "8:1", html: 'O LORD our Lord, <span class="pmw-kw">how excellent is thy name in all the earth</span>!' },
          { g: "", role: "interior", ref: "8:2–8", html: 'babes and sucklings · the moon and the stars · what is man · crowned with glory · dominion over the works of thy hands' },
          { g: "A′", role: "frame", ref: "8:9", html: 'O LORD our Lord, <span class="pmw-kw">how excellent is thy name in all the earth</span>!' }
        ],
        notation: "A &nbsp;…&nbsp; A′ &nbsp;(identical frame)",
        a: { Relation: "An identical opening and closing line encloses the whole psalm.", Key: "“how excellent is thy name in all the earth” — word-for-word repeated", Function: "Marks where the unit begins and ends, and names its subject: God’s name.", Claim: "strong", Caution: "Inclusio requires a real return of words or theme — here the frame is verbatim, the strongest kind." }
      },
      {
        tab: "Psalm 8", tabsub: "Ring",
        form: "Ring Composition", meta: "Framed center · Psalm 8:1–9",
        blurb: "The inclusio becomes a ring: matched frames on the outside, and at the turning point, the psalm’s great question — what is man?",
        lines: [
          { g: "A", role: "frame", ref: "8:1", html: 'O LORD our Lord, how excellent is thy name…' },
          { g: "B", role: "interior", ref: "8:3", html: 'When I consider thy heavens… the moon and the stars, which thou hast ordained;' },
          { g: "X", role: "center", ref: "8:4", html: 'What is man, that thou art mindful of him? and the son of man, that thou visitest him?' },
          { g: "B′", role: "interior", ref: "8:6", html: 'Thou madest him to have dominion over the works of thy hands;' },
          { g: "A′", role: "frame", ref: "8:9", html: 'O LORD our Lord, how excellent is thy name…' }
        ],
        notation: "A – B – X – B′ – A′",
        a: { Relation: "Mirrored members surround a center: name (A) · cosmos (B) · humanity (X).", Key: "the pivot is “what is man” — smallness set against the starry frame", Function: "The ring throws the weight onto the center — human dignity inside God’s vast name.", Claim: "moderate", Caution: "Ring composition is claimed only where the members truly correspond; Psalm 8’s frame is verbatim, its center clearly the hinge." }
      },
      {
        tab: "Psalm 24:7", tabsub: "Call & Response",
        form: "Call-and-Response (Responsorial)", meta: "Antiphonal · Psalm 24:7–10",
        blurb: "A liturgy for two voices at the temple gate: a summons, a challenge sung back — “Who is this King of glory?” — and the answer. Then it all repeats, intensified.",
        lines: [
          { g: "1", role: "frame", ref: "24:7", html: 'Lift up your heads, O ye gates… and the King of glory shall come in.' },
          { g: "?", role: "quest", ref: "24:8a", html: 'Who is this King of glory?' },
          { g: "!", role: "pair2", ref: "24:8b", html: 'The LORD strong and mighty, the LORD mighty in battle.' },
          { g: "1", role: "frame", ref: "24:9", html: 'Lift up your heads, O ye gates… and the King of glory shall come in.' },
          { g: "?", role: "quest", ref: "24:10a", html: 'Who is this King of glory?' },
          { g: "!", role: "pair2", ref: "24:10b", html: 'The LORD of hosts, he is the King of glory.' }
        ],
        notation: "Call → Q? → Answer &nbsp;(×2, rising)",
        a: { Relation: "Three voices alternate: summons, question, answer — then the cycle repeats.", Key: "“Who is this King of glory?” asked twice; answered “mighty in battle,” then “LORD of hosts”", Function: "Turns the psalm into a processional dialogue — likely sung antiphonally at the gates.", Claim: "strong", Caution: "The second answer heightens the first (“of hosts”), so the repetition advances rather than merely echoes." }
      },
      {
        tab: "Psalm 23:1", tabsub: "Metaphor",
        form: "Emblematic / Metaphor", meta: "Image + referent · Psalm 23:1–2",
        blurb: "One line gives an image, the next its meaning. The metaphor of the shepherd carries the doctrine of God’s provision better than any statement could.",
        lines: [
          { g: "IMG", role: "pair2", ref: "23:1a", html: '<span class="pmw-pr">The LORD is my shepherd;</span>' },
          { g: "→", role: "frame", ref: "23:1b", html: 'I shall not want.' },
          { g: "IMG", role: "pair2", ref: "23:2a", html: '<span class="pmw-pr">He maketh me to lie down in green pastures:</span>' },
          { g: "→", role: "frame", ref: "23:2b", html: 'he leadeth me beside the still waters.' }
        ],
        notation: "IMAGE &nbsp;⇒&nbsp; REFERENT",
        a: { Relation: "Each image line is paired with the provision it pictures.", Key: "shepherd ⇒ “I shall not want” · green pastures / still waters ⇒ rest & guidance", Function: "Teaches through a picture the hearer can feel, not just a claim to accept.", Claim: "strong", Caution: "Identify which line is the image and which is the point; the doctrine rides on the metaphor." }
      }
    ]
  };

  var LEGEND = [
    ["frame", "Matching pair / frame"], ["pair2", "Second pair"], ["quest", "Question member"],
    ["center", "Center / pivot"], ["key", "Repeated keyword"], ["contrast", "Contrast / reversal"],
    ["prog", "Progression"]
  ];

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  function build(container) {
    var set = container.getAttribute("data-set") || "psalms";
    var maps = POEM_SETS[set];
    if (!maps) { container.innerHTML = '<p>Poem set “' + set + '” not found.</p>'; return; }

    // legend
    var legend = el("div", "pmw-legend");
    legend.appendChild(el("h4", null, "How to read the map"));
    var lg = el("div", "pmw-legend-grid");
    LEGEND.forEach(function (p) {
      lg.appendChild(el("span", "pmw-lg", '<span class="pmw-sw ' + p[0] + '"></span>' + p[1]));
    });
    legend.appendChild(lg);
    container.appendChild(legend);

    // chips
    var chips = el("nav", "pmw-chips");
    chips.setAttribute("role", "tablist");
    container.appendChild(chips);

    // panel
    var panel = el("article", "pmw-panel");
    var head = el("div", "pmw-head");
    var fname = el("h3", "pmw-form-name");
    var fmeta = el("p", "pmw-form-meta");
    var fblurb = el("p", "pmw-blurb");
    head.appendChild(fname); head.appendChild(fmeta); head.appendChild(fblurb);
    var mapEl = el("div", "pmw-map");
    var notEl = el("div", "pmw-notation");
    var analysis = el("div", "pmw-analysis");
    var revealBtn = el("button", "pmw-reveal", "▸ Reveal the analysis");
    revealBtn.type = "button"; revealBtn.setAttribute("aria-expanded", "false");
    var acard = el("dl", "pmw-acard");
    analysis.appendChild(revealBtn); analysis.appendChild(acard);
    panel.appendChild(head); panel.appendChild(mapEl); panel.appendChild(notEl); panel.appendChild(analysis);
    container.appendChild(panel);

    container.appendChild(el("p", "pmw-provenance",
      "Text: KJV · Forms: standard biblical Hebrew poetics (Lowth) — Translation Hub framework"));

    function flash(role) {
      if (role === "interior") return;
      Array.prototype.forEach.call(mapEl.children, function (row) {
        if (row.getAttribute("data-role") === role) {
          row.classList.remove("pmw-flash"); void row.offsetWidth; row.classList.add("pmw-flash");
        }
      });
    }

    function select(i) {
      var m = maps[i];
      Array.prototype.forEach.call(chips.children, function (c, ci) {
        c.setAttribute("aria-selected", ci === i ? "true" : "false");
      });
      fname.textContent = m.form; fmeta.textContent = m.meta; fblurb.textContent = m.blurb;
      mapEl.innerHTML = "";
      m.lines.forEach(function (ln) {
        var row = el("div", "pmw-line");
        row.setAttribute("data-role", ln.role);
        row.innerHTML = '<div class="pmw-gutter">' + (ln.g || "") + '</div>' +
          '<div><span class="pmw-ref">' + ln.ref + '</span><span class="pmw-text">' + ln.html + '</span></div>';
        row.addEventListener("click", function () { flash(ln.role); });
        mapEl.appendChild(row);
      });
      notEl.innerHTML = m.notation;
      acard.innerHTML = "";
      Object.keys(m.a).forEach(function (k) {
        var v = m.a[k];
        if (k === "Claim") {
          v = '<span class="' + (v === "strong" ? "pmw-claim-strong" : "pmw-claim-mod") + '">' + v + "</span>";
        }
        var row = el("div", "pmw-arow");
        row.innerHTML = "<dt>" + k + "</dt><dd>" + v + "</dd>";
        acard.appendChild(row);
      });
      acard.classList.remove("pmw-open");
      revealBtn.setAttribute("aria-expanded", "false");
      revealBtn.textContent = "▸ Reveal the analysis";
    }

    maps.forEach(function (m, i) {
      var b = el("button", "pmw-chip", m.tab + "<b>" + m.tabsub + "</b>");
      b.type = "button"; b.setAttribute("role", "tab");
      b.addEventListener("click", function () { select(i); });
      chips.appendChild(b);
    });
    revealBtn.addEventListener("click", function () {
      var open = acard.classList.toggle("pmw-open");
      revealBtn.setAttribute("aria-expanded", open ? "true" : "false");
      revealBtn.textContent = open ? "▾ Hide the analysis" : "▸ Reveal the analysis";
    });
    select(0);
  }

  function init() {
    var nodes = document.querySelectorAll(".poetry-map-widget");
    Array.prototype.forEach.call(nodes, build);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
