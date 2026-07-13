#!/bin/sh
# Build the site WITH drafts and deploy a preview to Cloudflare Pages
# via direct upload (wrangler). Run from the repo root:
#   sh scripts/deploy-preview.sh
#
# Requires a one-time `npx wrangler login` on the machine.
# Production hosting is unaffected — GitHub Pages deploys main (deploy.yml).
# Preview URL: https://<branch-alias>.cfm-corner-previews.pages.dev
# (branch alias = branch name lowercased, / and _ become -, max 28 chars)
set -e

PROJECT=cfm-corner-previews
BRANCH=$(git rev-parse --abbrev-ref HEAD)
ALIAS=$(printf '%s' "$BRANCH" | tr '/_' '--' | tr '[:upper:]' '[:lower:]' | cut -c1-28 | sed 's/-*$//')
BASEURL="https://${ALIAS}.${PROJECT}.pages.dev/"

hugo -D --minify --baseURL "$BASEURL" --config hugo.toml,config-preview.toml
npx pagefind@latest --site public

# Keep previews out of search engines
printf 'User-agent: *\nDisallow: /\n' > public/robots.txt
printf '/*\n  X-Robots-Tag: noindex\n' > public/_headers

# Cloudflare Pages rejects files over 25 MiB — trim the 92 MiB verse DB to
# only the references the built site actually uses (public/ copy only).
python3 scripts/filter-scripture-preview.py

# Fail fast if anything else exceeds the limit
find public -type f -size +25M | grep . && { echo "ERROR: files over 25 MiB remain"; exit 1; } || true

npx wrangler pages deploy public --project-name "$PROJECT" --branch "$BRANCH" --commit-dirty=true
echo ""
echo "Preview (branch alias): $BASEURL"
