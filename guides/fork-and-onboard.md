# Fork & Onboard — Scaling the Vault to a Team

## The insight

A mature vault has two separable layers:

1. **The architecture** — file structure, session ritual, quality contract,
   self-correction loops, tier rules. *Transferable.*
2. **The content** — your facts, your people, your priorities. *Personal.*

**Forking a vault = copy the architecture, zero the content.** A new person
doesn't start from a blank page and six months of trial-and-error; they
start from a proven structure on day one, and only have to supply what
they uniquely know: their own context.

This is what turns a personal memory system into a team-scalable one.

## When to fork

- **A new team member** wants what they've watched you do with your AI
  partner ("how do I get one of those?")
- **A departing colleague's scope lands on someone** — the absorber
  suddenly needs 2–3 people's worth of context under management (the
  original production case: one person absorbed three roles with zero
  backfills; an AI-augmented operating model was the only way it could
  work)
- **A new domain** is distinct enough to deserve its own vault rather than
  a directory in yours

## How to fork

### Step 1 — Ship templates, not your files

Never fork your actual vault (it's full of your sensitive content). Fork
the *shape*: this repository's `templates/` directory IS the forkable
layer. For a team, maintain a small `handover-templates/` set matching
your house style — your source-of-truth skeleton, people reference,
quality contract, operational index — with all content replaced by
placeholder prompts.

### Step 2 — Seed the minimum viable content (one session)

The new person's first session with their AI partner fills in:

- **Identity & role** — who am I, what do I own, who do I report to
- **People** — manager, directs, 5–10 key stakeholders (names + one line)
- **Active priorities** — the 5–10 things actually in flight
- **Quality contract** — adopt the standard rules as-is; customize later

Do NOT try to backfill history. The vault earns depth session by session —
that's how it stays true. A day-one vault with 100 accurate lines beats a
day-one vault with 2,000 imported, unverified ones.

### Step 3 — Inherit the ritual verbatim

The session start/end ritual, the self-correction audits, and the
continuous-improvement loop transfer unchanged. These are the parts that
took the longest to get right and are the least personal. The new adopter
runs the standard ritual from session one and only tunes it when their own
Kaizen log gives them evidence to.

### Step 4 — Let their improvement loop diverge

After the fork, the vaults evolve independently — same architecture,
different content, different Kaizen histories. Resist the urge to keep
them synchronized. What SHOULD flow between team vaults is *pattern-level*
learning ("we added an action tracker and it fixed slippage — you might
too"), not content.

## The upstream pattern

Treat your framework the way open source treats a library:

- **Upstream** (this repo / your team's fork of it): templates, guides,
  tools, lessons — generic, scrubbed, shareable
- **Downstream** (each person's vault): private instantiation

When someone's private Kaizen produces a generalizable pattern, it flows
UP as a scrubbed guide or template improvement. When the upstream improves,
adopters pull the *idea* down into their own vault at their own pace.
Content never flows up. Structure never stops flowing down.

## Onboarding an absorber (the hard case)

When someone inherits a departed colleague's scope, fork-and-onboard has a
special form:

1. Fork the architecture as above
2. Seed from the **transition document** (if one exists) — but tag every
   imported fact as unverified until the absorber confirms it in practice
3. Build the entity files for the inherited vendors/clients/programs FIRST
   — that's where the operational risk lives
4. Weekly staleness audits matter double: inherited context rots faster
   because the absorber can't yet tell stale from fresh

## What this replaces

Team context tools want to solve onboarding by giving everyone access to a
shared context pool. That pools *content* — including everyone's noise,
errors, and half-truths. Fork-and-onboard shares *structure and
discipline* and lets each person build content they can actually trust.
Share the how, not the what.
