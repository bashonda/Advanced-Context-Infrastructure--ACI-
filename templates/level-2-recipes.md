# Operational Playbook

<!-- 
  LEVEL 2 RECIPES & PROCEDURES
  Every recurring process, ritual, and operational instruction lives here.
  Your AI follows these recipes to maintain consistency across sessions.
  
  Update frequency: When you refine a process or add a new one.
  Cross-ref: level-2-source-of-truth.md (System Reference)
-->

## Session Ritual

<!-- 
  This is the most important recipe — it defines what happens at the start and end
  of every AI session. Your AI should follow this automatically.
-->

### Start of Session
1. Read all Level 2 documents (source-of-truth, people, projects, recipes, quality)
2. Acknowledge review: "I've reviewed your SOT — here's where we left off..."
3. Surface relevant context: upcoming deadlines, open items, priority shifts
4. Run Tenth Man audit (see `level-2-quality.md#tenth-man-rule`)
5. Ask: "What are we working on today?" (unless task is already clear)

### End of Session
1. Update affected SOT documents with any new information
2. Add session log entry to `level-2-source-of-truth.md#session-log`
3. Update "Last updated" timestamps on changed documents
4. Check cross-references — new info lives in ONE canonical place with refs elsewhere
5. Run Tenth Man audit (end-of-session pass)
6. If last session of the business day → run Kaizen review (see `level-2-quality.md#kaizen`)
7. Confirm SOT updates with user

---

## Hard Rules

<!-- 
  Non-negotiable operational rules. These override everything else.
  Keep this list short and absolute.
-->

- **ALWAYS** read SOT documents at session start — no exceptions
- **ALWAYS** update session log before ending a session
- **NEVER** make up information — say "I don't know" or "let me check"
- **NEVER** delete SOT content without explicit permission
- **ALWAYS** flag when information might be stale (>2 weeks without update)
- **ALWAYS** ask before taking irreversible actions (sending messages, deleting files)
- **NEVER** store sensitive credentials in SOT files

---

## Meeting Prep Recipe

<!-- 
  Standard procedure for preparing for any meeting. AI should offer to run this
  when a meeting is mentioned or approaching.
-->

### Inputs Needed
- Meeting name/type
- Attendees
- Agenda (if available)
- Your goal for the meeting

### Procedure
1. **Pull people context** — Look up all attendees in `level-2-people.md`
2. **Pull project context** — Check `level-2-projects.md` for relevant initiatives
3. **Review last interaction** — Check session log for recent mentions of attendees/topics
4. **Draft prep brief:**
   - Attendee context & communication preferences
   - Relevant project status updates
   - Your talking points aligned to your goal
   - Questions to ask
   - Decisions needed
5. **Post-meeting:** Capture action items, update relevant SOT docs

---

## Weekly Rituals

<!-- Define your recurring weekly activities. AI can prompt you or help execute these. -->

### Monday: Week Planning
- Review `level-2-source-of-truth.md#active-priorities` — re-rank if needed
- Check all project statuses in `level-2-projects.md`
- Identify the 3 things that MUST happen this week
- Flag any blockers that need escalation

### Friday: Week Retro
- Update all project statuses
- Archive completed items
- Note wins and learnings
- Set up Monday for success

### [Day]: [Custom Ritual]
- [e.g., "Wednesday: Vendor check-in prep — pull metrics, draft talking points"]

---

## Data Sources & Tools

<!-- 
  Where your AI should look for different types of information.
  Keeps the AI from asking "where do I find X?" repeatedly.
-->

| Data Type | Source | Access Method | Notes |
|-----------|--------|---------------|-------|
| [Company metrics] | [Looker / Dashboard URL] | [Direct query or screenshot] | [Updated daily] |
| [Project tracking] | [Jira / Linear / Notion] | [API or manual check] | [Board: X] |
| [Documents] | [Google Drive / Confluence] | [Search or direct link] | [Shared drive: Y] |
| [Communication] | [Slack / Email] | [Channel: #team-channel] | [Check for async updates] |
| [Calendar] | [Google Calendar] | [Check for conflicts] | |

---

## Automation & Tool Instructions

<!-- Specific instructions for tools your AI has access to. Add as you discover patterns. -->

- **Slack:** [e.g., "Post standup updates to #team-standup, use thread for details"]
- **Calendar:** [e.g., "Default meeting length is 25min. Always include agenda in invite."]
- **File management:** [e.g., "All deliverables go in /projects/[name]/deliverables/"]

---

## Cross-References

- Session log → `level-2-source-of-truth.md#session-log`
- People lookup for meeting prep → `level-2-people.md#key-people`
- Quality gates & audit → `level-2-quality.md`
- Project status for updates → `level-2-projects.md#project-index`

---

*Version: 1.0 | Created: 2026-05-29 | Last updated: 2026-05-29*
*Part of the Level 2 Advanced Context Infrastructure — see level-2-source-of-truth.md for system index*
