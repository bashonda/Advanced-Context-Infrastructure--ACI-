# ACI vs. the Field — An Honest Comparison

*Last updated: 2026-07. We did this scan on ourselves before claiming anything.
Corrections welcome via PR — an inaccurate comparison row is a bug.*

## The four classes of "AI memory" in 2026

| Class | Representative tools | What they optimize |
|---|---|---|
| **Memory APIs / knowledge-graph engines** | Letta (MemGPT), Zep (Graphiti), Mem0, cognee | Retrieval accuracy, token efficiency, temporal reasoning |
| **Session-sync services** | UltraContext | Cross-agent portability of raw session context |
| **Governed / auditable memory** | Engram, Shomei, Bilinc | Provenance, tamper-evidence, contradiction detection |
| **File-based agent context** | Cline Memory Bank, CLAUDE.md / AGENTS.md, Basic Memory — **and ACI** | Persistent, human-readable context in files |

## Where ACI wins

**1. It's a methodology, not just storage.** Every other file-based approach
ships a file structure (Cline's six files, CLAUDE.md conventions). None ship
the *discipline*: session ritual, self-correction audits, continuous
improvement loop, output contracts, write verification, seeding rules,
structural audit tooling. Structure without ritual rots — that's not a
slogan, it's the documented failure mode the ritual exists to prevent.

**2. Multi-agent memory with zero infrastructure.** The documented limitation
of agent-centric memory frameworks is cross-agent sharing. Sync services
solve it with a daemon and a cloud API. A file vault + coordination rules
(see `guides/multi-agent-vault.md`) solves it with nothing — any agent that
reads files participates.

**3. The D/P taxonomy.** No framework in any class addresses the
deterministic-spec/probabilistic-executor drift problem — what happens when
an LLM is the thing executing your rules. ACI names it, tags every rule,
and provides the hardening ladder. This is the layer the memory APIs can't
see because they don't operate at the rules layer at all.

**4. Quality over token efficiency — deliberately.** Memory products
optimize token cost because they serve customers' cost curves. ACI's
position: **verification is a first-class spend.** Second-pass audits on
high-stakes outputs, read-back verification on every external write,
weekly structural audits. Tokens are cheap; a confidently wrong answer in
production is not. (See `guides/quality-ceiling.md`.)

## Where the field is ahead — honestly

**1. Deterministic provenance.** Governed-memory tools (Engram, Bilinc)
enforce provenance *architecturally* — cryptographic trails, verified
writes, rollback. ACI's cite-the-source rule was prose executed by an LLM
(DP-tier, drift-prone). **Our answer:** `tools/vault_map.py` now includes
deterministic provenance, temporal-validity, and cross-file-conflict
audits — heuristic, not cryptographic, but machine-run and honest about it.
If you need tamper-evidence for compliance, use a governed-memory product;
ACI's audits are for self-correction, not adversarial proof.

**2. Retrieval benchmarks.** The memory APIs compete on benchmark scores
(e.g., LoCoMo). ACI has no benchmark scores because it measures a different
thing: **defect rate in production use** (escapes, drift incidents,
staleness at audit — see the quality-ceiling guide's defect log). We report
our own longitudinal numbers instead of a leaderboard position. If your
use case is high-volume conversational recall, a vector/graph memory API
may genuinely serve you better — and can sit *underneath* an ACI vault as
a retrieval layer.

**3. Temporal knowledge graphs.** Zep tracks fact validity over time as a
first-class query. ACI's equivalent (supersession markers + git history +
the vault-map temporal audit) reconstructs validity rather than querying
it. Convention adopted: mark superseded facts inline (`SUPERSEDED by X`)
and date-bound facts (`valid-until: YYYY-MM-DD`) — the audit flags expired
ones. Lighter than a graph engine; sufficient for a curated vault.

## The one-sentence positioning

> Memory products make context **bigger and cheaper to retrieve. ACI makes
> it TRUE** — curated, audited, versioned, and owned by you — and lets any
> agent you'll ever use read it.

Accumulation is cheap. Curation is the moat.
