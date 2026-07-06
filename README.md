# Advanced Context Infrastructure (ACI)

> **"The AI doesn't forget. The AI doesn't hallucinate about what happened. The AI maintains itself."**

An open-source, battle-tested framework for building persistent context infrastructure for AI assistants. Born from **40+ production sessions** managing complex operations (org transitions, multi-stakeholder programs, incident response, cross-functional initiatives) with AI as a true partner — not a one-off chat.

The core insight: **AI assistants are only as good as their context.** Most people treat AI like a search engine — ask a question, get an answer, start over. This framework treats AI like a colleague — one who remembers everything, maintains their own notes, flags when something seems wrong, and gets better every day.

**New in v2:** the framework's organizing principle is now explicit — **know which parts of your system are deterministic and which are probabilistic, and label them.** Content is passive; rules and agents fire against it; every rule has a tier; failures get hardened down the ladder. See [The D/P Principle](#the-dp-principle-v2) below.

---

## The Problem

- AI sessions start from zero every time
- Context gets lost between sessions
- Facts go stale without anyone noticing
- Contradictions accumulate silently
- Rules you wrote down quietly stop being followed (**drift** — the failure mode nobody talks about)
- The more complex your work, the worse all of it gets

---

## The Solution: Three-Level Architecture

### Level 1: Single File (Start Here)

One markdown file. Everything in one place. Works for simple use cases (1–3 active projects, few stakeholders).

**When to use:** You're just getting started, or your work is focused on a single domain with limited moving parts.

### Level 2: Multi-File (Growing Complexity)

4–7 specialized files. Each answers a different question. Cross-referenced. Works for moderate complexity (5–10 active projects, multiple stakeholders, recurring meetings).

**When to use:** Your single file is getting unwieldy (500+ lines), you're losing things, or you need to separate "who" from "what" from "how."

### Level 3: Relational Architecture (Full Scale)

Core files (always loaded) + Operational Index (router) + Entity Files (on-demand) + Document Registry (intake) + Action Tracker (canonical open-items list). Three-tier memory (Active → Seeds → Deep). Self-correcting (Tenth Man + Kaizen). Structurally audited (Vault Map). Works for high complexity (10+ projects, large teams, multiple domains, strategic + operational work simultaneously).

**When to use:** You're managing across domains, your Level 2 files are bloating, and you need the AI to be selective about what it loads.

---

## The D/P Principle (v2)

The maturity leap in this framework isn't more files — it's **explicitly separating deterministic from probabilistic behavior** across everything that runs.

**Your vault's content files are passive repositories.** They don't fire anything. Rules, actions, and agents fire *against* them — and every one of those belongs to one of three tiers:

| Tier | What it is | Failure mode | Fix class |
|------|-----------|--------------|-----------|
| **D — Deterministic** | Code: scripts, queries, pollers, thresholds | Bugs | Patch once, fixed forever |
| **DP — Deterministic spec, Probabilistic executor** | A hard rule in prose, executed by an LLM | **Silent drift** | Tighten the spec, add a verify step, or harden to D |
| **P — Probabilistic** | Judgment, synthesis, drafting, scoring | "Almost right" | Calibrate, and always review |

The **DP tier is where most of your rules live and most of your failures happen** — the rule stays written down while adherence quietly erodes. The framework's answer is the **hardening ladder**: when a probabilistic behavior fails twice, harden it one tier down. Push mechanical work into code; keep judgment at the top. Probabilistic interprets; deterministic executes and verifies.

**→ Full guide: [`guides/deterministic-vs-probabilistic.md`](guides/deterministic-vs-probabilistic.md)** — the three tiers, the hardening ladder, real production failure stories, and how to tag every rule in your quality contract.

---

## Key Concepts

### Memory Tiers

| Tier | Description | Loaded At Start? | Update Frequency |
|------|-------------|-----------------|------------------|
| **Active Memory** | Current state, priorities, hot items | Always | Every session |
| **Seeds** | Compressed summaries of completed/stable items. 60% smaller, 100% fidelity. | Always (compact) | When items stabilize |
| **Deep Memory** | Full detail behind seeds. Cold storage. | Never | On retrieval only |

### Self-Correction Layer

