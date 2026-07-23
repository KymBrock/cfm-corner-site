# Working on CFM Corner from a phone or iPad

*Added 2026-07-23. How to edit lessons and field guides, and preview them, when you're
away from the desktop.*

There are two separate needs, and they have different answers:

1. **Editing** the markdown (guide pages, week front matter, staging flags) — works today,
   no setup.
2. **Previewing** the rendered result (the actual page, badges, the `/pipeline/` dashboard) —
   needs a one-time Cloudflare setup you can do from the iPad's browser.

---

## 1. Editing — available now

The repo is **public on GitHub** and the theme is committed directly (no submodules), so
nothing you'd edit is trapped on the desktop. Pick whichever fits the device:

| Tool | Device | Good for |
|---|---|---|
| **github.dev** | any browser (great on iPad) | Full VS Code in the browser. On the repo page press `.`, or change `github.com` → `github.dev` in the URL. Edit, commit to a branch. Best all-round option. |
| **Working Copy** | iOS / iPadOS app | A real native git client — clone, branch, edit, commit, push. Best if you'll do this often. |
| **GitHub mobile app / web** | phone | Quick single-file text fixes and typos. |

**Always commit to a branch, not `main`.** `main` auto-deploys to the live site. Use the
existing work branches (`claude/staging-pipeline`, `claude/eager-jang-5baf4c`) or make a new
one. Merging to `main` stays a deliberate desktop decision.

### The staging flags you'll actually touch remotely
From [`docs/staging-pipeline.md`](staging-pipeline.md):

```yaml
stage: review        # drafting → review → ready → live
stage_blockers:
  - "Weekly Resources"
  - "Weekly Insights"
```

`draft: true` keeps a page off the public site no matter its stage. A whole field guide is
staged from one line in its `_index.md` (`cascade: { stage: ready }`).

---

## 2. Previewing — one-time Cloudflare setup (do it from the browser)

You already have the build scripts (`scripts/cf-pages-build.sh`, `scripts/deploy-preview.sh`).
What was never done is connecting a Cloudflare Pages project to the repo. **You do not need
`wrangler` or any command line for the auto-build path** — it's all in the Cloudflare web
dashboard, which works from the iPad.

### Setup (once)
1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. Authorize GitHub, pick **`cfm-corner-site`**.
3. Build settings:
   - **Framework preset:** None
   - **Build command:** `sh scripts/cf-pages-build.sh`
   - **Build output directory:** `public`
4. **Environment variables** → add `HUGO_VERSION` = **`0.156.0`** (see version note below).
5. Save and deploy.

### After that — the remote loop
- **Every branch push auto-builds a preview** at `https://<branch-alias>.<project>.pages.dev`.
  Branch alias = branch name lowercased, `/` and `_` → `-`, capped at 28 chars.
- Preview builds run **with drafts** (`hugo -D`) and the staging UI on, so you'll see staged
  weeks, stage badges, and the `/pipeline/` dashboard rendered — the same as local
  `hugo server -D`.
- Every `*.pages.dev` build is **noindexed** (the script writes `robots.txt` + `_headers`),
  so previews never reach search engines. Production stays on GitHub Pages at
  `www.cfmcorner.com`.

So the away-from-desk workflow becomes: **edit in github.dev → commit to a branch →
Cloudflare builds → open the preview URL on your phone.**

### Heavier alternative: GitHub Codespaces
If you ever want to run `hugo server` *itself* remotely (live reload, not just per-push
builds), Codespaces gives you a full Linux dev environment in the browser, iPad included.
More capable, more setup, and it spins compute up and down. The Cloudflare path above is
lighter and enough for reviewing.

---

## Version pinning (why 0.156.0)

Hugo's output can shift between versions, so previews must build with the **same** Hugo as
production, or "looks right in preview" won't guarantee "looks right live." These were three
different versions and are now pinned to one:

| Where | Setting | Value |
|---|---|---|
| Local dev machine | `hugo` (Homebrew) | 0.156.0 |
| GitHub Pages (production) | `hugo-version` in `.github/workflows/deploy.yml` | **0.156.0** (was `latest`) |
| Cloudflare (preview) | `HUGO_VERSION` dashboard env var | **0.156.0** (docs said 0.164.0) |

`0.156.0` was chosen because it's what the desktop runs and what all current content was
authored and verified against. **To upgrade later, bump all three together** — the two
in-repo spots (`deploy.yml`, `cf-pages-build.sh`) plus the Cloudflare dashboard env var.

---

## One caveat about a public repo

Because `cfm-corner-site` is **public**, unpublished drafts (the Babylon guide, Week 31, etc.)
are readable as **source on GitHub** even while staging keeps them off the website and out of
search results. Staging controls the *published site*, not repo visibility. If a draft ever
needs to be genuinely private before launch, that's a repo-visibility decision — not something
the staging flags can do.
