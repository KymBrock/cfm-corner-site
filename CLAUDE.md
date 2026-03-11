# Claude Code Safety Rules for cfm-corner-site

⛔ CRITICAL SAFETY RULES — DO NOT VIOLATE ⛔

1. NEVER batch-regenerate weekly lesson HTML files. The files in
   `static/content/week01/` through `week52/` contain hand-crafted content
   that CANNOT be reproduced by any converter or script.

2. NEVER run a converter script against multiple weeks at once.

3. Only make targeted, single-file edits. One file at a time.

4. ALWAYS run `git diff` and show the output BEFORE committing.

5. NEVER commit changes to more than 3 week content files in a
   single commit without explicit approval from Kymber.

6. If a script or tool would modify multiple week files, STOP and
   ask Kymber before proceeding.

## Violation History

On 2026-02-21, commit `905fdfa` mass-regenerated all weeks 1–9 HTML,
destroying hand-crafted content. This required an emergency revert
(commit `2cfc1a0`). This must never happen again.

## Pre-Commit Hook

A git pre-commit hook blocks any commit touching more than 5 week
content files. Use `--no-verify` ONLY with Kymber's explicit approval.

## Recovery

If disaster strikes, the tag `stable-2026-02-21` marks a known-good state.

---

## Deployment Checklist

When deploying a new week, follow these steps in order:

### Week Front Matter (`content/weeks/NN.md`)
- [ ] Set `current: true` on the **new** week's `.md`
- [ ] Set `current: false` on the **previous** week's `.md`
- [ ] Verify all `charts:` entries match their actual article titles and descriptions
  — title and description must come from the article's own front matter, not be invented
- [ ] Verify chart `url:` paths resolve correctly (e.g., `study-library/articles/slug/`)

### Static Content (`static/content/weekNN/`)
- [ ] Run `link-audit.py` on all three files (study-guide, insights, resources) — zero issues
- [ ] Verify no emojis in any HTML files (monochromatic icons only)
- [ ] Verify all video cards use thumbnail format (never plain text links)

### Hugo Preview
- [ ] **Restart the Hugo server** after editing any file in `static/content/` — Hugo's
  `readFile` function caches at build time, so changes to static HTML files are NOT
  visible until the server is restarted
- [ ] Check all tabs load (Study Guide, Insights, Resources, Charts)
- [ ] Check lesson image displays
- [ ] Verify charts are interactive

### Git & Deploy
- [ ] Run `git diff` and review before committing
- [ ] Commit with message format: `Week NN: Scripture Reference`
- [ ] Push to main — GitHub Actions auto-deploys
- [ ] Verify live site at `www.cfmcorner.com/weeks/NN/`

---

## ⛔ CONTENT INTEGRITY — ABSOLUTE RULE ⛔

**NOTHING in any CFM Corner lesson, insight, study guide, or resource may be
fabricated, assumed, inferred, or written from general knowledge.**

Every claim, description, summary, or characterization of content MUST be
sourced from one of the following:

1. **Scripture text** — direct reference to the biblical passage
2. **Vault source files** — study guides, overviews, word studies, or
   other documents in the K Master Vault that Kymber has written or approved
3. **Processed video transcripts** — distilled content in `Video_Distilled/`
   that has been processed through Knowlchemy
4. **Conference talk text** — verified against the actual published talk
   at ChurchofJesusChrist.org before being cited or described
5. **Explicit user instruction** — Kymber has directly provided or
   confirmed the information in the current session
