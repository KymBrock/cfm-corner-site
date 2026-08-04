---
title: "Caught Between Two Empires"
description: "Judah's last forty years were one recurring question — Egypt or Babylon? — and its kings kept betting on Egypt. Why the prophets said Babylon, and why every wrong bet ended at a siege wall."
draft: true
---

{{< rawhtml >}}

<div style="max-width: 750px; margin: 0 auto;">

<img src="/images/culture/babylon/02b-hero.png" alt="Judah caught between the empires of Egypt and Babylon" style="width: 100%; height: auto; border-radius: 18px; box-shadow: 0 10px 24px rgba(0,0,0,0.08);">

<h2 style="text-align: center;">Caught Between Two Empires</h2>

<p style="text-align: center; color: #666; font-style: italic; margin-bottom: 2rem;">Why Judah&rsquo;s last kings kept betting on Egypt &mdash; and why the prophets said Babylon</p>

<!-- LISTEN PLAYER (section narration) -->
<div class="listen-player">
<div class="lp-head">
<span class="lp-icon" aria-hidden="true"></span>
<span class="lp-title">Listen to this section</span>
</div>
<audio controls preload="none">
<source src="/audio/culture/babylon/02b-two-empires.mp3" type="audio/mpeg">
Your browser doesn&rsquo;t support the audio element &mdash; <a href="/audio/culture/babylon/02b-two-empires.mp3">download the audio</a> instead.
</audio>
</div>
<!-- /LISTEN PLAYER -->

<p>For the last forty years of its life, the kingdom of Judah faced one question, over and over &mdash; and each answer decided everything: when the great powers collide, whose side are you on? To the south lay <strong>Egypt</strong>, the old familiar patron. To the east rose <strong>Babylon</strong>, new and terrible. Judah was too small to stand alone. And it sat right on the road between the two, so it could not be left alone either. Again and again, its kings bet on Egypt. Every bet failed. Here is what lifts this above ordinary politics: Judah&rsquo;s prophets were not neutral observers. Jeremiah, above all, insisted that Babylon was the safer road &mdash; and the God-appointed one. For saying so, he was branded a traitor. This section is the <em>why</em> behind the dates in <a href="/culture/ancient/babylon/02-timeline-and-empires/">Section 02</a> and the portraits in <a href="/culture/ancient/babylon/03-nebuchadnezzar-and-the-kings/">Section 03</a>.</p>

