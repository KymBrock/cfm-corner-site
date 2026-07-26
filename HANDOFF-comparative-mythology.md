# Handoff — Comparative Mythology Field Guide

**Date:** 2026-07-25 · **Branch:** `claude/biblical-cultures-mythologies-mct9hz` · **PR:** #3 (draft)
**From:** Claude Code on the web (restricted network) → **To:** desktop Claude Code (full tools)

---

## Why this handoff exists

The work was started in a **Claude Code web session** whose **network egress policy blocked
content hosts** and where the **Obsidian vaults were not mounted**. That made the core task —
gathering primary texts and podcast transcripts — impossible to finish there. Moving to the
**desktop** removes both limits: full outbound network, the `Sacred Texts/` and `WeeklyLessons/`
vaults, the NAS books, and a local Hugo. **Nothing is lost** — everything is committed to the
branch; pull it and continue.

Confirmed blocked in the web session (proxy logged "policy denial" on CONNECT):
`theancienttradition.com` (transcripts) **and** `sacred-texts.com` (primary texts). On desktop,
verify these are reachable and proceed.

---

## TL;DR — current state

- **Goal:** a new **Culture field guide** collecting the comparative mythologies of the biblical
  world — three threads under one hub: **comparative-myth motifs**, **astronomy/celestial**,
  **linguistic/cognate** word studies. It also feeds Kymber's linguistic + astronomy study.
- **Built & committed (3 commits):** prep scaffold, guide hub, Section 01, and a Cloudflare
  build fix. CI is **green**; preview is live.
- **Not yet built:** sections 02–10 (they need primary texts / transcripts / vault — the reason
  for the desktop move).
- **Read these two committed docs first:** `COMPARATIVE-MYTHOLOGY-PREP.md` (outline + Primary
  Source Registry + sourcing hierarchy) and this file. Also the project `CLAUDE.md` (safety +
  content-integrity rules — non-negotiable).

---

## What's built (committed to the branch)

