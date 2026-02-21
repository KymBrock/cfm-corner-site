# CFM Corner — Git Protocol
## Version Control Standards for All Repositories

**Updated:** 2026-02-20
**Status:** Active

---

## Repository Overview

| Repo | GitHub | Purpose | Deploy |
|------|--------|---------|--------|
| `cfm-corner-site` | `KymBrock/cfm-corner-site` | Hugo website — the live site | GitHub Actions → `cfmcorner.com` |
| `cfm-corner-tools` | `KymBrock/cfm-corner-tools` | Python automation tools | Manual (no deploy) |
| `knowlchemy-biblical` | `KymBrock/knowlchemy-biblical` | Biblical dictionaries & translation data | Manual |
| `cfm-ot-study` | `KymBrock/cfm-ot-study` | **Legacy Wix site** — archived, read-only | None |
| `Knowlchemy-Kymber` | `KymBrock/Knowlchemy-Kymber` | Knowlchemy personal instance | Manual |
| `Knowlchemy-Dec2024` | `Vishai/Knowlchemy-Dec2024` | Knowlchemy upstream | Manual |
| `knowlchemy-web` | `Vishai/knowlchemy-web` | Knowlchemy web frontend | Manual |
| `llama.cpp` | `ggerganov/llama.cpp` | Upstream LLM inference — **never push** | Never |

---

## Automatic Index Update (Post-Commit Hook)

**Both `cfm-corner-site` and `cfm-corner-tools` have a `post-commit` hook installed.**

After every `git commit` in either repo, this runs automatically:
```bash
/Users/kymberbrockbank/Developer/cfm-corner-tools/.venv/bin/python3 scripts/update_code_index.py
```

This updates:
```
K Master Vault/Tools/Developer/CODE_INDEX_AUTO.md
```

**You never need to run the index updater manually** — every commit triggers it.

If you ever need to manually refresh the index (e.g. after adding files without committing):
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-tools
.venv/bin/python3 scripts/update_code_index.py
```

Hook files are located at:
```
cfm-corner-site/.git/hooks/post-commit
cfm-corner-tools/.git/hooks/post-commit
```

> **Note:** Git hooks live in `.git/hooks/` which is NOT tracked by git itself.
> If you ever clone either repo fresh, you must reinstall the hooks manually (see Appendix A).

---

## 1. cfm-corner-site (Primary Active Repo)

### How Deployment Works
- **Push to `main`** → GitHub Actions auto-builds Hugo + Pagefind → deploys to GitHub Pages → live at `cfmcorner.com`
- No manual `hugo build` needed — GitHub Actions handles everything
- Build: `hugo --minify --baseURL "https://www.cfmcorner.com/"`
- Search: `npx pagefind@latest --site public`
- Allow ~2 minutes after push for the live site to update

### What to ALWAYS Commit
```
content/weeks/          ← Hugo front matter pages
content/hebrew/         ← Hebrew lesson markdown
static/content/weekNN/  ← HTML content files
static/data/            ← Popup JSON files (lexicon, scripture, LDS) — CRITICAL
static/css/             ← Site stylesheets
static/images/          ← Site images
themes/                 ← Hugo templates including baseof.html
scripts/                ← Utility scripts including link-audit.py
.github/workflows/      ← GitHub Actions deploy config
```

### What Is Gitignored (never commit)
```
public/                 ← Hugo build output (GitHub Actions regenerates this)
resources/_gen/         ← Hugo cache
.hugo_build.lock
.DS_Store
```

### Standard Weekly Commit Workflow
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-site

# 1. Run link audit BEFORE committing — fix all issues first
python3 scripts/link-audit.py --week weekNN

# 2. Stage all changes
git add -A

# 3. Commit with descriptive message
git commit -m "Week NN: Scripture Reference — brief description"
# ↑ post-commit hook auto-updates CODE_INDEX_AUTO.md in Obsidian

# 4. Push (triggers GitHub Actions auto-deploy)
git push

# 5. Verify live at https://www.cfmcorner.com/weeks/NN/
```

### Commit Message Conventions
```
# Weekly content
Week 09: Genesis 18-23 — insights, study guide, popup fixes
Week 10: Genesis 24-33 — initial content

# Site/template changes
Site: popup system updates — lexicon JSON, scripture JSON
Site: fix Hugo server renderToMemory issue

# Hebrew lessons
Hebrew: fix double-nested markdown links in lessons 01-08
Hebrew: add lesson 09

# Data/scripts
Data: rebuild lexicon-popups.json from Translation Hub
Data: rebuild scripture-verses.json — add Genesis 21 verses
Scripts: add link-audit.py
Scripts: update generate-email.sh

# Multi-item cleanup
Cleanup: link fixes weeks 08-09, popup JSON, audit script, style updates
```

### Branch Strategy
`main` is the only branch for routine work — commit directly.

For major experimental changes only (e.g. redesigning popup system or theme):
```bash
git checkout -b feature/description
# ... work and test ...
git checkout main
git merge feature/description
git push
git branch -d feature/description
```

### Currently Uncommitted Changes (as of 2026-02-20)
```bash
# Modified files:
content/hebrew/01-aleph-bet.md       ← double-nested link fixes
content/hebrew/02-08 (various)       ← double-nested link fixes
static/content/week08/resources.html ← updates
static/content/week09/insights.html  ← moreh/Yah/tsachaq/Machpelah links
static/content/week09/study-guide.html
static/css/style.css
themes/cfm/layouts/_default/baseof.html ← popup system

# Untracked (need git add):
static/data/                         ← CRITICAL — entire popup JSON folder
scripts/link-audit.py                ← new audit script
_archive/                            ← add to .gitignore or commit
```

