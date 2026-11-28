#!/bin/sh
# ── B1 CONTENT CHECK, GitHub deploy step (stage 3) ──────────────────────────────
# The same checker, host list and shared reader as the local pre-push hook. These public
# copies differ from the hook's pinned files only in comments, docstrings, one printed
# label and the reader's unused default list path; the checks they run are identical.
# The hook can be skipped with `git push --no-verify`; this step cannot be skipped from a
# computer, because the deploy job needs it to pass.
#
# Usage:  sh scripts/b1/ci_content_check.sh <tree> <github.event.before> <last-deployed>
#   <tree>           the commit being deployed (github.sha)
#   <event.before>   what main pointed at before this push (empty on a manual run)
#   <last-deployed>  the head commit of the last deploy run that SUCCEEDED
#
# THE BASE. The checker compares <tree> against a base, as the hook compares against the
# remote sha. The base is the LAST DEPLOYED commit. In a normal push that is the same commit
# as github.event.before. They differ only when commits reached main and were never
# deployed (a refused deploy, a cancelled queued run). Then event.before would let those
# commits through unchecked on the next push, so the step checks from the last deployed
# commit and says so. A run with no base would scan every page and always fail on her
# Digital Tools reference, so no base means cannot vouch.
#
# Exit: 0 pass · 1 refused on findings · 2 cannot vouch. Any non-zero stops the deploy.
set -u

readonly CC_CHECKER="scripts/b1/prepublish_content_check.py"
readonly CC_SHA="bb393227afbcf55c"
readonly CC_HOSTS="scripts/b1/approved_hosts.json"
readonly CC_HOSTS_SHA="a852627a126b474b"
readonly CC_READER="scripts/b1/lesson_release_gate.py"
readonly CC_READER_SHA="d450659d70751465"
readonly ZERO="0000000000000000000000000000000000000000"

sha16() { { sha256sum "$1" 2>/dev/null || shasum -a 256 "$1" 2>/dev/null; } | cut -c1-16; }
cannot_vouch() {
  printf '\n  REFUSED: the content check could not vouch for this deploy (exit 2).\n  %s\n  Nothing was deployed. This is not a finding about the pages.\n\n' "$1" >&2
  exit 2
}

tree="${1:-}"; before="${2:-}"; last="${3:-}"
[ -n "$tree" ] || cannot_vouch "No commit to check was given."
[ "$before" = "$ZERO" ] && before=""
[ -n "$last" ] || cannot_vouch "No earlier successful deploy was found to compare against."

[ "$(sha16 "$CC_CHECKER")" = "$CC_SHA" ] || cannot_vouch "The checker is missing or changed (expected $CC_SHA)."
[ "$(sha16 "$CC_HOSTS")" = "$CC_HOSTS_SHA" ] || cannot_vouch "The host list is missing or changed (expected $CC_HOSTS_SHA)."
# The reader's pin is checked by the checker itself (--ash-sha), exactly as in the hook.

echo "B1 content check: tree $tree"
echo "  base = last deployed $last"
if [ -n "$before" ] && [ "$before" != "$last" ]; then
  echo "  github.event.before is $before, which differs from the last deployed commit."
  echo "  These commits reached main without being deployed, so they are checked too:"
  git log --oneline "$last..$tree" 2>/dev/null | sed 's/^/    /'
elif [ -z "$before" ]; then
  echo "  no github.event.before (a manual run, or main was just created): checking everything since the last deploy"
fi

# -I as in the hook; -B so loading the reader leaves no __pycache__ in the checkout.
python3 -I -B "$CC_CHECKER" --hosts "$CC_HOSTS" --ash-reader "$CC_READER" --ash-sha "$CC_READER_SHA" \
  --repo . --tree "$tree" --base "$last" </dev/null
rc=$?
if [ "$rc" -eq 1 ]; then
  printf '\n  REFUSED: the content check found problems in the pages this deploy would publish.\n  Nothing was deployed. Fix the pages listed above and push again.\n  Kymber'"'"'s go-ahead does not override this check.\n\n' >&2
  exit 1
elif [ "$rc" -ne 0 ]; then
  cannot_vouch "It could not read what the deploy would publish, or a pinned file is missing or changed (exit $rc)."
fi
exit 0