- **Tenth Man Rule** — Every session, the AI audits its own context: staleness, contradictions, gaps, changed truths, cascade risks. Based on the Israeli intelligence principle: when everyone agrees, someone must dissent. *(Tier: DP — right-size it: fast triage at session start, full audit weekly.)*
- **Kaizen Engine** — End-of-day continuous improvement. "What should we do differently tomorrow?" Evidence-based, never auto-executes. *(In D/P terms: Kaizen IS the hardening ladder in motion — its log becomes a record of P→DP→D migrations.)*
- **Vault Map** — A purpose-built structural auditor (working tool included in `tools/`): orphans, islands, declared-vs-actual relationship gaps, staleness, heat, hub density — plus an interactive local map. *(Tier: D — the audit never lies.)*

### Operational Index (Level 3)

A routing table: "Given what I'm doing right now, which files should I load?" Prevents loading everything every time. Keeps sessions fast and focused. Its cross-reference matrix doubles as the **declared-relationship source** the Vault Map audits against.

### Document Registry (Level 3)

Intake system for new information. Every document that arrives gets cataloged: what is it, where does it live, what actions are needed, is it the canonical source?

### Action Tracker (Level 3)

A single canonical list of every open action item, surfaced at the start of every session. Before this file exists, actions scatter across priority tables and hide inside session-log prose — and items silently slip. New actions are added the moment they're captured; closed items archive after one session.

### Signal Scan (Level 3)

Most AI context systems are *pull* — you ask, the AI answers. The Signal Scan adds a *push* layer: at session start, the AI proactively reviews your communication channels and surfaces what's relevant to your current priorities, before you have to know to look. **Your SOT priorities ARE the relevance filter** — no separate interest profile to maintain. *(Hybrid by design: collection can be deterministic — see the poller pattern in the guide — while relevance scoring stays probabilistic.)*

### Output Contracts

The steps of your session ritual say *what to gather*; an **output contract** says *what the human actually sees* — a required structure plus an explicit quality bar. Without one, your best-ever session is one lazy session away from regressing into raw tool dumps. Pairs with the **write-verification mandate**: the AI may never claim an external write is "done" until it reads the target back and confirms the change landed. → [`guides/output-contract.md`](guides/output-contract.md)

---

## Performance Data (Real-World)

| Metric | Level 2 (flat) | Level 3 (relational) | Improvement |
|--------|----------------|---------------------|-------------|
| Lines loaded at session start | ~4,100 | ~1,240 | −70% |
| Time to first useful output | Slow (full parse) | Fast (core + route) | ~3x faster |
| Scaling cost (new entity) | O(n) — grows existing files | O(1) — new file + index entry | Constant |
| Document retrieval | Grep + hope | Registry search | Deterministic |
| Structural integrity | Trust + memory | Vault Map audit | Machine-checked |

First run of the Vault Map audit on the mature source vault (28 files, ~200 cross-references): zero orphans and zero islands — the cross-reference discipline held — but **6 declared-vs-actual gaps, 2 of which were real errors** in the index file. The audit pays for itself on day one.

---

## 13 Lessons Learned (40+ Sessions)

1. **Documentation is load-bearing infrastructure** — not optional
2. **If you explained it twice, write it down**
3. **Stale specs are worse than no specs** — update in the same session as changes
4. **One canonical location per fact** — cross-reference everywhere else
5. **Date everything, version everything, flag staleness**
6. **The system must be auditable** — "where does this fact live?" should have exactly one answer
7. **Memory quality > file size** — don't optimize for minimum, optimize for effectiveness
8. **Progressive adoption works** — start Level 1, upgrade when pain appears
9. **Self-correction is non-negotiable** — without Tenth Man, context rots silently
10. **Compression must preserve the whole** — over-fragmenting destroys coherence
11. **A single action tracker beats scattered to-dos.** When open actions live across multiple priority tables and session notes, the *feeling* of "I'm missing something" is usually correct. One canonical, session-surfaced action file fixes it.
12. **Push beats pull for the things you'd otherwise miss.** A pull-only system only surfaces what you think to ask about. A session-start Signal Scan surfaces what you didn't know to look for — which is exactly where things fall through.
13. **Purpose-built beats generic for visualization — because your SOT's semantics ARE the map.** We evaluated pointing Obsidian at the vault and rejected it: a generic graph only knows "files link to files," and demands its own link syntax. Your vault already encodes status heat, freshness, tiers, and *declared* relationships. A ~350-line read-only script renders all of that AND audits declared-vs-actual structure — the drift a generic tool can't even see. Never change your files to please a tool.

