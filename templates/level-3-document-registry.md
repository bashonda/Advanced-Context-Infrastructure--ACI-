# Level 3: Document Registry

<!-- 
  PATTERN: The Document Registry is the intake system for all new information.
  Every document that arrives — email attachment, shared doc, report, template —
  gets cataloged here with metadata and recommended actions.
  
  This prevents information from falling through cracks and ensures
  the AI can surface relevant docs when routing rules trigger.
  
  CROSS-REFERENCES:
  - level-3-operational-index.md → "Document intake / triage" route loads this file
  - level-3-entity-template.md → new docs may link to entity files
  - level-3-deep-memory.md → resolved/archived docs move to deep memory
-->

## Purpose

Every document that enters the system gets cataloged here. This is the **single intake point** for new information. The AI scans for new documents every session and catalogs them immediately with recommended actions.

## Registry Rules

1. **Scan every session** for new documents mentioned, shared, or received.
2. **Catalog immediately** — don't wait for the user to ask.
3. **Surface with recommended actions** — suggest what to do with each new doc.
4. **Update status** as actions are completed.
5. **Archive** completed entries to deep memory monthly (keep last 30 days active).

## Document Categories

| Category | Description | Typical Action |
|----------|-------------|----------------|
| Reference | Ongoing reference material | File in appropriate entity/project |
| Decision-Required | Needs a decision or response | Flag urgency, surface in next session |
| FYI | Informational only | Catalog, compress key points to SOT |
| Template | Reusable template or framework | Store in templates directory |
| Data Source | Raw data, reports, exports | Link to relevant operational file |

## Active Registry

| Date Received | Document | Source | Type | Location | Actions Needed | Status |
|---------------|----------|--------|------|----------|----------------|--------|
| 2026-05-15 | Q2 Vendor Scorecard | Operations Team | Data Source | `/reports/q2-vendor-scorecard.xlsx` | Review metrics, update vendor entity files | ✅ Complete |
| 2026-05-20 | Reorg Announcement Draft | VP of Eng | Decision-Required | Shared via email | Review, provide feedback by 5/24 | ✅ Complete |
| 2026-05-22 | New Onboarding Template | HR | Template | `/templates/onboarding-v3.md` | Adopt for next hire, update playbook | 🔄 In Progress |
| 2026-05-27 | Monthly Ops Dashboard | Auto-generated | Data Source | Looker Dashboard #142 | Review anomalies, flag in WBR | ⬜ Pending |
| 2026-05-29 | Partnership Proposal - Acme | BD Team | Decision-Required | `/docs/acme-proposal-v1.pdf` | Evaluate by 6/05, discuss in strategy session | ⬜ Pending |

## Intake Workflow

```
New document arrives
    ↓
Catalog in registry (date, source, type, location)
    ↓
Assign category
    ↓
Recommend action + deadline (if applicable)
    ↓
Link to relevant entity/project file
    ↓
Surface in next relevant routing trigger
    ↓
On completion → update status → archive to deep memory after 30 days
```

## Archive Rules

- **Active window:** Keep last 30 days in this file.
- **Archive trigger:** Status = ✅ Complete AND older than 30 days.
- **Archive destination:** `level-3-deep-memory.md` → Document Archive section.
- **Retain in registry:** Only the row (compressed). Full context moves to deep memory.

## Session Checklist

At every session start, the AI should:
- [ ] Check for any new documents mentioned or shared
- [ ] Catalog any uncataloged documents
- [ ] Surface any ⬜ Pending items with approaching deadlines
- [ ] Update status of 🔄 In Progress items if new info available

---

<!-- VERSION FOOTER -->
*Template version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of: Level 3 Advanced Context Infrastructure*
