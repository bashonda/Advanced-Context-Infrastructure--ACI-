# Advanced Context Infrastructure (ACI)

> **"The AI doesn't forget. The AI doesn't hallucinate about what happened. The AI maintains itself."**

**Give any AI assistant a persistent, self-maintaining, self-auditing memory — using nothing but markdown files on your machine.** No daemon, no API keys, no cloud service, no vendor. Born from **40+ production sessions** running complex global operations with AI as a true partner, not a one-off chat.

## 2-Minute Start

```bash
# 1. Grab the starter file
curl -O https://raw.githubusercontent.com/bashonda/Advanced-Context-Infrastructure--ACI-/main/templates/level-1-single-file.md
mv level-1-single-file.md my-context.md

# 2. Fill in the sections (who you are, priorities, key people) — 10 minutes

# 3. Every AI session, start with:
#      "Read my-context.md before we begin."
#    End every session with:
#      "Update my-context.md with what changed today."
```

That's the whole loop. Your AI now remembers. Everything else in this repo — the multi-file architecture, the self-correction audits, the structural tooling — is what to add **when you feel specific pain**, and each addition tells you which pain it fixes.

**Works with anything that reads files:** [Goose](https://github.com/block/goose), Claude, ChatGPT, Cursor, Windsurf, any MCP-compatible tool. Switching assistants costs nothing — the memory never lived inside the assistant.

---

## Provenance (or: why a battle-tested framework has a short public history)

This repository is the **architecture of a private production vault**, extracted under its own rule: *ship templates, not your files* ([`guides/fork-and-onboard.md`](guides/fork-and-onboard.md)). The structure, rituals, doctrine, and tooling are intact; the content — people, priorities, decisions — is zeroed. That's why it arrives as clean versioned releases rather than a long public commit graph: the battle-testing happened in the private vault this was distilled from, and its measurements are reported in this README rather than implied by commit count.

**Two homes, one truth:** the canonical repository is [`bashonda/Advanced-Context-Infrastructure--ACI-`](https://github.com/bashonda/Advanced-Context-Infrastructure--ACI-); a maintained mirror lives at [`bashonda2/advanced-context-infrastructure`](https://github.com/bashonda2/advanced-context-infrastructure). Every release pushes to both; if they ever disagree, the canonical repository wins.

---

## Why files? (vs. context-sync services and memory APIs)

A category of tools now exists to make agent context portable: sync daemons, cloud context stores, session-capture APIs, memory layers. They solve portability by **centralizing raw context in infrastructure**. ACI solves it with **curated files and zero infrastructure**. The difference is not cosmetic:

| | Context-sync / memory services | ACI (file-based vault) |
|---|---|---|
| What's stored | Raw session transcripts, auto-captured | Curated, verified knowledge |
| Quality control | None — capture is the product | Session ritual + Tenth Man audit + structural tooling — **curation is the product** |
| Trust required | Cloud provider, API keys, daemon uptime | None — local markdown |
| Sensitive work | Context leaves your machine | Never leaves your machine |
| Agent lock-in | SDK/API integration per agent | Anything that reads files |
| Cost | Subscription/usage | Zero |

The deeper issue is quality: **automatically accumulated context is unaudited context.** An agent drawing on a growing pile of raw transcripts inherits every error in the pile. An agent drawing on a curated vault inherits verified truth — because everything in it passed through a ritual before becoming "memory." Accumulation is cheap. Curation is the moat.

**We scanned the whole field before making claims** — memory APIs (Letta, Zep, Mem0, cognee), sync services, governed-memory tools (Engram, Bilinc), and the other file-based approaches (Cline Memory Bank, CLAUDE.md, Basic Memory) — including where each is honestly ahead of us and what we adopted in response. → [`COMPARISON.md`](COMPARISON.md)

**And one deliberate contrarian stance:** every memory product optimizes token efficiency; ACI optimizes **correctness**. Verification is a first-class spend — second-pass audits on high-stakes outputs, deterministic provenance/contradiction/staleness checks, a production defect log instead of a retrieval benchmark. → [`guides/quality-ceiling.md`](guides/quality-ceiling.md)

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
| **Seeds** | Compressed summaries of completed/stable items — ~60% smaller, with **every decision, commitment, and outcome preserved** (the full deliberation history moves to Deep). | Always (compact) | When items stabilize |
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

### Multi-Agent Vault

The vault is also the answer to "Agent A knows something — how does Agent B find out?" If every agent reads the same vault and writes through the same ritual, **the vault IS the sync layer** — different models, different vendors, same memory, zero infrastructure. Four coordination rules make it safe (partition write-ownership by file; one agent owns the master action list; scope specialists narrowly; same quality contract for every writer). Plus: local `git init` (no remote) as the deterministic versioning layer under your prose version footers. → [`guides/multi-agent-vault.md`](guides/multi-agent-vault.md)

### Fork & Onboard (Teams)

A mature vault separates into **architecture** (transferable) and **content** (personal). Forking = copy the structure, zero the content: a new team member starts from a proven skeleton on day one and supplies only what they uniquely know. Includes the hard case — onboarding someone who just absorbed a departed colleague's scope. Share the *how*, not the *what*. → [`guides/fork-and-onboard.md`](guides/fork-and-onboard.md)

---

## Performance Data (Real-World)

| Metric | Level 2 (flat) | Level 3 (relational) | Improvement |
|--------|----------------|---------------------|-------------|
| Lines loaded at session start | ~4,100 | ~1,240 | −70% |
| Time to first useful output | Full parse of everything | Core + route, load on demand | Tracks the −70% lines-loaded figure (~3×) |
| Scaling cost (new entity) | O(n) — grows existing files | O(1) — new file + index entry | Constant |
| Document retrieval | Grep + hope | Registry lookup | Deterministic — *when the intake ritual is followed (itself a DP-tier rule)* |
| Structural integrity | Trust + memory | Vault Map audit | Machine-checked |

*Method: measurements from the production source vault (one practitioner, 40+ sessions). Lines-loaded is counted directly from the session-start read set; "time to first useful output" is reported via its driver — lines parsed — rather than a wall-clock benchmark.*

First run of the Vault Map audit on the mature source vault (28 files, ~200 cross-references): zero orphans and zero islands — the cross-reference discipline held — but **6 declared-vs-actual gaps, 2 of which were real errors** in the index file. The audit pays for itself on day one.

---

## 16 Lessons Learned (40+ Sessions)

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
14. **Files are the sync layer.** Agent portability and multi-agent memory don't require a service — any agent that reads your vault shares it. Curation (ritual + audit) is what makes shared memory *trustworthy*; accumulation alone just shares the errors around.
15. **Version with git, narrate with footers.** Prose version footers are LLM-maintained and drift; a local git repo (no remote) under the vault gives deterministic diffs and time-travel for free. The hardening ladder applied to versioning itself.
16. **Optimize for correctness, not tokens.** Commercial memory layers minimize token cost because they serve platforms' economics; a personal/team vault's real cost is a wrong fact in production. Spend freely on verification: second passes, read-backs, background audits, defect logging. The most expensive token is the one that was wrong.

---

## Repository Structure

```
├── README.md                        # This file
├── COMPARISON.md                    # Honest scan of the field — where ACI wins, where it doesn't
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
│   ├── vault-map.md                 # Purpose-built vault visualizer + structural audit
│   ├── multi-agent-vault.md         # One memory, many agents — files as the sync layer
│   ├── fork-and-onboard.md          # Scaling the vault to a team
│   └── quality-ceiling.md           # Optimize for correctness, not tokens — defect log + verification spend
├── tools/
│   └── vault_map.py                 # Working visualizer/auditor (zero-dependency Python)
├── examples/                        # Real-world examples by persona
│   ├── manager.md                   # Manager with 5+ direct reports
│   ├── consultant.md                # Multi-client engagement
│   ├── founder.md                   # Product + sales + ops + fundraising
│   └── program-manager.md           # Cross-functional initiatives
└── LICENSE                          # Apache 2.0
```

> **⚠️ The status markers are load-bearing, not decoration.** `tools/vault_map.py` parses the emoji set 🔴 🟠 🟡 🟢 ⏸️ 🧊 for its heat audit and ISO `Last Updated: YYYY-MM-DD` dates for its staleness audit (default threshold: 14 days). Write "RED/GREEN" in prose, or freeform dates, and the structural audit goes blind to those files.

### Guide Map — read them in this order

Fifteen guides is a lot. Enter based on where you are:

| You are... | Read |
|-----------|------|
| Brand new | [`getting-started.md`](guides/getting-started.md), then copy the Level 1 template |
| Outgrowing one file | [`level-2-setup.md`](guides/level-2-setup.md) |
| Scaling to full architecture | [`level-3-migration.md`](guides/level-3-migration.md) · [`memory-tiers.md`](guides/memory-tiers.md) · [`action-tracker.md`](guides/action-tracker.md) |
| Installing the discipline | [`session-ritual.md`](guides/session-ritual.md) · [`tenth-man.md`](guides/tenth-man.md) · [`kaizen.md`](guides/kaizen.md) |
| Hardening against drift | [`deterministic-vs-probabilistic.md`](guides/deterministic-vs-probabilistic.md) · [`output-contract.md`](guides/output-contract.md) · [`quality-ceiling.md`](guides/quality-ceiling.md) |
| Extending the system | [`signal-scan.md`](guides/signal-scan.md) · [`multi-agent-vault.md`](guides/multi-agent-vault.md) · [`fork-and-onboard.md`](guides/fork-and-onboard.md) · [`vault-map.md`](guides/vault-map.md) |

---

## Who This Is For

- **Managers** with 5+ direct reports and multiple workstreams
- **Consultants** managing multiple client engagements
- **Founders** juggling product, sales, ops, and fundraising
- **Program managers** tracking cross-functional initiatives
- **Anyone** whose AI assistant context has outgrown a single file

---

## Platform Compatibility

The framework is markdown files, so any AI that reads files can participate. But the session ritual has a **write-back half** — the AI updates the vault at session end — and that's where platforms genuinely differ:

| Surface | Reads the vault | Writes it back | Ritual support |
|---------|-----------------|----------------|----------------|
| [Goose](https://github.com/block/goose) | ✅ | ✅ | Full |
| Claude Code / Claude Desktop (filesystem access) | ✅ | ✅ | Full |
| Cursor · Windsurf · AI-enabled editors | ✅ | ✅ | Full |
| Any MCP-compatible agent with filesystem access | ✅ | ✅ | Full |
| claude.ai (Projects / file upload) | ✅ | ❌ — you apply its proposed updates yourself | Read + manual write-back |
| ChatGPT (file upload / memory) | ✅ | ❌ — same | Read + manual write-back |

On chat-only surfaces the system still works: the AI proposes the end-of-session updates and you paste them in. But the compounding benefits arrive fastest where the AI can maintain the files itself. If you live in a chat interface, start at Level 1 and keep the write-back burden small.

**"Why not just use built-in memory?"** claude.ai and ChatGPT both ship native memory now, and it's genuinely useful — zero-effort recall. What it can't give you is a memory you can **read, diff, version, audit, and carry between vendors**. Built-in memory is per-app and opaque; a vault is portable, inspectable, git-versioned, shareable across every agent you use, and curated under an explicit discipline. The two compose fine: let built-in memory handle casual recall while the vault remains canon.

---

## Quick Start

1. Copy `templates/level-1-single-file.md` to your working directory
2. Fill in the sections with your current context
3. At the start of every AI session, tell your assistant to read the file
4. At the end of every session, ask your assistant to update it *(on chat-only platforms, apply its proposed updates yourself)*
5. When it gets unwieldy (~500+ lines), upgrade to Level 2
6. As rules accumulate, tag each one **D / DP / P** — and let your weekly review ask which DP rules are ready to harden down the ladder

---

## Philosophy

> **"89.6% of AI tokens are wasted re-reading context that could be managed."**

That figure is **our own measurement, not a borrowed stat**: in a controlled 50-conversation study across 5 work domains, managed context matched frontier-model output quality at ~89% lower token cost (n=50, p<0.001). The average AI conversation spends most of its capacity re-establishing context that was already known. This framework eliminates that waste by giving the AI a persistent, structured, self-maintaining memory system.

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
