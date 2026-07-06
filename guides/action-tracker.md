# Guide: The Action Tracker

> One canonical list of open actions, surfaced every session start.

## The Problem

In a Level 3 system, your open action items naturally end up scattered:

- Some in your **source-of-truth priority tables** (P0, This Week, Watchlist...)
- Some buried inside **session-log prose** ("...send the deck by Friday")
- Some only in **a meeting's notes**
- Some only in **your head**

Each location is individually reasonable. Collectively, they guarantee one thing: you
will *feel* like you're forgetting something — and you'll be right. There is no single
surface that answers "what do I actually owe right now?"

## The Fix

A dedicated **Action Tracker** core file (`action-tracker.md`) that is:

1. **Canonical** — the one place open actions live.
2. **An extract, not a replacement** — full context stays in your SOT priority tiers;
   this is the scannable "to-do" layer pulled from them.
3. **Surfaced every session start** — the AI reads it and leads the session brief with
   your open 🔴 / 🟠 items.
4. **Continuously maintained** — the moment an action is captured anywhere in a session,
   the AI also writes it here. Closed items are marked done and archived next session.

## Why It Works

- **Single source of scan.** You look in one place, every day. No reconciliation across
  five tables.
- **The AI owns upkeep.** You don't maintain a separate to-do app that drifts out of
  sync. The tracker is updated as a side effect of normal session work.
- **Status at a glance.** The 🔴/🟠/🟡/🟢/⏸️ taxonomy means you instantly see what's on
  fire vs. parked vs. waiting on someone.
- **Deferred ≠ dropped.** The ⏸️ status captures "I can't act until X" so blocked items
  stay visible instead of silently vanishing.

## Setup

1. Copy `templates/level-3-action-tracker.md` into your system as `action-tracker.md`.
2. **Seed it once:** ask your AI to sweep your existing SOT priority tables AND your
   recent session logs and compile every open action you own into the tracker. (This
   first compile is usually eye-opening — expect more items than you thought.)
3. **Wire it into your session ritual / router** so it's read at the start of every
   session and surfaced as an "Open Actions" block.
4. **Add a maintenance rule to your quality file:** "Any newly-captured action item is
   written to the Action Tracker in the same session. Closed items are marked done and
   archived at the next session."

## Status Taxonomy

| Status | Meaning |
|--------|---------|
| 🔴 | Overdue or urgent — blocking someone, or past due |
| 🟠 | Active this week — you intend to move it now |
| 🟡 | Open, no deadline — real but not time-boxed |
| 🟢 | Done — keep one session for visibility, then archive |
| ⏸️ | Deferred — waiting on a person, event, or upstream decision |

## What NOT to Put Here

- **Fully delegated items.** If someone else owns it end-to-end, it lives in their entity
  file. Only put it here if *you* have an action on it.
- **Full context.** Keep rows terse. The "why" lives in your SOT; link to it via the
  cross-reference column.
- **Reference material.** This is actions, not notes.

## The Payoff

The first time you run a clean session start and your AI opens with *"Here are your 3 red
and 7 amber open actions"* — pulled automatically, every day — the scattered-to-do
anxiety disappears. You stop wondering what you forgot, because there's one place that
always knows.
