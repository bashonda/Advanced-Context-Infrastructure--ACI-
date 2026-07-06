# Memory Tiers: Active → Seeds → Deep

> **Why three tiers:** Prevents both bloat (loading everything) and amnesia (losing important history).  
> **Key insight:** Over-fragmenting destroys coherence. Compression must preserve the whole.

---

## The Problem Three Tiers Solve

Without memory tiers, you face two bad options:

1. **Keep everything active** → Context window bloat, AI drowns in irrelevant detail, sessions are slow
2. **Delete old stuff** → Lose important history, can't reference past decisions, repeat mistakes

Memory tiers give you a third option: **graduated compression**. Recent and relevant stays full-fidelity. Resolved content gets compressed but remains accessible. Raw archives exist for when you need the complete picture.

---

## Tier 1: Active Memory

### What It Contains
- Current state and priorities
- Active projects and their status
- Key people you interact with regularly
- Open decisions and pending items
- Recent session logs (last 1–2 weeks)
- Anything you might need in today's session

### When to Update
- Every session (at minimum, session log entry)
- When status changes on any active item
- When new people or projects enter your world
- When priorities shift

### Sizing Principle

> **Active Memory must be big enough for Tenth Man to catch things it wasn't looking for.**

This is the critical sizing rule. If active memory is too lean, the Tenth Man audit can only verify what's explicitly there. It can't notice:
- A missing person who should be listed
- A project that went silent (because it's not there to go silent)
- A contradiction between two items (because one was archived too early)

**Target:** 1500–3000 lines total across all active content (core files + active entities).

**Too small (<1000 lines):** You're probably hiding problems in seeds/deep.  
**Too large (>5000 lines):** You're probably keeping resolved items active too long.

### What Doesn't Belong in Active
- Completed projects (seed them)
- People you haven't interacted with in 4+ weeks
- Decisions that were made and implemented
- Session logs older than 2 weeks
- Reference material that rarely changes

---

## Tier 2: Seeds

### What They Are

Seeds are **compressed summaries** of resolved content. They preserve all important facts in roughly 40% of the original space.

**The rule:** 60% compression, 100% fidelity.

This means: a seed is shorter, but it loses NO important information. All names, dates, amounts, decisions, outcomes, contacts, counts, and status must survive compression.

### Format Rules

Every seed must include:
- **All names** — people, companies, tools mentioned
- **All amounts** — money, quantities, percentages
- **All dates** — deadlines, milestones, when things happened
- **All contacts** — who to reach out to, who owns what
- **All counts** — how many, how often
- **All status** — final state of each item
- **Pointer to Deep** — where to find the full version

### Seed Format Example

**Original (Active, 45 lines):**
```markdown
## Office Move Project
Started: 2024-03-01
Completed: 2024-05-15

### Background
We outgrew the 5th floor space (42 people, capacity 35). Sarah initiated the move 
discussion in January. Evaluated 3 options: expand current floor, move to 8th floor, 
or go hybrid. Marcus approved 8th floor option on Feb 15 after cost analysis showed 
$12K/month increase but 60% more space.

### Timeline
- March 1: Project kicked off, Priya as logistics lead
- March 15: Floor plan approved (open plan with 4 focus rooms)
- April 1-15: Construction and IT infrastructure
- April 20: Furniture delivery (vendor: OfficeMax Pro, contact: Jake Sullivan)
- May 1: Phased move begins (team by team over 2 weeks)
- May 15: Move complete, old floor decommissioned

### Decisions Made
- Open plan with focus rooms (not all private offices) — cost driven
- Keep 5th floor as overflow/meeting space for 3 months (lease ends Aug 31)
- IT ran parallel networks during transition (extra $3K but zero downtime)

### Issues Encountered
- Furniture delayed 1 week (supply chain). Mitigated with temporary desks.
- 3 team members unhappy with open plan. Addressed with noise-canceling headphone 
  budget ($200/person, 3 people = $600).

### Final Status
Complete. Team settled. 8th floor at 42/55 capacity. Budget: $18K over original 
estimate ($3K IT + $12K furniture upgrade + $3K misc). Sarah approved overage.
```

**Seed (18 lines, 60% compression):**
```markdown
## Seed: Office Move Project
Pointer: deep/office-move-full.md
Seeded: 2024-06-01

Moved from 5th floor (42 people, 35 capacity) to 8th floor (55 capacity). 
Project ran March 1 – May 15, 2024. Priya led logistics.

Key facts: Marcus approved Feb 15. Cost: $12K/month increase, 60% more space. 
Open plan + 4 focus rooms. Vendor: OfficeMax Pro (contact: Jake Sullivan). 
IT ran parallel networks ($3K, zero downtime). 

Issues: 1-week furniture delay (mitigated), 3 team members unhappy with open plan 
(resolved: $200/person headphone budget, $600 total).

Final: Complete. 42/55 capacity. $18K over budget ($3K IT + $12K furniture + $3K misc). 
Sarah approved overage. Old floor kept as overflow until lease ends Aug 31.

Decisions: Open plan (cost-driven), parallel networks (reliability), 3-month overlap on old floor.
```

### When to Seed

**Propose seeding when:**
- A project is complete and unlikely to need active reference
- Session logs are 2+ weeks old
- A decision was made and implemented (deliberation history no longer needed daily)
- An entity becomes dormant

**Never auto-seed.** Always propose:
> "The office move project has been complete for 3 weeks. I'd like to seed it — here's the proposed seed. Shall I proceed?"

The human reviews the seed to ensure nothing important was lost.

---

## Tier 3: Deep Memory

### What It Contains
- Full, uncompressed archives of everything that was seeded
- Complete session logs
- Full decision deliberation histories
- Raw notes and brainstorms
- Email/message archives (if stored)

### When to Access
- When a seed doesn't have enough detail for the current question
- When you need the "why" behind a decision (seeds capture "what")
- When reconstructing a timeline of events
- When a dispute arises about what was said/decided

### Organization Principles

Organize deep memory by:
1. **Time period** — `deep/session-logs-2024-q1.md`
2. **Entity** — `deep/office-move-full.md`
3. **Type** — `deep/decision-log-2024.md`

Use whatever makes retrieval easiest. The operational index should map topics to their deep memory locations.

### Deep Memory Hygiene
- Deep memory doesn't need regular maintenance
- It's append-mostly (add new archives, rarely modify)
- No size limit — it's only loaded on demand
- Date everything clearly for future retrieval

---

## Compression Validation: The Blind Test

How do you know a seed preserves fidelity? Use the blind test:

### Method:
1. Create the seed
2. Hide the original (don't look at it)
3. Read only the seed
4. Ask yourself: "Can I answer any reasonable question about this topic from the seed alone?"
5. Try specific questions:
   - "Who was the vendor contact?" (must be in seed)
   - "How much over budget?" (must be in seed)
   - "When did it complete?" (must be in seed)
   - "What went wrong?" (must be in seed)

### If you can't answer from the seed:
The seed is missing critical information. Add it back.

### If you need more detail than the seed provides:
That's fine — that's what deep memory is for. The seed should answer 90% of questions. Deep memory handles the other 10%.

### Validation Checklist:
- [ ] All people names preserved
- [ ] All dates preserved
- [ ] All monetary amounts preserved
- [ ] All decisions and their rationale preserved
- [ ] All outcomes/status preserved
- [ ] All contact information preserved
- [ ] Pointer to deep memory included
- [ ] Seed is ≤40% the length of original

---

## The Coherence Principle

> **Over-fragmenting destroys coherence. Compression must preserve the whole.**

This is the most common mistake in memory tier systems. People fragment information too aggressively:

### Bad Fragmentation:
```
seeds/office-move-timeline.md    (just dates)
seeds/office-move-people.md      (just who was involved)  
seeds/office-move-budget.md      (just costs)
seeds/office-move-decisions.md   (just decisions)
```

### Why It's Bad:
- You lose the narrative thread
- Connections between facts disappear
- "The furniture delay caused the budget overage" is lost when timeline and budget are separated
- Reconstructing the full picture requires loading 4 files

### Good Compression:
```
seeds/office-move.md             (one coherent summary with everything)
```

Keep related information together. A seed should tell a complete story, just a shorter one.

---

## Tier Transitions

```
┌─────────────────────────────────────────────────┐
│                ACTIVE MEMORY                      │
│  (Full detail, always loaded, frequently updated)│
│                                                   │
│  Trigger to seed: Item resolved/dormant 2+ weeks │
└───────────────────────┬─────────────────────────┘
                        │ Propose seed
                        │ Human approves
                        ▼
┌─────────────────────────────────────────────────┐
│                   SEEDS                           │
│  (60% compressed, loaded on request, rarely      │
│   updated, pointer to deep)                      │
│                                                   │
│  Trigger to access deep: Seed insufficient       │
└───────────────────────┬─────────────────────────┘
                        │ Load on demand
                        ▼
┌─────────────────────────────────────────────────┐
│               DEEP MEMORY                         │
│  (Full archives, loaded rarely, append-only)     │
└─────────────────────────────────────────────────┘
```

### Can things move back UP?
Yes! If a seeded project becomes active again:
1. Load the seed
2. Load deep memory for full context
3. Reconstitute an active entity file
4. Remove the seed (or mark it superseded)

This is rare but important. Dormant projects sometimes wake up.

---

## Quick Reference

| Tier | Size | Loaded | Updated | Contains |
|------|------|--------|---------|----------|
| Active | 1500–3000 lines | Always | Every session | Current, relevant, changing |
| Seeds | No limit | On request | Rarely | Compressed resolved content |
| Deep | No limit | Rarely | Append-only | Full archives |

---

*Three tiers give you the best of both worlds: lean active context for fast sessions, plus complete history when you need it. The key is disciplined seeding with validated compression — never lose fidelity, just lose verbosity.*
