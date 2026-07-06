# Quality Contract

<!-- 
  LEVEL 2 QUALITY CONTRACT
  This file defines the rules, audits, and continuous improvement processes that keep
  your SOT system healthy and trustworthy. Your AI enforces these automatically.
  
  Update frequency: When rules change or Kaizen surfaces improvements.
  Cross-ref: level-2-source-of-truth.md (System Reference)
-->

## Hard Rules

<!-- 
  Absolute rules that must ALWAYS or NEVER happen. These are non-negotiable.
  Keep this list tight — if everything is a hard rule, nothing is.
-->

### ALWAYS
- [ ] Read all SOT documents at the start of every session
- [ ] Update session log before ending any session
- [ ] Flag information older than 14 days as potentially stale
- [ ] Confirm before taking irreversible actions
- [ ] Store new information in ONE canonical location with cross-refs
- [ ] Use specific dates, not relative time ("June 15" not "next week")
- [ ] Validate assumptions on high-stakes work before proceeding

### NEVER
- [ ] Fabricate information — state uncertainty explicitly
- [ ] Delete SOT content without explicit user permission
- [ ] Store credentials, tokens, or secrets in SOT files
- [ ] Skip the session ritual (start or end)
- [ ] Let contradictions between SOT files persist unresolved
- [ ] Make commitments on behalf of the user without confirmation

---

## Tenth Man Rule

<!-- 
  The self-correction audit. Run at the start AND end of every session.
  Purpose: Catch staleness, contradictions, and drift before they compound.
  
  Named after the principle: if 9 people agree, the 10th must argue the opposite.
  Here, the AI actively looks for what might be WRONG in the SOT.
-->

### Audit Checklist

Run through each item. Flag findings explicitly to the user.

| # | Check | Question to Ask | Action if Found |
|---|-------|----------------|-----------------|
| 1 | **Staleness** | Is any SOT content >14 days without update? | Flag it. Ask user: "Is [X] still accurate?" |
| 2 | **Contradictions** | Do any two SOT files say different things about the same topic? | Surface both versions. Resolve to one canonical truth. |
| 3 | **Gaps** | Is there context the AI needs but can't find in any SOT file? | Note the gap. Propose where it should live. |
| 4 | **Changed Truth** | Has something the user said previously become outdated? | Flag the old statement. Confirm the new reality. |
| 5 | **Cascade Risk** | If [X] changed, what else in the SOT is now wrong? | Trace dependencies. Update all affected sections. |
| 6 | **Seed Candidates** | Is there new info from this session that should be in the SOT? | Propose specific placement in the correct file. |
| 7 | **Challenge** | What assumption am I making that might be wrong? | State it explicitly. Ask user to confirm or correct. |
| 8 | **Honest Findings** | Am I being rigorous or just rubber-stamping? | Report at least ONE finding per audit, even if minor. |

### Audit Output Format
```
**Tenth Man Audit — [Date]**
- 🔍 Staleness: [Finding or "None detected"]
- ⚡ Contradictions: [Finding or "None detected"]  
- 🕳️ Gaps: [Finding or "None detected"]
- 🔄 Changed Truth: [Finding or "None detected"]
- 🌊 Cascade Risk: [Finding or "None detected"]
- 🌱 Seed Candidates: [Finding or "None detected"]
- 🤔 Challenge: [Finding or "None detected"]
- ✅ Honest Finding: [At least one observation]
```

---

## Kaizen — Continuous Improvement

<!-- 
  Runs at the end of the last session each business day.
  Purpose: Make the system 1% better every day.
  Named after the Japanese philosophy of continuous improvement.
-->

### Daily Kaizen Review (End of Day)

1. **What worked well today?** — Note effective patterns to reinforce
2. **What was friction?** — Where did the system slow you down or fail?
3. **What's one improvement?** — Propose ONE concrete change to any SOT file
4. **Implement or defer?** — If quick (<5 min), do it now. Otherwise, add to backlog.

### Improvement Backlog

<!-- Track proposed improvements that weren't implemented immediately -->

| Date Proposed | Improvement | File Affected | Status | Implemented |
|---------------|-------------|---------------|--------|-------------|
| [2026-05-29] | [Example: Add "energy level" field to session log] | [source-of-truth] | [Proposed] | [ ] |
| [2026-05-29] | [Example: Create template for vendor meeting prep] | [recipes] | [Proposed] | [ ] |

### Improvement History

<!-- Completed improvements — proof the system evolves -->

| Date | What Changed | Why | Impact |
|------|-------------|-----|--------|
| [2026-05-29] | [Example: Added Tenth Man audit to session ritual] | [Was missing self-correction] | [Caught 3 stale items in first week] |

---

## SLAs & Thresholds

<!-- 
  Measurable standards for SOT system health. 
  Review monthly — are these realistic? Too loose? Too tight?
-->

| Metric | Threshold | Measurement | Consequence if Breached |
|--------|-----------|-------------|------------------------|
| SOT freshness | No section >14 days stale | Check "Last updated" timestamps | Trigger staleness review |
| Session log completeness | 100% of sessions logged | Count sessions vs. log entries | Flag at next session start |
| Audit compliance | Tenth Man runs every session | Check for audit output | Remind user, run immediately |
| Contradiction resolution | Resolved same session as found | Track open contradictions | Escalate to top of next session |
| Cross-ref integrity | All refs point to valid sections | Spot-check monthly | Fix broken refs immediately |

---

## Quality Incidents

<!-- 
  Track when the system failed. Learn from it. No blame — just improvement.
  This is how you build trust in the system over time.
-->

| Date | What Happened | Root Cause | Fix Applied | Prevented Recurrence? |
|------|--------------|------------|-------------|----------------------|
| [YYYY-MM-DD] | [Example: AI used outdated project status in a stakeholder update] | [Project file not updated after milestone] | [Added "update projects" to end-of-session ritual] | [Yes — no recurrence in 30 days] |

---

## Cross-References

- Session ritual (where audits are triggered) → `level-2-recipes.md#session-ritual`
- Hard rules (operational version) → `level-2-recipes.md#hard-rules`
- Current priorities (context for audits) → `level-2-source-of-truth.md#active-priorities`
- Project statuses (common staleness source) → `level-2-projects.md#project-index`

---

*Version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of the Level 2 Advanced Context Infrastructure — see level-2-source-of-truth.md for system index*
