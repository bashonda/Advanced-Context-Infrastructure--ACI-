# Level 3: Entity Template

<!-- 
  PATTERN: This is a generic template for per-entity operational files.
  An "entity" can be a person, vendor, client, project, workstream, or system.
  
  Each entity gets its own file, loaded on-demand via the Operational Index
  routing table. This keeps entity-specific detail out of core files while
  making it instantly accessible when needed.
  
  USAGE: Copy this template, rename to the entity name, fill in sections.
  Store in an /entities/ subdirectory for clean organization.
  
  CROSS-REFERENCES:
  - level-3-operational-index.md → routing rules reference entity files
  - level-3-document-registry.md → documents may link to entity files
  - level-3-deep-memory.md → archived entity history lives there
-->

## Header

| Field | Value |
|-------|-------|
| **Name** | [Entity Name] |
| **Type** | [Person / Vendor / Client / Project / Workstream / System] |
| **Role / Relationship** | [Their role or relationship to you] |
| **Key Contact** | [Email, Slack handle, or primary channel] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |

## Summary

<!-- 2-3 sentences: Who/what is this entity, why do they matter, what's the current state? -->

[Brief summary of this entity — their significance, current status, and primary interaction pattern.]

## Domain / Scope

<!-- What does this entity own, control, or influence? -->

- **Owns:** [Areas of ownership or responsibility]
- **Influences:** [Adjacent areas they affect]
- **Dependencies:** [What they depend on from you or others]
- **Cadence:** [How often you interact — weekly 1:1, monthly review, ad-hoc]

## Key Documents

| Document | Location | Last Reviewed | Notes |
|----------|----------|---------------|-------|
| [Doc name] | [Path or link] | [Date] | [Context] |
| [Doc name] | [Path or link] | [Date] | [Context] |

## Current State

<!-- What's active right now with this entity? -->

- **Priority items:** [What's top of mind]
- **Blockers:** [Anything stalled or waiting]
- **Recent wins:** [Positive momentum]

## Open Questions

<!-- Questions to raise next time you interact with this entity -->

1. [Question — added YYYY-MM-DD]
2. [Question — added YYYY-MM-DD]
3. [Question — added YYYY-MM-DD]

## Session Notes

<!-- Running log of interactions. Most recent first. Keep compressed. -->
<!-- Move entries older than 90 days to deep memory. -->

### [YYYY-MM-DD] — [Brief Topic]

- **Context:** [What triggered this interaction]
- **Key Points:** [Bullet the important takeaways]
- **Actions:** [What was decided or committed to]
- **Follow-up:** [Next step and deadline]

### [YYYY-MM-DD] — [Brief Topic]

- **Context:** [What triggered this interaction]
- **Key Points:** [Bullet the important takeaways]
- **Actions:** [What was decided or committed to]
- **Follow-up:** [Next step and deadline]

## Archive Rules

- Session notes older than **90 days** → compress to one-line summary, move detail to deep memory.
- Resolved open questions → remove from this file, log resolution in session notes.
- If entity becomes inactive → mark as archived in header, move entire file to `/entities/archive/`.

---

<!-- VERSION FOOTER -->
*Template version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of: Level 3 Advanced Context Infrastructure*
