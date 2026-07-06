# Guide: The Signal Scan

> Make your AI *push* you the things you'd otherwise miss — not just answer what you ask.

## Pull vs. Push

Most AI context systems are **pull**: you ask a question, the AI answers from its context.
That's powerful, but it has a blind spot — it only ever surfaces what *you think to ask
about*. The things that hurt are the things you *didn't know to look for*: a message in a
channel you weren't watching, an update from a colleague you didn't ping, a document
dropped somewhere off your radar.

The **Signal Scan** adds a *push* layer to your session start. Before you've asked
anything, the AI reviews your communication surfaces and tells you what's relevant to
your current priorities.

## The Trigger Story

This pattern usually gets built the day something important slips. A teammate posts a
critical file in a channel you're in but don't monitor closely. You find it hours later,
by luck. You think: *"If my AI had just surfaced that at session start, I'd never have
missed it."* That's the Signal Scan.

## The Architecture (4 Layers)

The same shape every good signal tool uses — commercial or homegrown:

| Layer | Job | In a SOT system |
|-------|-----|-----------------|
| **1. Scope** | Decide *where* to look (which channels / people / inboxes) | A curated watchlist |
| **2. Profile** | Decide *what matters* to this specific user | **Your SOT priorities ARE the profile** |
| **3. Score** | Rank each item for relevance | AI scores messages against your priorities + boosts for @mentions, links, key people |
| **4. Surface** | Deliver to where the user actually looks | A block in your session-start brief |

**The unfair advantage of a SOT system:** commercial tools have to *interview you* to
build an "interest profile." You already maintain a far better one — your source of truth.
The AI scores incoming signal directly against your live priorities. No separate profile
to build or keep in sync.

## People-First Scoping (the watchlist that doesn't rot)

When you choose *what* to scan, resist the urge to list topics — topic lists go stale fast.
Scope by **people and proximity** instead:

- **Your manager** + their direct-reports channel + each of their reports individually
- **Your skip-level's** reports (signals from anyone in that org, wherever they post)
- **Your own** direct reports
- **Your team's** channel(s)
- **Direct messages** and **@mentions** to you

This is self-curating: the people in your org graph are *definitionally* your signal, and
the list stays valid as topics come and go. Add specific topic channels only as a bonus
layer for rooms where you're not personally mentioned.

### The 60-day sunset rule

Any channel with no traffic for 60+ days gets *proposed for removal* at your weekly
review. Keeps the watchlist lean without manual policing. (Propose — never auto-drop.)

## Two Capture Modes

Depending on your tools' capabilities, you'll usually split the work:

- **Background collection** (optional, see "The Poller" below): a read-only job that
  pre-fetches messages from stable channels on a timer.
- **Live at session start:** the AI runs person-based and @mention searches in-session
  (these often need search permissions a background job lacks).

Both feed the same scoring + surfacing step.

## The Poller (optional background collector)

If you want the session-start scan to be *instant* rather than making live calls every
time, add a small **read-only poller**:

```
scheduled job (every N minutes)
   → read recent messages from your watchlist (READ ONLY)
   → append new items (since last run) to a local signal file
        → de-duplicate; collapse repeated bot/alert noise
             → AI reads the file at session start, scores vs. SOT, surfaces the block
```

**Design principles that matter:**

- **Read-only.** The collector never writes, posts, or reacts. It only reads.
- **Local.** The signal file stays on your machine, next to your SOT. Nothing is sent
  anywhere new.
- **Dumb collector, smart scorer.** The poller does NOT decide importance — if it did,
  that logic would rot and you couldn't tune it. It just guarantees the AI never misses
  the raw material. *All relevance logic stays with the AI*, driven by your SOT.
- **Surface into what you read.** Write to a file the AI consumes at session start — NOT
  a separate "inbox" file you'll never open. (This is the #1 reason digest systems fail:
  they output somewhere the human never looks.)
- **De-noise.** Collapse repeated automated alerts ("Alert ×30") so one noisy bot doesn't
  bury the human messages.
- **Bounded.** Rotate the signal file (e.g., keep 72h) so it never grows unbounded. Cap
  the scan time; if it runs long, surface what you have and label it incomplete — never
  block the session.

## Weekly Re-Index

Once a week (pair it with your continuous-improvement review):

1. For each active priority and key person, probe which channels are currently carrying
   that signal.
2. **Propose adds** (new high-signal channels) and **drops** (60-day-silent channels, or
   priorities that have closed).
3. Confirm your watchlist entries still resolve.
4. Update the watchlist and log the change.

This keeps scope aligned to your *current* priorities, not last quarter's.

## A Caution Worth Internalizing

The failure mode for every "daily digest" is the same: **it writes to a file nobody
reads.** A summary delivered to a surface you don't check is worse than no summary —
it creates false confidence. The Signal Scan only works because its output lands *in the
session brief you read anyway*. Wire it there, or don't build it.

## The Payoff

You say "let's start," and before you ask anything, your AI opens with: *"Three things
from your channels since last session you'll want to see..."* — each one scored against
what you're actually working on. The "I didn't know to look there" failure mode goes away.
