# Tenth Man: The Self-Correction Layer

> **What it is:** A structured audit protocol that catches context rot before it causes problems.  
> **When to run:** Start AND end of every session.  
> **Time required:** 2–5 minutes per run.

---

## Origin

The Tenth Man doctrine comes from Israeli military intelligence. The rule:

> **If nine people in the room agree on a conclusion, it is the duty of the tenth to disagree and explore alternatives.**

After intelligence failures where groupthink led to missed threats, the IDF institutionalized structured dissent. Someone must always ask: "What if we're wrong?"

Applied to context systems: your SOT will silently rot unless something actively challenges it. The Tenth Man protocol is that something.

---

## Why It Matters

Context rot is invisible. It doesn't announce itself. Consider:

- A priority you marked "active" three weeks ago that you quietly abandoned
- A person's role that changed but the file still says the old title
- A decision you made based on an assumption that's no longer true
- A project status that says "on track" when it's actually blocked

Without active auditing, your AI operates on stale context and gives you confidently wrong answers. The Tenth Man catches this.

---

## The 8-Point Audit Checklist

Run through these eight checks at the start and end of every session:

### 1. Staleness

**Question:** Are there facts that might be outdated?

Look for:
- Dates that have passed without status updates
- "Temporary" states that have persisted too long
- People in roles they may have left
- Numbers or metrics from weeks/months ago

**Example finding:**
> ⚠️ STALE: "Migration at 60% complete" — last updated 3 weeks ago. Likely higher or blocked.

---

### 2. Contradictions

**Question:** Is the same fact stated differently in two places?

Look for:
- Different dates for the same deadline
- Different owners for the same project
- Status described differently in different files
- Numbers that don't match

**Example finding:**
> ⚠️ CONTRADICTION: source-of-truth.md says migration deadline is "Sept 15" but projects-reference.md says "Sept 22" (updated last session).

---

### 3. Gaps

**Question:** Were things discussed but never captured?

Look for:
- Decisions made verbally but not documented
- New people mentioned but not added to people reference
- Action items from last session with no follow-up
- Topics discussed at length with no SOT trace

**Example finding:**
> ⚠️ GAP: Last session we discussed hiring a contractor for the API work. No entry in projects or people files.

---

### 4. Changed Truth

**Question:** Have opinions, relationships, or situations evolved?

Look for:
- Relationships described in terms that no longer fit
- Strategies that shifted but the SOT still reflects the old approach
- Assessments ("this is going well") that may no longer be accurate
- Priorities that shifted in practice but not on paper

**Example finding:**
> ⚠️ CHANGED TRUTH: People reference describes Marcus as "temporary acting manager" — it's been 2 months. This may be permanent.

---

### 5. Cascade Risk

**Question:** If a base assumption changed, what else is now wrong?

This is the most powerful check. When you find one stale fact, trace its implications:

- If the deadline moved, are downstream dependencies still valid?
- If a person left, who owns their responsibilities now?
- If a strategy changed, are the projects still aligned?

**Example finding:**
> ⚠️ CASCADE: If migration deadline moved to Sept 22, then the Q3 planning doc (which assumes Sept 15 completion) needs revision. Also affects Acme Cloud contract renewal timeline.

---

### 6. Seed Candidates

**Question:** Is there resolved content that should be compressed?

Look for:
- Completed projects still taking up active space
- Decisions that were made and don't need the full deliberation history
- Session logs older than 2 weeks
- Context that's "done" but still loaded every session

**Example finding:**
> 💡 SEED CANDIDATE: The "Office Move" project completed 3 weeks ago. 45 lines of active context could be compressed to a 15-line seed.

---

### 7. Challenge

**Question:** Are there unvalidated claims or assumptions?

Look for:
- Things stated as fact that haven't been verified
- Assumptions about what others think or will do
- Predictions treated as certainties
- "I think" statements that hardened into "facts" over time

**Example finding:**
> ⚠️ CHALLENGE: SOT states "Marcus prefers data over opinions" — based on one interaction. May not be universally true. Validate.

---

### 8. Honest Findings

**Question:** Are failures and weaknesses captured, not just wins?

Look for:
- Projects described only in positive terms despite known issues
- Missing acknowledgment of missed deadlines or mistakes
- Relationships described as better than they are
- Capabilities overstated

**Example finding:**
> ⚠️ HONESTY: Projects file shows migration "on track" but we've missed two internal milestones. Should reflect actual status.

---

## When to Run

| Timing | Focus | Purpose |
|--------|-------|---------|
| **Session start** | Checks 1–5, 7 | Catch rot before it affects today's work |
| **Session end** | Checks 3, 6, 8 | Catch gaps from today's session |
| **Weekly deep audit** | All 8, thorough | Comprehensive review |

At session start, the audit is quick — scan for obvious staleness and contradictions. At session end, focus on what might have been missed from today's discussion.

---

## The Sizing Principle

> **Active Memory must be big enough for Tenth Man to catch things it wasn't looking for.**

This is critical. If your active memory is too compressed, the Tenth Man can only check what's explicitly there. It can't notice that something is *missing* if it never saw it.

The right size for active memory is: large enough that during a routine audit, you occasionally notice unexpected connections, staleness, or gaps. If every audit comes back clean, your active memory might be too small (hiding problems in deep storage).

---

## Running the Audit in Practice

You don't need to formally announce "running Tenth Man." In practice, it sounds like:

**Session start:**
> "I've read your SOT files. A few things I want to flag:
> - The migration status hasn't been updated in 2 weeks — is it still at 60%?
> - Your people file still lists Sarah as 'on leave until July' — it's now August. What's her status?
> - Last session you mentioned talking to a recruiter about the senior eng hire — I don't see that captured anywhere."

**Session end:**
> "Before we wrap up, a few audit notes:
> - We discussed changing the API approach today but I didn't update the migration entity file — should I?
> - The Q1 session logs are 3 weeks old and resolved — good seed candidate.
> - You mentioned frustration with the vendor timeline but the vendor file still says 'relationship: strong.' Want me to add nuance?"

---

## Key Principles

1. **Dissent is a feature, not a bug.** The Tenth Man's job is to find problems. A clean audit is suspicious.

2. **Small findings prevent big failures.** Catching a stale date today prevents a wrong decision next week.

3. **Run it even when you're in a hurry.** Especially when you're in a hurry — that's when context rot accelerates.

4. **The AI should flag, not fix.** Present findings and let the human decide what to do. Don't silently "correct" things.

5. **Track patterns.** If the same type of finding keeps appearing (e.g., people roles going stale), that's a systemic issue to address.

---

*The Tenth Man is what separates a living context system from a slowly-rotting document. It's 2–5 minutes of structured skepticism that keeps everything else honest.*