<!-- ===== JUDAH BETWEEN THE EMPIRES (jbe) ===== -->
<style>
.ers { border:1px solid #e2ddd3; border-radius:16px; overflow:hidden; margin:26px 0; background:#fbf9f5; box-shadow:0 6px 18px rgba(0,0,0,.07); font-family:-apple-system,Segoe UI,Roboto,sans-serif; }
.ers-head { padding:16px 18px 4px; }
.ers-head h4 { margin:0; font-size:1.05rem; color:#3c3a33; }
.ers-head p { margin:4px 0 0; font-size:.82rem; color:#8a8172; }
.ers-stage { position:relative; background:#dfe6e2; line-height:0; }
.ers-stage .ers-map { display:block; width:100%; height:auto; margin:0; opacity:0; transition:opacity .55s ease; }
.ers-map:first-of-type { position:relative; }
.ers-map:not(:first-of-type) { position:absolute; top:0; left:0; }
.ers-map.active { opacity:1; }
.ers-yrbadge { position:absolute; top:12px; left:14px; z-index:2; background:rgba(56,55,49,.72); color:#fff; font-size:.8rem; font-weight:800; letter-spacing:.03em; padding:4px 11px; border-radius:999px; }
.ers-cap { padding:12px 18px 6px; font-size:.9rem; line-height:1.5; color:#443f37; min-height:4.2em; border-top:1px solid #eee6d8; }
.ers-cap b { color:#7a3030; }
.ers-time { display:flex; gap:0; padding:8px 12px 18px; position:relative; }
.ers-time::before { content:""; position:absolute; left:60px; right:60px; top:16px; height:3px; background:#e0d8c7; border-radius:3px; }
.ers-step { flex:1; background:none; border:none; cursor:pointer; padding:0; display:flex; flex-direction:column; align-items:center; gap:7px; font-family:inherit; position:relative; z-index:1; }
.ers-dot { width:22px; height:22px; border-radius:50%; background:#fff; border:3px solid #c9b98f; transition:transform .2s,background .2s,border-color .2s; }
.ers-step.is-active .ers-dot { transform:scale(1.3); background:#c65528; border-color:#c65528; }
.ers-yr { font-size:.82rem; font-weight:800; color:#5a544a; }
.ers-lbl { font-size:.68rem; color:#8a8172; line-height:1.15; max-width:120px; }
.ers-step.is-active .ers-yr { color:#3c3a33; }
.ers-cred { text-align:center; font-size:.68rem; font-style:italic; color:#a89f90; padding:0 12px 12px; }
@media (max-width:560px){ .ers-lbl{ display:none; } .ers-time::before{ left:40px; right:40px; } }
</style>

<div class="ers">
  <div class="ers-head"><h4>Judah Between the Empires</h4>
  <p>Slide through the century that trapped Judah &mdash; from Assyria&rsquo;s iron grip to the rise of Babylon.</p></div>
  <div class="ers-stage" id="ers-stage">
    <span class="ers-yrbadge" id="ers-badge"></span>
    <img class="ers-map" src="/images/culture/babylon/maps/era-700bc.jpg" alt="The Assyrian empire at its height, c. 700 BC" loading="lazy">
    <img class="ers-map" src="/images/culture/babylon/maps/era-600bc.jpg" alt="The Near East after Assyria's fall, c. 600 BC: Babylon, Media, Lydia and Egypt" loading="lazy">
    <img class="ers-map" src="/images/culture/babylon/maps/era-500bc.jpg" alt="The Achaemenid Persian empire, c. 500 BC, stretching from the Aegean and Egypt to the Indus" loading="lazy">
  </div>
  <p class="ers-cap" id="ers-cap"></p>
  <div class="ers-time" id="ers-time"></div>
  <div class="ers-cred">Maps by CFM Corner on a S&eacute;mhur relief base (CC BY-SA 4.0)</div>
</div>

<script>
(function(){
  var ERAS=[
    {yr:"700 BC",lbl:"Assyria dominant",cap:"<b>700 BC &mdash; the Assyrian century.</b> One empire rules from Anatolia to the Gulf. The northern kingdom of <b>Israel</b> is already gone &mdash; its ten tribes deported &mdash; and <b>Judah</b> survives only as a trembling Assyrian vassal. Egypt watches from the southwest; Media stirs in the east."},
    {yr:"600 BC",lbl:"Babylon rising",cap:"<b>600 BC &mdash; Assyria shattered.</b> In a single generation the giant fell. <b>Babylon</b> and its Median ally have seized the old Assyrian heartland, while Lydia and Egypt carve off the west. Judah is left exactly where this section begins: caught between <b>Egypt</b> and <b>Babylon</b>, every wrong bet ending at a siege wall."},
    {yr:"500 BC",lbl:"Persia &amp; the return",cap:"<b>500 BC &mdash; the empire of deliverance.</b> Babylon itself has now fallen &mdash; to <b>Cyrus of Persia</b>, who let the exiles go home. The Achaemenid empire, the largest the world had yet seen, now rules from the Aegean to the Indus, Egypt included, and restored <b>Judah</b> is a small province within it. (Its story fills the <a href=\"/culture/ancient/achaemenid/\">Achaemenid guide</a>.)"}
  ];
  var stage=document.getElementById('ers-stage'),imgs=stage.querySelectorAll('.ers-map'),time=document.getElementById('ers-time'),cap=document.getElementById('ers-cap'),badge=document.getElementById('ers-badge');
  function show(n){
    for(var i=0;i<imgs.length;i++) imgs[i].classList.toggle('active',i===n);
    var btns=time.querySelectorAll('.ers-step'); for(var j=0;j<btns.length;j++) btns[j].classList.toggle('is-active',j===n);
    cap.innerHTML=ERAS[n].cap; badge.textContent=ERAS[n].yr;
  }
  ERAS.forEach(function(e,idx){
    var b=document.createElement('button'); b.className='ers-step'; b.type='button';
    b.innerHTML='<span class="ers-dot"></span><span class="ers-yr">'+e.yr+'</span><span class="ers-lbl">'+e.lbl+'</span>';
    b.addEventListener('click',function(){ show(idx); });
    time.appendChild(b);
  });
  show(0);
})();
</script>
<!-- ===== /jbe ===== -->

<br>

<hr>

<br>

<h3>Josiah&rsquo;s Fatal Gamble (609 BC)</h3>

<p>The turning point came before Babylon ever threatened Jerusalem. In 609 BC, Pharaoh <strong>Necho II</strong> marched his army north &mdash; not to attack Assyria, but to prop it up. Assyria was collapsing under Babylonian and Median blows. Egypt preferred a weak old neighbor to a strong new one, so it moved to save the dying giant. That sounds backwards if you know the King James Version, which says Necho &ldquo;went up <em>against</em> the king of Assyria&rdquo; (<a href="https://www.blueletterbible.org/kjv/2ki/23/29/" target="_blank" data-ref="2 Kings 23:29">2 Kings 23:29</a>). But the Hebrew preposition <em>&lsquo;al</em> can just as well mean &ldquo;to&rdquo; or &ldquo;in support of,&rdquo; and the Babylonian Chronicle settles it: in 609 Egypt and Assyria were <em>allies</em>, jointly trying to retake Harran from Babylon. Modern translations read &ldquo;went up <em>to</em> the king of Assyria&rdquo; &mdash; to help him.</p>

<p>Into that march stepped King <strong>Josiah</strong> of Judah. He intercepted Necho at Megiddo, and he was killed there (<a href="https://www.blueletterbible.org/kjv/2ch/35/20/" target="_blank" data-ref="2 Chronicles 35:20-24">2 Chronicles 35:20&ndash;24</a>). Whatever he intended, the effect is plain: by trying to keep Egypt from reinforcing Assyria, Josiah&rsquo;s death-ride objectively served <strong>Babylon</strong>. And notice who ruled Babylon at that moment. Not Nebuchadnezzar &mdash; not yet &mdash; but his father, <strong>Nabopolassar</strong>. Nebuchadnezzar was still the crown prince. He would not win Carchemish or take the throne until 605, four years after Josiah was already dead.</p>

<figure class="fg-figure">
  <img src="/images/culture/babylon/photos/tel-megiddo.jpg" alt="The ruins of Tel Megiddo, Israel" loading="lazy">
  <figcaption>Tel Megiddo &mdash; the strategic mound guarding the pass where Josiah rode out to stop Necho in 609 BC, and was killed. Its Greek name, Armageddon, became scripture&rsquo;s word for the last battle. <span class="fg-credit">Photo &copy; Anagoria, Wikimedia Commons (CC BY 3.0)</span></figcaption>
</figure>

<div style="background: linear-gradient(135deg, #f5f3f0 0%, #ebe7e1 100%); padding: 20px 24px; border-radius: 8px; margin: 24px 0;">
<p style="margin: 0;"><strong>One preposition, two directions:</strong> <a href="https://www.blueletterbible.org/kjv/2ki/23/29/" target="_blank" data-ref="2 Kings 23:29">2 Kings 23:29</a> has Necho going &ldquo;against the king of Assyria,&rdquo; and for most of history that was read as war between them. But the Hebrew <em>&lsquo;al</em> is simply ambiguous &mdash; &ldquo;against,&rdquo; but also &ldquo;to&rdquo; or &ldquo;alongside.&rdquo; The cuneiform record of 609 BC shows Egyptian and Assyrian troops besieging Harran <em>together</em> &mdash; so the second sense is the right one. A single small word, and the whole shape of the war turns on which way it points.</p>
</div>

<p>Why did Josiah do it? That is genuinely debated, and here the guide is reading between the lines rather than quoting them. Scripture never states his motive, and there is <em>no</em> record of a formal treaty between Judah and Babylon. Some historians see a simple bid to protect the independence he had won. Others notice that his reforms had reached north into the old kingdom of Israel &mdash; to Bethel and &ldquo;the cities of Samaria&rdquo; (<a href="https://www.blueletterbible.org/kjv/2ki/23/15/" target="_blank" data-ref="2 Kings 23:15-20">2 Kings 23:15&ndash;20</a>; <a href="https://www.blueletterbible.org/kjv/2ch/34/6/" target="_blank" data-ref="2 Chronicles 34:6">2 Chronicles 34:6</a>) &mdash; and they read in his stand a larger hope: that a Davidic king who broke Assyria&rsquo;s and Egypt&rsquo;s grip on the north might one day gather the scattered northern tribes home. That is a reasonable and moving reading. But it is a <em>reading</em>. What the sources give us is the act and its consequence, not the inside of the king&rsquo;s mind.</p>

<br>

<hr>

<br>

<h3>The Two Parties</h3>

<p>Josiah&rsquo;s death handed Judah straight back to Egypt. Necho deposed <strong>Jehoahaz</strong>, Josiah&rsquo;s chosen heir, installed <strong>Jehoiakim</strong> in his place, and levied a crushing tribute (<a href="https://www.blueletterbible.org/kjv/2ki/23/33/" target="_blank" data-ref="2 Kings 23:33-35">2 Kings 23:33&ndash;35</a>). For the next generation, Judah&rsquo;s court was Egypt&rsquo;s client by default. A pro-Egypt party ran its foreign policy &mdash; always betting the southern patron would ride to the rescue.</p>

<p>Against that party stood the prophets, and above all <strong>Jeremiah</strong>. His counsel never wavered, and to the court it sounded like treason: submit to Babylon and live. &ldquo;Bring your necks under the yoke of the king of Babylon, and serve him and his people, and live,&rdquo; he told Zedekiah (<a href="https://www.blueletterbible.org/kjv/jer/27/12/" target="_blank" data-ref="Jeremiah 27:12">Jeremiah 27:12</a>). He did not just say it &mdash; he wore a wooden yoke on his own neck as a walking picture of that submission. And his grounds were not strategic but <em>theological</em>: Babylon was the instrument of God&rsquo;s judgment, so to resist it was to fight God. In the Lord&rsquo;s own voice he calls Nebuchadnezzar &ldquo;my servant&rdquo; (<a href="https://www.blueletterbible.org/kjv/jer/27/6/" target="_blank" data-ref="Jeremiah 27:6">Jeremiah 27:6</a>). The optimists promised Babylon would fall within two years, and they spoke for the pro-Egypt hope. The prophet Hananiah went so far as to snap Jeremiah&rsquo;s wooden yoke in the temple court (<a href="https://www.blueletterbible.org/kjv/jer/28/1/" target="_blank" data-ref="Jeremiah 28">Jeremiah 28</a>). They were sincere, and they were wrong, and Jeremiah told them so to their faces.</p>

<br>

<hr>

<br>

<h3>The Pattern of Ruin</h3>

<p>What followed was the same mistake, three times over. In 601 BC, Babylon and Egypt fought an inconclusive clash, and Jehoiakim smelled Babylonian weakness. He withheld tribute and rebelled (<a href="https://www.blueletterbible.org/kjv/2ki/24/1/" target="_blank" data-ref="2 Kings 24:1">2 Kings 24:1</a>) &mdash; betting on Egypt. Babylon answered with the siege of <strong>597 BC</strong>. Jerusalem was taken. King Jehoiachin and the elite were carried into exile. And Nebuchadnezzar set Josiah&rsquo;s son Mattaniah on the throne as a puppet, renaming him <strong>Zedekiah</strong> (<a href="https://www.blueletterbible.org/kjv/2ki/24/17/" target="_blank" data-ref="2 Kings 24:17">2 Kings 24:17</a>) &mdash; an overlord&rsquo;s gesture, and a bid for a loyal client. Zedekiah broke faith in turn, &ldquo;sending his ambassadors into Egypt, that they might give him horses and much people&rdquo; (<a href="https://www.blueletterbible.org/kjv/eze/17/15/" target="_blank" data-ref="Ezekiel 17:15">Ezekiel 17:15</a>).</p>

<p>Egypt did come &mdash; briefly. When Pharaoh&rsquo;s army approached, the Babylonians lifted the siege of Jerusalem. Then Egypt thought better of the fight and withdrew, and the Babylonians came back and finished the work (<a href="https://www.blueletterbible.org/kjv/jer/37/5/" target="_blank" data-ref="Jeremiah 37:5-7">Jeremiah 37:5&ndash;7</a>). In the summer of <strong>586 BC</strong> the walls were breached and the temple burned. Every time Judah leaned on Egypt, Egypt proved exactly what an earlier taunt had named it: a &ldquo;bruised reed&rdquo; that runs into the hand of the one who leans on it (<a href="https://www.blueletterbible.org/kjv/2ki/18/21/" target="_blank" data-ref="2 Kings 18:21">2 Kings 18:21</a>). And the prophets who had said so were vindicated in the cruelest possible way.</p>

<br>

<hr>

<br>

<h3>The Neighbors Who Cheered</h3>

<p>Judah did not make its last gamble alone. When Zedekiah plotted revolt, envoys of Edom, Moab, Ammon, <strong>Tyre, and Sidon</strong> gathered in Jerusalem to coordinate the rising (<a href="https://www.blueletterbible.org/kjv/jer/27/3/" target="_blank" data-ref="Jeremiah 27:3">Jeremiah 27:3</a>). The Phoenician cities were Judah&rsquo;s <em>partners</em> in the anti-Babylon coalition, not its enemies. That is what makes Tyre&rsquo;s response to Jerusalem&rsquo;s fall so bitter. When the city broke, Tyre did not mourn a fellow rebel. It gloated, and counted its gain: &ldquo;Aha, she is broken that was the gates of the people: she is turned unto me: I shall be replenished, now she is laid waste&rdquo; (<a href="https://www.blueletterbible.org/kjv/eze/26/2/" target="_blank" data-ref="Ezekiel 26:2">Ezekiel 26:2</a>). Jerusalem had been a rival on the caravan roads; her ruin meant Tyre&rsquo;s profit. The prophet Amos had already named the sin: Tyre &ldquo;remembered not the brotherly covenant&rdquo; (<a href="https://www.blueletterbible.org/kjv/amo/1/9/" target="_blank" data-ref="Amos 1:9">Amos 1:9</a>). It was not a military betrayal. It was, in its way, worse &mdash; an ally cashing in on a partner&rsquo;s funeral.</p>

<p>And yet scripture saves one of its quieter ironies for the end. When Judah at last came home a lifetime later to rebuild, it was again to Tyre and Sidon that they sent for cedar &mdash; exactly as Solomon had for the first temple (<a href="https://www.blueletterbible.org/kjv/ezr/3/7/" target="_blank" data-ref="Ezra 3:7">Ezra 3:7</a>). The neighbors who cheered the fall also helped raise the house that rose from it. What that homecoming was like &mdash; who was welcomed, who was kept out, and why &mdash; belongs to the story of the Persian return, told in the <a href="/culture/ancient/achaemenid/">Achaemenid guide</a>.</p>

<br>

<hr>

<br>

<details class="seder-dropdown seder-dropdown--seder">
<summary>Sources and Further Reading</summary>
<div class="seder-dropdown-body" style="text-align: left;">

<ul style="margin: 12px 0; padding-left: 24px;">
<li><strong>Abraham Malamat</strong>, &ldquo;Josiah&rsquo;s Bid for Armageddon: The Background of the Judean-Egyptian Encounter in 609 B.C.,&rdquo; <em>Journal of the Ancient Near Eastern Society</em> 5 (1973) &mdash; The classic treatment of Josiah, Necho, and Megiddo.</li>
<li><strong>Nadav Na&rsquo;aman</strong>, &ldquo;The Kingdom of Judah under Josiah,&rdquo; <em>Tel Aviv</em> 18 (1991) &mdash; On the extent (and limits) of Josiah&rsquo;s northern reach.</li>
<li><strong>Mordechai Cogan and Hayim Tadmor</strong>, <em>II Kings</em> (Anchor Bible, 1988) &mdash; The standard commentary; treats the <em>&lsquo;al</em> &ldquo;against / to&rdquo; problem in 23:29.</li>
<li><strong>A. K. Grayson</strong>, <em>Assyrian and Babylonian Chronicles</em> (J. J. Augustin, 1975) &mdash; The Fall of Nineveh Chronicle (ABC 3), which places Egypt and Assyria together against Babylon at Harran in 609.</li>
<li><strong>Oded Lipschits</strong>, <em>The Fall and Rise of Jerusalem: Judah under Babylonian Rule</em> (Eisenbrauns, 2005) &mdash; Judah&rsquo;s last kings from both sides of the evidence.</li>
</ul>

<p><strong>Online Resources:</strong></p>
<ul style="margin: 12px 0 0 0; padding-left: 24px;">
<li><a href="https://www.livius.org/sources/content/mesopotamian-chronicles-content/abc-3-fall-of-nineveh-chronicle/" target="_blank"><strong>Livius.org</strong> &mdash; the Fall of Nineveh Chronicle (ABC 3)</a> &mdash; the primary text for 609 BC.</li>
<li><a href="https://www.worldhistory.org/Necho_II/" target="_blank"><strong>WHE</strong> &mdash; Necho II</a> (CC BY-NC-SA 4.0)</li>
</ul>

</div>
</details>

</div>

<link rel="stylesheet" href="/css/fg-gallery.css">

{{< /rawhtml >}}
