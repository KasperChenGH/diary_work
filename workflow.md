# Daily Agent — Project Workflow

## Overview

Daily Agent is a personal automation project powered by Claude Code as a **unified entry point**. It integrates with Notion, Zotero, Obsidian, Heptabase, and Rosebud-style journaling to handle three core workflows: journaling/reflection, academic research, and general AI-assisted Q&A.

## Three Core Workflows

### Workflow 1: 日記／反思工作流 (Journal & Reflection)

**Purpose:** Daily journaling, emotional reflection, self-awareness
**Tools:** Claude (replaces Rosebud) → Notion
**Goal:** Stable, low-maintenance journaling system with built-in intelligence

**Flow:**
```
User triggers journal session
  → Claude loads recent journal context (last 10 entries from journal/journal_log.md)
  → Claude checks previous tracking reminders, asks follow-up naturally
  → User picks template (or free dialogue) + persona
  → Claude reads chosen persona's soul file (rosebud/personas/<persona>.md)
  → Claude guides through conversation AS that persona (distinct tone, rules, techniques)
  → During conversation: adaptive questioning, cognitive distortion scan, goal micro-tracking
  → After conversation: auto-generates analysis block
  → Analysis saved to journal/journal_log.md + Notion (or local fallback)
```

**Intelligence layer (replaces Rosebud's AI engine):**

Claude provides the following capabilities natively, defined in `rosebud/journal_intelligence.md`:

| Capability | What Claude does |
|---|---|
| **Adaptive questioning** | Adjusts style based on response length, emotional state, and energy |
| **Cognitive distortion scan** | Detects all-or-nothing thinking, catastrophizing, "should" tyranny, etc. and gently mirrors them |
| **Goal micro-tracking** | Breaks goals into 5-15 min steps, creates If-Then strategies, tracks across entries |
| **Auto-analysis** | After each session: generates summary, emotion tags, people tags, key insight, action items |
| **Pattern recognition** | Compares across recent entries: emotional trends, recurring triggers, behavioral cycles, goal progress |
| **Cross-day linking** | Morning sessions reference last evening; evening sessions reference morning intention |
| **Tracking reminders** | Creates follow-up question, asks it at start of next session |

**Auto-analysis output (generated after every journal session):**
- 📝 摘要 — 2-4 sentence summary
- 🏷️ 情緒標籤 — detected emotions as tags (e.g., #焦慮 #感恩 #疲憊)
- 👥 提及的人 — people mentioned as tags (e.g., @老師 @媽媽)
- 💡 核心洞察 — the key realization or shift
- ✅ 行動項目 — specific next steps (5-15 min sized)
- 🔄 模式觀察 — patterns across recent entries
- 📌 追蹤提醒 — follow-up question for next session

**Storage (4 layers, each with a different purpose):**
- `journal/entries/[YYYY-MM-DD]_[type].md` — **permanent full analysis** per session (auto-analysis + key quotes). Always saved.
- `journal/diary_log.md` — **plain diary** of the user's own words, rolling 150 entries. For browsing via `past_record` command.
- `journal/journal_log.md` — **compact analysis summaries**, rolling 10 entries. For Claude's cross-entry intelligence.
- Notion — full entry + analysis as a page (with emotion/people multi-select tags)

**Personas (6 switchable AI roles, each with a dedicated soul file):**

| Persona | Soul File | Behavior |
|---|---|---|
| 🧭 引導者 (Guide) — DEFAULT | `rosebud/personas/guide.md` | Integrative, uses 4-part structured response, balances empathy with action |
| 🌿 園丁 (Gardener) | `rosebud/personas/gardener.md` | IFS parts work, assumes positive intent, slowest pace, body-first |
| 🔥 教練 (Coach) | `rosebud/personas/coach.md` | Motivational Interviewing, explores ambivalence, recalls past successes, tiny steps |
| 🪞 鏡子 (Mirror) | `rosebud/personas/mirror.md` | CBT, names distortions explicitly, maps thought→emotion→behavior chains |
| 🌊 錨 (Anchor) | `rosebud/personas/anchor.md` | Polyvagal, body before mind, somatic exercises, won't push action when dysregulated |
| 💬 夥伴 (Companion) | `rosebud/personas/companion.md` | Rogerian, zero structure, follows user's lead, only advises when asked |

**Free dialogue mode:** User can skip templates entirely. Claude follows the user's lead with no structured stages. Default persona: 夥伴. Intelligence layer still runs (auto-analysis generated at end).

**Reference files:**
- `rosebud/journal_intelligence.md` — intelligence layer rules (MUST read at session start)
- `rosebud/journal_personas.md` — persona overview + structured response format
- `rosebud/personas/*.md` — persona soul files (MUST read chosen persona before conversation)
- `rosebud/overview.md` — template index
- `rosebud/rosebud_*.md` — 16 individual journal templates

---

### Workflow 2: 學術工作流 (Academic Research)

**Purpose:** Literature collection, organization, research notes, knowledge synthesis, pre-writing
**Tools:** Elicit → Zotero → Obsidian → Heptabase, with Notion as metadata database

**Tool roles:**
| Tool | Role | API Access |
|---|---|---|
| **Elicit** | Literature search & discovery | Manual (user exports to Zotero) |
| **Zotero** | Source library — references, PDFs, annotations | Full REST API (pyzotero) |
| **Obsidian** | Research note library — structured literature notes from Zotero annotations | Local REST API plugin (requires Obsidian running) |
| **Notion** | Metadata database — reference tracking, status, tags | Full API via MCP |
| **Heptabase** | Visual thinking workspace — divergent/convergent thinking, pre-writing | No write API (Zotero sync connected inside Heptabase) |

**Flow:**
```
Elicit (manual) → Zotero (source library)
                    ↓ [Agent automates]
              Obsidian (literature notes from annotations)
                    ↓ [Agent automates]
              Notion (metadata database entry)
                    ↓ [User manual — Zotero sync already connected]
              Heptabase (visual thinking & pre-writing workspace)
```

**Fully automatic pipeline — user gives a topic, agent handles everything:**

1. **Load context** — Read `journal/research_questions.md` for open questions. If relevant open questions exist, mention them and ask if user wants to continue one
2. **Search** — `python zotero/api.py search "topic"` → find relevant papers
3. **Pull details** — `python zotero/api.py item KEY` + `python zotero/api.py annotations KEY` → get metadata, highlights, notes for each paper
4. **Create literature notes** — `python obsidian/api.py create ...` using `create_literature_note()` → structured notes with frontmatter, highlights, research sections
5. **Cross-paper comparison** — After collecting all papers, synthesize:
   - Common themes and shared conclusions
   - Conflicting findings and methodological differences
   - Research gaps (what no paper addresses)
   - How papers relate to each other (builds on, contradicts, extends)
6. **Create Notion page per topic** — via MCP → one new page per search topic containing:
   - Page title = user's topic
   - Summary of findings, key themes, **cross-paper synthesis**
   - List of all papers found (title, authors, year, DOI, tags, status)
   - Connections, patterns, and **research gaps**
   - **If Notion fails** → save to `findings/[YYYY-MM-DD]_<topic>.md` as fallback (same content, standardized naming)
   - Filename = user's topic, sanitised (e.g., `findings/transformer_architectures.md`)
7. **Present findings** — summarise to user: key themes, notable papers, cross-paper insights, research gaps
8. **Writing support** — After presenting findings, offer:
   - Literature review summary (structured academic summary of findings)
   - Writing outline (argument structure, evidence mapping, citation placement)
   - Draft in Traditional Chinese with proper academic style
9. **Update research questions** — Check `journal/research_questions.md`:
   - Update status of existing questions if this search provided answers
   - Add new questions that emerged during the search as 🔴 open
10. **Save knowledge** — append findings to `overall_knowledge.md`, update tool-specific `knowledge.md`/`skills.md` if new patterns discovered

**What stays manual:**
- Heptabase visual thinking (no write API; Zotero sync handles reference import)

**API scripts available:**

```bash
# Zotero (zotero/api.py)
search "query" | recent N | item KEY | annotations KEY
collections | collection KEY | tags | items_by_tag "tag"

# Obsidian (obsidian/api.py)
status | read "path" | create "path" "content" | append "path" "content"
delete "path" | search "query" | list | list "folder/"
daily | daily_append "content"
```

**References:**
- `zotero/knowledge.md`, `zotero/skills.md` — API details, pyzotero examples
- `obsidian/knowledge.md`, `obsidian/skills.md` — Local REST API, file access
- `heptabase/knowledge.md`, `heptabase/skills.md` — limitations, MCP read-only

---

### Workflow 3: 問答型 AI 工作流 (Q&A & General AI)

**Purpose:** Claude Code as unified entry point for everyday AI tasks
**Capabilities:**
- **問答 (Q&A):** Answer questions with web search, file reading, context from tools
- **摘要 (Summarization):** Summarize papers, articles, documents, meeting notes
- **轉格式 (Format Conversion):** Convert between formats (Markdown, CSV, JSON, etc.)
- **文件整理 (File Organization):** Organize, rename, restructure files and folders
- **任務拆解 (Task Breakdown):** Break complex tasks into actionable steps

**This workflow is implicit** — it's the default mode when the user isn't in a journal or academic session.

---

## Tool Integration Summary

### Notion (MCP Server)
- **Connection:** Notion MCP server configured in `.claude/mcp.json`, reads API key from `.env` via `${NOTION_API_SECRET}`
- **Capabilities:** Search, create/update pages & databases, manage views, read content
- **Used in:** All 3 workflows (journal storage, academic metadata, general organization)

### Zotero (REST API)
- **Connection:** Zotero Web API v3 at `https://api.zotero.org`
- **Auth:** API key via `Zotero-API-Key` header
- **Library:** pyzotero (Python)
- **Used in:** Academic workflow (source library)
- **Setup needed:** API key + userID in `.env`

### Obsidian (Local REST API Plugin)
- **Connection:** `https://127.0.0.1:27124` (requires Obsidian running + Local REST API plugin)
- **Auth:** Bearer token from plugin settings
- **Used in:** Academic workflow (research notes)
- **Setup needed:** Install Local REST API plugin, API key in `.env`, vault path discovery at runtime

### Heptabase (No API)
- **Connection:** None programmatic. Zotero sync connected inside Heptabase app.
- **Used in:** Academic workflow (visual thinking, manual), Journal workflow (manual)
- **Agent role:** Reference only — cannot read or write

### Rosebud (Replaced by Claude)
- **Reference:** `rosebud/` folder contains analyzed prompt templates
- **Used in:** Journal workflow — Claude replicates Rosebud's guided journaling

## Existing Workflows

### Travel Plan Creation
**Trigger:** User asks to create a travel plan
**Template:** `notion/travel_plan_template.md`
**Steps:**
1. Gather trip details (destination, dates, duration, purpose)
2. Create main Notion page with icon and title
3. Create 行程安排 database with schema (地點, 類別, 描述, Google Map, 照片, 第幾天, 預計停留時間)
4. Set up 7 views: 行程圖表 (board), 行程時間表格 (table), 景點/逛街/吃喝 (gallery), 住宿 (table)
5. Create sub-pages: 行李清單, 行程參考資料, 採購清單
6. Populate database with itinerary entries (each with time ranges)
7. Build page layout: callout, database, 3-column prep section, 出發Go!
8. Inform user to drag "行程圖表" tab to first position (API limitation)

**Content language:** Traditional Chinese (繁體中文)
**Day label format:** `D{n}.{MM}/{DD}({weekday})` — weekday in Chinese

## Conventions

- **Language:** Content created for the user should be in Traditional Chinese (繁體中文) unless specified otherwise
- **File location:** All configs and files stay inside the project directory, not global
- **Paths:** Use generic placeholders (e.g., `<VAULT_PATH>`) — discover actual paths at runtime on each machine
- **Notion content:** Follow the color conventions — section headers use `{color="green_bg"}`, callouts use `gray_bg` with 💡 icon
- **API keys:** Store in `.env`, never hardcode in config files
