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
      },
      {
        tab: "Psalms 1–2", tabsub: "Wordplay (Hebrew)", form: "Wordplay — One Verb, Two Ways", meta: "הָגָה hagah · Psalm 1:2 & 2:1", type: "wordplay",
        blurb: "The two gateway psalms hide a pun the English cannot show. The very same Hebrew verb — hagah — is used of the righteous and of the rebels, and it points opposite directions depending on the heart doing it.",
        lines: [
          { g: "", role: "frame", ref: "Psalm 1:2 · the righteous", html: 'in his law doth he <span class="pmw-kw">meditate</span> <b class="pmw-heb">יֶהְגֶּה</b> day and night' },
          { g: "", role: "frame", ref: "Psalm 2:1 · the nations", html: 'the people <span class="pmw-kw">imagine</span> <b class="pmw-heb">יֶהְגּוּ</b> a vain thing' }
        ],
        notation: "הָגָה &nbsp;hagah — “to murmur”: meditate · mutter · plot",
        a: { Relation: "One root, ה־ג־ה, binds Psalm 1 to Psalm 2.", Key: "the righteous *hagah* God’s law; the nations *hagah* a vain scheme", Function: "Links the Psalter’s twin gateway psalms and asks what a heart’s constant murmuring is filled with.", Claim: "strong (shared root); the deliberate link is the standard reading", Caution: "The KJV splits the one verb into “meditate” and “imagine,” so the pun is invisible in English. Root range from BLB (H1897): to mutter → meditate → plot." }
      },
      {
        tab: "Psalm 46", tabsub: "Wordplay (Hebrew)", form: "Wordplay — Keyword Reversal", meta: "מוֹט mot · Psalm 46:2, 5, 6", type: "wordplay",
        blurb: "Psalm 46 strikes one Hebrew word three times — mot, “to totter.” Everything in the world totters; the city of God, pointedly, does not. English hides that it is all the same word.",
        lines: [
          { g: "", role: "frame", ref: "Psalm 46:2 · the mountains", html: 'the mountains be <span class="pmw-kw">carried</span> <b class="pmw-heb">מוֹט</b> into the sea' },
          { g: "", role: "pair2", ref: "Psalm 46:5 · the city of God", html: 'she shall <span class="pmw-ct">not be moved</span> <b class="pmw-heb">בַּל־תִּמּוֹט</b>' },
          { g: "", role: "frame", ref: "Psalm 46:6 · the kingdoms", html: 'the kingdoms were <span class="pmw-kw">moved</span> <b class="pmw-heb">מָטוּ</b>' }
        ],
        notation: "מוֹט &nbsp;mot — “totter, slip” &nbsp;(×3; the city: NOT)",
        a: { Relation: "The root מ־ו־ט sounds three times — mountains, city, kingdoms.", Key: "the cosmos totters · the kingdoms totter · but the city of God “shall not totter” (bal-timmot)", Function: "The repeated keyword makes God’s city the one unshakable thing in a tottering world.", Claim: "strong", Caution: "The KJV renders the one root “carried,” “moved,” “moved,” so the contrast is invisible in English. Psalm 46 does the same trick with הָמָה hamah, “roar” — its waters roar and its nations roar. Roots from BLB (H4131; H1993)." }
      },
      {
        tab: "Psalm 25", tabsub: "Acrostic (Hebrew)", form: "Alphabetic Acrostic", meta: "Aleph → Tav · Psalm 25", type: "acrostic",
        blurb: "Here is a poem you cannot see in English at all. In the Hebrew, every verse of Psalm 25 begins with the next letter of the alphabet — a whole A-to-Z of trust running down the margin. Watch the aleph-bet descend.",
        rows: [
          { l: "א", n: "aleph", ref: "25:1", he: "<span class=\"pmw-w\" data-lang=\"he\" data-tip=\"dāviḏ · to David = &quot;beloved&quot; youngest son of Jesse and second…\">לְדָוִ֡ד</span> <span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"&#x27;ēl · to, toward, unto (of motion) you\">אֵלֶ֥יךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְ֝הוָ֗ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nep̄eš · my soul, self, life\">נַפְשִׁ֥י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāśā&#x27; · to lift, bear up, carry\">אֶשָּֽׂא</span>", en: "Unto thee, O LORD, do I lift up my soul." },
          { l: "ב", n: "bet", ref: "25:2", he: "<span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ĕlōhîm · my God\">אֱֽלֹהַ֗י</span> <span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"in you\">בְּךָ֣</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bāṭaḥ · to trust\">בָ֭טַחְתִּי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;al · not, no, nor\">אַל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bûš · to put to shame, be ashamed, be disconcerted\">אֵב֑וֹשָׁה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;al · not, no, nor\">אַל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿālaṣ · to rejoice, exult to exult\">יַֽעַלְצ֖וּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ōyēḇ · my enemy\">אֹיְבַ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"to me\">לִֽי</span>", en: "O my God, I trust in thee: let me not be ashamed." },
          { l: "ג", n: "gimel", ref: "25:3", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"also, even, indeed\">גַּ֣ם</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kôl · all, the whole all, the whole of any\">כָּל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"qāvâ · your to wait, look for, hope\">קֹ֭וֶיךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lō&#x27; · not, no not (with verb - absolute prohibition) not…\">לֹ֣א</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bûš · to put to shame, be ashamed, be disconcerted\">יֵבֹ֑שׁוּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bûš · to put to shame, be ashamed, be disconcerted\">יֵ֝בֹ֗שׁוּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bāḡaḏ · the to act treacherously, deceitfully, deal…\">הַבּוֹגְדִ֥ים</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"rêqām · vainly, emptilyin empty condition, empty\">רֵיקָֽם</span>", en: "Let none that wait on thee be ashamed." },
          { l: "ד", n: "dalet", ref: "25:4", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"dereḵ · your way, road, distance\">דְּרָכֶ֣יךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְ֭הוָה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāḏaʿ · to know to know to know, learn to know to perceive… me\">הוֹדִיעֵ֑נִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ōraḥ · your way, path\">אֹ֖רְחוֹתֶ֣יךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lāmaḏ · to learn. teach, exercise in to learn to teach to… me\">לַמְּדֵֽנִי</span>", en: "Shew me thy ways, O LORD; teach me thy paths." },
          { l: "ה", n: "he", ref: "25:5", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"dāraḵ · to tread, bend, lead me\">הַדְרִ֘יכֵ֤נִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ĕmeṯ · in your feminine noun\">בַאֲמִתֶּ֨ךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lāmaḏ · and to learn. teach, exercise in to learn to teach to… me\">וְֽלַמְּדֵ֗נִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּֽי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;atâ · you (second pers. sing. masc.)\">אַ֭תָּה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ĕlōhîm · God\">אֱלֹהֵ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yēšaʿ · my deliverance, salvation, rescue\">יִשְׁעִ֑י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ēṯ · sign of the definite direct object, not translated… you\">אוֹתְךָ֥</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"qāvâ · to wait, look for, hope\">קִ֝וִּ֗יתִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kôl · all, the whole all, the whole of any\">כָּל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yôm · the day, time, year day (as opposed to night) day (24…\">הַיּֽוֹם</span>", en: "Lead me in thy truth, and teach me.", note: "vav (ו) folded in here" },
          { l: "ז", n: "zayin", ref: "25:6", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"zâkar · to remember, recall, mention\">זְכֹר</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"raḥam · your masculine noun womb absolute state masculine plural…\">רַחֲמֶ֣יךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְ֭הוָה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥeseḏ · and your goodness, kindness, faithfulness a reproach\">וַחֲסָדֶ֑יךָ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּ֖י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿôlām · from long duration, antiquity, futurity\">מֵעוֹלָ֣ם</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"hēm · they, these, the same\">הֵֽמָּה</span>", en: "Remember thy tender mercies and thy lovingkindnesses." },
          { l: "ח", n: "chet", ref: "25:7", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"ḥaṭṭā&#x27;āṯ · sin, sinful sin, sin offering sin condition of sin\">חַטֹּ֤אות</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāʿur · my youth, early life\">נְעוּרַ֨י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"pešaʿ · and my transgression, rebelliontransgression (against…\">וּפְשָׁעַ֗י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;al · not, no, nor\">אַל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"zâkar · to remember, recall, mention\">תִּ֫זְכֹּ֥ר</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥeseḏ · as your goodness, kindness, faithfulness a reproach\">כְּחַסְדְּךָ֥</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"zâkar · to remember, recall, mention\">זְכָר</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"to me\">לִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;atâ · you (second pers. sing. masc.)\">אַ֑תָּה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"maʿan · purpose, intent preposition for the sake of in view…\">לְמַ֖עַן</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ṭûḇ · your goods, good things, goodness good things goods\">טוּבְךָ֣</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְהוָֽה</span>", en: "Remember not the sins of my youth." },
          { l: "ט", n: "tet", ref: "25:8", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"ṭôḇ · adjective good, pleasant, agreeable pleasant\">טוֹב</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāšār · and straight, upright, correct\">וְיָשָׁ֥ר</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְהוָ֑ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿal · preposition upon, on the ground of, according to\">עַל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kēn · adverb so, therefore, thus thus\">כֵּ֤ן</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yārâ · to throw, shoot, cast\">יוֹרֶ֖ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥaṭṭā&#x27; · masculine noun sinners adjective sinful exposed to…\">חַטָּאִ֣ים</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"dereḵ · in the way, road, distance\">בַּדָּֽרֶךְ</span>", en: "Good and upright is the LORD." },
          { l: "י", n: "yod", ref: "25:9", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"dāraḵ · to tread, bend, lead\">יַדְרֵ֣ךְ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿānāv · poor, humble, afflicted\">עֲ֭נָוִים</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"mišpāṭ · in the judgment, justice, ordinance judgment act of…\">בַּמִּשְׁפָּ֑ט</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lāmaḏ · and to learn. teach, exercise in to learn to teach to…\">וִֽילַמֵּ֖ד</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿānāv · poor, humble, afflicted\">עֲנָוִ֣ים</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"dereḵ · his way, road, distance\">דַּרְכּֽוֹ</span>", en: "The meek will he guide in judgment." },
          { l: "כ", n: "kaf", ref: "25:10", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"kôl · all, the whole all, the whole of any\">כָּל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ōraḥ · way, path\">אָרְח֣וֹת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְ֭הוָה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥeseḏ · goodness, kindness, faithfulness a reproach\">חֶ֣סֶד</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ĕmeṯ · and feminine noun\">וֶאֱמֶ֑ת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāṣar · to to guard, watch, watch over\">לְנֹצְרֵ֥י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bᵊrîṯ · his covenant, alliance, pledge\">בְ֝רִית֗וֹ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿēḏâ · and his testimony, witnessalways plural and always of laws…\">וְעֵדֹתָֽיו</span>", en: "All the paths of the LORD are mercy and truth." },
          { l: "ל", n: "lamed", ref: "25:11", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"maʿan · purpose, intent preposition for the sake of in view…\">לְמַֽעַן</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"šēm · your namenamereputation, fame, glorythe Name (as…\">שִׁמְךָ֥</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְהוָ֑ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"sālaḥ · and to forgive, pardon to forgive, pardon to be forgiven\">וְֽסָלַחְתָּ֥</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿāôn · to my perversity, depravity, iniquity\">לַ֝עֲוֺנִ֗י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"raḇ · adjective much, many, great much many abounding in…\">רַב</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"hû&#x27; · third person singular personal pronoun he, she, it…\">הֽוּא</span>", en: "For thy name's sake, O LORD, pardon mine iniquity." },
          { l: "מ", n: "mem", ref: "25:12", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"mî · who?, whose?, whom?\">מִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"zê · this, this one, here\">זֶ֣ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;îš · the man\">הָ֭אִישׁ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yārē&#x27; · fearing, reverent, afraid\">יְרֵ֣א</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְהוָ֑ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yārâ · to throw, shoot, cast him\">י֝וֹרֶ֗נּוּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"dereḵ · in way, road, distance\">בְּדֶ֣רֶךְ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bāḥar · to choose, elect, decide for\">יִבְחָֽר</span>", en: "What man is he that feareth the LORD?" },
          { l: "נ", n: "nun", ref: "25:13", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"nep̄eš · his soul, self, life\">נַ֭פְשׁוֹ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ṭôḇ · in adjective good, pleasant, agreeable pleasant\">בְּט֣וֹב</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lûn · to lodge, stop over, pass the night\">תָּלִ֑ין</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"zeraʻ · and his seed, offspring, descendants\">וְ֝זַרְע֗וֹ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāraš · to seize, dispossess, take possession off\">יִ֣ירַשׁ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ereṣ · land, earth\">אָֽרֶץ</span>", en: "His soul shall dwell at ease." },
          { l: "ס", n: "samekh", ref: "25:14", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"sôḏ · council, counsel, assembly council (of familiar…\">ס֣וֹד</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְ֭הוָה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yārē&#x27; · to his fearing, reverent, afraid\">לִירֵאָ֑יו</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bᵊrîṯ · and his covenant, alliance, pledge\">וּ֝בְרִית֗וֹ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāḏaʿ · to to know to know to know, learn to know to perceive… them\">לְהוֹדִיעָֽם</span>", en: "The secret of the LORD is with them that fear him." },
          { l: "ע", n: "ayin", ref: "25:15", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"ʿayin · my eyeeyeof physical eyeas showing mental qualitiesof…\">עֵינַ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"tāmîḏ · continuity, perpetuity, to stretchcontinually\">תָּ֭מִיד</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ēl · to, toward, unto (of motion)\">אֶל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"Yᵊhōvâ · the LORD (Yahweh)\">יְהוָ֑ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּ֤י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"hû&#x27; · third person singular personal pronoun he, she, it…\">הֽוּא</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāṣā&#x27; · to go out, come out, exit\">יוֹצִ֖יא</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"rešeṯ · from netnetfor catchingof judgment (fig)of leaders…\">מֵרֶ֣שֶׁת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"reḡel · my footfoot, legof God (anthropomorphic)of seraphim…\">רַגְלָֽי</span>", en: "Mine eyes are ever toward the LORD." },
          { l: "פ", n: "pe", ref: "25:16", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"pānâ · to turnto turn toward or from or awayto turn and…\">פְּנֵה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ēl · to, toward, unto (of motion) me\">אֵלַ֥י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥānan · and to be gracious, show favour, pity to show favour me\">וְחָנֵּ֑נִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּֽי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāḥîḏ · adjective only, only one, solitary\">יָחִ֖יד</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿānî · and poor, afflicted, humble\">וְעָנִ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ănî · I (first pers. sing. - usually used for emphasis)\">אָֽנִי</span>", en: "Turn thee unto me, and have mercy upon me." },
          { l: "צ", n: "tsade", ref: "25:17", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"ṣārâ · straits, distress, troublevexer\">צָר֣וֹת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"lēḇāḇ · my inner man, mind, will\">לְבָבִ֣י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"rāḥaḇ · to be or grow wide, be or grow large to be widened…\">הִרְחִ֑יבוּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"mᵊṣûqâ · from my straitness, distress, straits\">מִ֝מְּצֽוּקוֹתַ֗י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yāṣā&#x27; · to go out, come out, exit me\">הוֹצִיאֵֽנִי</span>", en: "The troubles of my heart are enlarged." },
          { l: "ק", n: "qof", ref: "—", en: "the qof line is skipped", flag: "gap" },
          { l: "ר", n: "resh", ref: "25:18", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"rā&#x27;â · to see, look at, inspect\">רְאֵ֣ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿŏnî · my affliction, poverty, miseryafflictionpoverty\">עָ֭נְיִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ʿāmāl · and my toil, trouble, labourtroubletrouble\">וַעֲמָלִ֑י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāśā&#x27; · and to lift, bear up, carry\">וְ֝שָׂ֗א</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kôl · to all, the whole all, the whole of any\">לְכָל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥaṭṭā&#x27;āṯ · my sin, sinful sin, sin offering sin condition of sin\">חַטֹּאותָֽי</span>", en: "Look upon mine affliction and my pain." },
          { l: "ר", n: "resh", ref: "25:19", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"rā&#x27;â · to see, look at, inspect\">רְאֵֽה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ōyēḇ · my enemy\">אוֹיְבַ֥י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"rāḇaḇ · to be or become many, be or become much, be or…\">רָ֑בּוּ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"śin&#x27;â · and hating, hatred, hatehatredof man\">וְשִׂנְאַ֖ת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥāmās · violence, wrong, cruelty\">חָמָ֣ס</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"śānē&#x27; · to hate, be hateful to hateof manof Godhater, one… me\">שְׂנֵאֽוּנִי</span>", en: "Consider mine enemies; for they are many.", note: "resh repeats" },
          { l: "ש", n: "shin", ref: "25:20", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"šāmar · to keep, guard, observe\">שָׁמְרָ֣ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nep̄eš · my soul, self, life\">נַ֭פְשִׁי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāṣal · and to snatch away, deliver, rescue me\">וְהַצִּילֵ֑נִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;al · not, no, nor\">אַל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"bûš · to put to shame, be ashamed, be disconcerted\">אֵ֝ב֗וֹשׁ</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּֽי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ḥāsâ · to seek refuge, flee for protectionto put trust in…\">חָסִ֥יתִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"in you\">בָֽךְ</span>", en: "O keep my soul, and deliver me." },
          { l: "ת", n: "tav", ref: "25:21", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"tōm · integrity, completenesscompleteness…\">תֹּם</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yōšer · and straightness, uprightness straightness, evenness…\">וָיֹ֥שֶׁר</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"nāṣar · to guard, watch, watch over me\">יִצְּר֑וּנִי</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kî · that, for, because\">כִּ֝֗י</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"qāvâ · to wait, look for, hope you\">קִוִּיתִֽיךָ</span>", en: "Let integrity and uprightness preserve me." },
          { l: "פ", n: "pe", ref: "25:22", he: "<span class=\"pmw-w pmw-w-key\" data-lang=\"he\" data-tip=\"pāḏâ · to ransom, redeem, rescue\">פְּדֵ֣ה</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ĕlōhîm · God\">אֱ֭לֹהִים</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"&#x27;ēṯ · sign of the definite direct object, not translated…\">אֶת</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"yiśrā&#x27;ēl · Israel = &quot;God prevails&quot; the second name for Jacob…\">יִשְׂרָאֵ֑ל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"kôl · from all, the whole all, the whole of any\">מִ֝כֹּ֗ל</span> <span class=\"pmw-w\" data-lang=\"he\" data-tip=\"ṣārâ · his straits, distress, troublevexer\">צָֽרוֹתָיו</span>", en: "Redeem Israel, O God, out of all his troubles.", flag: "extra" }
        ],
        notation: "א → ת &nbsp; (A to Z — then one more)",
        a: { Relation: "Each verse opens with the next Hebrew letter, aleph through tav.", Key: "22 letters = the whole alphabet · an ordered “A to Z” of prayer", Function: "Signals completeness — everything, start to finish, brought to God — and aids memory.", Claim: "strong", Caution: "Psalm 25’s acrostic is deliberately imperfect: vav folds into the he line, qof is skipped, resh repeats, and an extra pe is added at the end — a final cry, “Redeem Israel,” that breaks the alphabet on purpose." }
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
      if (m.type === "acrostic") {
        var acro = el("div", "pmw-acrostic");
        m.rows.forEach(function (r) {
          var row = el("div", "pmw-acro-row");
          if (r.flag) row.setAttribute("data-flag", r.flag);
          var note = r.note ? ' <span class="pmw-acro-note">' + r.note + '</span>' : "";
          var he = r.he ? '<div class="pmw-acro-he" lang="he" dir="rtl">' + r.he + '</div>' : "";
          row.innerHTML = '<div class="pmw-acro-letter" lang="he" dir="rtl">' + r.l +
            '<span class="pmw-acro-name">' + r.n + '</span></div>' +
            '<div class="pmw-acro-en"><span class="pmw-ref">' + r.ref + '</span>' + he +
            '<span class="pmw-acro-en-text">' + r.en + note + '</span></div>';
          acro.appendChild(row);
        });
        mapEl.appendChild(acro);
      } else {
        m.lines.forEach(function (ln) {
          var row = el("div", "pmw-line");
          row.setAttribute("data-role", ln.role);
          row.innerHTML = '<div class="pmw-gutter">' + (ln.g || "") + '</div>' +
            '<div><span class="pmw-ref">' + ln.ref + '</span><span class="pmw-text">' + ln.html + '</span></div>';
          row.addEventListener("click", function () { flash(ln.role); });
          mapEl.appendChild(row);
        });
      }
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
