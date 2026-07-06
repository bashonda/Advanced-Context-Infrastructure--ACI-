# Getting Started: Zero to Working SOT in One Session

> **Time required:** 20–30 minutes  
> **Outcome:** A living document your AI reads every session, giving it persistent memory across conversations.

---

## What You're Building

A **Source of Truth (SOT)** — a single file your AI reads at the start of every session and updates at the end. Instead of re-explaining who you are, what you're working on, and what happened last time, the AI already knows.

Think of it as giving your AI a notebook it actually reads.

---

## Step 1: Copy the Template (2 min)

Copy `level-1-single-file.md` from the templates directory into your working directory:

```bash
cp templates/level-1-single-file.md ~/my-brain/source-of-truth.md
```

Pick any directory you want. This is where your AI will look. Some good options:
- `~/brain/`
- `~/ai-context/`
- A project-specific folder if this is project-scoped

---

## Step 2: Fill in Current State (5 min)

Open the file and fill in the **Current State** section. Write 3–5 sentences about:

- What's your primary focus right now?
- What happened recently that matters?
- Any deadlines or transitions in progress?

**Example:**
```markdown
## Current State
I'm a product manager at Acme Corp, 6 months into the role. Currently leading the Q3 
platform migration — we're 60% through and the deadline is Sept 15. My manager Sarah 
just went on leave so I'm reporting to VP of Eng (Marcus) temporarily. I'm also 
exploring a side project around AI-assisted meal planning.
```

Don't overthink it. Write what you'd tell a smart colleague on their first day.

---

## Step 3: Fill in Active Priorities (5 min)

List 3–7 things you're actively working on, in priority order:

**Example:**
```markdown
## Active Priorities
1. Platform migration — on track, next milestone is API cutover (June 3)
2. Q3 planning doc — draft due to Marcus by Friday
3. Hire senior engineer — 2 candidates in final round
4. Side project: meal planning app — validating idea, talked to 5 users
```

Include enough context that your AI can ask good follow-up questions or remind you of deadlines.

---

## Step 4: Fill in Key People (5 min)

List the people who come up in your work. Include role and one line of context:

**Example:**
```markdown
## Key People
- **Sarah Chen** — My manager (on leave until July). Supportive, prefers async updates.
- **Marcus Webb** — VP Eng, acting manager. Direct communicator, wants data not opinions.
- **Priya Patel** — Tech lead on migration. Brilliant but overloaded. Shield her from meetings.
- **Jake** — My co-founder on the side project. Works evenings/weekends only.
```

This prevents your AI from asking "who's Marcus?" every session.

---

## Step 5: Tell Your AI to Read the File (1 min)

At the start of your next session, tell your AI:

> "Read the file at ~/my-brain/source-of-truth.md — that's our shared context. Acknowledge what you see and surface anything relevant."

**Pro tip:** If your AI tool supports system prompts or session instructions, add this there so it happens automatically:

```
At the start of every session, read ~/my-brain/source-of-truth.md and briefly 
acknowledge the current state. Surface any upcoming deadlines or open items.
```

---

## Step 6: At Session End, Ask AI to Update (2 min)

Before ending any session where meaningful things happened, say:

> "Update the source of truth with what we discussed today. Add a session log entry."

Your AI will update priorities, add new people, adjust current state, and log what happened.

**Example session log entry:**
```markdown
### Session Log
- **2024-06-01** — Discussed migration risk with Priya. Moved API cutover to June 7. 
  Added risk mitigation plan. Drafted Q3 planning doc outline.
```

---

## Tips for Your First Week

1. **Don't aim for perfection.** A rough SOT that gets read every session beats a perfect document that's stale.

2. **Update every session.** The habit matters more than the content. Even "no changes" is a signal.

3. **Let it grow organically.** You'll discover what's useful to include after 3–4 sessions.

4. **Keep it honest.** Include failures, blockers, and uncertainties — not just wins. Your AI can only help with what it knows about.

5. **Read it yourself occasionally.** Once a week, skim your SOT. You'll catch stale items your AI missed.

---

## Common Mistakes

| Mistake | Why It Hurts | Fix |
|---------|-------------|-----|
| Too vague ("things are going well") | AI can't act on vibes | Add specifics: names, dates, numbers |
| Never updating | SOT becomes fiction | Update every session, even briefly |
| Including everything | AI drowns in noise | Only active/relevant items. Archive the rest. |
| No people section | AI asks "who?" constantly | 1 line per person is enough |
| Treating it as a journal | Grows unbounded, buries signal | SOT = current state, not history |

---

## When to Upgrade to Level 2

You're ready for Level 2 when:
- Your single file exceeds ~500 lines
- You're scrolling past irrelevant sections to find what matters
- You have multiple distinct domains (work + side project + personal)
- Your AI occasionally misses context because there's too much to parse

**Next:** Read `level-2-setup.md` for the migration guide.

---

## Quick Reference

| When | Do This |
|------|---------|
| Session start | AI reads the file, acknowledges context |
| During session | Work normally — AI has context |
| Session end | AI updates file, adds log entry |
| Weekly | Skim the file yourself, prune stale items |
| File > 500 lines | Consider Level 2 upgrade |

---

*You now have persistent AI memory. It's not magic — it's a file that gets read and written. But the compound effect over weeks is transformative.*
