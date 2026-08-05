# Narration Studio production run — Achaemenid & Assyria

*Paste the block below into a new Claude Code session **on the Mac**. The Studio is
local-only (`localhost:8770` + the Chatterbox worker), so a cloud session cannot run it.*

---

```
CFM Corner — Narration Studio production run.

## What this is
CFM Corner (~/Developer/cfm-corner-site) is a Latter-day Saint scripture-study
site. Its "field guides" have podcast-style narration in Kym's cloned voice.
Babylon is done (11 sections live). Two guides now have finished scripts and
need audio produced: ACHAEMENID (10 sections) and ASSYRIA (11 sections).

## The scripts
/Users/kymberbrockbank/Obsidian/K Master Vault/Master Project Folder/Ongoing/
CFM Corner/OT_2026/Culture/<Achaemenid|Assyria>/_narration/<slug>.script.md

Each file has YAML front matter, a "How to use this script" note, a
`# SCRIPT` section, and a `# Pronunciation cheat-sheet`.
Load ONLY the body of the `# SCRIPT` section as the episode script — not the
front matter, not the how-to note, not the cheat-sheet. Confirm this parses
sensibly on the first episode before batching.

## The Studio
cd ~/Developer/narration-studio
export TTS_PYTHON=$PWD/tts-venv/bin/python
./.venv/bin/uvicorn app.main:app --port 8770
Voice reference: assets/kym-reference.wav
Pronunciation is automatic via lexicon.json (154 entries, already includes
every hard Persian/Assyrian term and diacritic form in these scripts).
No upload needed.

Pipeline per episode:
  POST /episode/load            {title, script}   -> episode id
  POST /episode/{eid}/auto-curve
  POST /episode/{eid}/generate-all
       (audition; regenerate individual phrases as needed)
  POST /episode/{eid}/export
  GET  /episode/{eid}/export/file
Useful: GET /health, GET /presets, GET /episodes.
Use the "engaged" preset with auto curve, matching the Babylon episodes.
Note the worker has a RAM floor (NARRATE_RAM_FLOOR_GB, default 25) and will
abort a batch below it — avoid running heavy work alongside it.

## Installing the result — IMPORTANT
Export lands at episodes/<eid>/export/<eid>.mp3 at 160 kbps.
Do NOT copy that master into the site. Re-encode to the published spec:

  ffmpeg -nostdin -v error -y -i <master>.mp3 -ac 1 -ar 48000 -b:a 64k \
    -map_metadata -1 \
    ~/Developer/cfm-corner-site/static/audio/culture/<guide>/<PAGE-SLUG>.mp3

**The output filename MUST equal the page's markdown filename exactly**
(e.g. content/culture/ancient/assyria/07-the-fall-of-the-north.md ->
07-the-fall-of-the-north.mp3). Studio episode names are looser than page
slugs — Babylon has babylon-08-babylon-the-bible exporting to
08-babylon-and-the-bible.mp3. Getting this wrong silently breaks the player.

Then add the listen-player block to the page. Copy it verbatim from an
existing page (e.g. content/culture/ancient/babylon/06-the-city-itself.md,
the block between <!-- LISTEN PLAYER --> and <!-- /LISTEN PLAYER -->),
swapping the two audio paths. It sits right after the centred italic
subtitle under the <h2>.

Note: Assyria pages 02 and 03 ALREADY have players pointing at audio that
doesn't exist yet — those two just need the mp3 dropped in, no page edit.

## Order of work
1. Produce ONE short episode first (suggest Achaemenid 09-major-sites,
   ~1,315 words). Export it, install it, and let Kym listen before batching.
   Check especially: pacing, and the KJV word "cieled" (Haggai 1:4) which is
   pronounced "seeld".
2. Only after Kym approves, work through the rest.
   Achaemenid scripts run ~9 min; Assyria ~10 min. Budget generation time.

## Constraints
- Work on branch claude/staging-pipeline in the site repo. Commit as you go.
- Do NOT merge to main and do NOT deploy. The guides are unpublished
  (draft: true) and gated behind the Babylon guide being finished.
- Do not publish audio anywhere without Kym's explicit go-ahead.
- Report progress per episode so Kym can follow along remotely.
```

---

## Human-review items on the scripts (not blocking)

The drafting agents flagged these for a person to confirm:

1. **Assyria 11 — D&C 133:26, 32.** The script elides *"and their prophets shall hear
   his voice, and shall no longer stay themselves"* and places its ellipsis earlier than
   the source page does. Both retained fragments are verbatim and the `…` is present.
2. **Assyria 11 — 3 Nephi 16:1.** Ends *"other sheep, which are not of this land."* with a
   period where the page continues with an ellipsis. Verbatim as far as it goes, but the
   period implies the quotation ended there. Changing it to `…` would match the page.
3. **Assyria 09 — Isaiah 10:13.** *"Assyria thinks it conquers by its own strength and
   wisdom"* is an unquoted paraphrase; the direct quote was cut for length. Check it does
   not read as quotation.
4. **Punctuation convention.** Scripts put terminal periods inside closing quotes
   (read-aloud convention, matching the Babylon exemplars); the source pages put them
   outside. Wording is otherwise character-exact.

## What was verified mechanically

- All 21 match the exemplar structure; `audio_out` paths correct
- **Zero numerals** appear in any script that are absent from its source page
- **105 quoted spans character-checked** across the five most quotation-dense scripts
  (Assyria 07, 08, 09, 10, 11) — zero mismatches
- Guide source pages confirmed untouched (`git diff` clean)
- Every non-ASCII word in every script resolves against the lexicon

**Not verified:** whether the scripts read well aloud. Hence step 1 above.
