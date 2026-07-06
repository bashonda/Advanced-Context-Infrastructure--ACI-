# Level 3 Migration: Scalable Context Architecture

> **When to read this:** Your Level 2 files are each 1000+ lines, you need entity-level files, or new info arrives faster than you can organize it.  
> **Time required:** 2–3 hours to migrate  
> **Outcome:** A scalable architecture with routing, memory tiers, and entity isolation.

---

## Signals It's Time to Upgrade

Level 3 is for power users managing complex, multi-domain operations:

- **Files > 1000 lines each** — Even specialized files are too large to load efficiently
- **Loading everything is slow** — Your AI's context window is being consumed by irrelevant detail
- **Entities need their own files** — A single project or vendor has 200+ lines of context
- **New info arrives faster than you can organize** — You're falling behind on updates
- **You need selective loading** — Not every session needs every piece of context

If this isn't you, stay at Level 2. It's simpler and sufficient for most people.

---

## Architecture Overview

```
~/my-brain/
├── core/                          # Always loaded
│   ├── source-of-truth.md         # Current state, priorities, active items
│   ├── people-reference.md        # Key people (summary level)
│   └── quality-contract.md        # Rules, standards, audit protocol
│
├── operational-index.md           # ROUTING FILE — tells AI where to find things
│
├── entities/                      # Loaded on demand
│   ├── projects/
│   │   ├── platform-migration.md
│   │   ├── meal-planning-app.md
│   │   └── q3-planning.md
│   ├── vendors/
│   │   ├── acme-cloud.md
│   │   └── dataflow-inc.md
│   └── domains/
│       ├── engineering.md
│       └── product.md
│
├── seeds/                         # Compressed historical context
│   ├── 2024-q1-summary.md
│   └── migration-phase-1.md
│
└── deep/                          # Full archives (rarely accessed)
    ├── session-logs-2024-q1.md
    └── migration-decisions-log.md
```

### Key Concepts

- **Core files** — Always loaded at session start. Kept lean (<500 lines each).
- **Operational Index** — A routing table that tells the AI where to find specific topics.
- **Entity files** — Loaded only when the session topic requires them.
- **Seeds** — Compressed summaries of resolved/historical content (60% smaller, 100% fidelity).
- **Deep memory** — Full archives accessed only when seeds aren't sufficient.

---

## Migration Steps

### Step 1: Create the Operational Index (30 min)

This is the most important new file. It's a routing table:

```markdown
# Operational Index
Last updated: 2024-06-01

## Routing Table

| Topic / Keyword | Location | Load When |
|----------------|----------|-----------|
| Platform migration | entities/projects/platform-migration.md | Discussing migration |
| Meal planning app | entities/projects/meal-planning-app.md | Side project work |
| Acme Cloud vendor | entities/vendors/acme-cloud.md | Vendor discussions |
| Q1 history | seeds/2024-q1-summary.md | Need Q1 context |
| Migration decisions | deep/migration-decisions-log.md | Need full decision history |

## Active Entities (load by default)
- entities/projects/platform-migration.md (active, deadline Sept 15)
- entities/projects/q3-planning.md (active, due this week)

## Dormant Entities (load on request)
- entities/projects/meal-planning-app.md (paused until July)
- entities/vendors/dataflow-inc.md (contract signed, no active work)
```

### Step 2: Extract Entities (60 min)

For each project, vendor, or domain that has 200+ lines of context:

1. Create a dedicated file in `entities/`
2. Move all relevant content from your Level 2 files
3. Leave a one-line summary + pointer in the core file
4. Add the entity to the operational index

**Before (in projects-reference.md):**
```markdown
## Platform Migration
[200 lines of status, decisions, risks, timeline, contacts...]
```

**After (in core/source-of-truth.md):**
```markdown
## Platform Migration
Status: 60% complete, deadline Sept 15. → entities/projects/platform-migration.md
```

### Step 3: Set Up the Registry (20 min)

