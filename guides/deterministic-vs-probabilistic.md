# Deterministic vs. Probabilistic — Tag Every Rule, Action, and Agent

**The v2 organizing principle.** As your context infrastructure matures, the
single most important discipline is knowing — and *explicitly labeling* —
which parts of your system are deterministic and which are probabilistic.
Consistency depends on it. So does your ability to adapt quickly, because
the label tells you exactly where a failure can be *fixed permanently*
versus merely *coached*.

---

## The three tiers (not two)

Most writing on this topic stops at two categories: deterministic code vs.
probabilistic models. In a real AI-partnership system there is a third tier
in the middle — and it's where most of your rules actually live, and where
most of your failures actually happen.

| Tier | What it is | Same input → same output? | Failure mode |
|------|-----------|---------------------------|--------------|
| **D — Deterministic** | Code. Scripts, SQL, cron jobs, hard-coded thresholds. | Always | Bugs — findable, fixable, fixed forever |
| **DP — Deterministic spec, Probabilistic executor** | A hard rule written in prose, executed by an LLM. The *specification* is exact; the *execution* is pattern-matched. | Usually — but degrades silently | **Drift** — the rule stays written down while adherence quietly erodes |
| **P — Probabilistic** | Judgment, synthesis, drafting, relevance scoring. Variation is the point. | No — by design | "Almost right, but not quite" |

**The content files in your vault are none of these** — they're passive
repositories. The D/DP/P distinction applies to the rules, actions, and
agents that *fire against* the content. Keep those two ideas separate:
nodes are what's known; rules are what runs.

---

## Why the middle tier matters most

The DP tier is invisible in most frameworks, and it's the most dangerous:

- A **D** failure announces itself (the script errors, the query returns
  garbage). You fix the code once.
- A **P** failure is expected and priced in (you review drafts, you verify
  recommendations).
- A **DP** failure is *silent*. The rule is still written in your quality
  contract. The AI still "knows" it. But execution drifts — a step gets
  skipped, a format erodes, a check gets summarized instead of run. Nothing
  errors. You discover it weeks later when something slips through.

Two real examples from the production system this framework comes from:

1. **The false "done" claim.** The AI reported "✅ document updated" on an
   external edit — and the edit had never landed. The fix was not "try
   harder": it was bolting a *deterministic procedure* onto the
   probabilistic executor — a mandatory read-back-and-verify step with an
   explicit pass/fail check before "done" may be claimed. DP rule, hardened
   with a D verification loop.
2. **The exceptional session that almost regressed.** A session-start
   briefing hit a quality bar the user wanted permanently. The *steps* were
   already written down (DP) — but the *output contract* wasn't, so quality
   was one lazy session away from eroding. The fix: freeze the output format
   as an explicit 8-section structure with a 5-point quality bar. Still DP —
   but a *tighter spec* dramatically narrows the executor's room to drift.

---

## The hardening ladder

The evolution pattern that emerges over dozens of sessions:

```
P  (the AI just... usually does it)
      │  fails or matters enough → write it down
      ▼
DP (written rule, LLM-executed)
      │  drifts or fails twice → harden the mechanical part
      ▼
D  (script / procedure / check — code does the invariant part;
    the LLM keeps only the judgment part)
```

**Rule of thumb: when a probabilistic behavior fails twice, harden it one
tier down.** Not the whole behavior — just the part that can be made
mechanical. Real examples of the ladder in action:

- *"Check for unanswered messages at session start"* began as habit (P) →
  became a written protocol step (DP) → a local read-only poller made the
  **collection** deterministic (D), leaving only the **judgment** of what
  matters probabilistic. Hybrid, by design.
- *"Flag stale files"* began as an audit instinct (P) → a written >2-week
  threshold (DP) → a script that computes staleness from file dates (D).
  The number never lies now; deciding what to *do* about a stale file is
  still judgment.

This is the hybrid architecture pattern: **probabilistic interprets messy
inputs and exercises judgment; deterministic executes actions and verifies
outcomes.** Push mechanical work down the ladder; keep judgment at the top.

---

## How to implement: tag your rules

In your quality contract (or wherever your hard rules live), add a tier tag
to every rule and recurring action:

```markdown
| Rule | Tier | Hardening |
|------|------|-----------|
| Weekly structural audit of the vault | D | `tools/vault_map.py` — script |
| Never claim an external write succeeded without read-back | DP+D | prose rule + mandatory verify procedure |
| Session brief follows the 8-section output contract | DP | tight spec (structure + quality bar) |
| Score incoming messages against current priorities | P | judgment — review, don't automate |
| Message collection for the session-start scan | D | local poller script |
| Drafting stakeholder communications | P | always human-reviewed before send |
```

Three payoffs:

1. **Consistency** — you know which behaviors you can *rely* on versus
   which you must *review*. Trust is allocated correctly.
2. **Debuggability** — when something fails, the tag tells you the fix
   class: patch code (D), tighten the spec or add a verify step (DP), or
   accept variance and add review (P).
3. **Nimbleness** — when you want to change behavior, D changes are a code
   edit (instant, permanent), DP changes are a spec edit (fast, needs a
   drift-watch), P changes are persona/prompt calibration (iterative).

## Audit question for your weekly review

> "Which DP rules failed or drifted this week — and is any of them ready to
> move down the ladder?"

Add it to your continuous-improvement ritual. The framework's own history
is largely a log of exactly these migrations — that's not an accident,
that's the system working.
