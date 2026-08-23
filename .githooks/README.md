# Hooks, tracked

`.git/hooks/` is **not tracked by git and is not cloned.** A guard that lives only there is
one `rm -rf .git` or one fresh clone away from silently disappearing — and nothing announces
its absence. These are the same hooks, kept in the repo so they survive.

## Activate them (once per clone)

    git config core.hooksPath .githooks

**That config line is itself local and untracked.** Tracking the hook file removes one failure
mode, not both. The durable version of `pre-push` is a **branch-protection rule on GitHub**,
which cannot be lost on a laptop.

## What each does

| hook | what it does |
|---|---|
| `pre-push` | **Refuses to push `main`** without `CFM_PUBLISH_AUTHORISED="kymber-said-yes"`. Feature branches are untouched. |
| `pre-commit` | Blocks a commit touching more than 5 `content/week` files — mass regeneration. `--no-verify` overrides. |
| `post-commit` | Rebuilds the Obsidian code index. |

## Why `pre-push` exists

`cfm-corner-site`, `cfm-corner-staging` and `cfm-week34` are **three worktrees on one `.git`**,
one object store, one remote. `git push origin main` needs no checkout, so **any of the three
publishes the live site** even though only staging has main checked out.

Kymber's standing rule: *"I do not want anything pushed live until I have reviewed and
authorized it."* Before this hook, that hold was three sessions each choosing correctly, every
time, forever.

**And `draft:` does not gate `static/`.** Files under `static/` are served directly, so a
fragment there publishes at a public URL the moment main lands. Found by fieldguide while
declining to clear three commits that were not theirs.

## Prove it can refuse

    .githooks/pre-push --self-test

A guard that has only ever been seen to allow is not known to work.
