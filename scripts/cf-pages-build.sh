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

if [ "$CF_PAGES_BRANCH" = "main" ]; then
  # Mirror of production as a smoke test — no drafts
  hugo --minify --baseURL "$CF_PAGES_URL/"
else
  # Feature branches: build WITH drafts, analytics off
  hugo -D --minify --baseURL "$CF_PAGES_URL/" --config hugo.toml,config-preview.toml
fi

npx pagefind@latest --site public

# Keep every *.pages.dev build out of search engines; the canonical site
# is www.cfmcorner.com via GitHub Pages.
printf 'User-agent: *\nDisallow: /\n' > public/robots.txt
printf '/*\n  X-Robots-Tag: noindex\n' > public/_headers