**Recommended commit:**
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-site
git add static/data/ scripts/link-audit.py themes/ static/content/ static/css/ content/hebrew/
git add -u
git commit -m "Site: popup system, popup JSON data, link fixes weeks 08-09, link audit script"
git push
```

---

## 2. cfm-corner-tools (Active Tooling Repo)

### Purpose
Python automation tools for content generation. Runs locally only — not deployed anywhere.

### What to ALWAYS Commit
```
cfm_cli.py              ← Primary CLI entry point
converters/             ← Markdown → HTML converters
generators/             ← HTML generators (resources, email, charts)
ingesters/              ← Video collection & distillation
scripts/                ← Utility scripts (update_code_index.py lives here)
data/                   ← Local data file copies (lexicon JSON etc.)
shared/                 ← Shared Python modules
verification/           ← Link verification tools
requirements.txt        ← Python dependencies
```

### What to NEVER Commit (verify .gitignore)
```
.venv/                  ← Python virtual environment
__pycache__/ *.pyc
config.yaml             ← Contains API keys — NEVER COMMIT
.youtube_api_key        ← API key file — NEVER COMMIT
logs/
output/
ingesters/.cache/
.DS_Store
```

### Standard Commit Workflow
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-tools

git add -A
git commit -m "Brief description of what changed"
# ↑ post-commit hook auto-updates CODE_INDEX_AUTO.md in Obsidian
git push
```

### Currently Uncommitted Changes (as of 2026-02-20)
```bash
# Modified:
cfm_cli.py
data/lexicon-popups.json              ← rebuilt from Translation Hub
ingesters/collect_and_distill_videos.py

# Deleted (Wix-era cleanup):
converters/html_to_markdown.py
converters/md_to_html_ui.py
converters/run_converter_ui.sh
converters/wix_converter.py
converters/wix_formatter.py
generators/weekly_resources/generate_weekly_resources_full.py

# Untracked:
_archive/                             ← moved Wix-era files
scripts/                              ← new scripts folder
```

**Recommended commit:**
```bash
cd /Users/kymberbrockbank/Developer/cfm-corner-tools
git add -A
git commit -m "Cleanup: remove Wix-era converters, update lexicon data, add scripts folder"
git push
```

---

## 3. knowlchemy-biblical (Biblical Data Repo)

### Purpose
Biblical dictionaries and translation reference data used by cfm-corner-tools.

### Commit Workflow
```bash
cd /Users/kymberbrockbank/Developer/knowlchemy-biblical
git add -A
git commit -m "Add/update [language] dictionary data"
git push
```

### Note on Post-Commit Hook
This repo does **not** have the post-commit hook. If you add scripts to this repo
that should appear in CODE_INDEX_AUTO.md, either:
- Add the hook manually (see Appendix A), or
- Run `update_code_index.py` manually after committing

---

## 4. cfm-ot-study (Legacy — Read Only)

This is the old Wix-era site. **Do not make new commits here.**
Use only for reference to recover old content if needed.

```bash
# To look something up:
cd /Users/kymberbrockbank/Developer/cfm-ot-study
git log --oneline     # browse history
git show <hash>       # inspect a specific commit
# DO NOT: git add, git commit, git push
```

---

## 5. llama.cpp (Upstream — Never Push)

This is a fork of the upstream llama.cpp repo. Pull updates from upstream, never push.
```bash
cd /Users/kymberbrockbank/Developer/llama.cpp
git fetch origin
git pull origin master
# Never: git push
```

---

## Quick Reference Card

```
DAILY WORK (cfm-corner-site):
  python3 scripts/link-audit.py --week weekNN   ← always before commit
  git add -A
  git commit -m "Week NN: description"          ← triggers index update + deploy
  git push

TOOL CHANGES (cfm-corner-tools):
  git add -A
  git commit -m "description"                   ← triggers index update
  git push

NEVER COMMIT:
  config.yaml  .youtube_api_key  .venv/  public/  __pycache__

INDEX UPDATE (automatic after every commit, or manual):
  cd cfm-corner-tools
  .venv/bin/python3 scripts/update_code_index.py
```

---

## Appendix A: Reinstalling Post-Commit Hooks After Fresh Clone

If you clone either repo fresh, the `.git/hooks/` directory won't have the post-commit hook.
Run this to reinstall:

```bash
# For cfm-corner-site:
cat > /Users/kymberbrockbank/Developer/cfm-corner-site/.git/hooks/post-commit << 'EOF'
#!/bin/sh
cd /Users/kymberbrockbank/Developer/cfm-corner-tools
.venv/bin/python3 scripts/update_code_index.py
EOF
chmod +x /Users/kymberbrockbank/Developer/cfm-corner-site/.git/hooks/post-commit

# For cfm-corner-tools:
cat > /Users/kymberbrockbank/Developer/cfm-corner-tools/.git/hooks/post-commit << 'EOF'
#!/bin/sh
cd /Users/kymberbrockbank/Developer/cfm-corner-tools
.venv/bin/python3 scripts/update_code_index.py
EOF
chmod +x /Users/kymberbrockbank/Developer/cfm-corner-tools/.git/hooks/post-commit
```

---

*CFM Corner Git Protocol | Updated 2026-02-20*
