# Vault Map — Visualize and Audit Your SOT's Structure

## The problem

A file-based SOT grows relationally: core files, person files, entity files,
workstream files, all cross-referencing each other. The prose enforces the
discipline ("→ see entities/acme.md §Renewal") — but nothing *audits* it.
Over months, three failure modes creep in silently:

1. **Orphans** — a file exists but nothing points to it anymore. Is it
   resolved (archive it) or forgotten (a gap)?
2. **Declared-vs-actual drift** — your index/router file *says* two files
   relate ("this person owns that entity"), but neither file actually
   references the other. The map in your head and the map on disk disagree.
3. **Invisible staleness** — a file about an active topic quietly ages past
   your freshness threshold while attention is elsewhere.

## Why not Obsidian (or any generic graph tool)?

We tried this thought experiment and rejected it. A generic tool only knows
one relationship: *file links to file* — and usually only via its own
`[[wikilink]]` syntax, which would force you to rewrite your files to fit
the tool. Your SOT knows much more:

| Your SOT's semantic layer | What a purpose-built lens does with it |
|---|---|
| Status markers (red/orange/yellow/green) | Node size = open-item heat |
| "Last Updated" dates + version footers | Staleness rendered visually (aged ring) |
| Prose cross-refs in YOUR convention | Real edges, zero file changes |
| The index file's cross-reference matrix | **Declared-vs-actual audit** — the killer feature |
| Tier structure (core / operational / cold) | Radial layout that mirrors your architecture |

**Principle: don't change the files to please a tool.** A ~350-line script
that understands your conventions beats a powerful generic tool that doesn't.
The SOT stays the source; the visual is just a rendering.

## What the script does

`vault_map.py` (in `tools/`) — Python 3, zero dependencies, **read-only**.

**Audit report (stdout), six sections:**
1. **Orphans** — files with no inbound references
2. **Islands** — files with no links in either direction
3. **Declared-vs-actual** — relationships your index file declares (any table
   row mentioning two files of different types) where neither file actually
   references the other
4. **Staleness** — no date newer than N days (default 14)
5. **Heat concentration** — which files carry the most open red/orange items
6. **Hub density** — most-referenced files (your bloat/consolidation signal)

**Interactive map (`vault_map.html`)** — self-contained, no CDN, opens from
disk. Deterministic radial layout (core center, tiers in orbits — no physics
simulation to fight). Node size = heat, dashed ring = stale, click to
highlight a file's neighborhood, scroll/drag to zoom/pan.

> Layout lesson learned the hard way: force-directed physics looks great in
> demos and produces an unreadable exploded hairball on real vaults. A
> deterministic radial layout that mirrors your tier architecture is stable,
> legible, and means the map looks the same every run — which matters when
> you're comparing week over week.

## Security note

The HTML renders your vault's content — names, numbers, whatever is in your
files. **Keep it local. Never deploy it to shared hosting.** The script never
writes to your vault files.

## Cadence

Run it at your weekly quality review. The audit output is machine-checkable —
your AI partner can act on it directly ("2 declared-vs-actual gaps, 2 stale
active files — fix now or queue?"). First run on a mature 28-file vault
caught 6 declared-vs-actual gaps, 2 of which were real errors in the index
file (a stale ownership row) — proof the audit works on day one.

## Setup

1. Copy `tools/vault_map.py` into your vault (e.g., `vault/tools/`)
2. Edit the CONFIGURE block: your core/on-demand/cold filenames, operational
   directory names, index filename, exclusions
3. `python3 tools/vault_map.py` — read the audit, open the HTML