Add metadata to your operational index that tracks:
- When each entity was last updated
- Whether it's active or dormant
- Dependencies between entities

```markdown
## Entity Registry

| Entity | Status | Last Updated | Dependencies |
|--------|--------|-------------|--------------|
| platform-migration | Active | 2024-06-01 | acme-cloud, q3-planning |
| meal-planning-app | Paused | 2024-05-15 | None |
| acme-cloud | Active | 2024-05-28 | platform-migration |
```

### Step 4: Establish Memory Tiers (30 min)

Review all content and assign it to a tier:

- **Active (core/ + active entities):** Current, relevant, changes frequently
- **Seeds (seeds/):** Resolved but might be referenced. Compress to ~40% of original size.
- **Deep (deep/):** Full archives. Only accessed when seeds aren't enough.

Create your first seed by taking a completed project or past quarter and compressing it. See `memory-tiers.md` for the compression protocol.

---

## How the Operational Index Works

The operational index is what makes Level 3 scalable. Here's the routing logic:

### At Session Start:
1. AI reads `core/` files + `operational-index.md`
2. AI checks which entities are marked "Active" → loads those too
3. AI does NOT load dormant entities, seeds, or deep memory

### During Session:
4. If a topic comes up that maps to a dormant entity → AI loads it
5. If historical context is needed → AI checks seeds first, deep only if needed

### At Session End:
6. AI updates only the files that changed
7. AI updates the operational index if entity status changed

### Example Routing Decision:

**User says:** "Let's talk about the Acme Cloud contract renewal"

**AI thinks:**
- "Acme Cloud" → operational index says `entities/vendors/acme-cloud.md`
- Status: Active
- Load that file now
- Also note: depends on platform-migration (already loaded)

---

## Three-Tier Memory Setup

### Active Memory (Always Loaded)
- Core files: source-of-truth.md, people-reference.md, quality-contract.md
- Operational index
- Active entity files
- **Target size:** < 3000 lines total across all active content

### Seeds (Loaded on Request)
- Compressed summaries of resolved content
- Must preserve: all names, dates, amounts, decisions, outcomes
- **Compression target:** 60% reduction from original
- **Format:** Narrative summary with all specifics preserved

### Deep Memory (Rarely Loaded)
- Full session logs, complete decision histories, raw notes
- Only accessed when a seed doesn't have enough detail
- **Organization:** By time period or by entity

See `memory-tiers.md` for detailed protocols on each tier.

---

## Session Ritual at Level 3

### Start:
1. Read core/ files
2. Read operational-index.md
3. Load active entities per the index
4. Run Tenth Man audit on loaded content
5. Surface relevant deadlines and open items

### End:
1. Update affected files (core + entities)
2. Update operational index if status changed
3. Add session log entry to source-of-truth.md
4. Check: should any content be seeded? (Propose, don't auto-execute)
5. Run Tenth Man (end pass)
6. If last session of day: run Kaizen review

---

## Common Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|-----------|
| Too many active entities | Context window bloat | Ruthlessly mark things dormant |
| Stale operational index | AI loads wrong things | Update index every session |
| Over-fragmenting | Lose coherence between related items | Keep related things together until they're truly independent |
| Skipping seeds | Deep memory grows unbounded | Seed completed items within 2 weeks |
| No routing logic | AI guesses what to load | Keep operational index current and specific |

---

## When Level 3 Is Overkill

Be honest with yourself. Level 3 is only worth the overhead if you:
- Manage 10+ active entities
- Have sessions spanning very different domains
- Need historical context frequently
- Generate enough new information to overwhelm Level 2

Most professionals thrive at Level 2 indefinitely. Level 3 is for operators managing complex systems, multiple businesses, or high-velocity environments.

---

*Level 3 trades simplicity for scale. The operational index is your new best friend — keep it accurate and the system works beautifully. Let it rot and you'll wish you'd stayed at Level 2.*
