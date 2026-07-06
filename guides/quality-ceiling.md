# The Quality Ceiling — Optimizing for Correctness, Not Tokens

## The decision most frameworks made for you

Every commercial memory layer optimizes token efficiency. They have to —
they serve thousands of customers' cost curves, and benchmarks reward
retrieving less, faster, cheaper.

You are not a platform. You are one person (or one team) whose real costs
are **wrong facts in production**: the misremembered commitment, the stale
number in an executive email, the rule that quietly stopped being followed.
Against those costs, tokens are nearly free.

**The Quality-Ceiling doctrine: verification is a first-class spend.**
Spend context, spend passes, spend background compute — on being right.

## The five operating rules

### 1. Latency ≠ tokens

Don't confuse the two budgets. The *interactive* path (session start, live
questions) should stay fast — that's the human's time. The *quality* spend
goes into depth that doesn't block anyone: background audits, delegated
deep scans, second passes that run while the human works.

### 2. Second-pass audit on high-stakes artifacts

Any artifact with real blast radius — an executive email, an external
document, a financial figure, a report others will act on — gets an
independent verification pass before handover:

> Re-read the artifact as if you did not write it. Check every number,
> name, date, and claim against the vault's canonical source. Report
> "second-pass verified" or list what you corrected.

This is agent-checks-agent in miniature. It costs one extra pass. It
catches the class of error that costs trust.

### 3. Count defects — don't just feel them

Keep a small defect log with three classes, reviewed weekly:

| Class | Definition |
|---|---|
| **ESCAPE** | An error the human caught that the AI didn't |
| **DRIFT** | A written rule that degraded in execution |
| **STALE** | Staleness found at audit (your structural tool's count) |

Each entry: date, what happened, root cause, and whether it was *hardened*
(a permanent fix down the D/P ladder) or just corrected. The trend line is
your real benchmark — **defect rate in production use** — and it's more
meaningful for a curated vault than any retrieval leaderboard.

### 4. Full audit depth as a background job

Session-start audits should be fast triage. But once a week, run the FULL
audit — every file, every cross-reference, provenance sweep, contradiction
scan — as a delegated or background task. Depth without blocking.

### 5. Fidelity beats size, everywhere

When compressing (seeds, summaries, archives): 100% fidelity is the
constraint, compression is the bonus. Never trade a name, a number, a date,
or a link for brevity. A compact summary that loses one load-bearing fact
is more expensive than the tokens it saved.

## Deterministic quality checks (the tooling)

Prose rules like "always cite your source" are DP-tier — exactly specified,
LLM-executed, drift-prone. The vault-map tool (`tools/vault_map.py`)
hardens three of them to D-tier:

- **Provenance audit** — flags material claims (currency amounts,
  percentages, headcounts) in operational files that carry no visible
  source signal. Heuristic by design; tune the patterns to your house
  citation style.
- **Temporal validity** — flags `SUPERSEDED` markers and expired
  `valid-until: YYYY-MM-DD` tags so outdated facts can't lurk in active
  files. (Convention: mark superseded facts inline instead of deleting
  them silently — the audit keeps you honest about cleanup.)
- **Cross-file conflict candidates** — flags the same entity appearing
  with diverging numbers across files. Expect noise; the point is a cheap
  weekly sweep that surfaces the one real contradiction among the false
  positives.

Run all three at the weekly review. Machine-run checks never get tired,
never skip a step, and never convince themselves it's probably fine.

## Why this is a competitive position, not just hygiene

A framework that optimizes tokens converges on: retrieve less, trust the
store, never re-check. A framework that optimizes quality converges on:
load what matters, verify what's load-bearing, audit continuously. These
produce different systems. The second one is what you want when the vault
runs your actual work — because the most expensive token is the one that
was wrong.
