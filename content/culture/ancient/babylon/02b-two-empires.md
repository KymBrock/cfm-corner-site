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
<div class="listen-player" style="max-width: 750px; margin: 0 auto 1.75rem auto; background: linear-gradient(135deg, #f2f5f2 0%, #dce8dd 100%); border: 1px solid #cdddce; border-radius: 14px; padding: 16px 18px; box-shadow: 0 4px 12px rgba(74,107,82,0.08);">
<div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
<span aria-hidden="true" style="flex: 0 0 auto; display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; border-radius: 50%; background: #4a6b52;">
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#f2f5f2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 14v-2a9 9 0 0 1 18 0v2"></path><path d="M21 15a2 2 0 0 1-2 2h-1v-5h1a2 2 0 0 1 2 2z"></path><path d="M3 15a2 2 0 0 0 2 2h1v-5H5a2 2 0 0 0-2 2z"></path></svg>
</span>
<div style="flex: 1; min-width: 0;">
<div style="font-weight: 700; color: #3c5743; font-size: 1.02em; line-height: 1.2;">Listen to this section</div>
<div style="color: #6a8470; font-size: 0.85em; margin-top: 2px;">Narrated in Kym&rsquo;s voice</div>
</div>
</div>
<audio controls preload="none" style="width: 100%; height: 40px; border-radius: 8px;">
<source src="/audio/culture/babylon/02b-two-empires.mp3" type="audio/mpeg">
Your browser doesn&rsquo;t support the audio element &mdash; <a href="/audio/culture/babylon/02b-two-empires.mp3">download the audio</a> instead.
</audio>
</div>
<!-- /LISTEN PLAYER -->

<p>For the last forty years of its life, the kingdom of Judah faced one recurring question, and its answer each time decided everything: when the great powers collide, whose side are you on? To the south lay <strong>Egypt</strong>, the old familiar patron. To the east rose <strong>Babylon</strong>, new and terrible. Judah was too small to stand alone and too well-placed on the road between them to be left alone &mdash; and its kings, again and again, bet on Egypt. Every bet failed. What lifts this above ordinary politics is that Judah&rsquo;s prophets were not neutral observers. Jeremiah above all insisted that Babylon was the safer road &mdash; and the God-appointed one &mdash; and was branded a traitor for saying so. This section is the <em>why</em> behind the dates in <a href="/culture/ancient/babylon/02-timeline-and-empires/">Section 02</a> and the portraits in <a href="/culture/ancient/babylon/03-nebuchadnezzar-and-the-kings/">Section 03</a>.</p>

