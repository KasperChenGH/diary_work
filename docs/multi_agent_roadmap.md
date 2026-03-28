# Multi-Agent Architecture Roadmap

Planning document for future agent expansion. Currently all workflows run through a single Claude Code session. This roadmap outlines how to decompose into specialized agents when the system grows.

**Current state:** Single Claude Code entry point handling all three workflows via CLAUDE.md instructions.
**Future state:** Specialized agents that can be dispatched for specific tasks.

## Proposed Agent Architecture

```
Claude Code (unified entry point)
  ├── journal-agent        — guided journaling with intelligence layer
  ├── research-assistant   — academic pipeline orchestrator
  ├── literature-agent     — Zotero search, annotation extraction, note creation
  ├── notion-sync          — Notion page creation and database management
  ├── qa-agent             — general Q&A, summarization, format conversion
  ├── lesson-prep          — teaching material preparation (future)
  ├── admin-assistant      — administrative task handling (future)
  └── line-bridge          — LINE remote commands and notifications (future)
```

## Phase Plan

### Phase 1: Current (Single Agent) ✅
All workflows handled by one Claude Code session with CLAUDE.md routing.
- Journal workflow with intelligence layer, personas, free dialogue
- Academic pipeline (Zotero → Obsidian → Notion)
- Q&A as default mode
- **This is sufficient for daily use.** Only move to Phase 2 when tasks become too complex for a single session.

### Phase 2: Specialized Subagents (When Needed)
Split long-running or complex tasks into subagents dispatched from the main session.

**journal-agent:**
- Reads journal_intelligence.md, journal_personas.md, journal_log.md
- Handles full journal conversation + auto-analysis
- Saves to journal_log.md and Notion
- Could run as a scheduled daily prompt

**research-assistant:**
- Orchestrates the academic pipeline
- Dispatches literature-agent for paper collection
- Does cross-paper synthesis and writing support
- Manages research_questions.md

**literature-agent:**
- Focused: search Zotero, pull annotations, create Obsidian notes
- No user interaction — just executes and returns results
- Good candidate for parallel dispatch (search multiple topics simultaneously)

**notion-sync:**
- Handles all Notion operations (create pages, update databases, manage views)
- Shared by journal and academic workflows
- Isolates Notion API complexity

### Phase 3: Extended Agents (Future)
Only build these when there's a clear, repeated need.

**lesson-prep:**
- Prepare teaching materials from research notes
- Generate slides, handouts, discussion questions
- Pull from Zotero and Obsidian

**admin-assistant:**
- Administrative tasks: scheduling, email drafts, document formatting
- Task breakdown and project management

**line-bridge:**
- Receive commands via LINE messages
- Send notifications (task complete, errors, reminders)
- Query system status remotely
- Requires: LINE Messaging API, webhook server

## When to Split

Don't split prematurely. A single Claude Code session handles most daily work fine. Split when:
- A task takes so long it blocks other work
- Multiple independent tasks could run in parallel
- A specific workflow needs isolation (e.g., long research session shouldn't affect journal context)
- You want to schedule automated runs (e.g., daily journal reminder)

## Implementation Notes

- Use Claude Code's Agent tool with `subagent_type` for dispatching
- Each agent should have its own CLAUDE.md or instruction set
- Shared state through files (journal_log.md, research_questions.md, overall_knowledge.md)
- No database needed — file-based state is sufficient for personal use
