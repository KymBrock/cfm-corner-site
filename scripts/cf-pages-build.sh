#!/bin/sh
# Build script for Cloudflare Pages (draft previews while traveling).
# Production hosting stays on GitHub Pages (deploy.yml, main branch) —
# every Cloudflare build, including main, is noindexed below.
#
# Dashboard settings (Workers & Pages -> project -> Settings -> Builds):
#   Build command:          sh scripts/cf-pages-build.sh
#   Build output directory: public
#   Env var (all envs):     HUGO_VERSION = 0.156.0
#
# Keep HUGO_VERSION in sync with the local dev machine and the GitHub Pages
# deploy (hugo-version in .github/workflows/deploy.yml). Bump all three
# together so previews match production. See docs/working-remotely.md.
set -e

# Never let a step wait on stdin. A Cloudflare build has no terminal, so any
# interactive prompt hangs the build forever instead of failing (we lost a
# build to `npx` asking "Ok to proceed?" for ~2 hours). CI=1 puts npm/npx in
# non-interactive mode; `--yes` on npx below is the belt-and-braces version.
export CI=1
export NPM_CONFIG_YES=true

echo "=== cf-pages-build: branch=$CF_PAGES_BRANCH url=$CF_PAGES_URL ==="
echo "=== hugo version ==="
hugo version

if [ "$CF_PAGES_BRANCH" = "main" ]; then
  # Mirror of production as a smoke test — no drafts
  echo "=== building PRODUCTION mirror (no drafts) ==="
  hugo --minify --baseURL "$CF_PAGES_URL/"
else
  # Feature branches: build WITH drafts, analytics off, staging UI on
  echo "=== building PREVIEW (with drafts) ==="
  hugo -D --minify --baseURL "$CF_PAGES_URL/" --config hugo.toml,config-preview.toml
fi

# Search index. `--yes` stops npx prompting when the package isn't cached.
# If this ever fails we still ship the site — search just won't be indexed —
# because a missing search index is far better than a failed deploy.
echo "=== building search index (pagefind) ==="
npx --yes pagefind@latest --site public || echo "WARNING: pagefind failed; continuing without a search index"

# Cloudflare Pages rejects ANY single file over 25 MiB and fails the whole
# deploy at the asset-validation step. GitHub Pages (the real production
# host) has no such limit, so this only ever affects Cloudflare builds.
#
# Today this is static/data/scripture-verses.json (~92 MB) — the verse text
# behind the scripture popups. Dropping it degrades gracefully: baseof.html
# fetches it lazily and already falls back to {} when the fetch fails, so
# popups still render, just without verse text. Everything else is intact.
#
# Anything dropped is named explicitly below — a preview that silently
# omitted files would be worse than one that says what it is missing.
echo "=== checking for files over Cloudflare's 25 MiB per-file limit ==="
find public -type f -size +25M | while read -r f; do
  echo "  DROPPED: $f ($(du -h "$f" | cut -f1)) — exceeds Cloudflare's 25 MiB limit."
  echo "           This preview will render without it. Production is unaffected."
  rm -f "$f"
done

# Keep every *.pages.dev build out of search engines; the canonical site
# is www.cfmcorner.com via GitHub Pages.
printf 'User-agent: *\nDisallow: /\n' > public/robots.txt
printf '/*\n  X-Robots-Tag: noindex\n' > public/_headers

echo "=== cf-pages-build: done ==="
