# The Staging Pipeline — producing lessons in advance

*Added 2026-07-23. Lets weeks and field guides be built weeks ahead, reviewed at
each tier, and shipped by adding only the last-minute pieces.*

## The two gates

Staging uses **two independent controls**. Understanding the split is the whole system.

| Control | Question it answers | Effect |
|---|---|---|
| **`draft:`** | Is this on the public site? | The hard gate. `draft: true` = not built for production **at all** — no page, no sitemap entry, nothing. |
| **`stage:`** | Where is this in production? | Pipeline position. Drives badges, the dashboard, and listing visibility. |

> **`draft` is the only real gate.** Hiding a card from a listing does **not** hide the
> page — the URL still works and still lands in `sitemap.xml`. Anything not yet public
> must stay `draft: true`, whatever its stage.

### The guard (so you can't forget)

Because the rule above is easy to forget, `scripts/check-staging.sh` enforces it: **any page
with a non-`live` stage that lacks `draft: true` fails the check.** It runs in the GitHub Pages
deploy workflow *before* the Hugo build, so a forgotten `draft:` **fails CI instead of
publishing an unfinished lesson.** Run it yourself any time:

```sh
sh scripts/check-staging.sh
```

## The four stages

```yaml
stage: ready
stage_blockers:
  - "Weekly Resources"
  - "Weekly Insights"
```

| stage | meaning | `draft:` should be | public? |
|---|---|---|---|
| `drafting` | being written | `true` | no |
| `review` | reads end-to-end, needs Kym's pass | `true` | no |
| `ready` | verified — waiting only on the blockers listed | `true` | no |
| `live` | shipped | `false` | **yes** |

**A page with no `stage:` counts as `live`.** All existing content therefore behaves
exactly as it did before — nothing had to be back-filled.

## Where you review it

| Surface | Command / URL | Shows drafts? | Staging UI? |
|---|---|---|---|
| Local | `hugo server -D` → `localhost:1315` | yes | yes |
| Cloudflare preview | push any branch → `<branch>.cfm-corner-previews.pages.dev` | yes | yes |
| **Production** | GitHub Pages from `main` | **no** | **no** |

Previews are noindexed and run with analytics off. The staging UI (badges, banner,
`/pipeline/`) is switched on by `isPreview = true` in `config-preview.toml`, or by
`hugo.IsServer` locally — production sets neither, so unpublished work cannot leak in.

## The dashboard

**`/pipeline/`** — every week and field guide, grouped by stage, with blockers.
Built from `content/pipeline.md`, which is `draft: true`, so the dashboard exists
**only** on staging builds and can never be published. Designed to read on a phone.

## Staging a whole field guide at once

Set the stage once in the guide's `_index.md`; `cascade` pushes it to every page:

```yaml
stage: ready
stage_blockers:
  - "Babylon guide (3 cross-links)"
cascade:
  stage: ready
```

## Shipping a week

1. Build it early at `stage: drafting`, `draft: true`.
2. When it reads end-to-end → `stage: review`. Review on the preview URL.
3. When verified → `stage: ready`, and list what's outstanding in `stage_blockers`
   (typically Weekly Resources and Insights, which can't exist until they're posted).
4. Add the last-minute pieces, clear `stage_blockers`.
5. Ship: `stage: live` **and** `draft: false`. Merge to `main`.

Step 5 is the only step that changes anything public.

## Files involved

| File | Role |
|---|---|
| `layouts/partials/stage-badge.html` | The badge + blocker text |
| `layouts/partials/staging-notice.html` | "You are on a staging build" banner |
| `layouts/weeks/list.html` | Week listing — filters non-live on production |
| `layouts/culture/list.html` | Guide listing — filters non-live on production |
| `layouts/_default/pipeline.html` | The dashboard |
| `content/pipeline.md` | Dashboard page (`draft: true` = preview-only) |
| `config-preview.toml` | Sets `isPreview = true` |

The two list layouts are **project overrides** of theme files. The theme is untouched;
deleting these two files reverts the site to its previous behaviour exactly.
