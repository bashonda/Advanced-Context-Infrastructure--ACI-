# Level 3: Deep Memory (Cold Storage)

<!-- 
  PATTERN: Deep Memory is the archive layer — full detail behind compressed seeds.
  It is NEVER loaded at session start. The AI loads specific sections on-demand
  only when a compressed seed in active memory requires expansion.
  
  Think of this as a database the AI queries, not a document it reads cover-to-cover.
  Organization by topic/entity with clear headers enables surgical retrieval.
  
  CROSS-REFERENCES:
  - level-3-operational-index.md → routing rules specify when to load deep memory sections
  - level-3-document-registry.md → archived documents land here
  - level-3-entity-template.md → entity session notes older than 90 days archive here
-->

## Purpose

This file stores **full detail behind compressed seeds**. Active memory files contain compressed one-liners that point here for expansion. This keeps active files lean while preserving institutional knowledge.

## How to Use

1. **Never load this file at session start.** It's cold storage.
2. **Load specific sections on demand** when a seed in active memory says "→ see deep memory."
3. **Search by header** — each section has a clear, searchable title.
4. **Reference format in active files:** `[→ DM: Section Name]` indicates a deep memory pointer.

## What Goes Here

| Category | Criteria | Example |
|----------|----------|---------|
| Resolved items | Decision made, no longer active | "Why we chose Vendor X over Y" |
| Completed projects | Project closed, lessons captured | "Q1 Migration — retrospective" |
| Historical context | Background that rarely changes | "Org history before reorg" |
| Archived session notes | Entity notes older than 90 days | "1:1 notes with [Person], Jan-Mar" |
| Archived registry entries | Completed docs older than 30 days | "Q1 document intake log" |

## Structure Convention

Each deep memory entry follows this format:

```markdown
### [Topic/Entity] — [Brief Description]
**Seed:** [The compressed one-liner that lives in active memory]
**Archived:** [Date moved to deep memory]
**Context:** [Full expanded detail]
```

---

## Archived Entries

### Vendor Selection — Why We Chose CloudCorp

**Seed:** "Vendor selection: CloudCorp won over DataFlow (cost + integration). [→ DM: Vendor Selection]"  
**Archived:** 2026-04-15  
**Context:**

In Q1 2026, we evaluated three vendors for the data pipeline rebuild:
- **CloudCorp** — $42K/yr, native integration with our Databricks stack, 99.9% SLA, dedicated CSM. POC completed in 2 weeks with zero blockers.
- **DataFlow** — $38K/yr, required custom connector ($15K one-time), 99.5% SLA. POC surfaced 3 compatibility issues.
- **StreamLine** — $55K/yr, best features but overkill for our scale. No POC completed (declined after discovery).

Decision made 2026-03-20 by Aaron + VP Eng. Key factor: total cost of ownership over 2 years favored CloudCorp by ~$30K when including integration costs. Contract signed 2026-04-01.

---

### Q4 2025 Reorg — Team Structure Changes

**Seed:** "Q4 reorg: Eng split into Platform + Product. Aaron moved to Platform. [→ DM: Q4 Reorg]"  
**Archived:** 2026-02-01  
**Context:**

Effective 2025-11-01, Engineering was split into two orgs:
- **Platform Engineering** (Aaron's new org) — Infrastructure, data, DevOps, SRE. Reports to CTO.
- **Product Engineering** — Feature teams, frontend, mobile. Reports to VP Product.

Key changes:
- Aaron transitioned from hybrid role to pure Platform leadership
- Inherited 3 additional direct reports (SRE team)
- Budget increased 40% to cover infrastructure investments
- Dotted-line relationship maintained with Product Eng for shared services

Transition completed by 2025-12-15. First full quarter as Platform lead: Q1 2026.

---

### Project Alpha — Completed Migration Retrospective

**Seed:** "Project Alpha: Completed 2026-03-30. On-time, 5% under budget. [→ DM: Project Alpha Retro]"  
**Archived:** 2026-04-10  
**Context:**

**Project Alpha** — Migration of legacy monolith to microservices architecture.
- **Duration:** 2025-10-01 to 2026-03-30 (6 months)
- **Budget:** $180K allocated, $171K spent (5% under)
- **Team:** 4 engineers + 1 contractor
- **Outcome:** 12 services extracted, latency reduced 60%, deployment frequency 4x

**Lessons learned:**
1. Starting with the least-coupled service was the right call — built confidence early
2. Should have invested in observability tooling in month 1 (added in month 3, caused blind spots)
3. Contractor ramp-up took 3 weeks longer than planned — budget for this next time
4. Stakeholder communication cadence (bi-weekly) was perfect — don't reduce

**What we'd do differently:** Automated canary deployments from day 1, not month 4.

---

## Version Footer Archive

<!-- When active files update their version footers, old versions log here -->

| File | Previous Version | Updated To | Date | Change Summary |
|------|-----------------|------------|------|----------------|
| [filename] | [old version] | [new version] | [date] | [what changed] |

---

<!-- VERSION FOOTER -->
*Template version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of: Level 3 Advanced Context Infrastructure*