| File | What it is |
|---|---|
| `COMPARATIVE-MYTHOLOGY-PREP.md` | The plan: hub + 10-section outline, four-layer discipline, **sourcing hierarchy**, and the **Primary Source Registry** (which primary text → which edition to cite → which open edition to link). |
| `content/culture/comparative-mythology/_index.md` | Guide hub (generic `culture/list.html`; child sections auto-surface as cards). Working title *"Echoes of the First Tradition."* |
| `content/culture/comparative-mythology/01-the-first-tradition.md` | Framing essay — the reading protocol for the whole guide. Sourced only from existing site content (the Ugarit page's "fragments" argument), verifiable scripture (Acts 17:26–27; Deut 32:8; Alma 29:8), and the attributed podcast thesis. |
| `scripts/cf-pages-build.sh` | Fix: trims the 92 MiB `scripture-verses.json` in preview builds (mirrors `deploy-preview.sh`) so Cloudflare's 25 MiB/file limit is not tripped. |

**Commits:** `5bd0b7b` (scaffold + Section 01) · `5a3a531` (build fix) · `7ad4364` (sourcing
reframe). **Preview:** `https://claude-biblical-cultures-myt.cfm-corner-previews.pages.dev/culture/comparative-mythology/`

---

## Decisions locked in (don't re-litigate)

1. **Structure:** a standalone Culture **field guide** (not a Study Library series, not woven
   into existing guides). Home: `content/culture/comparative-mythology/` (provisional; renames
   trivially). Working title *"Echoes of the First Tradition."*
2. **Scope:** all three threads under one hub.
3. **Sourcing = primary texts first.** The actual ancient texts in credible scholarly
   translation (original language where it matters) are the backbone. *The Ancient Tradition*
   podcast (Jack Logan) is **one labeled [INTERP] lens among several**, never a source of fact.
   Add **Mircea Eliade** and other comparative scholars (see below) to the scholarship tier.
4. **Framing:** the four-layer discipline (**biblical text / reconstruction / interpretation /
   LDS frame**) kept distinct on every page; comparative parallels are **resonance, never
   proof**; **"deepens, not debunks."**

---

## The discipline (from `CLAUDE.md` — must hold on every page)

- **Content Integrity:** nothing fabricated, inferred, or written from general knowledge. Every
  claim traces to scripture, a **primary text quoted from a real edition**, the vault, a verified
  source, or Kymber's direct instruction. **No primary-text quotations from memory** — read the
  source.
- **Scholars:** every named scholar real and verified before shipping.
- **Scripture/term linking contract:** full book + chapter refs; `data-ref` on every scripture
  link; BLB lexicon popups; the mandatory Greek-LXX / Latin-Vulgate / English cross-language row
  in word studies.
- **Safety rules:** never batch-regenerate week HTML; targeted single-file edits; **run
  `git diff` and show it before committing**; a pre-commit hook blocks commits touching >5 week
  content files (this guide touches **zero** week files). Work only on the branch above.
- **Images:** self-owned / PD / CC only, with provenance; Moedim visual style; no emojis
  (monochrome icons only).
- **Hugo caching:** after editing anything in `static/`, restart the Hugo server (readFile
  caches at build time).

---

## Sourcing — what to gather on desktop

Full detail is in `COMPARATIVE-MYTHOLOGY-PREP.md` → *Primary Source Registry*. In short:

- **Primary texts (open, link + quote):** *Enūma Eliš* (sacred-texts, King PD) · Sumerian Flood
  Story / Eridu Genesis (ETCSL `t.1.7.4`) · *Gilgamesh* XI (sacred-texts) · Eddas / Avesta
  (sacred-texts) · Hebrew MT via Sefaria + BLB · Hesiod/Aratus via Perseus.
- **Primary texts (cite, quote briefly — in copyright):** Lambert *Babylonian Creation Myths*;
  A.R. George *Gilgamesh*; Lambert & Millard *Atra-ḥasīs*; Dalley *Myths from Mesopotamia*;
  Finkel *The Ark Before Noah*.
- **Comparative scholarship (peer-reviewed [INTERP] tier):** **Mircea Eliade** (*Patterns in
  Comparative Religion*; *The Sacred and the Profane*; *The Myth of the Eternal Return*;
  *Images and Symbols*) — axis mundi / sacred tree / sacred center / sacred time. Plus the
  ANE-specific load-bearing set to consider: Thorkild Jacobsen (*Treasures of Darkness*), S.N.
  Kramer (*Sumerian Mythology*), Henri Frankfort (*Kingship and the Gods*), John H. Walton
  (*ANE Thought and the OT*), Othmar Keel (*Symbolism of the Biblical World*); for the sacred
  tree specifically E.O. James (*The Tree of Life*) and Geo Widengren (*The King and the Tree of
  Life*). Handle Campbell / Frazer / *Hamlet's Mill* as **use-with-care [INTERP]**; keep
  Jonathan Z. Smith on hand as the critical corrective. Confirm which of these Kymber wants.
- **NAS + vault:** Kymber has some of these books on the **NAS**; the approved vault source lanes
  are listed in `CLAUDE.md` (Sacred Texts vault, LDS canon, Talmud/Midrash/Targum, Conference
  Talks, WeeklyLessons, IF research). Use them directly from the desktop.
- **The Ancient Tradition transcripts:** the site posts per-episode audio transcripts; pick the
  3–5 episodes to echo on sections 02–04 (creation / flood / sacred tree) and pull those.

---

## Pending work (build order)

Per the prep-doc outline: **02** Creation & the Primordial Waters (Marduk/Tiamat ↔ *tehom*;
Gen 1 as counter-statement) → **03** The Flood → **04** The Sacred Tree → **05** Cosmic Mountain,
Temple & Divine Council → **06–07** Astronomy (Mazzaroth, Kimah/Kesil, the host of heaven —
greenfield) → **08–09** Linguistic / cognate word studies → **10** Reading Faithfully +
`sources.md`. Build one section at a time, `git diff` before each commit, keep the PR moving.

**Recommended first build on desktop:** Section 02, straight from the *Enūma Eliš* primary text +
Genesis + BLB/Sefaria, to the same discipline and four-layer framing as Section 01.

---

## Build / preview mechanics
- Hugo **0.164.0** (pinned; `HUGO_VERSION` in `cf-pages-build.sh`). Local preview:
  `hugo server` (the project notes port 1326 in some tooling).
- Cloudflare preview via `scripts/deploy-preview.sh` (wrangler); the dashboard build uses
  `scripts/cf-pages-build.sh` (now trims the verse DB).
- **Deferred (Kymber's laptop task):** sharding `data/scripture-verses.json` for on-demand popup
  loading — the long-term fix for the 25 MiB limit and a site-wide performance win. Not started.

---

## First actions in the desktop session
1. `git fetch && git checkout claude/biblical-cultures-mythologies-mct9hz && git pull`.
2. Read `CLAUDE.md`, `COMPARATIVE-MYTHOLOGY-PREP.md`, and this file.
3. Verify network + sources: fetch `theancienttradition.com` (a chosen episode transcript) and
   `sacred-texts.com/ane/stc/` (*Enūma Eliš*) to confirm both are reachable.
4. Confirm the comparative-scholar shortlist with Kymber; note which books are on the NAS.
5. Build **Section 02** from primary sources; `git diff`; commit; push; keep PR #3 moving.