---

## Repository Structure

```
├── README.md                        # This file
├── templates/                       # Ready-to-use template files
│   ├── level-1-single-file.md       # Single-file SOT template
│   ├── level-2-source-of-truth.md
│   ├── level-2-people.md
│   ├── level-2-projects.md
│   ├── level-2-recipes.md
│   ├── level-2-quality.md
│   ├── level-3-operational-index.md
│   ├── level-3-document-registry.md
│   ├── level-3-action-tracker.md    # Canonical open-actions list
│   ├── level-3-entity-template.md
│   └── level-3-deep-memory.md
├── guides/                          # Detailed how-to guides
│   ├── getting-started.md           # Zero to working SOT in one session
│   ├── level-2-setup.md             # When and how to upgrade to Level 2
│   ├── level-3-migration.md         # When and how to upgrade to Level 3
│   ├── deterministic-vs-probabilistic.md  # ★ v2 organizing principle: D / DP / P tiers + hardening ladder
│   ├── output-contract.md           # Freeze your best session; verify every external write
│   ├── tenth-man.md                 # Self-correction layer deep dive
│   ├── kaizen.md                    # Continuous improvement engine
│   ├── memory-tiers.md              # Active → Seeds → Deep memory
│   ├── session-ritual.md            # Start/end session protocol
│   ├── action-tracker.md            # The canonical open-actions list
│   ├── signal-scan.md               # Proactive message surfacing at session start
│   └── vault-map.md                 # Purpose-built vault visualizer + structural audit
├── tools/
│   └── vault_map.py                 # Working visualizer/auditor (zero-dependency Python)
├── examples/                        # Real-world examples by persona
│   ├── manager.md                   # Manager with 5+ direct reports
│   ├── consultant.md                # Multi-client engagement
│   ├── founder.md                   # Product + sales + ops + fundraising
│   └── program-manager.md           # Cross-functional initiatives
└── LICENSE                          # Apache 2.0
```

---

## Who This Is For

- **Managers** with 5+ direct reports and multiple workstreams
- **Consultants** managing multiple client engagements
- **Founders** juggling product, sales, ops, and fundraising
- **Program managers** tracking cross-functional initiatives
- **Anyone** whose AI assistant context has outgrown a single file

---

## Platform Compatibility

This framework is platform-agnostic. It works with any AI assistant that can read local files:

- [Goose](https://github.com/block/goose) (open-source AI agent)
- Claude (via Projects or file upload)
- ChatGPT (via file upload or memory)
- Cursor / Windsurf / other code editors with AI
- Any MCP-compatible tool

---

## Quick Start

1. Copy `templates/level-1-single-file.md` to your working directory
2. Fill in the sections with your current context
3. At the start of every AI session, tell your assistant to read the file
4. At the end of every session, ask your assistant to update it
5. When it gets unwieldy (~500+ lines), upgrade to Level 2
6. As rules accumulate, tag each one **D / DP / P** — and let your weekly review ask which DP rules are ready to harden down the ladder

---

## Philosophy

> "89.6% of AI tokens are wasted re-reading context that could be managed."

The average AI conversation wastes most of its capacity re-establishing context that was already known. This framework eliminates that waste by giving the AI a persistent, structured, self-maintaining memory system.

And as the system matures, the philosophy sharpens: **probabilistic AI interprets and judges; deterministic infrastructure executes and verifies.** The AI becomes a true partner — not a stranger you brief from scratch every time, and not a black box you have to blindly trust either.

---

## Contributing

PRs welcome. If you've built a context system that works, share what you learned — especially examples of the hardening ladder in action (P → DP → D migrations from your own practice).

---

## License

Apache 2.0

---

## Author

**Aaron Blonquist** — built across 40+ production sessions managing complex global operations at scale.