<!-- ===== JUDAH BETWEEN THE EMPIRES (jbe) ===== -->
<style>
.jbe { border:1px solid #e2ddd3; border-radius:16px; overflow:hidden; margin:26px 0; background:#fbf9f5; box-shadow:0 6px 18px rgba(0,0,0,.07); font-family:-apple-system,Segoe UI,Roboto,sans-serif; }
.jbe-head { padding:16px 18px 4px; }
.jbe-head h4 { margin:0; font-size:1.05rem; color:#3c3a33; }
.jbe-head p { margin:4px 0 0; font-size:.82rem; color:#8a8172; }
.jbe-map { display:block; width:100%; height:auto; }
.jbe-arrow { fill:none; stroke-width:10; stroke-linecap:round; opacity:0; transition:opacity .35s; }
.jbe-arrow.show { opacity:1; }
.jbe-egy { stroke:#f0b400; } .jbe-egy-h { fill:#f0b400; }
.jbe-bab { stroke:#d84315; } .jbe-bab-h { fill:#d84315; }
.jbe-dash { stroke-dasharray:18 13; }
.jbe-burst { opacity:0; transition:opacity .35s; }
.jbe-burst.show { opacity:1; }
.jbe-burst circle { fill:none; stroke:#c0392b; stroke-width:6; }
.jbe-cap { padding:12px 18px 6px; font-size:.9rem; line-height:1.5; color:#443f37; min-height:3.2em; border-top:1px solid #eee6d8; }
.jbe-cap b { color:#7a3030; }
.jbe-time { display:flex; gap:0; padding:6px 10px 16px; position:relative; }
.jbe-time::before { content:""; position:absolute; left:44px; right:44px; top:26px; height:3px; background:#e0d8c7; border-radius:3px; }
.jbe-step { flex:1; background:none; border:none; cursor:pointer; padding:0; display:flex; flex-direction:column; align-items:center; gap:6px; font-family:inherit; position:relative; z-index:1; }
.jbe-dot { width:20px; height:20px; border-radius:50%; background:#fff; border:3px solid #c9b98f; transition:transform .2s,border-color .2s,background .2s; }
.jbe-step.egy .jbe-dot { border-color:#d5a93c; } .jbe-step.bab .jbe-dot { border-color:#d84315; }
.jbe-step.is-active .jbe-dot { transform:scale(1.35); background:#d84315; border-color:#d84315; }
.jbe-step.is-active.egy .jbe-dot { background:#d5a93c; border-color:#d5a93c; }
.jbe-yr { font-size:.78rem; font-weight:800; color:#5a544a; }
.jbe-lbl { font-size:.66rem; color:#8a8172; line-height:1.1; max-width:88px; }
.jbe-step.is-active .jbe-yr { color:#3c3a33; }
.jbe-legend { display:flex; gap:16px; justify-content:center; padding:0 10px 14px; font-size:.7rem; color:#8a8172; }
.jbe-legend span { display:inline-flex; align-items:center; gap:5px; }
.jbe-sw { width:16px; height:4px; border-radius:2px; display:inline-block; }
@media (max-width:560px){ .jbe-lbl{display:none;} .jbe-time::before{top:16px;} }
</style>

<div class="jbe">
  <div class="jbe-head"><h4>Judah Between the Empires</h4>
  <p>The same mistake, three times over. Step through 609&ndash;586 BC &mdash; each bet on Egypt ended at a siege wall.</p></div>
  <svg class="jbe-map" viewBox="230 440 1800 1090" role="img" aria-label="Map of the campaigns between Egypt and Babylon, 609 to 586 BC">
    <defs>
      <marker id="jbe-ah-egy" markerWidth="5" markerHeight="5" refX="3.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" class="jbe-egy-h"/></marker>
      <marker id="jbe-ah-bab" markerWidth="5" markerHeight="5" refX="3.5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" class="jbe-bab-h"/></marker>
      <filter id="jbe-sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="#000" flood-opacity="0.55"/></filter>
    </defs>
    <image href="/images/culture/babylon/maps/babylon-campaign-base.jpg" x="0" y="0" width="3840" height="2403"/>

    <!-- campaign arrows removed pending exact city coords from Illustrator; map + timeline stepper stand alone -->
    <g id="jbe-s0"></g><g id="jbe-s1"></g><g id="jbe-s2"></g><g id="jbe-s3"></g><g id="jbe-s4"></g>
  </svg>
  <p class="jbe-cap" id="jbe-cap"></p>
  <div class="jbe-time" id="jbe-time"></div>
  <div class="jbe-legend"><span><i class="jbe-sw" style="background:#f0b400;"></i> a bet on Egypt</span><span><i class="jbe-sw" style="background:#d84315;"></i> Babylon&rsquo;s answer</span></div>
</div>

<script>
(function(){
  var STEPS=[
    {yr:"609 BC",lbl:"Megiddo",side:"egy",cap:"<b>609 BC &mdash; Megiddo.</b> Pharaoh Necho marches north to prop up dying Assyria. Josiah rides out to stop him and is killed &mdash; and his death-ride objectively clears the road for Babylon."},
    {yr:"605 BC",lbl:"Carchemish",side:"bab",cap:"<b>605 BC &mdash; Carchemish.</b> Crown prince Nebuchadnezzar shatters Egypt&rsquo;s army and takes the throne. Judah passes, by default, into Babylon&rsquo;s hand as a vassal."},
    {yr:"601 BC",lbl:"Jehoiakim rebels",side:"egy",cap:"<b>601 BC &mdash; the bloody draw.</b> Babylon and Egypt fight to a standstill near the border. Sensing weakness, Jehoiakim withholds tribute and rebels &mdash; betting on Egypt."},
    {yr:"597 BC",lbl:"First siege",side:"bab",cap:"<b>597 BC &mdash; the first siege.</b> Nebuchadnezzar takes Jerusalem, carries King Jehoiachin and the elite into exile, and installs Zedekiah as his puppet."},
    {yr:"586 BC",lbl:"Jerusalem falls",side:"bab",cap:"<b>586 BC &mdash; the fall.</b> Zedekiah rebels and calls for Egypt; the relief march comes, then withdraws; Babylon returns, breaches the walls, and burns the temple."}
  ];
  var groups=[],time=document.getElementById('jbe-time'),cap=document.getElementById('jbe-cap');
  for(var i=0;i<STEPS.length;i++)groups.push(document.getElementById('jbe-s'+i));
  function show(n){
    for(var i=0;i<groups.length;i++){var on=(i===n);var ar=groups[i].querySelectorAll('.jbe-arrow');for(var a=0;a<ar.length;a++)ar[a].classList.toggle('show',on);var bs=groups[i].querySelectorAll('.jbe-burst');for(var b=0;b<bs.length;b++)bs[b].classList.toggle('show',on);}
    var btns=time.querySelectorAll('.jbe-step');for(var j=0;j<btns.length;j++)btns[j].classList.toggle('is-active',j===n);
    cap.innerHTML=STEPS[n].cap;
  }
  STEPS.forEach(function(s,idx){var b=document.createElement('button');b.className='jbe-step '+s.side;b.type='button';b.innerHTML='<span class="jbe-dot"></span><span class="jbe-yr">'+s.yr+'</span><span class="jbe-lbl">'+s.lbl+'</span>';b.addEventListener('click',function(){show(idx);});time.appendChild(b);});
  show(0);
})();
</script>
<!-- ===== /jbe ===== -->

<br>

<hr>

<br>

<h3>Josiah&rsquo;s Fatal Gamble (609 BC)</h3>

<p>The turning point came before Babylon ever threatened Jerusalem. In 609 BC, Pharaoh <strong>Necho II</strong> marched his army north &mdash; not to attack Assyria, but to prop it up. Assyria was collapsing under Babylonian and Median blows, and Egypt, preferring a weak old neighbor to a strong new one, moved to save it. The King James Version says Necho &ldquo;went up <em>against</em> the king of Assyria&rdquo; (<a href="https://www.blueletterbible.org/kjv/2ki/23/29/" target="_blank" data-ref="2 Kings 23:29">2 Kings 23:29</a>), which for centuries read as hostility &mdash; but the Hebrew preposition <em>&lsquo;al</em> can equally mean &ldquo;to&rdquo; or &ldquo;in support of,&rdquo; and the Babylonian Chronicle settles it: in 609 Egypt and Assyria were <em>allies</em>, jointly trying to retake Harran from Babylon. Modern translations read &ldquo;went up <em>to</em> the king of Assyria&rdquo; &mdash; to help him.</p>

<p>Into that march stepped King <strong>Josiah</strong> of Judah, who intercepted Necho at Megiddo and was killed (<a href="https://www.blueletterbible.org/kjv/2ch/35/20/" target="_blank" data-ref="2 Chronicles 35:20-24">2 Chronicles 35:20&ndash;24</a>). Whatever he intended, the effect is plain: by trying to keep Egypt from reinforcing Assyria, Josiah&rsquo;s death-ride objectively served <strong>Babylon</strong> &mdash; ruled then not yet by Nebuchadnezzar but by his father <strong>Nabopolassar</strong>. Nebuchadnezzar was still the crown prince; he would not win Carchemish or take the throne until 605, four years after Josiah was already dead.</p>

<figure class="fg-figure">
  <img src="/images/culture/babylon/photos/tel-megiddo.jpg" alt="The ruins of Tel Megiddo, Israel" loading="lazy">
  <figcaption>Tel Megiddo &mdash; the strategic mound guarding the pass where Josiah rode out to stop Necho in 609 BC, and was killed. Its Greek name, Armageddon, became scripture&rsquo;s word for the last battle. <span class="fg-credit">Photo &copy; Anagoria, Wikimedia Commons (CC BY 3.0)</span></figcaption>
</figure>

<div style="background: linear-gradient(135deg, #f5f3f0 0%, #ebe7e1 100%); padding: 20px 24px; border-radius: 8px; margin: 24px 0;">
<p style="margin: 0;"><strong>One preposition, two directions:</strong> 2 Kings 23:29 has Necho going &ldquo;against the king of Assyria,&rdquo; and for most of history that was read as war between them. The Hebrew <em>&lsquo;al</em> is simply ambiguous &mdash; &ldquo;against,&rdquo; but also &ldquo;to&rdquo; or &ldquo;alongside.&rdquo; The cuneiform record of 609 BC, in which Egyptian and Assyrian troops besiege Harran <em>together</em>, shows the second sense is the right one. A single small word &mdash; and the whole shape of the war turns on which way it points.</p>
</div>

<p>Why Josiah did it is genuinely debated, and here the guide is reading between the lines rather than quoting them. Scripture never states his motive, and there is <em>no</em> record of a formal treaty between Judah and Babylon. Some historians see simply a bid to protect the independence he had won; others note that his reforms had reached north into the old kingdom of Israel &mdash; to Bethel and &ldquo;the cities of Samaria&rdquo; (<a href="https://www.blueletterbible.org/kjv/2ki/23/15/" target="_blank" data-ref="2 Kings 23:15-20">2 Kings 23:15&ndash;20</a>; <a href="https://www.blueletterbible.org/kjv/2ch/34/6/" target="_blank" data-ref="2 Chronicles 34:6">2 Chronicles 34:6</a>) &mdash; and read in his stand a larger hope: that a Davidic king who broke Assyria&rsquo;s and Egypt&rsquo;s grip on the north might one day gather the scattered northern tribes home. That is a reasonable and moving reading. But it is a <em>reading</em>. What the sources give us is the act and its consequence, not the inside of the king&rsquo;s mind.</p>

<br>

<hr>

<br>

<h3>The Two Parties</h3>

<p>Josiah&rsquo;s death handed Judah straight back to Egypt. Necho deposed Josiah&rsquo;s chosen heir, installed <strong>Jehoiakim</strong>, and levied a crushing tribute (<a href="https://www.blueletterbible.org/kjv/2ki/23/33/" target="_blank" data-ref="2 Kings 23:33-35">2 Kings 23:33&ndash;35</a>). For the next generation, Judah&rsquo;s court was, by default, Egypt&rsquo;s client, and a pro-Egypt party ran its foreign policy &mdash; always betting the southern patron would ride to the rescue.</p>

<p>Against that party stood the prophets, and above all <strong>Jeremiah</strong>. His counsel never wavered, and to the court it sounded like treason: submit to Babylon and live. &ldquo;Bring your necks under the yoke of the king of Babylon, and serve him and his people, and live,&rdquo; he told Zedekiah (<a href="https://www.blueletterbible.org/kjv/jer/27/12/" target="_blank" data-ref="Jeremiah 27:12">Jeremiah 27:12</a>). His grounds were not strategic but <em>theological</em>: Babylon was the instrument of God&rsquo;s judgment, so to resist it was to fight God. In the Lord&rsquo;s own voice he calls Nebuchadnezzar &ldquo;my servant&rdquo; (<a href="https://www.blueletterbible.org/kjv/jer/27/6/" target="_blank" data-ref="Jeremiah 27:6">Jeremiah 27:6</a>). The optimists who promised Babylon would fall within two years &mdash; the prophet Hananiah, snapping Jeremiah&rsquo;s wooden yoke in the temple court (<a href="https://www.blueletterbible.org/kjv/jer/28/1/" target="_blank" data-ref="Jeremiah 28">Jeremiah 28</a>) &mdash; spoke for the pro-Egypt hope. They were sincere, and they were wrong, and Jeremiah told them so to their faces.</p>

<br>

<hr>

<br>

<h3>The Pattern of Ruin</h3>

<p>What followed was the same mistake, three times over. Sensing Babylonian weakness after an inconclusive clash with Egypt in 601 BC, Jehoiakim withheld tribute and rebelled (<a href="https://www.blueletterbible.org/kjv/2ki/24/1/" target="_blank" data-ref="2 Kings 24:1">2 Kings 24:1</a>) &mdash; betting on Egypt. Babylon answered with the siege of <strong>597 BC</strong>: Jerusalem taken, King Jehoiachin and the elite carried into exile, and Nebuchadnezzar setting Josiah&rsquo;s son Mattaniah on the throne as a puppet, renaming him <strong>Zedekiah</strong> (<a href="https://www.blueletterbible.org/kjv/2ki/24/17/" target="_blank" data-ref="2 Kings 24:17">2 Kings 24:17</a>) &mdash; an overlord&rsquo;s gesture, and a bid for a loyal client. Zedekiah broke faith in turn, &ldquo;sending his ambassadors into Egypt, that they might give him horses and much people&rdquo; (<a href="https://www.blueletterbible.org/kjv/eze/17/15/" target="_blank" data-ref="Ezekiel 17:15">Ezekiel 17:15</a>).</p>

<p>Egypt did come &mdash; briefly. When Pharaoh&rsquo;s army approached, the Babylonians lifted the siege of Jerusalem; when it thought better of the fight and withdrew, they came back and finished the work (<a href="https://www.blueletterbible.org/kjv/jer/37/5/" target="_blank" data-ref="Jeremiah 37:5-7">Jeremiah 37:5&ndash;7</a>). In the summer of <strong>586 BC</strong> the walls were breached and the temple burned. Every time Judah leaned on Egypt, Egypt proved exactly what an earlier taunt had named it &mdash; a &ldquo;bruised reed&rdquo; that runs into the hand of the one who leans on it (<a href="https://www.blueletterbible.org/kjv/2ki/18/21/" target="_blank" data-ref="2 Kings 18:21">2 Kings 18:21</a>) &mdash; and the prophets who had said so were vindicated in the cruelest possible way.</p>

<br>

<hr>

<br>

<h3>The Neighbors Who Cheered</h3>

<p>Judah did not make its last gamble alone. When Zedekiah plotted revolt, envoys of Edom, Moab, Ammon, <strong>Tyre, and Sidon</strong> gathered in Jerusalem to coordinate the rising (<a href="https://www.blueletterbible.org/kjv/jer/27/3/" target="_blank" data-ref="Jeremiah 27:3">Jeremiah 27:3</a>). The Phoenician cities were Judah&rsquo;s <em>partners</em> in the anti-Babylon coalition, not its enemies &mdash; which is what makes Tyre&rsquo;s response to Jerusalem&rsquo;s fall so bitter. When the city broke, Tyre did not mourn a fellow rebel; it gloated, and counted its gain: &ldquo;Aha, she is broken that was the gates of the people: she is turned unto me: I shall be replenished, now she is laid waste&rdquo; (<a href="https://www.blueletterbible.org/kjv/eze/26/2/" target="_blank" data-ref="Ezekiel 26:2">Ezekiel 26:2</a>). Jerusalem had been a rival on the caravan roads; her ruin meant Tyre&rsquo;s profit. The prophet Amos had already named the sin: Tyre &ldquo;remembered not the brotherly covenant&rdquo; (<a href="https://www.blueletterbible.org/kjv/amo/1/9/" target="_blank" data-ref="Amos 1:9">Amos 1:9</a>). It was not a military betrayal. It was, in its way, worse &mdash; an ally cashing in on a partner&rsquo;s funeral.</p>

<p>And yet, in one of scripture&rsquo;s quieter ironies, when Judah at last came home a lifetime later to rebuild, it was again to Tyre and Sidon that they sent for cedar &mdash; exactly as Solomon had for the first temple (<a href="https://www.blueletterbible.org/kjv/ezr/3/7/" target="_blank" data-ref="Ezra 3:7">Ezra 3:7</a>). The neighbors who cheered the fall also helped raise the house that rose from it. What that homecoming was like &mdash; who was welcomed, who was kept out, and why &mdash; belongs to the story of the Persian return, told in the <a href="/culture/ancient/achaemenid/">Achaemenid guide</a>.</p>

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
