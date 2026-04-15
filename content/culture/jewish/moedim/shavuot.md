---
title: "Shavuot: The Feast of Weeks / Pentecost"
description: "From Sinai to Bountiful — how the ancient wheat harvest feast connects the giving of the Torah, the descent of the Spirit at Pentecost, the Sermon on the Mount, and Christ's appearance at the temple in 3 Nephi. Includes the Higher Law framework, Restoration harvest imagery, and traditional observances."
weight: 3
draft: false
image: /images/culture/jewish-festivals/feast-icons/pentecost.png
hide_nav: true
related_weeks: ["17"]
aliases:
  - /culture/jewish-festivals/shavuot/
  - /culture/jewish-festivals/pentecost/
---

<style>
/* ═══════ Core Styles (shared with other moedim pages) ═══════ */
.comparison-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}
.compare-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}
.compare-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}
.compare-card h4 {
    color: #1a6b74;
    margin-bottom: 1rem;
    margin-top: 0;
}
.info-box {
    background: #f8f9fa;
    border-left: 4px solid #d4a53e;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 4px;
}
.info-box.insight {
    border-left-color: #1a6b74;
    background: #e7f3f5;
}
.info-box.sinai {
    border-left-color: #8b4513;
    background: #fdf5ef;
}
/* Feast Timeline */
.feast-timeline {
    display: flex;
    gap: 1rem;
    margin: 2rem 0;
    padding: 1.5rem;
    background: linear-gradient(135deg, #f5f5f5, #fff);
    border-radius: 12px;
    overflow-x: auto;
}
.timeline-item {
    flex: 1;
    min-width: 150px;
    padding: 1rem;
    border-radius: 8px;
    background: white;
    border: 2px solid #e0e0e0;
    transition: all 0.3s ease;
    text-align: center;
}
.timeline-item img {
    width: 50px !important;
    height: 50px !important;
    object-fit: contain;
    display: block;
    margin: 0 auto 0.5rem !important;
}
.timeline-item:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}
.timeline-item.highlight {
    background: linear-gradient(135deg, #1a6b74, #2a8a94);
    color: white;
    border-color: #1a6b74;
}
.timeline-item.highlight img {
    background: white;
    border-radius: 50%;
    padding: 8px;
}
.timeline-item h4 { font-size: 0.9rem; margin-bottom: 0.5rem; color: inherit; }
.timeline-item p { font-size: 0.85rem; margin: 0; opacity: 0.9; }
/* Feast Header */
.feast-header {
    display: flex;
    align-items: center;
    gap: 2rem;
    padding: 2rem;
    background: linear-gradient(135deg, #1a6b74, #2a8a94);
    border-radius: 16px;
    margin-bottom: 2rem;
    color: white;
}
.feast-icon {
    width: 100px; height: 100px;
    background: rgba(255,255,255,0.9);
    border-radius: 50%; padding: 15px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.feast-icon img { width: 70px !important; height: 70px !important; object-fit: contain; }
/* Dropdown Styling */
details {
    background: #f8f9fa;
    border-radius: 8px;
    margin: 1.5rem 0;
    border: 1px solid #e0e0e0;
}
details summary {
    padding: 1rem 1.25rem;
    cursor: pointer;
    font-weight: bold;
    color: #1a6b74;
    list-style: none;
}
details summary::-webkit-details-marker { display: none; }
details summary::before { content: "▶ "; font-size: 0.8rem; margin-right: 0.5rem; }
details[open] summary::before { content: "▼ "; }
details > div { padding: 0 1.25rem 1.25rem; }

/* ═══════ Shavuot-specific Styles ═══════ */

/* Commandment Cards */
.commandment-card {
    border: 2px solid #d4a53e;
    border-radius: 12px;
    margin-bottom: 1.25rem;
    overflow: hidden;
    transition: box-shadow 0.3s ease;
}
.commandment-card:hover {
    box-shadow: 0 4px 16px rgba(212,165,62,0.2);
}
.commandment-header {
    background: linear-gradient(135deg, #f7eed8, #fdf5e7);
    padding: 1rem 1.25rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    color: #5a4a2a;
    font-size: 1.05rem;
}
.commandment-header .num {
    background: #d4a53e;
    color: white;
    min-width: 32px; height: 32px;
    padding: 0 6px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.8rem;
    margin-right: 0.75rem;
    flex-shrink: 0;
}
.commandment-header .arrow { font-size: 0.8rem; color: #8b6914; transition: transform 0.3s; }
.commandment-card.open .commandment-header .arrow { transform: rotate(90deg); }
.commandment-body {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
}
.commandment-body-inner { padding: 1.25rem; }
.law-row {
    display: flex;
    gap: 0.75rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid #f0e8d8;
    align-items: flex-start;
}
.law-row:last-child { border-bottom: none; }
.law-label {
    min-width: 140px;
    font-weight: 600;
    font-size: 0.85rem;
    padding: 4px 10px;
    border-radius: 4px;
    text-align: center;
    flex-shrink: 0;
}
.law-label.telestial { background: #fde8d0; color: #8b4513; }
.law-label.terrestrial { background: #d4edda; color: #2e7d32; }
.law-label.celestial { background: #d4e8f0; color: #1a6b74; }
.law-label.blessing { background: #fff3cd; color: #856404; }
.law-text { font-size: 0.95rem; line-height: 1.6; color: #444; }

/* Mountain Cards */
.mountain-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}
.mountain-card {
    border-radius: 12px;
    padding: 1.75rem;
    color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
}
.mountain-card:hover { transform: translateY(-4px); }
.mountain-card.sinai { background: linear-gradient(135deg, #6b5b3a, #8b7a4a); }
.mountain-card.galilee { background: linear-gradient(135deg, #7a7843, #9a9260); }
.mountain-card.bountiful { background: linear-gradient(135deg, #8a7d5a, #c4ad72); }
.mountain-card h4 { margin-top: 0; font-size: 1.2rem; color: white; }
.mountain-card ul { padding-left: 1.25rem; line-height: 1.8; }

/* Proximity Table */
.proximity-table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
    font-size: 0.9rem;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.proximity-table th {
    background: #1a6b74;
    color: white;
    padding: 12px 15px;
    text-align: left;
    font-weight: 600;
}
.proximity-table td {
    padding: 10px 15px;
    border-bottom: 1px solid #e0e0e0;
}
.proximity-table tr:nth-child(even) td { background: #f8faf8; }
.proximity-table tr:hover td { background: #e7f3f5; }

/* Recipe Grid */
.recipe-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}
.recipe-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border-top: 4px solid #d4a53e;
    transition: transform 0.3s ease;
}
.recipe-card:hover { transform: translateY(-4px); }
.recipe-card h4 { color: #8b6914; margin-top: 0; }
.recipe-card .recipe-desc { font-size: 0.9rem; color: #555; line-height: 1.6; }

/* Table of Contents */
.toc-nav {
    background: linear-gradient(135deg, #fdf5e7, #fff8dc);
    border: 1px solid #e8dcc8;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin: 1.5rem 0 2rem;
}
.toc-nav h3 {
    margin: 0 0 0.75rem;
    font-size: 1rem;
    color: #8b6914;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.toc-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 0.4rem;
}
.toc-nav li { margin: 0; }
.toc-nav a {
    display: block;
    padding: 0.4rem 0.75rem;
    color: #5a4a2a;
    text-decoration: none;
    font-size: 0.9rem;
    border-radius: 6px;
    transition: background 0.2s;
}
.toc-nav a:hover {
    background: rgba(212, 165, 62, 0.15);
    color: #8b6914;
}
.toc-nav a::before {
    content: "▸ ";
    color: #d4a53e;
    font-size: 0.8rem;
}

/* Section Dropdowns (large collapsible sections) */
details.section-dropdown {
    background: white;
    border: 2px solid #e8dcc8;
    border-radius: 12px;
    margin: 2rem 0;
}
details.section-dropdown > summary {
    padding: 1.25rem 1.5rem;
    font-size: 1.3rem;
    font-weight: 600;
    color: #5a4a2a;
    background: linear-gradient(135deg, #fdf5e7, #fff8dc);
    border-radius: 10px;
    list-style: none;
    cursor: pointer;
}
details.section-dropdown > summary::-webkit-details-marker { display: none; }
details.section-dropdown > summary::before { content: "▶  "; font-size: 0.7rem; color: #d4a53e; vertical-align: middle; }
details.section-dropdown[open] > summary::before { content: "▼  "; }
details.section-dropdown[open] > summary {
    border-radius: 10px 10px 0 0;
    border-bottom: 1px solid #e8dcc8;
}
details.section-dropdown > .section-body {
    padding: 1.5rem;
}

/* Responsive */
@media (max-width: 768px) {
    .feast-timeline { flex-direction: column; }
    .feast-header { flex-direction: column; text-align: center; }
    .mountain-grid { grid-template-columns: 1fr; }
    .law-row { flex-direction: column; }
    .law-label { min-width: unset; }
    .toc-nav ul { grid-template-columns: 1fr; }
}
</style>

<!-- ═══════════════════════════════════════════════════════════════════════════
     HEADER
     ═══════════════════════════════════════════════════════════════════════════ -->

<div style="border-radius: 16px; overflow: hidden; margin-bottom: 2rem; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
    <img src="/images/culture/jewish-festivals/shavuot/shavuot-hero.gif" alt="Shavuot — Harvest of Covenant and Spirit" style="width: 100%; display: block;">
    <div style="background: linear-gradient(135deg, #6b5b3a, #8b7a4a); padding: 1.5rem 2rem; display: flex; align-items: center; gap: 1.5rem;">
        <div class="feast-icon" style="width: 70px; height: 70px; padding: 10px; flex-shrink: 0;">
            <img src="/images/culture/jewish-festivals/feast-icons/pentecost.png" alt="Shavuot" style="width: 50px !important; height: 50px !important;">
        </div>
        <div>
            <h1 style="margin: 0; color: white; font-size: 2rem;">Shavuot / Pentecost</h1>
            <p style="margin: 0.25rem 0 0; font-size: 1rem; opacity: 0.9; color: white;">The Feast of Weeks — From Stone to Flesh, From Sinai to Bountiful</p>
            <p style="margin: 0.25rem 0 0; font-size: 0.85rem; opacity: 0.7; color: white;">6 Sivan — 50 days after Passover</p>
        </div>
    </div>
</div>

<div class="toc-nav">
<h3>In This Article</h3>
<ul>
<li><a href="#overview">Overview</a></li>
<li><a href="#the-spring-feast-timeline">Spring Feast Timeline</a></li>
<li><a href="#the-biblical-foundation">Biblical Foundation</a></li>
<li><a href="#sinai-section">The First Shavuot: Sinai</a></li>
<li><a href="#pentecost-section">Pentecost (Acts 2)</a></li>
<li><a href="#higher-law-section">The Law, the Higher Law, and the Blessing</a></li>
<li><a href="#mountains-section">Four Mountains: A Temple Progression</a></li>
<li><a href="#bountiful-section">The Bountiful Visit as Shavuot</a></li>
<li><a href="#wheat-section">Wheat Harvest in Restoration Scripture</a></li>
<li><a href="#ruth-section">The Book of Ruth</a></li>
<li><a href="#recipes-section">Traditional Shavuot Foods</a></li>
<li><a href="#family-section">Family Shavuot Activities</a></li>
<li><a href="#from-stone-to-flesh-the-arc-of-shavuot">From Stone to Flesh</a></li>
<li><a href="#modern-observance">Modern Observance & LDS Resonance</a></li>
</ul>
</div>

## Overview

Shavuot (שָׁבֻעוֹת, "Weeks") is the fourth of the seven biblical feasts — and the one that bridges the spring and summer seasons. It falls exactly fifty days after Bikkurim (Firstfruits), completing the Counting of the Omer. In Greek it became Pentecost (πεντηκοστή, "fiftieth"). While the Torah describes it as a harvest festival, Jewish tradition identifies it as the anniversary of the most transformative event in Israelite history: the giving of the Torah at Mount Sinai.

For Latter-day Saints, Shavuot holds layers of significance that extend far beyond ancient Israel. The same God who descended on Sinai in fire and smoke ascended a mountain in Galilee to deliver the Sermon on the Mount, then descended in a white robe to the temple at Bountiful. At each station, He gave covenant instruction to His people. And each time, the pattern deepened — from enforced distance to invited touch, from law on stone to law on hearts, from terror to Hosanna.

This article traces that progression: from the original Shavuot at Sinai, through the New Testament Pentecost, to the Sermon on the Mount and the Sermon at the Temple in 3 Nephi — revealing a single divine pattern of covenant-giving that culminates in the presence of the risen Christ.

---

## The Spring Feast Timeline

<div class="feast-timeline">
    <div class="timeline-item">
        <img src="/images/culture/jewish-festivals/feast-icons/passover.png" alt="Passover">
        <h4>14 Nisan: Passover</h4>
        <p>Lamb slain at twilight &bull; Christ crucified</p>
    </div>
    <div class="timeline-item">
        <img src="/images/culture/jewish-festivals/feast-icons/unleavened-bread.png" alt="Unleavened Bread">
        <h4>15 Nisan: Unleavened Bread</h4>
        <p>High Sabbath &bull; Christ in tomb</p>
    </div>
    <div class="timeline-item">
        <img src="/images/culture/jewish-festivals/feast-icons/bikkurim.png" alt="Firstfruits">
        <h4>16 Nisan: Firstfruits</h4>
        <p>Christ rises &bull; Barley sheaf waved</p>
    </div>
    <div class="timeline-item highlight">
        <img src="/images/culture/jewish-festivals/feast-icons/pentecost.png" alt="Pentecost">
        <h4>+50 Days: SHAVUOT</h4>
        <p>Torah given &bull; Spirit descends &bull; Wheat harvest</p>
    </div>
</div>

The gap between Bikkurim and Shavuot is not empty time. It is the Counting of the Omer — forty-nine days of deliberate, numbered anticipation. Israel counted each day between the first harvest and the full harvest, between resurrection and revelation, between deliverance and covenant.

> "And ye shall count unto you from the morrow after the sabbath, from the day that ye brought the sheaf of the wave offering; seven sabbaths shall be complete: Even unto the morrow after the seventh sabbath shall ye number fifty days; and ye shall offer a new meat offering unto the LORD." (<a href="https://www.blueletterbible.org/kjv/lev/23/15/" target="_blank" data-ref="Leviticus 23:15-16">Leviticus 23:15-16</a>)

---

## The Biblical Foundation

### The Names of the Feast

| Name | Hebrew / Greek | Meaning | Reference |
|------|--------|---------|-----------|
| **Feast of Weeks** | <a href="https://www.blueletterbible.org/lexicon/h7620/kjv/wlc/0-1/" target="_blank">שָׁבֻעוֹת</a> (*Shavuot*) | Seven weeks after Firstfruits | <a href="https://www.blueletterbible.org/kjv/deu/16/10/" target="_blank" data-ref="Deuteronomy 16:10">Deuteronomy 16:10</a> |
| **Feast of Harvest** | חַג הַקָּצִיר (*Chag HaKatzir*) | Celebrates the wheat harvest | <a href="https://www.blueletterbible.org/kjv/exo/23/16/" target="_blank" data-ref="Exodus 23:16">Exodus 23:16</a> |
| **Pentecost** | πεντηκοστή (*Pentekoste*) | "Fiftieth" — the Greek name | <a href="https://www.blueletterbible.org/kjv/act/2/1/" target="_blank" data-ref="Acts 2:1">Acts 2:1</a> |

<div class="info-box">
<strong>A note on "firstfruits":</strong> Numbers 28:26 also calls Shavuot <em>Yom HaBikkurim</em> ("Day of Firstfruits"), but this refers to the <strong>wheat</strong> firstfruits offered at the end of the grain harvest — distinct from the <strong>barley</strong> firstfruits (<em>Bikkurim</em>) waved during Passover week (<a href="https://www.blueletterbible.org/kjv/lev/23/10/" target="_blank" data-ref="Leviticus 23:10-11">Leviticus 23:10-11</a>). The Passover-week Bikkurim — fulfilled in Christ's resurrection — is covered in our <a href="/culture/jewish/moedim/bikkurim/">Bikkurim article</a>.
</div>

Unlike Passover and Sukkot, Shavuot has no specific date in the Torah — only a count. It is defined entirely by its relationship to what came before. You cannot observe Shavuot without first counting from Passover. The feast is, by design, a destination reached through sustained anticipation.

### The Pilgrimage Requirement

Shavuot is one of the three pilgrimage festivals (*shalosh regalim*) when every Israelite male was commanded to appear before the Lord at the Temple:

> "Three times in a year shall all thy males appear before the LORD thy God in the place which he shall choose; in the feast of unleavened bread, and in the feast of weeks, and in the feast of tabernacles" (<a href="https://www.blueletterbible.org/kjv/deu/16/16/" target="_blank" data-ref="Deuteronomy 16:16">Deuteronomy 16:16</a>)

This is why Jerusalem was packed with "devout men, out of every nation under heaven" on the day of Pentecost in Acts 2:5 — they were there for Shavuot.

### The Two Loaves

<div class="info-box insight">
The distinctive offering of Shavuot is unique among the feasts: two loaves of bread baked <strong>with leaven</strong> (<a href="https://www.blueletterbible.org/kjv/lev/23/17/" target="_blank" data-ref="Leviticus 23:17">Leviticus 23:17</a>). Every other grain offering in the Temple was unleavened. The two leavened loaves are the only exception. Why leaven? Leaven typically symbolizes sin in scripture (1 Corinthians 5:6-8). But at Shavuot, leavened bread is offered to God — perhaps signaling that the covenant is for a people who are <strong>not yet perfected</strong>. God accepts what still rises and ferments. The Torah is given not to the sinless but to the willing.
</div>

The two loaves have been interpreted as representing:
- Israel and the nations (both invited into covenant)
- The Written Torah and the Oral Torah
- The Old Covenant and the New Covenant

---

<details class="section-dropdown" id="sinai-section">
<summary>The First Shavuot: Sinai</summary>
<div class="section-body">

## The First Shavuot: Sinai

### The Timing

| Event | Date | Source |
|-------|------|--------|
| Exodus from Egypt | 15 Nisan (Passover) | Exodus 12:41 |
| Arrival at Sinai | 1 Sivan ("the third month") | Exodus 19:1 |
| Three days of sanctification | 3-5 Sivan | Exodus 19:10-11 |
| God descends on Sinai | 6 Sivan = **Shavuot** | <a href="https://www.sefaria.org/Shabbat.86b" target="_blank">Talmud, Shabbat 86b</a> |

Fifty days from Passover to Sinai. The same count that defines Shavuot in Leviticus 23 matches the narrative timeline in Exodus 19. The harvest festival and the covenant-giving converge on the same date.

### What Happened at Sinai

> "There were thunders and lightnings, and a thick cloud upon the mount, and the voice of the trumpet exceeding loud; so that all the people that was in the camp trembled... mount Sinai was altogether on a smoke, because the LORD descended upon it in fire" (<a href="https://www.blueletterbible.org/kjv/exo/19/16/" target="_blank" data-ref="Exodus 19:16-18">Exodus 19:16-18</a>)

Three features define the Sinai encounter:

1. **Enforced distance.** Boundaries were set around the mountain. "Whosoever toucheth the mount shall be surely put to death" (Exodus 19:12). The holiness of God required maximum separation.

2. **Mediated communication.** Moses alone ascended as the designated mediator. The people heard God's voice but could not bear it: "Let not God speak with us, lest we die" (Exodus 20:19). They retreated further, and Moses stood between them and God.

<div class="info-box sinai">
<strong>Moses as <em>Mesites</em>:</strong> The Greek word for mediator — <a href="https://www.blueletterbible.org/lexicon/g3316/kjv/tr/0-1/" target="_blank">μεσίτης</a> (<em>mesites</em>) — comes from <a href="https://www.blueletterbible.org/lexicon/g3319/kjv/tr/0-1/" target="_blank">μέσος</a> (<em>mesos</em>), meaning "middle, in the midst." A mediator is literally one who stands in the middle between two parties. Moses' very role at Sinai — ascending to God, descending to the people, standing in the gap — defines what a <em>mesites</em> does. In this sense, Moses represents a type and shadow for Jesus Christ. And <em>mesites</em> is the exact word the author of Hebrews uses to describe what Christ fulfills: "Jesus the <strong>mediator</strong> [<em>mesites</em>] of a new covenant" (<a href="https://www.blueletterbible.org/kjv/heb/12/24/" target="_blank" data-ref="Hebrews 12:24">Hebrews 12:24</a>; see also <a href="https://www.blueletterbible.org/kjv/heb/8/6/" target="_blank" data-ref="Hebrews 8:6">Hebrews 8:6</a>). Moses stood in the <em>mesos</em> at Sinai; Christ is the <em>mesites</em> of the better covenant — the one who does not merely stand between God and man but <em>is</em> both God and man.
</div>

3. **Law on stone.** The covenant was inscribed on tablets — external, objective, unchangeable. The people received commandments written by God's finger on dead rock.

The final image of Sinai is distance: "The people stood afar off, and Moses drew near unto the thick darkness where God was" (Exodus 20:21). One man close; the whole nation far away.

### The Rabbinic Shavuot Traditions

<details>
<summary>Tikkun Leil Shavuot — All-Night Torah Study</summary>
<div>
The practice of staying awake all night studying Torah. According to midrash, Israel overslept on the morning God was to give the Torah, so Moses had to wake them. To atone for this, Jews stay awake all night demonstrating eagerness for God's word (<a href="https://www.sefaria.org/Shabbat.86b" target="_blank">Talmud, Shabbat 86b</a>).
</div>
</details>

<details>
<summary>The Voice in Seventy Languages</summary>
<div>
<a href="https://www.sefaria.org/Shemot_Rabbah.5.9" target="_blank">Exodus Rabbah 5:9</a> teaches that God's voice at Sinai "went forth and was divided into seventy languages, so that all nations heard it." Torah was offered to the whole world. This tradition foreshadows Pentecost, when the disciples spoke "in every language" (Acts 2:4-11).
</div>
</details>

<details>
<summary>God Offered Torah to All Nations</summary>
<div>
<a href="https://www.sefaria.org/Sifrei_Devarim.343" target="_blank">Sifre Deuteronomy 343</a> records that God approached every nation before Israel. Each asked what the Torah contained and declined when they heard a commandment that conflicted with their way of life. Only Israel accepted without conditions: "All that the LORD hath spoken we will do" (Exodus 19:8).
</div>
</details>

<details>
<summary>Reading the Book of Ruth</summary>
<div>
Ruth is read on Shavuot because she exemplifies voluntary acceptance of Torah. As a Moabite widow, she had every reason to return home. Instead she declared: "Thy people shall be my people, and thy God my God" (<a href="https://www.blueletterbible.org/kjv/rut/1/16/" target="_blank" data-ref="Ruth 1:16">Ruth 1:16</a>) — a convert's acceptance of covenant, echoing Israel's acceptance at Sinai. See our <a href="#ruth-section">expanded Ruth section</a> below for the full Shavuot connections.
</div>
</details>

<details>
<summary>Greenery, Dairy, and Other Customs</summary>
<div>
<strong>Decorating with greenery:</strong> Synagogues are adorned with flowers and plants, representing Mount Sinai blooming in the desert when God descended.<br><br>
<strong>Dairy foods:</strong> Traditional Shavuot meals feature dairy dishes. Multiple explanations exist: Israel had not yet received the kosher laws and so could not prepare meat properly; or the Torah is compared to "milk and honey" (Song of Solomon 4:11); or the two dairy meals plus one meat meal equal the three-day sanctification period.
</div>
</details>


</div>
</details>

<details class="section-dropdown" id="pentecost-section">
<summary>The New Testament Shavuot: Pentecost (Acts 2)</summary>
<div class="section-body">

## The New Testament Shavuot: Pentecost (Acts 2)

Fifty days after Christ's resurrection — on the very day of Shavuot — the Holy Spirit descended on the assembled disciples in Jerusalem.

> "And when the day of Pentecost was fully come, they were all with one accord in one place. And suddenly there came a sound from heaven as of a rushing mighty wind, and it filled all the house where they were sitting. And there appeared unto them cloven tongues like as of fire, and it sat upon each of them. And they were all filled with the Holy Ghost, and began to speak with other tongues, as the Spirit gave them utterance." (<a href="https://www.blueletterbible.org/kjv/act/2/1/" target="_blank" data-ref="Acts 2:1-4">Acts 2:1-4</a>)

<table class="proximity-table">
<thead>
<tr><th>Sinai (Exodus 19-20)</th><th>Pentecost (Acts 2)</th></tr>
</thead>
<tbody>
<tr><td>Fire descends on the mountain</td><td>Tongues of fire descend on each person</td></tr>
<tr><td>Voice divided into 70 languages (Exodus Rabbah 5:9)</td><td>Disciples speak in every language (Acts 2:4-11)</td></tr>
<tr><td>Law written on stone tablets</td><td>Law written on hearts by the Spirit (Jeremiah 31:33)</td></tr>
<tr><td>Moses mediates between God and people</td><td>The Spirit indwells each believer directly</td></tr>
<tr><td>Israel formed as covenant nation</td><td>The Church formed as covenant community</td></tr>
<tr><td>"The people stood afar off" (Exodus 20:18)</td><td>"They were all with one accord in one place" (Acts 2:1)</td></tr>
<tr><td>Boundaries enforce distance from God</td><td>The Spirit removes the veil — God dwells within</td></tr>
</tbody>
</table>

<div class="info-box insight">
<strong>The Fulfillment of Jeremiah:</strong> "I will put my law in their inward parts, and write it in their hearts; and will be their God, and they shall be my people" (<a href="https://www.blueletterbible.org/kjv/jer/31/33/" target="_blank" data-ref="Jeremiah 31:33">Jeremiah 31:33</a>). Pentecost is the fulfillment of Sinai. What was external becomes internal. What was mediated becomes direct. What was written on stone is written on the heart.
</div>


</div>
</details>

<details class="section-dropdown" id="higher-law-section" open>
<summary>The Law, the Higher Law, and the Blessing</summary>
<div class="section-body">

## The Law, the Higher Law, and the Blessing

<div class="info-box" style="background: linear-gradient(135deg, #fdf5e7, #fff8dc); border-left-color: #8b6914;">
<strong style="font-size: 1.1rem;">"There is a law, irrevocably decreed in heaven before the foundations of this world, upon which all blessings are predicated — And when we obtain any blessing from God, it is by obedience to that law upon which it is predicated."</strong>
<div style="margin-top: 0.5rem; font-size: 0.9rem;">— <a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/130?lang=eng&id=20-21" target="_blank" data-ref="D&C 130:20-21">D&C 130:20-21</a></div>
</div>

### The Two Sets of Tablets: Same Words, Different Capacity

The Joseph Smith Translation of Exodus 34 reveals something the world has missed. When God commanded Moses to hew a second set of tablets, He said:

> "Hew thee two other tables of stone like unto the first, and I will write upon them also **the words of the law, according as they were written at the first** on the tables which thou brakest; **but it shall not be according to the first**, for I will take away the priesthood out of their midst; therefore, **my holy order and the ordinances thereof shall not go before them**; for my presence shall not go up in their midst, lest I destroy them." (<a href="https://www.churchofjesuschrist.org/study/scriptures/jst/jst-ex/34?lang=eng&id=1" target="_blank" data-ref="JST Exodus 34:1">JST Exodus 34:1</a>)

> "But I will give unto them **the law as at the first**, but it shall be after **the law of a carnal commandment**; for I have sworn in my wrath that they shall not enter into my presence, into my rest, in the days of their pilgrimage." (<a href="https://www.churchofjesuschrist.org/study/scriptures/jst/jst-ex/34?lang=eng&id=2" target="_blank" data-ref="JST Exodus 34:2">JST Exodus 34:2</a>)

<div class="info-box sinai">
<strong>The profound implication:</strong> The writing on the second tablets was <strong>identical</strong> to the first. "The words of the law, according as they were written at the first." The law did not change. What changed was Israel's <em>capacity to interpret it</em>. Two things were removed: Moses was "taken out of their midst" as mediator of the higher covenant (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/84?lang=eng&id=25" target="_blank" data-ref="D&C 84:25">D&C 84:25</a>), and "the holy order and the ordinances thereof" — the Melchizedek Priesthood and its temple ordinances — were withdrawn. Without the priesthood, without the ordinances, without the prophet in their midst, the people could read the same words but could only see the surface — the prohibitions, the carnal commandments — not the deeper covenant layers the words had always contained.
</div>

The difference between the "lower law" and the "higher law" is not in the written text alone. It is in the **interpretation** — and the interpretation depends on one's understanding of the priesthood, the ordinances, the patterns outlined in the Plan of Salvation, and the presence of God's authorized servants. Without this, man is left to their own devices to interpret the text, and thus we get a list of "Thou shalt not's." But there is so much more.

This may be part of the reason why Christ said in the Sermon on the Mount:

> "Except your righteousness shall **exceed the righteousness of the scribes and Pharisees**, ye shall in no case enter into the kingdom of heaven." (<a href="https://www.blueletterbible.org/kjv/mat/5/20/" target="_blank" data-ref="Matthew 5:20">Matthew 5:20</a>)

The Pharisees read the same Torah. They kept the letter meticulously. But they could not see past the prohibition to the transformation — because the higher priesthood and its ordinances had been lost. Christ, as the Lawgiver Himself, now reopened what had been sealed. His "but I say unto you" statements are not *new* laws — they are the **original depth** of the law restored. He is reading the same tablets Moses brought down, but reading them with the eyes of the Holy Order.

### Three Layers of the Law: Telestial, Terrestrial, Celestial

Every commandment, then, contains three layers — and every layer carries an inherent blessing:

- **The Telestial Layer (The Prohibition):** "Thou shalt not..." — the base law that restrains the hand. This is the law of carnal commandments, the minimum standard. Obedience at this level keeps society from collapse. It is the law as the Pharisees understood it.

- **The Terrestrial Layer (The Transformation):** "But I say unto you..." — the higher law that transforms the heart. Christ moves from the act to the intent, from the hand to the motive. Anger, not just murder. Lust, not just adultery. This level purifies the inner person.

- **The Celestial Layer (The Covenant Action):** "Be ye therefore perfect..." — the fullness of the law, which is not merely avoiding evil or even purifying the heart, but **actively pursuing the opposite virtue**. Reconcile with your brother. Love your enemies. Offer your gifts at the altar. This is consecration — the complete embrace of the Atonement, which qualifies us for the celestial kingdom and the presence of God.

> "There is a law, irrevocably decreed in heaven before the foundations of this world, upon which all blessings are predicated — And when we obtain any blessing from God, it is by obedience to that law upon which it is predicated." (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/130?lang=eng&id=20-21" target="_blank" data-ref="D&C 130:20-21">D&C 130:20-21</a>)

**Click any commandment to explore its three layers and inherent blessing:**

<div id="commandments-container">
</div>

<script>
const commandments = [
    {num: 1, title: '"Thou shalt have no other gods before me" (Exodus 20:3)', law: 'Do not worship false gods — remove idols from your life', higher: '"Seek ye first the kingdom of God, and his righteousness" (Matthew 6:33) — God is not merely first among priorities; He is the organizing principle of all priorities', covenant: 'Love the Lord "with all thy heart, and with all thy soul, and with all thy mind" (Matthew 22:37) — total, undivided devotion', blessing: '"All these things shall be added unto you" (Matthew 6:33); "the fulness of the earth is yours" (D&C 59:16)'},
    {num: 2, title: '"Thou shalt not make unto thee any graven image" (Exodus 20:4)', law: 'Do not reduce God to an object you can control or manipulate', higher: '"God is a Spirit: and they that worship him must worship him in spirit and in truth" (John 4:24) — worship the living God, not a concept of God shaped to your preferences', covenant: '"Blessed are the pure in heart: for they shall see God" (Matthew 5:8) — replace the graven image with the living vision; see God as He truly is', blessing: 'Theophany — "they shall see God"; the promise of entering His presence, face to face'},
    {num: 3, title: '"Thou shalt not take the name of the LORD thy God in vain" (Exodus 20:7)', law: 'Do not swear false oaths or use God\'s name carelessly', higher: '"Swear not at all... But let your communication be, Yea, yea; Nay, nay" (Matthew 5:34, 37) — live with such integrity that your simple word is sufficient', covenant: 'Take His name upon you in covenant (sacrament prayer) and honor it by how you live — you bear His name; your life is the testimony', blessing: '"I, the Lord, am bound when ye do what I say" (D&C 82:10) — when we honor His name, He honors His promises'},
    {num: 4, title: '"Remember the sabbath day, to keep it holy" (Exodus 20:8)', law: 'Cease from labor on the seventh day', higher: '"Call the sabbath a delight, the holy of the LORD, honourable" (Isaiah 58:13) — not merely stopping work but finding joy in worship, rest, and renewal', covenant: '"Offer up thy sacraments upon my holy day" (D&C 59:9) — actively renew covenant through the sacrament; minister to others; sanctify the day with deliberate worship', blessing: '"I will cause thee to ride upon the high places of the earth, and feed thee with the heritage of Jacob" (Isaiah 58:14); "the fulness of the earth is yours" (D&C 59:16)'},
    {num: 5, title: '"Honour thy father and thy mother" (Exodus 20:12)', law: 'Respect and care for your parents', higher: 'Honor the divine pattern of family; see parenthood as participation in God\'s creative work', covenant: 'Turn the hearts of the children to the fathers (Malachi 4:6) — perform temple ordinances that seal families across generations; honor not only living parents but all ancestors', blessing: '"That thy days may be long upon the land which the LORD thy God giveth thee" (Exodus 20:12) — the only commandment with an explicit promise of longevity and inheritance'},
    {num: 6, title: '"Thou shalt not kill" (Exodus 20:13)', law: 'Do not take life', higher: '"Whosoever is angry with his brother without a cause shall be in danger of the judgment" (Matthew 5:22) — address the root, not just the fruit; anger is the seed of violence', covenant: '"Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift" (Matthew 5:23-24) — actively pursue reconciliation', blessing: '"Blessed are the peacemakers: for they shall be called the children of God" (Matthew 5:9) — those who make peace inherit divine identity'},
    {num: 7, title: '"Thou shalt not commit adultery" (Exodus 20:14)', law: 'Do not violate the marriage covenant', higher: '"Whosoever looketh on a woman to lust after her hath committed adultery with her already in his heart" (Matthew 5:28) — purity begins in the gaze, not just in the act', covenant: 'Guard the heart with radical devotion; "if thy right eye offend thee, pluck it out" (Matthew 5:29) — remove whatever leads you toward betrayal, however valuable it seems', blessing: '"Blessed are the pure in heart: for they shall see God" (Matthew 5:8) — purity of heart opens the way to God\'s presence. Virtue and fidelity demonstrate not only our loyalty to our covenants with our spouse, they also represent our loyalty to God and our covenants with God. Israel is the betrothed bride of Jehovah.'},
    {num: 8, title: '"Thou shalt not steal" (Exodus 20:15)', law: 'Do not take what belongs to another', higher: '"Give to him that asketh thee, and from him that would borrow of thee turn not thou away" (Matthew 5:42) — move from not taking to freely giving', covenant: 'Consecrate what you have: "Inasmuch as ye have done it unto one of the least of these my brethren, ye have done it unto me" (Matthew 25:40) — see your possessions as stewardship, not ownership', blessing: '"Blessed are the merciful: for they shall obtain mercy" (Matthew 5:7); "I will open you the windows of heaven" (Malachi 3:10)'},
    {num: 9, title: '"Thou shalt not bear false witness" (Exodus 20:16)', law: 'Do not lie about your neighbor', higher: '"Let your communication be, Yea, yea; Nay, nay" (Matthew 5:37) — live with such transparent honesty that oaths are unnecessary', covenant: 'Bear true witness of Christ — become a living testimony; "ye shall be witnesses unto me" (Acts 1:8). The tablets are called "tablets of the testimony" (luchot ha-edut) — bearing witness is the heart of the covenant', blessing: '"Ye shall know the truth, and the truth shall make you free" (John 8:32) — truth liberates; falsehood enslaves'},
    {num: 10, title: '"Thou shalt not covet" (Exodus 20:17)', law: 'Do not desire what belongs to your neighbor', higher: '"Lay not up for yourselves treasures upon earth... but lay up for yourselves treasures in heaven" (Matthew 6:19-20) — redirect desire from temporal to eternal', covenant: 'Cultivate gratitude and generosity; "freely ye have received, freely give" (Matthew 10:8) — the antidote to coveting is not suppressing desire but redirecting it toward God and His children', blessing: '"Blessed are they which do hunger and thirst after righteousness: for they shall be filled with the Holy Ghost" (3 Nephi 12:6) — when desire is rightly directed, it is not suppressed but fulfilled'}
];

const container = document.getElementById('commandments-container');
commandments.forEach(c => {
    const card = document.createElement('div');
    card.className = 'commandment-card';
    card.innerHTML = `
        <div class="commandment-header" onclick="toggleCommandment(this)">
            <div style="display:flex;align-items:center;"><span class="num">${c.num}</span> ${c.title}</div>
            <span class="arrow">&#9654;</span>
        </div>
        <div class="commandment-body">
            <div class="commandment-body-inner">
                <div class="law-row"><div class="law-label telestial">Telestial</div><div class="law-text">${c.law}</div></div>
                <div class="law-row"><div class="law-label terrestrial">Terrestrial</div><div class="law-text">${c.higher}</div></div>
                <div class="law-row"><div class="law-label celestial">Celestial</div><div class="law-text">${c.covenant}</div></div>
                <div class="law-row"><div class="law-label blessing">Blessing</div><div class="law-text">${c.blessing}</div></div>
            </div>
        </div>
    `;
    container.appendChild(card);
});

function toggleCommandment(header) {
    const card = header.parentElement;
    const body = header.nextElementSibling;
    const isOpen = card.classList.contains('open');
    if (isOpen) {
        body.style.maxHeight = '0px';
        card.classList.remove('open');
    } else {
        body.style.maxHeight = body.scrollHeight + 'px';
        card.classList.add('open');
        setTimeout(() => { if (card.classList.contains('open')) body.style.maxHeight = 'none'; }, 500);
    }
}
</script>

### The Governing Principle

The words on the second tablets were identical to the first. The law never changed. What changed was Israel's capacity to read it — because the priesthood, the ordinances, and the prophet were taken from their midst. The movement from telestial to terrestrial to celestial is not a movement from one law to another. It is the movement from reading the surface to reading the depth — from the letter that kills to the Spirit that gives life (2 Corinthians 3:6).

At the telestial level, the commandments restrain the hand. At the terrestrial level, they transform the heart. At the celestial level, they consecrate the whole person — and qualify us for the presence of God. This is what the Sermon on the Mount restores: not a new law, but the original depth of the law, read through the eyes of the Holy Order.

> "I, the Lord, am bound when ye do what I say; but when ye do not what I say, ye have no promise." (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/82?lang=eng&id=10" target="_blank" data-ref="D&C 82:10">D&C 82:10</a>)

> "Consider on the blessed and happy state of those that keep the commandments of God. For behold, they are blessed in all things, both temporal and spiritual; and if they hold out faithful to the end they are received into heaven, that thereby they may dwell with God in a state of never-ending happiness." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/2?lang=eng&id=41" target="_blank" data-ref="Mosiah 2:41">Mosiah 2:41</a>)


</div>
</details>

<details class="section-dropdown" id="mountains-section">
<summary>The Mountain of the Lord: A Temple Progression</summary>
<div class="section-body">

## The Mountain of the Lord: A Temple Progression

> "And it shall come to pass in the last days, that the mountain of the LORD's house shall be established in the top of the mountains, and shall be exalted above the hills; and all nations shall flow unto it." (<a href="https://www.blueletterbible.org/kjv/isa/2/2/" target="_blank" data-ref="Isaiah 2:2">Isaiah 2:2</a>)

Mountain and temple are synonymous. John W. Welch, in <a href="https://scholarsarchive.byu.edu/mi/89/" target="_blank"><em>The Sermon at the Temple and the Sermon on the Mount</em></a> (FARMS, 1990), argued that the Sermon on the Mount is a **temple text** — a structured progression through the stages of approaching, covenanting with, and entering God's presence. He identified **25 temple-related stages** in Matthew, **doubled to approximately 50** at the temple in Bountiful.

### Four Mountains, One Progression

<div class="mountain-grid" style="grid-template-columns: 1fr;">
    <div class="mountain-card sinai" style="padding: 0; overflow: hidden;">
        <img src="/images/culture/jewish-festivals/shavuot/shavuot-hero.gif" alt="Mount Sinai" style="width: 100%; display: block;">
        <div style="padding: 1.75rem;">
            <h4>1. Mount Sinai — The Distant Mountain</h4>
            <ul>
                <li>God descends in fire, smoke, and earthquake</li>
                <li>Boundaries enforced: touch the mountain and die</li>
                <li>The people stand "afar off" and beg for a mediator</li>
                <li>Moses alone ascends</li>
                <li>Law given on stone — external, objective, unbending</li>
            </ul>
        </div>
    </div>
    <div class="mountain-card galilee" style="padding: 0; overflow: hidden;">
        <img src="/images/culture/jewish-festivals/shavuot/sermon-mount-hero.gif" alt="Sermon on the Mount" style="width: 100%; display: block;">
        <div style="padding: 1.75rem;">
            <h4>2. The Mountain in Galilee — The Teaching Mountain</h4>
            <ul>
                <li>Jesus ascends; disciples come to Him (no boundary mentioned)</li>
                <li>He sits — the rabbinic posture of authoritative instruction</li>
                <li>He teaches directly; no intermediary needed</li>
                <li>The crowd is "astonished" — awe replaces terror</li>
                <li>Fulfillment is future: "till all be fulfilled" (Matthew 5:18)</li>
            </ul>
        </div>
    </div>
    <div style="background: linear-gradient(135deg, #9a7a48, #c4a060); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <img src="/images/culture/jewish-festivals/shavuot/pentecost-hero.gif" alt="Pentecost" style="width: 100%; display: block;">
        <div style="padding: 1.75rem; color: white;">
            <h4 style="color: white; margin-top: 0; font-size: 1.2rem;">3. The Temple Mount in Jerusalem — The Mountain of the Spirit</h4>
            <ul style="padding-left: 1.25rem; line-height: 1.8;">
                <li>The disciples are gathered at the Temple for Shavuot — the same mountain where Abraham bound Isaac, where Solomon built the Temple</li>
                <li>Tongues of fire rest on each person individually</li>
                <li>Disciples speak in every language — fulfilling the seventy languages at Sinai</li>
                <li>The law is written on hearts, not stone (Jeremiah 31:33)</li>
                <li>No mediator — the Spirit indwells each believer directly</li>
            </ul>
        </div>
    </div>
    <div class="mountain-card bountiful" style="padding: 0; overflow: hidden;">
        <img src="/images/culture/jewish-festivals/shavuot/third-nephi-hero.gif" alt="Christ at Bountiful" style="width: 100%; display: block;">
        <div style="padding: 1.75rem;">
            <h4>4. The Temple at Bountiful — The Temple of Presence</h4>
            <ul>
                <li>Christ descends in a white robe, stands "in the midst of them"</li>
                <li>"Come forth unto me, that ye may feel the prints of the nails"</li>
                <li>The multitude goes forth "one by one" — every person touches Him</li>
                <li>"Hosanna! Blessed be the name of the Most High God!"</li>
                <li>Fulfillment is past: "In me it hath all been fulfilled"</li>
            </ul>
        </div>
    </div>
</div>

### The Escalating Proximity

<table class="proximity-table">
<thead>
<tr><th>Feature</th><th>Sinai</th><th>Galilee</th><th>Jerusalem (Pentecost)</th><th>Bountiful</th></tr>
</thead>
<tbody>
<tr><td><strong>God's approach</strong></td><td>Descends in fire/smoke</td><td>Jesus ascends mountain</td><td>Spirit descends as wind and fire</td><td>Christ descends in white robe, stands among them</td></tr>
<tr><td><strong>Touch</strong></td><td>Death for touching the mount</td><td>No command</td><td>Tongues of fire sit on each person</td><td>"Come forth... feel the prints"</td></tr>
<tr><td><strong>People's response</strong></td><td>Fell back; stood afar off</td><td>Astonished</td><td>"With one accord in one place"</td><td>Fell down; rose; worshipped</td></tr>
<tr><td><strong>Contact with God</strong></td><td>Moses only</td><td>No record of touch</td><td>Spirit indwells each believer</td><td>One by one, ALL touched Him</td></tr>
<tr><td><strong>Intermediary</strong></td><td>Moses (essential)</td><td>None (Jesus teaches directly)</td><td>None — the Spirit is direct</td><td>None; multitude comes directly</td></tr>
<tr><td><strong>Law written on</strong></td><td>Stone tablets</td><td>Interpreted from within</td><td>Hearts (Jeremiah 31:33)</td><td>Fulfilled in Christ's person</td></tr>
<tr><td><strong>Fulfillment</strong></td><td>Law given (to be fulfilled)</td><td>"Till all be fulfilled" (future)</td><td>Spirit empowers obedience</td><td>"In me it hath all been fulfilled" (past)</td></tr>
<tr><td><strong>Perfection standard</strong></td><td>N/A</td><td>"Your Father in heaven" (5:48)</td><td>N/A</td><td>"Even as I, or your Father" (12:48)</td></tr>
<tr><td><strong>Covenant ordinance</strong></td><td>Follows in Exodus 24</td><td>No immediate ordinance</td><td>Baptism of 3,000 (Acts 2:41)</td><td>Baptism established immediately</td></tr>
</tbody>
</table>

### The Beatitudes, Psalm 119, and Temple Entry

The word we translate as "blessed" carries a rich linguistic history across four languages:

| Language | Term | Connection |
|----------|------|------------|
| **Hebrew** | <a href="https://www.blueletterbible.org/lexicon/h835/kjv/wlc/0-1/" target="_blank">אַשְׁרֵי</a> (*ashrei*) | The original — an exclamation recognizing a person in covenant motion |
| **Greek** | <a href="https://www.blueletterbible.org/lexicon/g3107/kjv/tr/0-1/" target="_blank">μακάριοι</a> (*makarioi*) | The New Testament rendering — used in Matthew 5 and 3 Nephi 12 |
| **Latin** | <a href="https://logeion.uchicago.edu/beatus" target="_blank">*beati*</a> | The Vulgate translation — root of "**Beatitudes**" |
| **English** | <a href="https://webstersdictionary1828.com/Dictionary/Blessed" target="_blank">blessed</a> | From Old English *blēdsian*, from Proto-Germanic *\*blōdisōną* — "<a href="https://www.etymonline.com/word/bless" target="_blank">to hallow with blood</a>" |

The Hebrew *ashrei* is not passive contentment. It is active recognition: "How blessed is the one who walks!" It describes a person already in covenant motion — walking, keeping, doing. This is the word that opens both the Beatitudes and Psalm 119.

<div class="info-box">
<strong>A note on the English word:</strong> In Hebrew, Greek, and Latin, the word for "blessed" carries the sense of <em>happiness</em> — walking rightly, being fortunate, dwelling in felicity. The English word stands alone. Old English <em>blēdsian</em> descends from Proto-Germanic <em>*blōdisōną</em>, "to hallow with blood" — a word rooted in the ritual sprinkling of altars with sacrificial blood. When the Anglo-Saxon translators needed a word for <em>ashrei</em>, they reached not for "happy" but for "consecrated by sacrifice." English speakers hear "blessed" with an echo of blood that the original Hebrew, Greek, and Latin do not carry. Whether by accident or providence, the English Beatitudes whisper what the Hebrew text does not say aloud: that the blessedness Christ pronounces on the mountain is inseparable from the blood He will shed on another.
</div>

#### The Psalm 119 Connection

When Christ delivered the Beatitudes, He was not inventing a new literary form. He was drawing directly from **Psalm 119** — the longest chapter in the Bible and the great Torah psalm. The connections are structural, not just thematic:

**The doubled** ***ashrei*** **opening:** Psalm 119 opens with *ashrei* declared **twice** before a single commandment is given:

> "**Blessed** [*ashrei*] are the undefiled in the way, who walk in the law of the LORD. **Blessed** [*ashrei*] are they that keep his testimonies, and that seek him with the whole heart." (Psalm 119:1-2)

Two declarations of blessedness, then the Torah instruction begins. No other psalm opens with *ashrei* doubled.

**The eight-verse acrostic structure:** Psalm 119 is an acrostic poem of 22 stanzas (one for each letter of the Hebrew alphabet), with **eight verses per stanza**. This octave structure represents a complete cycle of reflection and contemplation on the law — eight lines of meditation on Torah for each letter, 176 verses total. The number eight in Hebrew thought signifies completion and new beginning (circumcision on the eighth day, the octave in music that completes the scale and begins again).

**The Beatitudes as octave:** Christ delivers **eight Beatitudes** in the Sermon on the Mount (Matthew 5:3-10) — the same octave pattern as Psalm 119's stanzas. This is not coincidence. Christ is structuring His teaching on the Torah psalm's own architecture: a complete cycle of covenant blessedness, each one building on the last, culminating in the promise of the kingdom of heaven.

#### The Bountiful Doubling

At Bountiful, Christ mirrors the Psalm 119 pattern with even greater precision. Before the formal Beatitudes begin, He opens with **two** preliminary blessings — exactly as Psalm 119 opens with *ashrei* doubled:

> "**Blessed** are ye if ye shall give heed unto the words of these twelve whom I have chosen" (3 Nephi 12:1)

> "And again, **more blessed** are they who shall believe in your words" (3 Nephi 12:2)

Then the Beatitudes proper begin at 3 Nephi 12:3. The doubled *ashrei* opening of Psalm 119 — the great Torah psalm — reappears at the temple in Bountiful, where the resurrected Christ delivers the fulfilled Torah to His covenant people. The Lawgiver is quoting His own psalm.

#### The Side-by-Side: Psalm 119, the Sermon on the Mount, and the Sermon at the Temple

Click any row to expand the full verse text. <span class="ashrei-highlight">Gold highlighting</span> marks every occurrence of *ashrei* / "blessed."

<style>
/* Beatitudes Comparison */
.beat-compare { margin: 2rem 0; }
.beat-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0;
    border-bottom: 1px solid #e8dcc8;
    cursor: pointer;
    transition: background 0.2s;
}
.beat-row:hover { background: #fdf9f2; }
.beat-row.header-row {
    background: linear-gradient(135deg, #1a6b74, #2a8a94);
    color: white;
    cursor: default;
    border-radius: 12px 12px 0 0;
    position: sticky;
    top: 0;
    z-index: 2;
}
.beat-row.header-row .beat-cell { font-weight: 700; font-size: 0.95rem; border-right-color: rgba(255,255,255,0.2); }
.beat-row.section-label {
    background: linear-gradient(135deg, #fdf5e7, #fff8dc);
    cursor: default;
    border-bottom: 2px solid #d4a53e;
}
.beat-row.section-label .beat-cell {
    font-weight: 700;
    color: #8b6914;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.6rem 1rem;
}
.beat-cell {
    padding: 0.75rem 1rem;
    font-size: 0.9rem;
    line-height: 1.5;
    border-right: 1px solid #e8dcc8;
}
.beat-cell:last-child { border-right: none; }
.beat-cell .ref { display: block; font-size: 0.75rem; color: #888; margin-top: 0.25rem; }
.beat-cell .ref a { color: #1a6b74; text-decoration: none; }
.beat-cell .ref a:hover { text-decoration: underline; color: #8b6914; }
.beat-cell .hebrew-text { font-family: "SBL Hebrew", "Ezra SIL", serif; font-size: 1rem; direction: rtl; text-align: right; line-height: 1.8; }
.beat-detail {
    display: none;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0;
    background: #f8f9fa;
    border-bottom: 2px solid #e8dcc8;
}
.beat-detail.open { display: grid; }
.beat-detail .beat-cell {
    font-size: 0.85rem;
    color: #444;
    padding: 0.75rem 1rem;
    border-right: 1px solid #e0e0e0;
}
.beat-detail .beat-cell:last-child { border-right: none; }
.ashrei-highlight {
    background: linear-gradient(135deg, #fde68a, #fbbf24);
    padding: 1px 4px;
    border-radius: 3px;
    font-weight: 600;
    color: #78350f;
}
.beat-diff {
    background: #dbeafe;
    padding: 1px 4px;
    border-radius: 3px;
    font-weight: 600;
    color: #1e40af;
}
.beat-empty { color: #ccc; font-style: italic; font-size: 0.8rem; }
.beat-compare-wrapper {
    border: 2px solid #e8dcc8;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
@media (max-width: 768px) {
    .beat-row, .beat-detail { grid-template-columns: 1fr; }
    .beat-cell { border-right: none; border-bottom: 1px solid #e8dcc8; }
    .beat-cell:last-child { border-bottom: none; }
    .beat-row.header-row { border-radius: 12px 12px 0 0; }
    .beat-cell .hebrew-text { font-size: 0.95rem; }
}
</style>

<div class="beat-compare">
<div class="beat-compare-wrapper">

<div class="beat-row header-row">
    <div class="beat-cell">Psalm 119 <span style="opacity:0.7; font-weight:400;">(Torah Psalm)</span></div>
    <div class="beat-cell">Matthew 5 <span style="opacity:0.7; font-weight:400;">(Sermon on the Mount)</span></div>
    <div class="beat-cell">3 Nephi 12 <span style="opacity:0.7; font-weight:400;">(Sermon at the Temple)</span></div>
</div>

<!-- SECTION: Doubled Ashrei Opening -->
<div class="beat-row section-label">
    <div class="beat-cell" style="grid-column: 1 / -1;">The Doubled <em>Ashrei</em> Opening — Psalm 119 and 3 Nephi only</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="ashrei-highlight">אַשְׁרֵי</span> תְמִימֵי־דָרֶךְ<span class="ref"><a href="https://www.blueletterbible.org/kjv/psa/119/1/" target="_blank" data-ref="Psalm 119:1">Psalm 119:1</a></span></div>
    <div class="beat-cell"><span class="beat-empty">— no preliminary blessing —</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are ye if ye shall give heed unto the words of these twelve<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=1" target="_blank" data-ref="3 Nephi 12:1">3 Nephi 12:1</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"><span class="hebrew-text">אַשְׁרֵ֥י תְמִֽימֵי־דָ֑רֶךְ הַ֝הֹלְכִ֗ים בְּתוֹרַ֥ת יְהֹוָֽה׃</span><br><span class="ashrei-highlight">Blessed</span> are the undefiled in the way, who walk in the law of the LORD.</div>
    <div class="beat-cell"><span class="beat-empty">Matthew begins directly with the Beatitudes proper. No preliminary declaration.</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are ye if ye shall give heed unto the words of these twelve whom I have chosen from among you to minister unto you, and to be your servants; and unto them I have given power that they may baptize you with water; and after that ye are baptized with water, behold, I will baptize you with fire and with the Holy Ghost; therefore <span class="ashrei-highlight">blessed</span> are ye if ye shall believe in me and be baptized, after that ye have seen me and know that I am.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="ashrei-highlight">אַשְׁרֵי</span> נֹצְרֵי עֵדֹתָיו<span class="ref"><a href="https://www.blueletterbible.org/kjv/psa/119/2/" target="_blank" data-ref="Psalm 119:2">Psalm 119:2</a></span></div>
    <div class="beat-cell"><span class="beat-empty">— no preliminary blessing —</span></div>
    <div class="beat-cell">And again, <span class="ashrei-highlight">more blessed</span> are they who shall believe in your words<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=2" target="_blank" data-ref="3 Nephi 12:2">3 Nephi 12:2</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"><span class="hebrew-text">אַ֭שְׁרֵי נֹצְרֵ֥י עֵדֹתָ֗יו בְּכׇל־לֵ֥ב יִדְרְשֽׁוּהוּ׃</span><br><span class="ashrei-highlight">Blessed</span> are they that keep his testimonies, and that seek him with the whole heart.</div>
    <div class="beat-cell"><span class="beat-empty">The absence in Matthew is itself significant: the doubled ashrei appears only where the Lawgiver delivers the fulfilled Torah — at the Psalm's beginning and at Bountiful.</span></div>
    <div class="beat-cell">And again, <span class="ashrei-highlight">more blessed</span> are they who shall believe in your words because that ye shall testify that ye have seen me, and that ye know that I am. Yea, <span class="ashrei-highlight">blessed</span> are they who shall believe in your words, and come down into the depths of humility and be baptized, for they shall be visited with fire and with the Holy Ghost, and shall receive a remission of their sins.</div>
</div>

<!-- SECTION: The Eight Beatitudes -->
<div class="beat-row section-label">
    <div class="beat-cell" style="grid-column: 1 / -1;">The Eight Beatitudes — The Octave of Covenant Blessedness</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">Octave stanza pattern begins</span><span class="ref">8 verses per letter</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the poor in spirit: for theirs is the kingdom of heaven.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/3/" target="_blank" data-ref="Matthew 5:3">Matthew 5:3</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the poor in spirit <span class="beat-diff">who come unto me</span>, for theirs is the kingdom of heaven.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=3" target="_blank" data-ref="3 Nephi 12:3">3 Nephi 12:3</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell">Psalm 119's octave structure — eight verses per stanza — provides the architectural template for the eight Beatitudes. Each stanza is a complete meditation on Torah; each Beatitude is a complete stage of covenant transformation.</div>
    <div class="beat-cell">The first and last Beatitudes both promise "the kingdom of heaven" — forming an <em>inclusio</em> that brackets the entire sequence.</div>
    <div class="beat-cell">3 Nephi adds <span class="beat-diff">"who come unto me"</span> — at Bountiful, poverty of spirit is not enough; it must be directed toward the risen Christ who stands before them.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are they that mourn: for they shall be comforted.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/4/" target="_blank" data-ref="Matthew 5:4">Matthew 5:4</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are all they that mourn, for they shall be comforted.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=4" target="_blank" data-ref="3 Nephi 12:4">3 Nephi 12:4</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"></div>
    <div class="beat-cell">The Bountiful audience has just survived three days of catastrophic destruction and darkness (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/8?lang=eng" target="_blank" data-ref="3 Nephi 8">3 Nephi 8-10</a>). Their mourning is not abstract — it is recent and visceral.</div>
    <div class="beat-cell">For the Nephites at the temple, "they shall be comforted" carries immediate weight: the Comforter Himself is standing before them.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the meek: for they shall inherit the earth.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/5/" target="_blank" data-ref="Matthew 5:5">Matthew 5:5</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the meek, for they shall inherit the earth.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=5" target="_blank" data-ref="3 Nephi 12:5">3 Nephi 12:5</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"><em>Ashrei</em> describes the person who walks in God's way — the meek are those who walk humbly in covenant, not the passive or weak.</div>
    <div class="beat-cell" colspan="2">Identical in both accounts. Echoes <a href="https://www.blueletterbible.org/kjv/psa/37/11/" target="_blank" data-ref="Psalm 37:11">Psalm 37:11</a>: "The meek shall inherit the earth; and shall delight themselves in the abundance of peace."</div>
    <div class="beat-cell"></div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are they which do hunger and thirst after righteousness: for they shall be filled.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/6/" target="_blank" data-ref="Matthew 5:6">Matthew 5:6</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are all they who do hunger and thirst after righteousness, for they shall be filled <span class="beat-diff">with the Holy Ghost</span>.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=6" target="_blank" data-ref="3 Nephi 12:6">3 Nephi 12:6</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"><em>Ashrei</em> nōtzrei edotav — "blessed are those who keep his testimonies" (<a href="https://www.blueletterbible.org/kjv/psa/119/2/" target="_blank" data-ref="Psalm 119:2">Psalm 119:2</a>). Keeping testimony and hungering for righteousness are the same covenant posture: active pursuit.</div>
    <div class="beat-cell">Matthew leaves "filled" open — filled with what?</div>
    <div class="beat-cell">3 Nephi names the gift: <span class="beat-diff">filled with the Holy Ghost</span>. This is the Pentecostal promise made explicit. At Bountiful, the Shavuot pattern is complete — covenant instruction followed by the outpouring of the Spirit.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the merciful: for they shall obtain mercy.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/7/" target="_blank" data-ref="Matthew 5:7">Matthew 5:7</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the merciful, for they shall obtain mercy.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=7" target="_blank" data-ref="3 Nephi 12:7">3 Nephi 12:7</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"></div>
    <div class="beat-cell" colspan="2">Identical in both. The reciprocal structure — mercy given, mercy received — mirrors the covenant relationship itself: "I, the Lord, am bound when ye do what I say" (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/82?lang=eng&id=10" target="_blank" data-ref="D&C 82:10">D&C 82:10</a>).</div>
    <div class="beat-cell"></div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the pure in heart: for they shall see God.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/8/" target="_blank" data-ref="Matthew 5:8">Matthew 5:8</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are all the pure in heart, for they shall see God.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=8" target="_blank" data-ref="3 Nephi 12:8">3 Nephi 12:8</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell">בְּכׇל־לֵב יִדְרְשׁוּהוּ — "with the whole heart they seek him" (<a href="https://www.blueletterbible.org/kjv/psa/119/2/" target="_blank" data-ref="Psalm 119:2">Psalm 119:2</a>). The pure, whole heart that seeks God in the Psalm is the same heart that will see God in the Beatitudes.</div>
    <div class="beat-cell">"They shall see God" — a future promise.</div>
    <div class="beat-cell">At Bountiful, the Nephites have <em>already</em> seen God. This Beatitude, spoken by the resurrected Christ standing before them, transforms from promise to present reality. They are living it.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">·</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are the peacemakers: for they shall be called the children of God.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/9/" target="_blank" data-ref="Matthew 5:9">Matthew 5:9</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are all the peacemakers, for they shall be called the children of God.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=9" target="_blank" data-ref="3 Nephi 12:9">3 Nephi 12:9</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell"></div>
    <div class="beat-cell">Identical in both. "Children of God" — the covenant identity promised to those who make peace.</div>
    <div class="beat-cell">At Bountiful, Christ will soon pray to the Father and call the Nephites His children (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/17?lang=eng&id=21-24" target="_blank" data-ref="3 Nephi 17:21-24">3 Nephi 17:21-24</a>). The promise of divine sonship is being enacted in real time.</div>
</div>

<div class="beat-row" onclick="toggleBeat(this)">
    <div class="beat-cell"><span class="beat-empty">Octave complete</span><span class="ref">cycle restarts at next letter</span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are they which are persecuted for righteousness' sake: for theirs is the kingdom of heaven.<span class="ref"><a href="https://www.blueletterbible.org/kjv/mat/5/10/" target="_blank" data-ref="Matthew 5:10">Matthew 5:10</a></span></div>
    <div class="beat-cell"><span class="ashrei-highlight">Blessed</span> are all they who are persecuted for <span class="beat-diff">my name's</span> sake, for theirs is the kingdom of heaven.<span class="ref"><a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=10" target="_blank" data-ref="3 Nephi 12:10">3 Nephi 12:10</a></span></div>
</div>
<div class="beat-detail">
    <div class="beat-cell">The octave completes and the cycle begins again — just as each Hebrew letter stanza ends and the next begins, an endless meditation on Torah.</div>
    <div class="beat-cell">Matthew: persecuted "for righteousness' sake" — an abstract principle.</div>
    <div class="beat-cell">3 Nephi: persecuted "for <span class="beat-diff">my name's</span> sake" — Christ personalizes it. At Bountiful, covenant fidelity is not to an idea but to a Person they have seen and touched. The kingdom of heaven brackets the sequence: first Beatitude and last both point to the same destination.</div>
</div>

</div><!-- end beat-compare-wrapper -->
</div><!-- end beat-compare -->

<script>
function toggleBeat(row) {
    const detail = row.nextElementSibling;
    if (detail && detail.classList.contains('beat-detail')) {
        detail.classList.toggle('open');
    }
}
</script>

<div class="info-box insight">
<strong>The Pattern:</strong> Psalm 119 gives the architecture — doubled <em>ashrei</em> opening, octave structure, Torah meditation. Matthew delivers the content on a mountain in Galilee. 3 Nephi fulfills both form and content at the temple in Bountiful: the doubled opening reappears, the eight Beatitudes are delivered by the Lawgiver Himself, and the promises shift from future to present tense. The Psalm is the blueprint. The Sermon on the Mount is the teaching. The Sermon at the Temple is the arrival.
</div>


</div>
</details>

<details class="section-dropdown" id="bountiful-section">
<summary>The Bountiful Visit as Shavuot</summary>
<div class="section-body">

## The Bountiful Visit as Shavuot

### The Nephites and the Law of Moses

The Book of Mormon is explicit: the Nephites observed the Law of Moses throughout their history:

> "And we did observe to keep the judgments, and the statutes, and the commandments of the Lord in all things, **according to the law of Moses**." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/5?lang=eng&id=10" target="_blank" data-ref="2 Nephi 5:10">2 Nephi 5:10</a>)

> "They observed to keep the law of Moses and the **sabbath day** holy unto the Lord." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/jarom/1?lang=eng&id=5" target="_blank" data-ref="Jarom 1:5">Jarom 1:5</a>)

> "They did keep the law of Moses; for it was expedient that they should keep the law of Moses as yet, for it was not all fulfilled. But notwithstanding the law of Moses, they did look forward to the coming of Christ, considering that **the law of Moses was a type of his coming**." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/25?lang=eng&id=15" target="_blank" data-ref="Alma 25:15">Alma 25:15</a>)

Even shortly before Christ's coming, the text confirms ongoing observance: some preached "that it was no more expedient to observe the law of Moses. Now in this thing they did err, having not understood the scriptures" (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/1?lang=eng&id=24" target="_blank" data-ref="3 Nephi 1:24">3 Nephi 1:24</a>).

### The Typological Pattern

If the Nephites kept the Law of Moses — including the three pilgrimage festivals — then the faithful among them would have been gathered at the temple for Shavuot in the weeks following Passover season. The destruction in 3 Nephi 8 occurred "in the thirty and fourth year, in the first month, on the fourth day of the month" (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/8?lang=eng&id=5" target="_blank" data-ref="3 Nephi 8:5">3 Nephi 8:5</a>) — Passover season. Fifty days later would place Shavuot squarely in the window when the multitude was gathered "round about the temple" at Bountiful (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/11?lang=eng&id=1" target="_blank" data-ref="3 Nephi 11:1">3 Nephi 11:1</a>).

On the other side of the world, the apostles were gathered at the temple in Jerusalem for the same feast — Pentecost — when the Spirit descended in Acts 2.

<table class="proximity-table">
<thead>
<tr><th>Pattern</th><th>Old Testament</th><th>New Testament</th><th>Book of Mormon</th></tr>
</thead>
<tbody>
<tr><td><strong>Deliverance</strong></td><td>Passover / Red Sea</td><td>Christ's death and resurrection</td><td>Three days of darkness; destruction of the wicked</td></tr>
<tr><td><strong>Waiting period</strong></td><td>50 days (Omer count)</td><td>50 days (Acts 1:3)</td><td>Darkness lifts; the faithful gather at the temple — likely for Shavuot</td></tr>
<tr><td><strong>Covenant event</strong></td><td>Torah given at Sinai</td><td>Holy Spirit at Pentecost</td><td>Christ appears at Bountiful; teaches; baptizes</td></tr>
<tr><td><strong>Fire</strong></td><td>Fire on the mountain</td><td>Tongues of fire on each person</td><td>3 Nephi 19:14 — "encircled about as if it were by fire"</td></tr>
<tr><td><strong>Result</strong></td><td>Israel formed as covenant nation</td><td>Church formed as covenant community</td><td>Nephite covenant community renewed</td></tr>
</tbody>
</table>

### What the Resurrected Christ Changed

<div class="comparison-grid">
    <div class="compare-card">
        <h4>Fulfillment Tense</h4>
        <p><strong>Matthew 5:18:</strong> "...till all <strong>be fulfilled</strong>" — future</p>
        <p><strong>3 Nephi 12:18:</strong> "...in me it hath all <strong>been fulfilled</strong>" — past</p>
    </div>
    <div class="compare-card">
        <h4>Perfection Standard</h4>
        <p><strong>Matthew 5:48:</strong> "...even as <strong>your Father</strong>"</p>
        <p><strong>3 Nephi 12:48:</strong> "...even as <strong>I, or your Father</strong>" — Christ adds Himself</p>
    </div>
    <div class="compare-card">
        <h4>The Lord's Prayer</h4>
        <p><strong>Matthew 6:10:</strong> "<strong>Thy kingdom come.</strong>"</p>
        <p><strong>3 Nephi 13:10:</strong> "Thy kingdom come" is <strong>absent</strong> — the kingdom is already present</p>
    </div>
    <div class="compare-card">
        <h4>Antithesis Formula</h4>
        <p><strong>Matthew 5:21:</strong> "Ye have <strong>heard</strong>..."</p>
        <p><strong>3 Nephi 12:21:</strong> "...and it is also <strong>written before you</strong>" — adapted for a written-law people</p>
    </div>
    <div class="compare-card">
        <h4>Filled with the Spirit</h4>
        <p><strong>Matthew 5:6:</strong> "...they shall be <strong>filled</strong>"</p>
        <p><strong>3 Nephi 12:6:</strong> "...filled <strong>with the Holy Ghost</strong>" — the Pentecostal gift named</p>
    </div>
</div>


</div>
</details>

<details class="section-dropdown" id="wheat-section">
<summary>The Wheat Harvest in Restoration Scripture</summary>
<div class="section-body">

## The Wheat Harvest in Restoration Scripture

<img src="/images/culture/jewish-festivals/seven-species/wheat.png" alt="Wheat" style="float: right; width: 80px; margin: 0 0 1rem 1.5rem; opacity: 0.8;">

Shavuot is the wheat harvest. And the imagery of wheat, sheaves, sickles, and garners saturates Restoration scripture.

### "The Field Is White Already to Harvest"

> "Behold, the field is white already to harvest; therefore, whoso desireth to reap, let him thrust in his sickle with his might, and reap while the day lasts, that he may treasure up for his soul everlasting salvation in the kingdom of God." (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/4?lang=eng&id=4" target="_blank" data-ref="D&C 4:4">D&C 4:4</a>; repeated in D&C 6:3, 11:3, 12:3, 14:3, 33:3, 7)

This language comes from Christ Himself at Jacob's well (<a href="https://www.blueletterbible.org/kjv/jhn/4/35/" target="_blank" data-ref="John 4:35">John 4:35</a>). At Shavuot, the wheat fields were indeed white and ripe. When the Lord uses this language in the Doctrine and Covenants, He is invoking the Shavuot harvest as the image for missionary gathering.

### Ammon and the Sheaves

> "Behold, the field was ripe, and blessed are ye, for ye did thrust in the sickle, and did reap with your might, yea, all the day long did ye labor; and behold the number of your **sheaves**! And they shall be gathered into the **garners**, that they are not wasted." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/26?lang=eng&id=5" target="_blank" data-ref="Alma 26:5">Alma 26:5</a>)

> "But behold, they are in the hands of the **Lord of the harvest**, and they are his; and he will raise them up at the last day." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/26?lang=eng&id=7" target="_blank" data-ref="Alma 26:7">Alma 26:7</a>)

### Laden with Sheaves

> "Thrust in your sickle with all your soul, and your sins are forgiven you, and you shall be **laden with sheaves upon your back**, for the laborer is worthy of his hire." (<a href="https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/31?lang=eng&id=5" target="_blank" data-ref="D&C 31:5">D&C 31:5</a>)

At Shavuot, Israelite farmers literally carried sheaves of wheat to the Temple as offerings. The image of a missionary laden with sheaves — souls gathered to Christ — mirrors the Shavuot pilgrim arriving at the House of the Lord.

### The Pattern

<div class="comparison-grid">
    <div class="compare-card"><h4>White Fields</h4><p>"The field is white already to harvest" (D&C 4:4) — echoing Shavuot's ripe wheat fields</p></div>
    <div class="compare-card"><h4>Thrust in Sickles</h4><p>Missionaries called to "thrust in your sickle" (D&C 31:5) — the harvest laborers</p></div>
    <div class="compare-card"><h4>Sheaves to Garners</h4><p>Converts gathered to Zion and temples — the Shavuot ingathering</p></div>
    <div class="compare-card"><h4>Two Leavened Loaves</h4><p>A people not yet perfected, offered to God — covenant is for the willing</p></div>
    <div class="compare-card"><h4>Wheat from Tares</h4><p>"Gather out the wheat" (D&C 86:7) — the final separation at harvest</p></div>
    <div class="compare-card"><h4>Covenant Renewal</h4><p>The gathering culminates in temple covenants — Shavuot's covenant pattern</p></div>
</div>


</div>
</details>

<details class="section-dropdown" id="ruth-section">
<summary>The Book of Ruth: A Shavuot Story</summary>
<div class="section-body">

## The Book of Ruth: A Shavuot Story

<div style="border-radius: 12px; overflow: hidden; margin-bottom: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <img src="/images/culture/jewish-festivals/ruth-gleaning.jpg" alt="Ruth gleaning in the fields during the barley harvest" style="width: 100%; display: block;">
    <p style="text-align: center; color: #666; font-size: 0.85rem; padding: 0.5rem; margin: 0;"><em>Ruth gleaning in the fields of Boaz</em></p>
</div>

The Book of Ruth is read aloud in synagogues on Shavuot. Of all the books that could accompany the giving of the Torah, the rabbis chose this short story of a Moabite widow gleaning in a barley field. The reasons run deeper than tradition.

### Why Ruth on Shavuot?

<div class="comparison-grid">
    <div class="compare-card">
        <h4>The Harvest Setting</h4>
        <p>Ruth arrives in Bethlehem "at the beginning of the barley harvest" (<a href="https://www.blueletterbible.org/kjv/rut/1/22/" target="_blank" data-ref="Ruth 1:22">Ruth 1:22</a>) and gleans "until the barley harvest and the wheat harvest were finished" (<a href="https://www.blueletterbible.org/kjv/rut/2/23/" target="_blank" data-ref="Ruth 2:23">Ruth 2:23</a>). Her story spans exactly the Omer count — from Bikkurim (barley firstfruits) to Shavuot (wheat harvest). The agricultural calendar of the feasts is the calendar of Ruth's redemption.</p>
    </div>
    <div class="compare-card">
        <h4>Voluntary Covenant</h4>
        <p>At Sinai, all Israel declared: "All that the LORD hath spoken we will do" (<a href="https://www.blueletterbible.org/kjv/exo/19/8/" target="_blank" data-ref="Exodus 19:8">Exodus 19:8</a>). Ruth — a Moabite with no obligation to Israel's God — made her own Sinai declaration: "Thy people shall be my people, and thy God my God" (<a href="https://www.blueletterbible.org/kjv/rut/1/16/" target="_blank" data-ref="Ruth 1:16">Ruth 1:16</a>). Reading Ruth on Shavuot reminds Israel that covenant is not inherited by blood alone — it is chosen.</p>
    </div>
    <div class="compare-card">
        <h4>The Convert's Pattern</h4>
        <p>Jewish tradition considers Ruth the model convert. The rabbis see in her words to Naomi a systematic acceptance of every dimension of covenant life — people, God, land, law, and even burial among God's people (<a href="https://www.blueletterbible.org/kjv/rut/1/16/" target="_blank" data-ref="Ruth 1:16-17">Ruth 1:16-17</a>). Shavuot is the feast of receiving Torah; Ruth is the story of choosing Torah.</p>
    </div>
    <div class="compare-card">
        <h4>The Davidic Line</h4>
        <p>Ruth's son Obed was "the father of Jesse, father of David" (<a href="https://www.blueletterbible.org/kjv/rut/4/17/" target="_blank" data-ref="Ruth 4:17">Ruth 4:17</a>). A Moabite widow who chose covenant became the great-grandmother of Israel's greatest king — and an ancestress of Christ (<a href="https://www.blueletterbible.org/kjv/mat/1/5/" target="_blank" data-ref="Matthew 1:5">Matthew 1:5</a>). Reading Ruth on Shavuot proclaims that the harvest of Torah includes the nations.</p>
    </div>
</div>

### Ruth's Declaration and Israel's at Sinai

Ruth's words to Naomi follow a structure that echoes the covenant pattern at Sinai:

<table class="proximity-table">
<thead>
<tr><th>Ruth's Declaration (<a href="https://www.blueletterbible.org/kjv/rut/1/16/" target="_blank" data-ref="Ruth 1:16-17">Ruth 1:16-17</a>)</th><th>Covenant Element</th><th>Israel at Sinai</th></tr>
</thead>
<tbody>
<tr><td>"Whither thou goest, I will go"</td><td><strong>Journey</strong> — following God's direction</td><td>Israel followed the pillar of cloud and fire</td></tr>
<tr><td>"Where thou lodgest, I will lodge"</td><td><strong>Dwelling</strong> — sharing the covenant community</td><td>Israel camped together at Sinai's base</td></tr>
<tr><td>"Thy people shall be my people"</td><td><strong>Identity</strong> — joining the covenant nation</td><td>"Ye shall be unto me a kingdom of priests" (<a href="https://www.blueletterbible.org/kjv/exo/19/6/" target="_blank" data-ref="Exodus 19:6">Exodus 19:6</a>)</td></tr>
<tr><td>"Thy God my God"</td><td><strong>Worship</strong> — accepting the God of Israel</td><td>"I am the LORD thy God" (<a href="https://www.blueletterbible.org/kjv/exo/20/2/" target="_blank" data-ref="Exodus 20:2">Exodus 20:2</a>)</td></tr>
<tr><td>"Where thou diest, will I die, and there will I be buried"</td><td><strong>Permanence</strong> — covenant unto death</td><td>"All that the LORD hath spoken we will do" (<a href="https://www.blueletterbible.org/kjv/exo/19/8/" target="_blank" data-ref="Exodus 19:8">Exodus 19:8</a>)</td></tr>
</tbody>
</table>

### Gleaning, Gathering, and *Hesed*

Ruth's story is built on the Torah's gleaning laws. Leviticus commands: "When ye reap the harvest of your land, thou shalt not wholly reap the corners of thy field, neither shalt thou gather the gleanings of thy harvest... thou shalt leave them for the poor and stranger" (<a href="https://www.blueletterbible.org/kjv/lev/19/9/" target="_blank" data-ref="Leviticus 19:9-10">Leviticus 19:9-10</a>). Ruth — both poor and stranger — becomes the living embodiment of the Torah's provision. When Boaz tells his reapers to leave extra grain for her (<a href="https://www.blueletterbible.org/kjv/rut/2/15/" target="_blank" data-ref="Ruth 2:15-16">Ruth 2:15-16</a>), the law moves from text to act.

The word that threads through Ruth is <a href="https://www.blueletterbible.org/lexicon/h2617/kjv/wlc/0-1/" target="_blank">חֶסֶד</a> (*hesed*) — covenant faithfulness, loyal love, lovingkindness. Naomi speaks it over Ruth and Orpah: "The LORD deal kindly [*hesed*] with you, as ye have dealt with the dead, and with me" (<a href="https://www.blueletterbible.org/kjv/rut/1/8/" target="_blank" data-ref="Ruth 1:8">Ruth 1:8</a>). Boaz recognizes it in Ruth: "Blessed be thou of the LORD, my daughter: for thou hast shewed more kindness [*hesed*] in the latter end than at the beginning" (<a href="https://www.blueletterbible.org/kjv/rut/3/10/" target="_blank" data-ref="Ruth 3:10">Ruth 3:10</a>). *Hesed* is the covenant virtue — the quality that makes Torah livable. Ruth doesn't just accept Torah; she embodies its deepest principle.

### Under His Wings

When Boaz first blesses Ruth, he uses a striking image:

> "The LORD recompense thy work, and a full reward be given thee of the LORD God of Israel, **under whose wings thou art come to trust**." (<a href="https://www.blueletterbible.org/kjv/rut/2/12/" target="_blank" data-ref="Ruth 2:12">Ruth 2:12</a>)

The Hebrew word for "wings" here is <a href="https://www.blueletterbible.org/lexicon/h3671/kjv/wlc/0-1/" target="_blank">כָּנָף</a> (*kanaph*). When Ruth later goes to the threshing floor and asks Boaz to redeem her, she uses the same word: "Spread therefore thy skirt [*kanaph*] over thine handmaid; for thou art a near kinsman" (<a href="https://www.blueletterbible.org/kjv/rut/3/9/" target="_blank" data-ref="Ruth 3:9">Ruth 3:9</a>). The wing of divine protection and the garment of the redeemer are the same word. Boaz's act of redemption becomes an enactment of God's covenant shelter. The imagery carries into the Psalms — "How excellent is thy lovingkindness, O God! therefore the children of men put their trust under the shadow of thy wings [*kanaph*]" (<a href="https://www.blueletterbible.org/kjv/psa/36/7/" target="_blank" data-ref="Psalm 36:7">Psalm 36:7</a>) — and into Christ's own lament over Jerusalem: "How often would I have gathered thy children together, even as a hen gathereth her chickens under her wings" (<a href="https://www.blueletterbible.org/kjv/mat/23/37/" target="_blank" data-ref="Matthew 23:37">Matthew 23:37</a>).

<div class="info-box insight">
<strong>The Shavuot arc of Ruth:</strong> A foreign woman arrives at the barley harvest (Bikkurim), chooses covenant, gleans through the wheat harvest (Shavuot), receives redemption under the <em>kanaph</em> of her kinsman-redeemer, and becomes the ancestress of David and Christ. Her story is the Shavuot pattern in miniature: harvest, covenant, gathering, redemption. The Torah is not only given — it is lived. And the one who lives it most fully in this story is not a priest or a prophet but a Moabite widow gleaning at the edges of a field.
</div>


</div>
</details>

<details class="section-dropdown" id="recipes-section">
<summary>Traditional Shavuot Foods</summary>
<div class="section-body">

## Traditional Shavuot Foods

Dairy dishes are the hallmark of the Shavuot table. Multiple traditions explain why: before receiving the Torah at Sinai, Israel was not yet bound by the laws of *kashrut*, including ritual slaughter, so they could not prepare meat; Solomon compared the Torah to milk — "Honey and milk are under thy tongue" (<a href="https://www.blueletterbible.org/kjv/sgs/4/11/" target="_blank" data-ref="Song of Solomon 4:11">Song of Solomon 4:11</a>); and the Hebrew word for milk (<a href="https://www.blueletterbible.org/lexicon/h2461/kjv/wlc/0-1/" target="_blank">חָלָב</a>, *chalav*) has the numerical value of 40, representing Moses' 40 days on Sinai.

Traditionally, meat is served at the evening meal and dairy is served for the daytime meal or a morning *kiddush*. The recipes below represent traditions from Jewish communities around the world.

### Ashkenazi Traditions

<div class="recipe-grid">
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/cheesecake.jpg" alt="Classic New York Cheesecake" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Classic Cheesecake</h4>
        <p class="recipe-desc">The quintessential Shavuot dessert. Rich and creamy, made with farmer's cheese or cream cheese on a graham cracker crust. Some families top with fresh strawberries or blueberries; others serve it plain. A symbol of the "land flowing with milk and honey." Every Jewish family has their grandmother's recipe — and insists it is the only correct one.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://toriavey.com/new-york-cheesecake/" target="_blank" style="color: #8b6914;">Recipe: Tori Avey's New York Cheesecake</a> · <span style="color: #999;">Photo: Tori Avey</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/cheese-blintzes.jpg" alt="Cheese Blintzes with Strawberry Topping" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Cheese Blintzes</h4>
        <p class="recipe-desc">Thin crepes filled with sweetened ricotta or farmer's cheese, folded envelope-style and pan-fried until golden. Often served with sour cream, fresh berries, or a dusting of powdered sugar. A Shavuot morning tradition. The crepe batter is simple — the art is in the folding and the frying.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://toriavey.com/shiksa-blintzes/" target="_blank" style="color: #8b6914;">Recipe: Tori Avey's Cheese Blintzes</a> · <span style="color: #999;">Photo: Tori Avey</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/noodle-kugel.jpg" alt="Sweet Lokshen Kugel" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Noodle Kugel</h4>
        <p class="recipe-desc">A sweet baked noodle pudding with cottage cheese or cream cheese, eggs, cinnamon, and raisins. Golden and custardy, served warm or at room temperature. Some add a cornflake topping for crunch. The ultimate Shavuot comfort food — and equally at home on a Sabbath table.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://toriavey.com/sweet-lokshen-kugel/" target="_blank" style="color: #8b6914;">Recipe: Tori Avey's Sweet Noodle Kugel</a> · <span style="color: #999;">Photo: Tori Avey</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/cheese-kreplach.jpg" alt="Cheese Kreplach" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Cheese Kreplach</h4>
        <p class="recipe-desc">Small dumplings (similar to ravioli) filled with sweetened cheese, boiled and then sometimes fried. The Ashkenazi answer to filled pasta — typically served in butter or with sour cream. A labor of love that brings multiple generations into the kitchen together.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://www.kosher.com/recipe/cheese-kreplach-7088/" target="_blank" style="color: #8b6914;">Recipe: Kosher.com's Cheese Kreplach</a> · <span style="color: #999;">Photo: Kosher.com</span></p>
    </div>
</div>

### Sephardic and Middle Eastern Traditions

<div class="recipe-grid">
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/cheese-bourekas.jpg" alt="Cheese Bourekas" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Cheese Bourekas</h4>
        <p class="recipe-desc">Flaky pastry pockets filled with feta, kashkaval, or a blend of cheeses. A Sephardic tradition from Turkey, Greece, and the Balkans. Shaped as triangles to represent the three patriarchs — or, some say, the three-peaked Mount Sinai. Serve warm with hard-boiled eggs and fresh tomatoes.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://toriavey.com/cheese-bourekas/" target="_blank" style="color: #8b6914;">Recipe: Tori Avey's Cheese Bourekas</a> · <span style="color: #999;">Photo: Tori Avey</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/atayef.jpg" alt="Atayef — stuffed Middle Eastern pancakes" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Atayef (Cheese Pancakes)</h4>
        <p class="recipe-desc">Small, spongy pancakes folded around a sweet cheese filling, then deep-fried and soaked in rosewater or orange blossom syrup. Popular among Syrian and Lebanese Jewish communities. The contrast between the crispy shell and warm cheese interior is extraordinary.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://www.myjewishlearning.com/article/atayef-stuffed-syrian-pancakes/" target="_blank" style="color: #8b6914;">Recipe: My Jewish Learning's Atayef</a> · <span style="color: #999;">Photo: Feel Good Foodie</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/cheese-sambusak.jpg" alt="Cheese Sambusak" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Cheese Sambusak</h4>
        <p class="recipe-desc">Half-moon pastries filled with cheese (often *jibneh* or feta), pinched closed with a decorative rope edge. An Iraqi and Syrian Jewish specialty. The dough is tender and slightly flaky, the filling tangy and warm. Often served as a Shavuot appetizer.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://toriavey.com/cheese-sambusak/" target="_blank" style="color: #8b6914;">Recipe: Tori Avey's Cheese Sambusak</a> · <span style="color: #999;">Photo: Tori Avey</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/siete-cielos.jpg" alt="Siete Cielos — Seven Heavens Challah" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Siete Cielos (Seven Heavens Bread)</h4>
        <p class="recipe-desc">A stunning bread from the Tunisian and Moroccan Jewish tradition. The seven layers of dough represent the seven heavens God traversed to deliver the Torah to Moses. A central ball of dough depicts Mount Sinai, with seven ascending ropes around it. A labor-intensive showpiece that embodies the joy of receiving Torah.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://onthechocolatetrail.org/2019/05/los-siete-cielos-or-seven-heaven-challah/" target="_blank" style="color: #8b6914;">Recipe: On the Chocolate Trail's Seven Heavens Challah</a></p>
    </div>
</div>

### Other Shavuot Traditions

<div class="recipe-grid">
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/kadeh.jpg" alt="Kadeh — Kurdish cheese bread with zizik" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Kadeh (Kurdish Cheese Bread)</h4>
        <p class="recipe-desc">A flatbread stuffed with soft cheese, baked until golden and slightly crispy. Kurdish Jewish families serve this as a centerpiece of the Shavuot dairy meal, often alongside a tangy yogurt sauce called *zizik*. Simple ingredients, deeply satisfying.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://www.jewishfoodsociety.org/recipes/kadeh-cheese-and-spinach-stuffed-bread" target="_blank" style="color: #8b6914;">Recipe: Jewish Food Society's Kadeh</a> · <span style="color: #999;">Photo: Jewish Food Society</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/sutlac.jpg" alt="Sütlaç — Turkish rice pudding" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Sütlaç (Rice Pudding)</h4>
        <p class="recipe-desc">Creamy rice pudding baked until the top forms a golden skin, then decorated with cinnamon in intricate patterns. A Turkish and Sephardic tradition. Some families draw the Ten Commandments tablets or Mount Sinai in the cinnamon — edible art that teaches Torah.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://www.jewishfoodsociety.org/recipes/sutlac-turkish-rice-pudding" target="_blank" style="color: #8b6914;">Recipe: Jewish Food Society's Sütlaç</a> · <span style="color: #999;">Photo: Jake Cohen / Jewish Food Society</span></p>
    </div>
    <div class="recipe-card">
        <img src="/images/culture/jewish-festivals/shavuot/recipes/kahee.jpg" alt="Kahi — Iraqi flaky pastry" style="width: 100%; border-radius: 8px 8px 0 0; margin: -1.5rem -1.5rem 1rem; width: calc(100% + 3rem); object-fit: cover; max-height: 200px;">
        <h4>Kahi (Buttered Pastry)</h4>
        <p class="recipe-desc">An Iraqi Jewish specialty: thin sheets of dough layered with generous amounts of butter, fried until golden, then drenched in sugar syrup. Traditionally served for breakfast on Shavuot morning with *qei'mar* (clotted cream). Rich, flaky, and unapologetically indulgent.</p>
        <p style="font-size: 0.8rem; margin-top: 0.75rem;"><a href="https://www.jewishfoodsociety.org/recipes/kahi-sweet-and-flaky-flatbread" target="_blank" style="color: #8b6914;">Recipe: Jewish Food Society's Kahi</a> · <span style="color: #999;">Photo: Jewish Food Society</span></p>
    </div>
    <div class="recipe-card" style="border-top-color: #1a6b74;">
        <h4 style="color: #1a6b74;">A Note on Dairy</h4>
        <p class="recipe-desc">Not all communities observe the dairy custom. Yemenite Jews, for example, do not eat dairy on Shavuot. The tradition, while widespread, is a custom (*minhag*) rather than a commandment — a beautiful example of how communities develop unique expressions of the same celebration. What unites every Shavuot table is not the menu but the joy of receiving Torah.</p>
    </div>
</div>


</div>
</details>

<details class="section-dropdown" id="family-section">
<summary>Family Shavuot: Bringing the Feast Home</summary>
<div class="section-body">

## Family Shavuot: Bringing the Feast Home

You don't have to be Jewish to let Shavuot shape your family's worship. The themes of this feast — covenant, Torah, harvest, and the movement from distance to presence — are already woven through Latter-day Saint life. Here are ways to bring them to the surface.

### 1. A Family Tikkun: All-Night (or Late-Night) Scripture Study

The Jewish practice of *Tikkun Leil Shavuot* — staying awake all night to study Torah — grew from a midrash that Israel overslept the morning God came to give the law, and Moses had to wake them (<a href="https://www.sefaria.org/Shabbat.86b" target="_blank">Talmud, Shabbat 86b</a>). To show they would not oversleep again, Jews stay up studying.

<div class="info-box">
<strong>For families:</strong> Choose a night near Shavuot (late May or early June) and set up a family study marathon. It doesn't have to be all night — even staying up an hour or two past bedtime feels special to children. Read through the Ten Commandments together (<a href="https://www.blueletterbible.org/kjv/exo/20/1/" target="_blank" data-ref="Exodus 20:1-17">Exodus 20:1-17</a>), then discuss the three layers for one or two commandments: What does the <strong>prohibition</strong> say? What does the <strong>heart</strong> behind it look like? What is the <strong>covenant action</strong> — the opposite virtue? (See the <a href="#higher-law-section">interactive commandment cards</a> above for all ten.) Close by reading Christ's Beatitudes at Bountiful (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12?lang=eng&id=1-12" target="_blank" data-ref="3 Nephi 12:1-12">3 Nephi 12:1-12</a>) and talking about how the law was fulfilled — not replaced — in Him.
</div>

### 2. Read the Book of Ruth Together

Ruth is the Shavuot book — read aloud in synagogues every year on this feast. It is short enough (four chapters) to read in a single sitting, and the story is vivid enough for all ages.

<div class="info-box">
<strong>For families:</strong> Read <a href="https://www.blueletterbible.org/kjv/rut/1/1/" target="_blank" data-ref="Ruth 1">Ruth 1-4</a> aloud together, assigning roles (Naomi, Ruth, Boaz, the narrator). Pause at Ruth's declaration in <a href="https://www.blueletterbible.org/kjv/rut/1/16/" target="_blank" data-ref="Ruth 1:16-17">Ruth 1:16-17</a> and ask: <em>What does it mean to choose covenant the way Ruth did? What did she give up? What did she gain?</em> Then connect it to Sinai: Israel also chose — "All that the LORD hath spoken we will do" (<a href="https://www.blueletterbible.org/kjv/exo/19/8/" target="_blank" data-ref="Exodus 19:8">Exodus 19:8</a>). Ask your family: <em>When have you chosen to stay, even when it would have been easier to go back?</em> (See the <a href="#ruth-section">expanded Ruth section</a> for the full Shavuot connections.)
</div>

### 3. Cook a Shavuot Dairy Meal

Dairy dishes are the tradition of the Shavuot table — and making them together is the tradition within the tradition. Kurdish women gathered around a fire to cook *kadeh*; Ashkenazi grandmothers passed down cheesecake recipes; Moroccan families built seven-layer *siete cielos* bread together.

<div class="info-box">
<strong>For families:</strong> Pick one recipe from the <a href="#recipes-section">Traditional Shavuot Foods</a> section and make it together. Cheesecake is the crowd favorite, but cheese blintzes are more hands-on for kids (everyone gets to fold). While you cook, talk about <em>why</em> dairy: Israel received the Torah at Sinai but didn't yet know the kosher laws, so they couldn't prepare meat — all they could eat was dairy. The simplest food became the feast. Ask: <em>What simple things in our life carry the deepest meaning?</em>
</div>

### 4. The Four Mountains — A Family Home Evening Lesson

The <a href="#mountains-section">Four Mountains progression</a> (Sinai → Galilee → Jerusalem → Bountiful) tells the story of how God draws closer to His people across scripture. This makes a natural family lesson.

<div class="info-box">
<strong>For families:</strong> Draw or print four simple mountains. Label them Sinai, Galilee, Temple Mount, and Bountiful. For each mountain, ask three questions: <em>How close did the people get to God? How did they feel? What did God give them?</em>
<ul style="margin-top: 0.75rem; line-height: 1.8;">
<li><strong>Sinai:</strong> "Touch the mountain and die" — God is near but terrifying (<a href="https://www.blueletterbible.org/kjv/exo/19/12/" target="_blank" data-ref="Exodus 19:12">Exodus 19:12</a>)</li>
<li><strong>Galilee:</strong> Jesus sits and teaches — the crowd is astonished, not afraid (<a href="https://www.blueletterbible.org/kjv/mat/5/1/" target="_blank" data-ref="Matthew 5:1-2">Matthew 5:1-2</a>)</li>
<li><strong>Jerusalem (Pentecost):</strong> The Spirit comes <em>inside</em> each person — no mountain needed (<a href="https://www.blueletterbible.org/kjv/act/2/1/" target="_blank" data-ref="Acts 2:1-4">Acts 2:1-4</a>)</li>
<li><strong>Bountiful:</strong> "Come forth unto me, that ye may <em>feel</em>" — every person touches the risen Christ (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/11?lang=eng&id=14-15" target="_blank" data-ref="3 Nephi 11:14-15">3 Nephi 11:14-15</a>)</li>
</ul>
End by asking: <em>Where are we on that journey? How is God drawing us closer?</em>
</div>

### 5. Decorate with Greenery and Wheat

Jewish families adorn their homes and synagogues with flowers and plants on Shavuot, representing Mount Sinai blooming when God descended. Wheat and barley sheaves recall the harvest.

<div class="info-box">
<strong>For families:</strong> Gather wildflowers, branches, or potted plants and arrange them around your dinner table or scripture study area. If you can find dried wheat stalks (craft stores often carry them), place them in a vase as a centerpiece. Let the greenery and grain be a visual reminder: God descended on a mountain and it <em>bloomed</em>. His covenant brings life to barren places. This is a simple act — five minutes of preparation — but it transforms the space and signals to the family that tonight is set apart.
</div>

### Putting It All Together

These activities work individually, but they also build into a full Shavuot evening:

1. **Decorate** the table with greenery and wheat
2. **Cook** a dairy dish together
3. **Read Ruth** aloud during or after dinner
4. **Discuss** the Four Mountains or the three layers of a commandment
5. **Stay up late** studying scripture together — showing God you won't oversleep when He comes to speak

<div class="info-box insight">
<strong>The point is not to "become Jewish."</strong> It is to let the biblical feasts do what they were designed to do — teach the Plan of Salvation through lived experience. When your family cooks dairy because Israel couldn't prepare meat at Sinai, you are <em>inside</em> the story. When you read Ruth aloud, you hear a woman choosing covenant in real time. When you stay up late studying Torah, you are answering the same question Israel faced at the mountain: <em>Will you be awake when God speaks?</em>
</div>


</div>
</details>

---

## From Stone to Flesh: The Arc of Shavuot

<div style="background: linear-gradient(135deg, #f8f5f0, #fdf9f2); border-radius: 16px; padding: 2rem; margin: 2rem 0;">

**Sinai:** God writes His law on stone and delivers it through a mediator. The people cannot bear His presence. They stand afar off.

**The Sermon on the Mount:** The Lawgiver Himself sits among the people and interprets His own law. Distance is reduced. Fear becomes astonishment. But fulfillment remains future — the law is still operative, the kingdom still anticipated.

**Pentecost (Acts 2):** The Spirit descends and writes the law on hearts. No mediator, no tablets, no mountain. God dwells within each person. The promise of Jeremiah 31:33 is realized.

**Bountiful:** The resurrected Christ descends, stands among His people, and invites every single one to touch Him. The law is fulfilled. The kingdom is present. The veil is gone. Where Sinai said "touch the mountain and die," the risen Lord says "come forth unto me, that ye may feel."

**This is the arc of Shavuot: from stone to flesh, from distance to embrace, from "let not God speak with us, lest we die" to "Hosanna! Blessed be the name of the Most High God."**

</div>

<details class="section-dropdown" id="observance-section">
<summary>Modern Observance & Latter-day Saint Resonance</summary>
<div class="section-body">

## Modern Observance

### Jewish Practice Today

- **Tikkun Leil Shavuot** — All-night Torah study sessions
- **Reading the Ten Commandments** — Congregations stand during the chanting of the Decalogue
- **Reading the Book of Ruth** — A story of voluntary covenant acceptance
- **Decorating with flowers and greenery** — Representing Sinai blooming
- **Dairy meals** — Cheesecake, blintzes, and other dairy dishes
- **Confirmation ceremonies** — In Reform Judaism, Shavuot is the day for confirming young people

### Latter-day Saint Resonance

#### Abinadi's Shavuot Discourse

One of the most striking Shavuot echoes in the Book of Mormon may be hiding in plain sight. When Abinadi appeared before King Noah and his priests, he challenged them: "Ye have said that ye teach the law of Moses. And what know ye concerning the law of Moses?" (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/12?lang=eng&id=31" target="_blank" data-ref="Mosiah 12:31">Mosiah 12:31</a>). Then he did something remarkable — he recited the **entire Ten Commandments** from Exodus 20, beginning with the preamble:

> "I am the Lord thy God, who hath brought thee out of the land of Egypt, out of the house of bondage. Thou shalt have no other God before me." (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/12?lang=eng&id=34-35" target="_blank" data-ref="Mosiah 12:34-35">Mosiah 12:34-35</a>; see full Decalogue in <a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/13?lang=eng&id=12-24" target="_blank" data-ref="Mosiah 13:12-24">Mosiah 13:12-24</a>)

The public reading of the Ten Commandments is the **central liturgical act of Shavuot**. Synagogues read the Decalogue during Shavuot morning services, with the congregation standing. If Noah's people claimed to observe the Law of Moses — which they did (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/12?lang=eng&id=28" target="_blank" data-ref="Mosiah 12:28">Mosiah 12:28</a>) — and if Abinadi's appearance coincided with a festival season when the Decalogue was being publicly read or taught, his discourse would fit the pattern of a **Shavuot confrontation**: a prophet standing before corrupt priests who claim to teach Torah, reciting the very commandments they have broken, and calling them to account for the covenant they have violated.

Abinadi then moved beyond the letter of the law to its deeper meaning — teaching that the commandments point to Christ, that "God himself should come down among the children of men, and take upon him the form of man" (<a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/13?lang=eng&id=34" target="_blank" data-ref="Mosiah 13:34">Mosiah 13:34</a>). Like Christ in the Sermon on the Mount, Abinadi read the same tablets but revealed the deeper covenant layer — the layer the priests of Noah could not see.

<div class="info-box insight">
<strong>The pattern repeats:</strong> At Sinai, the people received the commandments but could not bear God's presence. Before Abinadi, the priests claimed to teach the law but could not see past its surface. At the Sermon on the Mount, Christ reopened the deeper reading. At Bountiful, He declared it fulfilled. The Shavuot pattern — receiving Torah and being tested by it — runs through every dispensation.
</div>

#### Temple, Sacrament, and Restoration

**Temple worship** follows the Sinai-to-Bountiful progression. We prepare (sanctification), receive instruction (covenant law), make covenants (the stipulations), and are promised entry into God's presence. The temple *is* the mountain of the Lord.

**The sacrament** renews covenant weekly — a personal Shavuot rhythm. We recommit to the covenant every Sabbath, taking upon ourselves the name of Christ.

**Scripture study** mirrors Tikkun Leil Shavuot. Daily engagement with God's word is the Latter-day Saint version of staying awake for Torah.

**The Restoration and the Feast Days.** Several key Restoration events fall on specific Israelite feast days — a pattern that may reflect divine intentionality in the timing of the Restoration:

| Restoration Event | Gregorian Date | Hebrew Calendar | Feast Day |
|-------------------|---------------|-----------------|-----------|
| **Moroni delivers the gold plates** | September 22, 1827 | 1 Tishrei 5588 | **Yom Teruah** (Feast of Trumpets) — the day the shofar sounds to announce the coming of the King. An angel, often depicted with a trumpet, delivers the record that will restore the covenant. |
| **Kirtland Temple dedicated** | March 27, 1836 | 14 Nisan 5596 | **Eve of Passover** — the dedication of the Lord's house begins on the very evening Israel prepares the Paschal lamb. |
| **Elijah, Moses, and Elias appear** (D&C 110) | April 3, 1836 | 21 Nisan 5596 | **Last day of Passover** (also Easter Sunday) — Elijah returns to the Temple on the feast when Jews open the door for him at every Seder. He restores the sealing keys (D&C 110:13-16), fulfilling Malachi 4:5-6. |

The D&C 110 / Passover correlation is documented in Stephen D. Ricks, "<a href="https://scholarsarchive.byu.edu/byusq/vol23/iss4/10/" target="_blank">The Appearance of Elijah and Moses in the Kirtland Temple and the Jewish Passover</a>," *BYU Studies* 23, no. 4 (1983): 483-486. The Elijah connection is particularly striking: for centuries, Jews have poured a cup for Elijah and opened the door at every Passover Seder, anticipating his return. On Passover 1836, Elijah came — not to a Seder table, but to a temple — and restored the keys that turn the hearts of the fathers to the children.

The Melchizedek Priesthood restoration (May-June 1829) falls in the same general window as Shavuot 5589 (June 3-4, 1829) — the feast of covenant-giving — but the exact date is not established historically, so this correlation remains suggestive rather than confirmed.


</div>
</details>

<!-- ═══════════════════════════════════════════════════════════════════════════
     REFLECTION & CLOSING
     ═══════════════════════════════════════════════════════════════════════════ -->

<div style="background: linear-gradient(135deg, #fdf6e3, #fef9ef); border-radius: 16px; padding: 2rem; margin: 2rem 0; border: 1px solid #e8dcc8;">
<h2 style="margin-top: 0; color: #8b6914; text-align: center;">Reflection Questions</h2>
<div style="display: grid; gap: 1rem; margin-top: 1.5rem;">
<div style="background: white; padding: 1rem 1.25rem; border-radius: 8px; border-left: 4px solid #d4a574;">
<strong style="color: #1a6b74;">The Deepening Law:</strong> Which commandment is God deepening for you right now — moving you from the letter to the heart, from prohibition to covenant action?
</div>
<div style="background: white; padding: 1rem 1.25rem; border-radius: 8px; border-left: 4px solid #d4a574;">
<strong style="color: #1a6b74;">The Four Mountains:</strong> Where in your life do you see the Sinai-to-Bountiful pattern — from distance to closeness with God?
</div>
<div style="background: white; padding: 1rem 1.25rem; border-radius: 8px; border-left: 4px solid #d4a574;">
<strong style="color: #1a6b74;">The Harvest:</strong> What "sheaves" has God entrusted to your harvest this season? Who has He asked you to gather?
</div>
<div style="background: white; padding: 1rem 1.25rem; border-radius: 8px; border-left: 4px solid #d4a574;">
<strong style="color: #1a6b74;">The Pattern:</strong> How does understanding the Shavuot pattern change the way you think about Pentecost, the temple, and covenant-making?
</div>
</div>
</div>

<div style="background: linear-gradient(135deg, #1a6b74, #2a8a94); color: white; border-radius: 16px; padding: 2rem; margin: 2rem 0; text-align: center;">
<h2 style="margin-top: 0; color: white;">An Invitation</h2>

<p style="font-size: 1.1rem; line-height: 1.7; max-width: 700px; margin: 0 auto 1.5rem;">Shavuot reminds us that deliverance is only the beginning. God did not free Israel from Egypt simply to wander. He freed them for covenant — for relationship, for instruction, for the privilege of ascending His mountain and hearing His voice.</p>

<p style="font-size: 1.1rem; line-height: 1.7; max-width: 700px; margin: 0 auto 1.5rem;">The four mountains remind us where the story ends: not at a distance, not through a mediator, not in terror — but face to face, hand to wound, one by one.</p>

<blockquote style="background: rgba(255,255,255,0.15); border-radius: 8px; padding: 1.25rem; margin: 1.5rem auto; max-width: 600px; font-style: italic;">
"Arise and come forth unto me, that ye may thrust your hands into my side, and also that ye may feel the prints of the nails in my hands and in my feet, that ye may know that I am the God of Israel."
<div style="margin-top: 0.5rem; font-style: normal; font-size: 0.9rem;">— <a href="https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/11?lang=eng&id=14" target="_blank" data-ref="3 Nephi 11:14" style="color: #fef5e7;">3 Nephi 11:14</a></div>
</blockquote>

<p style="font-size: 1.1rem; margin-bottom: 0;"><strong>From stone to flesh. From distance to embrace. Come forth.</strong></p>
</div>

---

## Sources & Additional Resources

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
<div style="background: #f8f9fa; border-radius: 10px; padding: 1.25rem;">
<h4 style="margin-top: 0; color: #1a6b74;">Jewish Sources</h4>
<ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
<li><a href="https://www.sefaria.org/Shabbat.86b" target="_blank">Talmud, Shabbat 86b</a> — Shavuot timing</li>
<li><a href="https://www.sefaria.org/Shemot_Rabbah.5.9" target="_blank">Exodus Rabbah 5:9</a> — Voice in 70 languages</li>
<li><a href="https://www.sefaria.org/Sifrei_Devarim.343" target="_blank">Sifre Deuteronomy 343</a> — Torah offered to all nations</li>
<li><a href="https://www.myjewishlearning.com/article/shavuot-101/" target="_blank">Shavuot 101</a> — My Jewish Learning</li>
</ul>
</div>
<div style="background: #f8f9fa; border-radius: 10px; padding: 1.25rem;">
<h4 style="margin-top: 0; color: #1a6b74;">Scholarly Sources</h4>
<ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
<li><a href="https://scholarsarchive.byu.edu/mi/89/" target="_blank">John W. Welch, <em>The Sermon at the Temple and the Sermon on the Mount</em></a> (FARMS, 1990)</li>
<li><a href="https://scripturecentral.org/knowhy/why-did-jesus-deliver-a-version-of-the-sermon-on-the-mount-at-the-temple-in-bountiful" target="_blank">KnoWhy 203</a> — Temple elements at Bountiful</li>
<li><a href="https://rsc.byu.edu/reflections-mormonism/sermon-mount-third-nephi" target="_blank">Krister Stendahl, "The Sermon on the Mount and Third Nephi,"</a> in <em>Reflections on Mormonism</em>, ed. Truman G. Madsen (BYU Religious Studies Center, 1978) — 3 Nephi as Pentecost</li>
</ul>
</div>
<div style="background: #f8f9fa; border-radius: 10px; padding: 1.25rem;">
<h4 style="margin-top: 0; color: #1a6b74;">Related Articles</h4>
<ul style="margin: 0; padding-left: 1.25rem; line-height: 1.8;">
<li><a href="/culture/jewish/moedim/bikkurim/">Bikkurim: Feast of Firstfruits</a></li>
<li><a href="/culture/jewish/moedim/matzot/">Matzot: Feast of Unleavened Bread</a></li>
<li><a href="/weeks/17/">Week 17: Exodus 18-20</a></li>
</ul>
</div>
</div>

<p style="text-align: center; font-style: italic; color: #666; margin-top: 2rem;">Part of our series on Jewish festivals and their fulfillment in Christ.</p>
