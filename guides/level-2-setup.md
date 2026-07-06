# Level 2 Setup: Multi-File SOT Architecture

> **When to read this:** Your single-file SOT has grown unwieldy (500+ lines) or you're managing multiple domains.  
> **Time required:** 45–60 minutes to migrate  
> **Outcome:** 4–5 specialized files that are faster to read, easier to update, and less likely to rot.

---

## Signals It's Time to Upgrade

You need Level 2 when you notice any of these:

- **File > 500 lines** — Your AI is spending context window on irrelevant sections
- **Scrolling to find things** — You can't quickly locate what you need
- **AI missing context** — Important details buried in a wall of text
- **Multiple domains** — Work, side projects, personal goals all in one file
- **Update anxiety** — You hesitate to add things because the file is already too long

If you're experiencing 2+ of these, it's time.

---

## The Level 2 Architecture

Split your single file into 4–5 specialized documents:

```
~/my-brain/
├── source-of-truth.md        # Current state, priorities, session log
├── people-reference.md        # All people, relationships, org context
├── projects-reference.md      # Active projects, milestones, decisions
├── recipes-playbook.md        # Procedures, data sources, how-to's
└── quality-contract.md        # (Optional) Standards, thresholds, rules
```

Each file has a single responsibility. No file should need to duplicate content from another.

---

## What Goes Where (Decision Tree)

When you're not sure where something belongs, use this:

```
Is it about a PERSON or RELATIONSHIP?
  → people-reference.md

Is it a PROCEDURE or RECIPE (how to do something)?
  → recipes-playbook.md

Is it a PROJECT with milestones, decisions, or deliverables?
  → projects-reference.md

Is it about CURRENT STATE, PRIORITIES, or SESSION HISTORY?
  → source-of-truth.md

Is it a RULE, THRESHOLD, or QUALITY STANDARD?
  → quality-contract.md
```

**When in doubt:** Put it in source-of-truth.md and move it later. Better to capture than to lose.

---

## Migration Steps

### Step 1: Create the new files (10 min)

Create empty files with headers for each section. Use the Level 2 templates if available, or create your own structure:

```markdown
# People Reference
Last updated: 2024-06-01

## Core Team
## Stakeholders  
## External Contacts
## Org Context & Transitions
```

### Step 2: Move content from your single file (20 min)

Go through your existing SOT section by section:
- **Cut** content from the single file
- **Paste** into the appropriate specialized file
- **Add context** if needed (a sentence that made sense in the original might need a header in the new location)

### Step 3: Add cross-references (5 min)

Where content in one file relates to another, add a pointer:

```markdown
## Platform Migration
Status: 60% complete, deadline Sept 15
Tech lead: Priya Patel (see people-reference.md)
Runbook: see recipes-playbook.md § Migration Procedures
```

### Step 4: Update your session instructions (5 min)

Change your AI's startup instruction to read ALL files:

```
At the start of every session:
1. Read all files in ~/my-brain/
2. Briefly acknowledge current state
3. Surface upcoming deadlines or open items
```

### Step 5: Validate (10 min)

Start a new session. Does your AI have full context? Can it answer:
- "What am I working on?" (source-of-truth.md)
- "Who is Marcus?" (people-reference.md)
- "What's the migration status?" (projects-reference.md)
- "How do I run the deploy?" (recipes-playbook.md)

If anything is missing, it fell through a crack during migration.

---

## Cross-Referencing Rules

The most important rule in a multi-file system:

> **Every fact lives in ONE canonical location. Everywhere else gets a pointer.**

### Why This Matters

If "Priya is the migration tech lead" appears in both `people-reference.md` and `projects-reference.md`, they will eventually contradict each other. One will get updated, the other won't.

### How to Do It

**Canonical location** — where the full detail lives:
```markdown
# people-reference.md
## Priya Patel
- Role: Senior Engineer, Tech Lead on Platform Migration
- Reports to: Marcus Webb
- Working style: Deep focus, prefers Slack over meetings
- Note: Overloaded in Q3 — shield from non-essential meetings
```

**Pointer** — in other files that reference this person:
```markdown
# projects-reference.md
## Platform Migration
- Tech Lead: Priya Patel (→ people-reference.md)
```

### Decision: Where Is Canonical?

| Information Type | Canonical Location |
|-----------------|-------------------|
| Person's role, style, relationships | people-reference.md |
| Project status, milestones, decisions | projects-reference.md |
| How to do something | recipes-playbook.md |
| Current priorities, state | source-of-truth.md |
| Rules, thresholds | quality-contract.md |

---

## Session Ritual Changes

Your session ritual evolves at Level 2:

### Session Start
1. AI reads **all** SOT files (not just one)
2. AI acknowledges current state and surfaces relevant items
3. AI notes any staleness or contradictions across files

### Session End
1. AI updates **only the affected files** (not all of them)
2. Session log entry goes in source-of-truth.md
3. AI checks: did new info get added to the right canonical location?
4. Timestamps updated on changed files

### Example End-of-Session Update

> "Today we discussed the migration timeline change. I've updated:
> - `projects-reference.md` — new deadline (Sept 22), added risk note
> - `source-of-truth.md` — session log entry, updated priority #1
> - `people-reference.md` — no changes needed"

---

## Tips for Level 2

1. **Don't over-split.** 4–5 files is the sweet spot. More than 7 and you'll lose coherence.

2. **Keep source-of-truth.md as the "home base."** It should always answer: "What's happening right now?"

3. **Version your files.** Add `Last updated: YYYY-MM-DD` at the top of each file. Stale dates are a smell.

4. **Review monthly.** Once a month, read all files front-to-back. Archive completed projects. Remove departed people.

5. **Trust the system.** It feels weird at first to split things up. After 2 weeks, you won't go back.

---

## When to Upgrade to Level 3

You're ready for Level 3 when:
- Individual files exceed ~1000 lines
- Loading everything at session start is slow or wasteful
- Entities (projects, people, vendors) need their own dedicated files
- New information arrives faster than you can organize it
- You need memory tiers (active vs. archived)

**Next:** Read `level-3-migration.md` for the advanced architecture.

---

*Level 2 is where most people should stay. It handles complex professional lives with multiple projects and dozens of stakeholders. Only upgrade to Level 3 if you're hitting real limits.*
