# Multi-Agent Vault — One Memory, Many Agents

## The problem everyone is trying to solve

A new category of tools has emerged to answer: *"Agent A knows something —
how does Agent B find out?"* Start a task in one coding agent, continue in
another. Ask what a teammate's agent is doing. The commercial answers are
sync daemons, cloud context stores, and session-capture APIs.

**The file-based vault already solves this — with zero infrastructure.**

If every agent reads the same vault at session start and writes back
through the same ritual, the vault *is* the sync layer. There is no daemon,
no API key, no cloud service holding your context, and nothing to break.
Agent portability is a *property* of file-based memory, not a feature you
buy.

```
        Agent A (daily ops)      Agent B (deep project)     Agent C (scheduled)
              │                        │                          │
              ▼                        ▼                          ▼
        ┌─────────────────────────────────────────────────────────────┐
        │                     THE VAULT (markdown files)              │
        │   core files · index · entities · workstreams · tracker     │
        └─────────────────────────────────────────────────────────────┘
```

Any agent that can read local files participates: different models,
different vendors, different tools, same memory. Switching agents costs
nothing because the memory never lived inside the agent.

## The rules that make it safe

Shared memory without coordination rules produces conflicts and context
poisoning. Four rules, learned in production:

### Rule 1 — Partition write ownership by file

Two agents must never both own writes to the same file. Partition by
domain: the deep-project agent owns the project workstream files; the daily
agent owns everything else. Reads are unrestricted — everyone reads
everything relevant.

### Rule 2 — One agent owns the master action list

Actions are the highest-collision surface. Designate exactly one agent as
the **catch-layer**: it maintains the canonical action tracker for ALL
items regardless of which agent's session captured them. Other agents
surface actions *to* it (or to the human), never write the tracker
directly.

> Production example: a deep, high-volume project was deliberately moved to
> a second agent instance so it couldn't crowd out daily operations. The
> boundary that made it work: *the daily agent holds the master action
> tracker — all actions regardless of origin; the project agent does
> project depth only.* Actions discovered in project sessions flow to the
> master tracker via the human or a handoff note.

### Rule 3 — Scope the specialist agents narrowly

The deep-project agent gets the project directory and its workstream file —
not the whole vault. This is the operational index's routing logic applied
to agents: load what the job needs. A narrow agent can't corrupt files it
never opens, and its context window stays dedicated to its job.

### Rule 4 — Same quality contract for every writer

Any agent that writes to the vault follows the same rules: update version
footers, verify external writes, flag staleness, never duplicate canonical
facts. The vault's integrity comes from the ritual, not from which agent
runs it. If an agent can't follow the contract, it gets read-only access.

## Why not a sync service?

Context-sync services solve portability by **centralizing your context in
someone else's infrastructure** — a daemon captures agent sessions and
ships them to a cloud API. That's a reasonable trade for ephemeral coding
sessions. It's the wrong trade for a knowledge vault:

| | Sync service | File-based vault |
|---|---|---|
| What syncs | Raw session transcripts | Curated, verified knowledge |
| Trust required | Cloud provider + API keys | None — local files |
| Curation | None (capture is the product) | Session ritual + self-correction |
| Sensitive work | Your context leaves the machine | Never leaves the machine |
| Failure mode | Service/daemon outage | None — files don't go down |

The deeper issue is **quality**: automatically accumulated raw context is
unaudited context. Two agents sharing a growing pile of transcripts share
each other's mistakes. Two agents sharing a curated vault share verified
truth — because everything in the vault passed through the ritual (session
updates, Tenth Man audit, seeding) before it became "memory."

Accumulation is cheap. Curation is the product.

## Versioning: make the history deterministic

Version footers in prose are maintained by the LLM — exact in
specification, drift-prone in execution (a DP-tier rule; see
`deterministic-vs-probabilistic.md`). Harden the history one tier down:

```bash
cd your-vault && git init          # LOCAL ONLY — add no remote
git add -A && git commit -m "baseline"
# then: commit at every session close
```

A local git repo (no remote — the vault contains your most sensitive
context) gives you deterministic diffs, time-travel, and structure-audit
comparisons week over week, for free. Keep the prose footers for human
narrative; git is the layer that never lies.

**Session-close addition:** `git add -A && git commit -m "Session N —
one-line summary"`. That's the whole discipline.

## Minimum viable adoption

1. Decide your agent roster (start with one; add a second only when a
   domain is heavy enough to crowd out daily work)
2. Write the partition into your operational index: which agent owns which
   files, who is the catch-layer
3. `git init` the vault, local only
4. Every agent gets the same boot instruction: read the core files, follow
   the ritual, respect the partition
