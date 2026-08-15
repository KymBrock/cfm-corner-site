# Session continuity


> **Rescued to `main` 2026-08-15.** This convention was decided 2026-07-26 and committed
> in `2ed6617`, which is not an ancestor of `main` — so it has been invisible to every
> session working where lessons are built. Text below is verbatim. (Fable audit K7.)

## Narration script location — CONVENTION (decided 2026-07-26)

Narration scripts live in **both** places, kept in sync:
- **Vault** (canonical): `~/Obsidian/K Master Vault/.../Culture/<Guide>/_narration/<slug>.script.md`
- **Repo**: `docs/narration/<guide>/<slug>.script.md`

The vault is where the Narration Studio run reads from; the repo copy is for easy find/edit
(e.g. github.dev from a phone). Edit one, update the other. 05b lives on the calendar branch
(PR #2) in the repo until that PR merges.
