# Session Ritual: Start and End Protocols

> **What it is:** A repeatable protocol for beginning and ending every AI session to maintain context integrity.  
> **Why it matters:** Without rituals, context rots between sessions. With them, every session builds on the last.

---

## Session Start Protocol

Every session begins with these steps, in order:

### Step 1: Read Core Files

The AI reads all SOT files relevant to the current architecture level:

**Level 1:** Read the single SOT file  
**Level 2:** Read all 4–5 specialized files  
**Level 3:** Read core files + operational index + active entities

This gives the AI full context before any work begins.

**What "read" means:** Actually process the content, not just acknowledge the files exist. The AI should be able to answer questions about current state without re-reading.

---

### Step 1b: Publish the Vault Map (if you use the tooling)

Regenerate and open the local vault map (`python3 tools/vault_map.py`) so
the human *sees* the vault's current state — structure, heat, staleness —
before work begins. New audit findings feed the Tenth Man step below.
Vault health becomes ambient instead of pull-only. (Local file only —
never deploy the map; it renders your vault's content.)

---

### Step 2: Run Tenth Man Audit

Before diving into work, run a quick audit (see `tenth-man.md` for full protocol):

- Scan for staleness (dates passed, statuses unchanged too long)
- Check for contradictions across files
- Note any gaps from previous sessions
- Flag cascade risks if base assumptions may have changed

**This takes 1–2 minutes.** It's not a deep review — it's a quick scan that catches obvious rot.

**Example output:**
> "I've reviewed your SOT. Two flags:
> 1. The Q3 planning doc was due Friday — no update on whether it was submitted.
> 2. People reference still shows Sarah on leave, but her return date was last week.
> 
> Want to address these before we start, or shall we proceed?"

---

### Step 3: Surface Relevant Context

Based on what the AI knows about today's likely topics, proactively surface:

- **Upcoming deadlines** (next 7 days)
- **Open items** from previous sessions
- **Blocked work** that might be unblocked now
- **Scheduled events** that affect priorities

**Example:**
> "Relevant context for today:
> - Migration API cutover is scheduled for tomorrow (June 4)
> - You have 2 candidates in final round — decision needed by EOW
> - Last session you asked me to remind you to follow up with Jake about the prototype"

---

### Step 4: Check for New Information (if tools available)

If the AI has access to communication tools (Slack, email, etc.):

- Check relevant channels for updates since last session
- Flag any messages that affect active priorities
- Note any new information that should be captured in the SOT

**If no tools available:** Skip this step. The human will bring new information as needed.

---

## Session End Protocol

Every session ends with these steps before closing:

### Step 1: Update Affected Files

Identify what changed during the session and update the appropriate files:

- New decisions → projects file or entity file
- New people mentioned → people reference
- Status changes → source of truth + relevant entity
- New procedures learned → recipes/playbook

**Key rule:** Update only files that actually changed. Don't touch files with no new information.

**Example:**
> "Updating based on today's session:
> - `source-of-truth.md` — Priority #1 updated (migration cutover moved to June 7)
> - `entities/projects/platform-migration.md` — Added risk note about API compatibility issue
> - No changes needed to people-reference.md or quality-contract.md"

---

### Step 2: Add Session Log Entry

Add a concise entry to the session log in source-of-truth.md:

```markdown
- **2024-06-03** — Discussed migration cutover delay (moved to June 7 due to API 
  compatibility issue found in testing). Drafted risk mitigation plan. Reviewed 
  2 engineering candidates — leaning toward Candidate A (stronger system design).
```

**What makes a good session log entry:**
- Date
- Key topics discussed (not every detail)
- Decisions made
- Action items created
- Status changes

**What makes a bad session log entry:**
- Too vague: "Discussed work stuff"
- Too detailed: Full transcript of the conversation
- Missing decisions: Lists topics but not outcomes

---

### Step 3: Update Timestamps and Versions

Every file that was modified gets its "Last updated" timestamp refreshed:

```markdown
# Source of Truth
Last updated: 2024-06-03
```

This serves two purposes:
1. Tenth Man can spot stale files (old timestamps = potential rot)
2. Humans can quickly see what's current

---

### Step 4: Check Cross-References

If new information was added, verify it lives in the right canonical location:

- Did we add a person? → Canonical in people-reference, pointer elsewhere
- Did we add a project detail? → Canonical in project entity, pointer in SOT
- Did we add a procedure? → Canonical in recipes/playbook

**The rule:** Every fact lives in ONE place. Everywhere else gets a pointer.

**Quick check:**
> "New info added today: API compatibility issue. Canonical location: platform-migration.md entity file. Cross-reference added to source-of-truth.md priority #1. ✓"

---

### Step 5: Run Tenth Man (End Pass)

Run the audit again, focused on today's session:

- **Gaps:** Did we discuss anything that didn't get captured?
- **Seed candidates:** Did anything get resolved that should be compressed?
- **Honest findings:** Are we representing today's outcomes accurately (including setbacks)?

This is lighter than the start-of-session audit. It's focused on: "Did we capture everything from today?"

---

### Step 5b: Commit + Republish the Vault Map (if you use the tooling)

After updates are written: `git add -A && git commit -m "Session N — summary"`
(local repo, no remote), then regenerate and reopen the vault map. The human
sees what the session *changed* as a visual diff — new nodes, closed gaps,
staleness movement. One line of narration is enough: "added 1 workstream
file, closed 2 declared-vs-actual gaps." Git holds the textual diff; the
map shows the structural one. Bookending every session this way makes the
vault's evolution visible instead of abstract.

---

### Step 6: If Last Session of Day → Run Kaizen

If this is the final session of the business day, run the Kaizen review (see `kaizen.md`):

- Reflect on the day's sessions
- Identify friction or inefficiency
- Propose improvements (if warranted)
- Review pending improvement proposals

**Not every day produces a Kaizen proposal.** Some days the system works perfectly. That's fine.

---

## Handling Multi-Topic Sessions

When a session covers multiple unrelated topics:

### During the session:
- Work normally — context switching is fine
- The AI tracks which files each topic relates to

### At session end:
- Update ALL affected files (may be more than usual)
- Session log entry covers all topics, grouped:

```markdown
- **2024-06-03** — 
  - Migration: Cutover delayed to June 7 (API compatibility). Risk plan drafted.
  - Hiring: Reviewed candidates A and B. Leaning A. Decision by Friday.
  - Side project: Brainstormed pricing models. Decided on freemium. Jake to prototype.
```

### Cross-file consistency:
Multi-topic sessions are where contradictions sneak in. Extra attention on Step 4 (cross-references).

---

## Handling Interrupted Sessions

Sometimes sessions end abruptly (connection lost, emergency, time runs out):

### If you can do a quick wrap:
- Minimal session log entry ("Session interrupted. Discussed X, no decisions finalized.")
- Skip the full end protocol — do it at the start of next session instead

### If the session just ends:
- Next session start should include: "Last session may have ended abruptly. Let me check what was captured..."
- Run a slightly more thorough Tenth Man to catch gaps

---

## Timing Guide

| Step | Time | Notes |
|------|------|-------|
| **Start: Read files** | 30–60 sec | AI processing time |
| **Start: Tenth Man** | 1–2 min | Quick scan, not deep dive |
| **Start: Surface context** | 30 sec | Brief, relevant items only |
| **Start: Check messages** | 1–2 min | Skip if no tools available |
| **End: Update files** | 2–3 min | Only changed files |
| **End: Session log** | 1 min | Concise entry |
| **End: Timestamps** | 10 sec | Quick update |
| **End: Cross-references** | 30 sec | Quick check |
| **End: Tenth Man** | 1–2 min | Focused on today |
| **End: Kaizen** | 3–5 min | Only last session of day |

**Total overhead:** ~5 min at start, ~5 min at end (10 min on Kaizen days).

This is a small investment for persistent, accurate, self-correcting context.

---

## Tips

1. **Don't skip the ritual when you're busy.** That's when context rot accelerates fastest.

2. **The start ritual prevents wasted time.** 2 minutes of context loading saves 10 minutes of re-explanation.

3. **Session logs are for future-you.** Write them so that in 3 weeks, you can understand what happened without re-reading the full conversation.

4. **Let the AI drive the ritual.** Once trained, it should do this automatically. You just confirm.

5. **Adapt the ritual to your style.** If Step 4 (cross-references) never catches anything, simplify it. If Tenth Man consistently finds staleness, add a mid-session check.

---

*The session ritual is the heartbeat of your context system. It's what transforms a collection of files into a living, self-maintaining knowledge base. Skip it and entropy wins. Run it consistently and your AI gets smarter every session.*
