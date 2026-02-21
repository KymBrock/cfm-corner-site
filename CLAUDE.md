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
