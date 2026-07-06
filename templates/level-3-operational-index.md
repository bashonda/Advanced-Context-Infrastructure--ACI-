# Level 3: Operational Index (Router)

<!-- 
  PATTERN: The Operational Index is the AI's "dispatch table."
  It answers: "Given what I'm doing right now, which files should I load?"
  
  This eliminates wasted context by loading only what's needed per activity.
  Core files are always loaded. Everything else is on-demand.
  
  CROSS-REFERENCES:
  - level-3-document-registry.md → for new document intake routing
  - level-3-entity-template.md → entity files referenced in routing rules
  - level-3-deep-memory.md → cold storage, loaded only when seeds require expansion
-->

## Purpose

This file is the **router**. At session start, the AI reads this file to determine which additional files to load based on the current activity or trigger. This keeps context lean and relevant.

## Core Files (Always Loaded)

These files load at the start of **every** session, regardless of activity:

| # | File | Purpose |
|---|------|---------|
| 1 | Source of Truth (SOT) | Current state, priorities, session log |
| 2 | People Reference | Key people, org context, stakeholder map |
| 3 | Operational Index (this file) | Routing and dispatch |
| 4 | Quality Contract | SLAs, thresholds, validation rules |
| 5 | Kaizen SOT | Continuous improvement engine |

## Routing Table

| Activity / Trigger | Additional Files to Load | Notes |
|--------------------|--------------------------|-------|
| Session start (no specific task) | Core 5 only | Do NOT load operational or deep memory files |
| Meeting prep with [Person] | `people.md` + `entities/[person].md` + relevant project file | Check entity file for open questions to raise |
| Vendor WBR review | `operations.md` + `entities/[vendor].md` + `data-sources.md` | Pull latest metrics before discussion |
| Project deep-dive: [Project] | `projects.md` + `entities/[project].md` + linked docs | Load deep-memory section if historical context needed |
| 1:1 with direct report | `entities/[person].md` + `projects.md` (their projects only) | Surface open questions and last session notes |
| Document intake / triage | `document-registry.md` | Catalog new docs, assign actions |
| Strategic planning | `projects.md` + `people.md` + `deep-memory.md` (strategy section) | Broader context needed for planning |
| Incident / escalation | `operations.md` + `entities/[affected-system].md` + `quality-contract.md` | Time-sensitive — load fast, act fast |
| End-of-week review | Core 5 + `document-registry.md` + `kaizen.md` | Run audits, update session log, close loops |
| AI venture / side project work | `projects.md` (ventures section) + `entities/[venture].md` | Isolate from day-job context unless crossover |

## Routing Rules

1. **Core files are non-negotiable.** They load every session.
2. **Operational files load on demand.** Only when the activity requires them.
3. **Deep memory is NEVER loaded at session start.** Only load specific sections when a compressed seed in active memory requires expansion.
4. **Entity files are surgical.** Load only the specific entity relevant to the task.
5. **When in doubt, ask.** If the activity doesn't match a routing rule, ask the user which files to load.
6. **Multiple activities = union of files.** If a session covers multiple activities, load the union of all required files.
7. **New routing rules get added here.** If a new recurring activity emerges, add a row to the table.

## How to Add a New Route

```markdown
| [Activity description] | [Files to load] | [Any special notes] |
```

Then validate:
- Does this activity recur at least weekly?
- Are the files it references already cataloged in the document registry?
- Does this overlap with an existing route? (If so, merge or differentiate.)

---

<!-- VERSION FOOTER -->
*Template version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of: Level 3 Advanced Context Infrastructure*
