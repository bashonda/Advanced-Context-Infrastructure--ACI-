# Source of Truth — Marcus Johnson, Senior Program Manager (Platform Migration)

> **Last updated:** 2026-05-28 | **Version:** 2.7 | **Next review:** 2026-06-04

---

## 🧭 Current State

I'm leading the Atlas-to-Nexus platform migration at Greenfield Corp — moving 3 engineering teams (Payments, Identity, Notifications) off a legacy monolith onto our new microservices platform. This is a 6-month program (started March 1), currently in Month 3.

**Key context:**
- **Overall status:** 🟡 Yellow — Payments team is on track, Identity team is 2 weeks behind, Notifications team hasn't started migration work yet (blocked on API contract finalization)
- **Exec sponsor:** CTO (Vanessa Liu) — supportive but impatient. Wants green status by steering committee on 6/10.
- **Biggest risk right now:** Identity team's tech lead (Omar) is pushing back on the prescribed architecture pattern. If we don't resolve this by 6/6, it cascades into a 4-week delay.
- **Vendor dependency:** CloudForge (our infrastructure vendor) owes us a custom connector by 6/13. Their PM has missed 2 status updates. Escalation needed.
- **Change management:** Training rollout for new platform starts 6/16. Materials are 60% complete.

**Program health:**
- Budget: 🟢 On track ($1.2M allocated, $480K spent through Month 3)
- Timeline: 🟡 At risk (Identity team slippage)
- Scope: 🟢 No scope creep (yet — watching Notifications team's "enhancement requests")
- Stakeholders: 🟡 Mixed — Payments happy, Identity frustrated, Notifications disengaged

---

## 🎯 Active Priorities

| # | Priority | Status | Due | Notes |
|---|----------|--------|-----|-------|
| 1 | Resolve Identity team architecture dispute | 🔴 Escalation needed | 6/6 | Omar wants event-sourcing; platform team says CQRS. Need Vanessa to break tie. |
| 2 | Unblock Notifications team (API contract) | 🟡 In progress | 6/4 | API spec review meeting scheduled 6/3. Platform team owes final spec. |
| 3 | CloudForge vendor escalation | 🔴 Overdue | Was 5/23 | Their PM (Steve Larkin) missed 2 check-ins. Escalating to their VP. |
| 4 | Steering committee prep (6/10) | 🟡 Drafting | 6/9 | Need to frame Identity delay honestly without triggering panic. |
| 5 | Training materials — complete remaining 40% | 🟡 In progress | 6/13 | Change management lead (Fiona) owns. Needs SME input from each team. |
| 6 | Payments team — Phase 2 cutover planning | 🟢 On track | 6/20 | They're ahead of schedule. Model team for the others. |
| 7 | Risk register update | 🟡 Overdue | Was 5/26 | 3 new risks identified this week. Need to log + assign mitigations. |
| 8 | Dependency mapping refresh | ⚪ Scheduled | 6/11 | Monthly refresh. Last one revealed 2 unknown upstream dependencies. |
| 9 | Stakeholder satisfaction pulse survey | 🟢 Sent | Results by 6/2 | Anonymous survey to all 3 team leads + their managers. |
| 10 | Program retrospective (Month 3) | ⚪ Scheduled | 6/6 | Format: what worked, what didn't, what to change for Month 4-6. |

---

## 👥 Key People

| Name | Role | Team/Org | Notes |
|------|------|----------|-------|
| Vanessa Liu | CTO / Exec Sponsor | Executive | Wants green by 6/10 steering committee. Direct but fair. Needs concise updates. |
| Raj Patel | Director of Engineering | Payments | Supportive. His team is the model. Good ally in steering committee. |
| Omar Hassan | Tech Lead | Identity | Pushing back on architecture. Technically brilliant but stubborn. Needs to feel heard. |
| Christine Park | Engineering Manager | Identity | Omar's manager. Sympathetic to timeline but won't override Omar on technical decisions. |
| Devon Williams | Engineering Manager | Notifications | Disengaged — feels his team was "voluntold" into this migration. Needs re-motivation. |
| Fiona McCarthy | Change Management Lead | PMO | Owns training rollout. Competent but under-resourced. Needs more SME time from teams. |
| Steve Larkin | PM, CloudForge | Vendor | Unreliable. Missed 2 status updates. Need to escalate past him. |
| Angela Reeves | VP Customer Success, CloudForge | Vendor | Steve's boss. Escalation target. Met her at kickoff — professional, responsive. |
| Nathan Cross | Platform Architect | Platform Team | Owns the target architecture. Key voice in Omar dispute. Needs to be more flexible. |
| Diane Okafor | Finance Business Partner | Finance | Tracks program budget. Monthly check-in. No issues currently. |
| Yuki Tanaka | VP Product | Product | Stakeholder — cares about migration not disrupting feature velocity. Quarterly update. |

---

## 📋 Active Projects

### Phase 1: Payments Team Migration
- **Status:** 🟢 Ahead of schedule
- **Milestone:** Phase 1 cutover planned for 6/20 (was 6/27 — pulled in)
- **Notes:** Clean execution. Using as reference architecture for other teams.

### Phase 2: Identity Team Migration
- **Status:** 🔴 2 weeks behind — architecture dispute
- **Milestone:** Was 7/15 cutover, now projecting 7/29 at best
- **Blocker:** Omar/Nathan architecture disagreement. Escalation to Vanessa by 6/6.
- **Fallback:** If dispute isn't resolved by 6/6, propose a "spike" week where both approaches are prototyped.

### Phase 3: Notifications Team Migration
- **Status:** 🟡 Blocked — hasn't started migration work
- **Milestone:** 8/15 cutover (at risk if API contract isn't finalized by 6/4)
- **Blocker:** API contract spec not finalized. Meeting 6/3.
- **Risk:** Devon's disengagement could become active resistance if not addressed.

### Training & Change Management Rollout
- **Owner:** Fiona McCarthy | **Start:** 6/16
- **Status:** 🟡 Materials 60% complete
- **Dependencies:** Needs 2 hours of SME time from each team lead (not yet scheduled)
- **Risk:** If materials aren't done by 6/13, training start slips, which cascades into go-live support.

---

## 📖 Operational Index

**When prepping for steering committee** → Load:
- `migration-status.md` (team-by-team progress + metrics)
- `risk-register.md` (current risks, owners, mitigations)
- `stakeholder-map.md` (who cares about what, influence/interest grid)
- `budget-tracker.xlsx` (spend vs. plan)

**When dealing with vendor issues** → Load:
- `cloudforge-contract.pdf` (SLAs, escalation clauses)
- `vendor-communication-log.md` (all interactions, commitments made)
- `escalation-playbook.md` (who to contact, what leverage we have)

**When resolving team conflicts** → Load:
- `architecture-decision-records/` (ADRs for all platform decisions)
- `team-feedback-log.md` (concerns raised, how they were addressed)
- `raci-matrix.md` (who decides what)

**When updating executives** → Load:
- `exec-summary-template.md` (Vanessa's preferred format: status, risks, asks)
- `metrics-dashboard` (Jira velocity, migration completion %, test coverage)

---

## 📓 Session Log

| Date | Summary |
|------|---------|
| 2026-05-28 | Identified CloudForge escalation path. Drafted email to Angela Reeves. Reviewed Identity architecture dispute — documented both positions. Prepped 6/3 API spec meeting agenda. |
| 2026-05-23 | Steering committee debrief — Vanessa accepted yellow status but wants recovery plan by 6/10. Payments team pulled in their timeline (good news). Devon no-showed our 1:1 (concerning). |
| 2026-05-20 | Month 3 budget review with Diane — on track. Identified training materials gap with Fiona. Sent stakeholder pulse survey. |

---

## 🔟 Tenth Man Audit (Last run: 2026-05-28)

- ⚠️ **Escalation gap:** CloudForge vendor issue has been "overdue" for 5 days with no documented escalation action taken. If the connector is late, Notifications timeline is dead.
- ⚠️ **People risk:** Devon Williams (Notifications EM) no-showed a 1:1 and his team hasn't started work. This may be passive resistance, not just disengagement. Needs a direct conversation — possibly with Vanessa's backing.
- ⚠️ **Optimism bias:** Payments being ahead of schedule doesn't mean Identity/Notifications will recover. The "model team" narrative may be creating false confidence in steering committee.
- ⚠️ **Staleness:** Risk register hasn't been updated since 5/22 despite 3 new risks identified. This is the primary governance artifact — must stay current.
- ✅ Budget tracking is clean and current.
- ✅ Steering committee cadence is working — exec sponsor is engaged.

---

## 📊 Program Metrics (Month 3 Snapshot)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Migration completion (services) | 35% | 28% | 🟡 |
| Budget consumed | 40% | 40% | 🟢 |
| Critical risks open | ≤3 | 5 | 🔴 |
| Team satisfaction (1-5) | ≥3.5 | 3.1 | 🟡 |
| Training materials complete | 80% | 60% | 🟡 |

---

*Cross-references: Jira board → ATLAS-NEXUS project. Risk register → Confluence/Migration/Risks. Vendor contract → Legal shared drive. Architecture decisions → ADR repo.*
