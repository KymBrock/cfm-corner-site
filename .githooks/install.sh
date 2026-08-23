#!/bin/sh
# Copy the tracked hooks into the live hooks directory.
#
# WHY A COPY AND NOT core.hooksPath: all three cfm worktrees pin core.hooksPath to the
# ABSOLUTE path of cfm-corner-site/.git/hooks, and they sit on DIFFERENT BRANCHES. A relative
# hooksPath resolves per-worktree, so pointing them at `.githooks` would break hooks on any
# worktree whose branch does not yet carry this directory. Copying keeps one installed set
# that works from all three, with a tracked source that survives a clone.
set -e
HOOKS="$(git rev-parse --git-common-dir)/hooks"
SRC="$(cd "$(dirname "$0")" && pwd)"
for h in pre-push pre-commit post-commit; do
  [ -f "$SRC/$h" ] || continue
  cp "$SRC/$h" "$HOOKS/$h"
  chmod +x "$HOOKS/$h"
  echo "  installed $h -> $HOOKS/$h"
done
echo
"$HOOKS/pre-push" --self-test