6. **Approved Hebrew grammar references** — the following textbooks are
   approved sources for Hebrew grammatical claims, linguistic terminology,
   and grammatical classifications. When citing, reference the author,
   chapter/section, and page number:

   - **Gesenius' Hebrew Grammar (GKC)** — H.F.W. Gesenius, ed. E. Kautzsch,
     trans. A.E. Cowley. Oxford: Clarendon Press, 2nd English ed. 1910.
     *The universal standard reference grammar for Biblical Hebrew.*
     Vault: `Books/EPUB/Gesenius_Hebrew_Grammar_GKC.pdf`

   - **A Practical Grammar for Classical Hebrew** — J. Weingreen.
     Oxford University Press, 2nd ed. 1959.
     *The standard grammar used in Jewish studies programs and seminaries.*
     Vault: `Books/EPUB/Weingreen_Practical_Grammar_Classical_Hebrew.pdf`

   - **A Grammar for Biblical Hebrew** — William D. Barrick & Irvin A.
     Busenitz. The Master's Seminary, rev. July 2004.
     *Seminary-level grammar with exegetical insights per chapter.*
     Vault: `Books/EPUB/B_B_Hebrew_Grammar_2005.pdf`

   - **Simplified Hebrew Grammar** — Justin T. Alfred. Blue Letter Bible.
     *Accessible introduction hosted by BLB; covers conjunction,
     consecutive, prepositions, article, and verb tenses.*
     Vault: `Books/EPUB/BLB_Simplified_Hebrew_Grammar_Alfred.pdf`

   - **Blue Letter Bible online tools** — blueletterbible.org.
     Lexicon entries, interlinear, and grammar pages are approved sources.

7. **Approved rabbinic primary sources for letter symbolism** — the
   following texts are approved sources for claims about the Jewish
   tradition of finding meaning in Hebrew letter forms. These are
   *midrashic* sources (homily and meditation), NOT grammar references.
   Never conflate them with linguistic analysis.

   - **Babylonian Talmud, Shabbat 104a** — The children's alphabet
     homily. Young students derive moral and symbolic lessons from the
     names, forms, and sequences of the Hebrew letters.
     Sefaria (bilingual): https://www.sefaria.org/Shabbat.104a
     Vault: `Books/EPUB/Shabbat_104a_Letter_Symbolism_Sefaria.md`

   - **Otiyot de-Rabbi Akiva (Alphabet of Rabbi Akiva)** — Post-Talmudic
     midrashic text building extended homilies around each letter. Version 1
     features the letters petitioning God to begin creation.
     Sefaria (Version 1): https://www.sefaria.org/Otzar_Midrashim,_Midrashim_of_Rabbi_Akiba,_Aleph_Bet_of_Rabbi_Akiba_(Version_1)
     Sefaria (Version 2): https://www.sefaria.org/Otzar_Midrashim,_Midrashim_of_Rabbi_Akiba,_Aleph_Bet_of_Rabbi_Akiba_(Version_2)
     Vault: `Books/EPUB/Otiyot_de_Rabbi_Akiva_Sefaria.md`

### What this means in practice:

- **Video descriptions** — NEVER describe what a video "covers" or
  "focuses on" unless the transcript has been processed and is in
  `Video_Distilled/`. If no distillation exists, list the title only
  and direct readers to the Resources tab.

- **Conference talk quotes** — NEVER paraphrase or characterize a talk
  without verifying the actual text. If uncertain, link to the talk
  and let readers read it themselves.

- **Hebrew/Greek claims** — NEVER assert a linguistic meaning, root, or
  connection that is not sourced from BLB, an approved grammar reference,
  a vault word study, or Kymber's direct instruction.

- **Pictographic claims** — The connection between ancient pictographic
  letter forms and grammatical function is Kymber's personal mnemonic
  approach. It is NOT conventional grammar pedagogy. Always present
  pictographic connections as memory aids, never as scholarly consensus.
  The grammar itself (sourced from approved references) is what matters.

- **Historical/cultural claims** — NEVER add "enriching" context that
  comes from training data alone. Source it from vault files or flag it
  as needing verification.

### When in doubt:

Leave a placeholder and flag it explicitly, e.g.:
`[VIDEO SUMMARY PENDING — awaiting Knowlchemy distillation]`
`[QUOTE PENDING VERIFICATION]`

**It is always better to publish less and be accurate than to publish
more and be wrong. Kymber's readers trust this content for scripture
study. That trust must never be violated.**
