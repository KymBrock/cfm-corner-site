#!/bin/sh
# Build script for Cloudflare Pages (draft previews while traveling).
# Production hosting stays on GitHub Pages (deploy.yml, main branch) —
# every Cloudflare build, including main, is noindexed below.
#
# Dashboard settings (Workers & Pages -> project -> Settings -> Builds):
#   Build command:          sh scripts/cf-pages-build.sh
#   Build output directory: public
#   Env var (all envs):     HUGO_VERSION = 0.164.0
set -e

if [ "$CF_PAGES_BRANCH" = "main" ]; then
  # Mirror of production as a smoke test — no drafts
  hugo --minify --baseURL "$CF_PAGES_URL/"
else
  # Feature branches: build WITH drafts, analytics off
  hugo -D --minify --baseURL "$CF_PAGES_URL/" --config hugo.toml,config-preview.toml
fi

npx pagefind@latest --site public

# Cloudflare Pages rejects files over 25 MiB. The full scripture-popup DB
# (public/data/scripture-verses.json) is ~92 MiB, so trim the built copy to
# only the verses this build actually references. Applies to every Cloudflare
# build (previews and the main smoke test); static/data/ and the GitHub Pages
# production deploy (deploy.yml) are untouched and still ship the full DB.
python3 scripts/filter-scripture-preview.py

# Fail fast if anything still exceeds the 25 MiB limit.
find public -type f -size +25M | grep . && { echo "ERROR: files over 25 MiB remain"; exit 1; } || true

# Keep every *.pages.dev build out of search engines; the canonical site
# is www.cfmcorner.com via GitHub Pages.
printf 'User-agent: *\nDisallow: /\n' > public/robots.txt
printf '/*\n  X-Robots-Tag: noindex\n' > public/_headers
