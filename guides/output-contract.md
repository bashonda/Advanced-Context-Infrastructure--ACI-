# The Output Contract — Freezing Your Best Session So It Can't Regress

Two related patterns for the DP tier (deterministic spec, probabilistic
executor — see `deterministic-vs-probabilistic.md`): the **session brief
output contract** and the **write-verification mandate**. Both exist because
an LLM executing a written rule drifts unless the spec is tight and the
mechanical parts are verified.

---

## Pattern 1: Session Brief Output Contract

### The problem

Your session-start protocol lists *what to gather* (read core files, check
messages, scan channels, review actions). One day the AI synthesizes all of
it into a genuinely exceptional brief. You say "do it like that every time."

Without an explicit output contract, it won't. The gathering steps are
written down; the *presentation quality* lives in one session's context and
evaporates. Within weeks you're back to walls of raw tool output.

### The fix: spec the output, not just the process

Add a required output format to your protocol — structure AND quality bar:

**Required structure (adapt sections to your world):**

| # | Section | What it must contain |
|---|---------|----------------------|
| 1 | Confirmation | One line: core files read, date verified |
| 2 | Today's shape | Not a calendar dump — the *shape* of the day, the 1–2 things that matter, prep pointers |
| 3 | Unanswered items | Each one status-reasoned: answered / blocked-on-X / truly open |
| 4 | Signal scan | Tiered (needs-you / FYI / noise-collapsed), each tied to a priority |
| 5 | Open actions | Extract of the urgent tier only — not the whole tracker |
| 6 | Health check | One-liner per domain you track, only calling out movement |
| 7 | Audit flags | Staleness/contradictions found, each as Finding → Fix |
| 8 | Close | 2–4 concrete next-move options — a real question, never "what now?" |

**Quality bar (the part that actually prevents regression):**

1. **Synthesize, don't dump.** Raw data in, meaning out. A message becomes
   its *status*, not its existence.
2. **Lead with what's time-sensitive.** Not a fixed-order recital.
3. **Status-reason every flag.** Say where each item stands and *why*, so
   the human knows what needs them vs. what's handled.
4. **Tier ruthlessly.** Don't make the human sort.
5. **Close with a focused question.** Tied to today's real options.

### Why it works

The structure is checkable — a session brief either has 8 sections or it
doesn't. That converts "be excellent" (pure P, unenforceable) into a spec
the executor can be held to (DP with a tight contract). Drift becomes
visible the moment it starts.

---

## Pattern 2: Write-Verification Mandate

### The problem

The AI edits an external artifact (a doc, a message, a deployment) and
reports "✅ done." Sometimes the edit never landed — the tool returned
success, the content didn't change, and the false claim ships wrong
information to people who trusted it. This failure mode is *documented from
production*: an AI claimed two document edits were complete when neither
had landed, caught only because the human happened to re-read the doc.

### The fix: a deterministic verify loop on every external write

Hard rule — the AI may never report an external write as "done" until:

1. **Execute** the write.
2. **Read the target back** (re-fetch the doc / range / message).
3. **Explicit pass/fail check on the exact change** — new content present
   AND old content gone (for replaces/deletes).
4. Only then claim success. If verification can't run, say **"submitted but
   unverified"** — never "done."

### The principle

A tool returning HTTP 200 is not the same as the change being present.
"Done" requires *verified* evidence. This is the hybrid architecture in
miniature: the probabilistic agent decides what to write; a deterministic
procedure verifies that reality changed accordingly.

---

## Adopting both

Add them to your quality contract as hard rules, tagged **DP** (brief
contract) and **DP+D** (write verification — prose rule plus mechanical
verify step). Then let your weekly review ask the standard question: *did
either drift this week?*
