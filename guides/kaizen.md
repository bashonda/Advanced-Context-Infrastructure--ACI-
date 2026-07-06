# Kaizen: The Continuous Improvement Engine

> **Philosophy:** "Based on what happened today, what should we do differently tomorrow?"  
> **When to run:** End of every business day (not every session).  
> **Key rule:** Kaizen proposes, human approves. Never auto-executes.

---

## What Is Kaizen?

Kaizen (改善) is the Japanese philosophy of continuous improvement through small, incremental changes. In the context of your SOT system, it means:

- Observing what worked and what didn't today
- Proposing specific, evidence-based improvements
- Implementing only what the human approves
- Tracking outcomes to learn what actually helps

It's not about big redesigns. It's about 1% better every day.

---

## When to Run

**End of every business day** — not every session.

If you have 3 sessions in a day, Kaizen runs once at the end of the last session. It looks across the entire day's work, not just one conversation.

**Why not every session?**
- Too frequent = improvement fatigue
- Daily cadence gives enough data to spot patterns
- Respects the human's decision-making energy

**Exception:** If something clearly broke during a session (wrong context loaded, critical info missing, system failure), note it immediately for the Kaizen review.

---

## What It Produces

A Kaizen review produces **specific, evidence-based improvement proposals**. Not vague suggestions — concrete changes with clear rationale.

### Bad Kaizen Output:
> "We should organize things better."

### Good Kaizen Output:
> "**Observation:** Today we needed Q1 vendor pricing 3 times but had to search deep memory each time.  
> **Proposal:** Create a 'vendor-pricing-summary.md' seed in the seeds/ directory with key rates and contract dates.  
> **Expected benefit:** Eliminates repeated deep memory lookups for frequently-referenced data.  
> **Effort:** 10 minutes to create."

---

## The Golden Rule

> **Kaizen proposes, human approves. Never auto-executes.**

The AI should never:
- Restructure files without permission
- Change the system architecture unilaterally
- Implement improvements silently
- Assume approval from lack of objection

The AI should always:
- Present the observation and evidence
- Propose a specific change
- Wait for explicit approval
- Implement only after "yes"

This protects against well-intentioned changes that break things the AI doesn't fully understand.

---

## Improvement Log Format

Track all proposals in a structured log:

```markdown
## Improvement Log

| ID | Date | Observation | Proposal | Status | Outcome |
|----|------|-------------|----------|--------|---------|
| K-001 | 2024-06-01 | Migration status asked 4x this week, always stale | Add "last verified" date to migration entity | ✅ Approved | Reduced stale-status findings by 80% |
| K-002 | 2024-06-01 | People file has 3 people who left the company | Add "departed" section, move inactive people there | ✅ Approved | Cleaner active roster |
| K-003 | 2024-06-02 | Session logs growing fast, rarely re-read | Seed logs older than 2 weeks automatically (with approval) | ❌ Rejected | Human prefers manual seeding |
| K-004 | 2024-06-03 | Vendor discussions always need contract dates | Add contract summary table to operational index | ⏳ Pending | — |
```

### Status Values:
- ⏳ **Pending** — Proposed, awaiting human decision
- ✅ **Approved** — Implemented
- ❌ **Rejected** — Declined (note why, to avoid re-proposing)
- 🔄 **Revised** — Modified based on feedback, re-proposed

---

## Categories of Improvement

### 1. System Improvements
Changes to the SOT architecture itself:
- Adding or removing files
- Changing what's in core vs. entities
- Modifying the operational index structure
- Adjusting memory tier boundaries

**Example:**
> **K-005:** Observation: The recipes-playbook.md file is 80% deployment procedures that only matter on deploy days. Proposal: Extract deployment recipes into entities/domains/deployment.md, load only on deploy days. Saves ~400 lines of context window on non-deploy sessions.

### 2. Workflow Improvements
Changes to how sessions are conducted:
- Session ritual adjustments
- New checks or steps
- Removing unnecessary steps
- Changing when things happen

**Example:**
> **K-006:** Observation: We always forget to check the shared Slack channel for updates before starting work. Proposal: Add "Check #platform-updates channel" to session start ritual, step 4. Takes 30 seconds, prevents working on stale assumptions.

### 3. Quality Improvements
Changes to accuracy, completeness, or reliability:
- New Tenth Man checks
- Better cross-referencing
- Validation rules
- Formatting standards

**Example:**
> **K-007:** Observation: Dates in the SOT use 3 different formats (June 1, 6/1, 2024-06-01). Proposal: Standardize on ISO format (YYYY-MM-DD) everywhere. Reduces ambiguity, especially for deadlines.

---

## Running the Kaizen Review

At the end of the last session of the business day, the AI should:

### 1. Reflect on the day's sessions
- What went well?
- What was friction?
- What information was missing when needed?
- What information was present but irrelevant?

### 2. Check for patterns
- Is this the first time this issue appeared, or recurring?
- Did a previous improvement help or not?
- Are there systemic issues (not just one-off problems)?

### 3. Propose improvements (if any)
- Be specific: what exactly would change?
- Be evidence-based: what happened that prompted this?
- Be realistic: is this worth the effort?
- Be humble: propose, don't prescribe

### 4. Review pending proposals
- Any pending items that should be re-raised?
- Any approved items that need outcome tracking?
- Any rejected items that should be reconsidered given new evidence?

---

## Example Kaizen Review

> **Kaizen Review — 2024-06-03**
> 
> **Today's sessions:** 2 sessions (morning: migration planning, afternoon: side project brainstorm)
> 
> **What went well:**
> - Migration entity file had exactly the context needed for the planning discussion
> - People reference correctly noted Marcus's communication preferences, which helped draft the status update
> 
> **Friction observed:**
> - During the side project session, I loaded all migration context unnecessarily (it's marked "active" in the index). Wasted ~300 lines of context window.
> - Needed the user research notes from 2 weeks ago but they'd already been seeded. The seed was sufficient but took an extra load step.
> 
> **Proposals:**
> 
> | ID | Observation | Proposal |
> |----|-------------|----------|
> | K-008 | Migration context loaded during unrelated sessions | Add "domain tags" to operational index so entities only load when their domain is relevant |
> | K-009 | User research seed was sufficient but required extra step | No change needed — system working as designed. The extra step is acceptable. |
> 
> **Pending review:**
> - K-004 (vendor contract table) — still pending. Raising again: this would have helped today when discussing renewal timeline.

---

## Anti-Patterns

Things Kaizen should NOT do:

| Anti-Pattern | Why It's Bad |
|-------------|-------------|
| Proposing changes every single day | Improvement fatigue. Only propose when there's real evidence. |
| Vague proposals ("be more organized") | Can't be implemented or measured |
| Re-proposing rejected items without new evidence | Disrespects human decision |
| Optimizing for edge cases | Don't redesign the system for something that happens once a month |
| Changing things that work | If it ain't broke, don't Kaizen it |

---

## Measuring Success

How do you know Kaizen is working?

- **Tenth Man findings decrease over time** — fewer stale items, fewer contradictions
- **Session start is faster** — less irrelevant context loaded
- **Less "where is that?" moments** — information is findable
- **Fewer repeated explanations** — context persists reliably
- **The system feels lighter** — not heavier — over time

If your system is getting more complex without getting more useful, Kaizen has gone wrong. Simplification is a valid improvement.

---

*Kaizen is the engine that keeps your context system evolving with you. Small daily improvements compound into a system that fits your work perfectly — because it was shaped by your actual work, one day at a time.*
