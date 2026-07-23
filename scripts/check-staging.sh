#!/bin/sh
# check-staging.sh — production safety guard for the staging pipeline.
#
# Enforces the one invariant the whole system depends on:
#   any page whose `stage:` is set and is NOT "live" MUST also be `draft: true`.
#
# `stage:` only controls listings and badges; it does NOT keep a page off the
# public site. `draft:` is the real gate. A non-live page that forgets
# draft:true renders at a public URL and lands in sitemap.xml. This script
# catches that BEFORE deploy: it runs in the GitHub Pages workflow ahead of
# the Hugo build, so a forgotten draft fails CI instead of publishing an
# unfinished lesson.
#
# Run locally any time:  sh scripts/check-staging.sh
# Exit 0 = clean, exit 1 = at least one leak (details printed).

python3 - <<'PY'
import pathlib, re, sys

root = pathlib.Path("content")
leaks = []
for md in sorted(root.rglob("*.md")):
    txt = md.read_text(errors="ignore")
    parts = txt.split("---")
    if len(parts) < 3:
        continue
    fm = parts[1]
    m = re.search(r'^stage:\s*"?(\w+)', fm, re.M)
    stage = m.group(1) if m else "live"
    is_draft = bool(re.search(r'^draft:\s*true', fm, re.M))
    # cascade can push a stage onto children from an _index.md; the _index
    # itself is what we check, and cascade + draft are set together there.
    if stage != "live" and not is_draft:
        leaks.append((str(md), stage))

if leaks:
    print("STAGING GUARD FAILED — non-live pages that would publish:")
    for f, s in leaks:
        print(f"  [stage: {s}]  {f}   <-- add `draft: true`")
    print("\nEvery page not at stage:live must also be draft:true.")
    print("See docs/staging-pipeline.md.")
    sys.exit(1)

print("Staging guard OK — every non-live page is draft:true.")
PY
