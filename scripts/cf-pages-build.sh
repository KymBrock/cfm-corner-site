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

# EVERY Cloudflare build is the STAGING SITE — drafts included, on every branch.
#
# This used to special-case main and build it without drafts, as a mirror of
# production. That left staged work with nowhere to be seen: content on main
# marked draft:true appeared on neither the public site nor any preview, so the
# only way to read a staged lesson was a local `hugo -D`. The /pipeline/
# dashboard — which exists precisely to show what is drafting, in review, ready
# or live — was invisible for the same reason.
#
# Changed 2026-08-15 so that staged content lives on main and is visible here
# while it is being built. The alternative, a long-lived staging branch tracking
# main, reintroduces the divergence that let a branch reach 336 files.
#
# PRODUCTION IS UNAFFECTED. Readers are served by GitHub Pages from main via
# deploy.yml, which builds WITHOUT drafts and never loads config-preview.toml.
# The smoke-test value is retained: a build error still fails here first, and
# building with drafts exercises strictly more of the site than without.
hugo -D --minify --baseURL "$CF_PAGES_URL/" --config hugo.toml,config-preview.toml

npx pagefind@latest --site public

# Keep every *.pages.dev build out of search engines; the canonical site
# is www.cfmcorner.com via GitHub Pages.
printf 'User-agent: *\nDisallow: /\n' > public/robots.txt
printf '/*\n  X-Robots-Tag: noindex\n' > public/_headers
