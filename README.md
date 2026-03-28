# Daily Agent

Personal automation system powered by [Claude Code](https://claude.ai/code) as a unified entry point for three daily workflows: guided journaling, academic research, and general AI assistance.

Integrates with **Notion**, **Zotero**, **Obsidian**, and **Heptabase** through REST APIs and MCP (Model Context Protocol). Replaces the Rosebud journaling app with Claude-guided therapeutic prompts.

## How It Works

Open Claude Code in the project directory. Type `start` to pick a workflow, or just start talking — Q&A mode is the default.

```
你好！請選擇今天要使用的工作流：

1. 📝 日記／反思 — 引導式日記、情緒反思、自我覺察
2. 📚 學術工作流 — 文獻搜尋、整理、研究筆記、知識沉澱
3. 💬 問答型 AI — 問答、摘要、轉格式、文件整理、任務拆解
```

## Workflows

### 1. Journal & Reflection (日記／反思)

Claude replaces the Rosebud journaling app with a full intelligence layer. 16 templates, 6 switchable AI personas, and a free dialogue mode.

```
User starts journal session
  → Claude loads recent journal context (last 10 entries)
  → Checks previous tracking reminders, asks follow-up
  → User picks template (or free dialogue) + persona
  → Guides through conversation with chosen persona's style
  → Adapts questioning, scans for cognitive distortions, tracks goals
  → Auto-generates analysis: summary, emotion tags, people tags, key insight, actions, patterns
  → Saves to journal log + Notion
```

**Personas** (defined in `rosebud/journal_personas.md`):
- 🧭 **引導者 (Guide)** — warm, practical, structured (default)
- 🌿 **園丁 (Gardener)** — IFS parts work, gentle curiosity
- 🔥 **教練 (Coach)** — motivational, forward-moving, goal-oriented
- 🪞 **鏡子 (Mirror)** — CBT reframing, cognitive clarity
- 🌊 **錨 (Anchor)** — nervous system regulation, somatic grounding
- 💬 **夥伴 (Companion)** — non-directive, just listens (pairs with free dialogue)

**Intelligence features** (built on Claude, defined in `rosebud/journal_intelligence.md`):
- Adaptive questioning based on response length and emotional state
- Cognitive distortion detection (all-or-nothing, catastrophizing, "should" tyranny, etc.)
- Structured mid-conversation responses (patterns, leverage action, If-Then strategies, closing line)
- Auto-analysis after each session: summary, emotion tags, people tags, key insight, action items
- Cross-entry pattern recognition (emotional trends, recurring triggers, behavioral cycles)
- Cross-day linking (morning references evening, evening references morning intention)
- Reading integration (summarize books/articles, connect to current goals)
- Tracking reminders carried across sessions
- Free dialogue mode (no template, user leads, intelligence layer still active)

Templates include: daily intention, evening check-in, gratitude, dream journal, reframing negative thoughts, boundary setting, communication repair, nervous system rebalancing, and more. See `rosebud/overview.md` for the full index.

### 2. Academic Research (學術工作流)

Automated pipeline from literature search to structured notes, with cross-paper synthesis, writing support, and research question tracking.

```
User provides topic (or picks from open research questions)
  → Search Zotero for papers
  → Pull metadata + annotations for each result
  → Create structured literature notes in Obsidian
  → Cross-paper comparison: themes, conflicts, gaps
  → Create topic summary page in Notion (or fallback to findings/)
  → Offer writing support: literature review summary or outline
  → Update research question tracker
  → Present findings to user
```

```
Elicit (manual) → Zotero (source library)
                    ↓ automated
              Obsidian (literature notes)
                    ↓ automated
              Notion (metadata database)
                    ↓ manual (Zotero sync)
              Heptabase (visual thinking)
```

### 3. Q&A & General AI (問答型 AI) — Default

The default mode. Claude Code handles Q&A, summarization, format conversion, file organization, and task breakdown. No setup needed.

## Tool Integration

| Tool | Role | Access |
|------|------|--------|
| **Notion** | Page/database management, journal storage, academic metadata, travel plans | MCP server (`@notionhq/notion-mcp-server`) |
| **Zotero** | Academic source library — references, PDFs, annotations | REST API v3 via `zotero/api.py` |
| **Obsidian** | Research note library — structured literature notes | Local REST API plugin via `obsidian/api.py` |
| **Heptabase** | Visual thinking workspace | No write API — manual only, syncs from Zotero |
| **Rosebud** | Replaced by Claude | Templates in `rosebud/` folder |

## Prerequisites

- **Python 3.6+**
- **Node.js + npm** (for Notion MCP server via `npx`)
- **Zotero** desktop app (for academic workflow)
- **Obsidian** desktop app with [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin (for academic workflow)
- **Notion** account with an [internal integration](https://www.notion.so/my-integrations)
- **Heptabase** account (optional, manual use only)

## Setup After Cloning

After you clone this repo, some files are excluded from git for security and portability. Follow these steps to get everything running:

### Step 1: Clone and enter the project

```bash
git clone https://github.com/KasperChenGH/diary_work.git Daily_Agent
cd Daily_Agent
```

### Step 2: Create your `.env` from the template

The repo includes `.env.example` with empty API keys. Copy it to `.env`:

```bash
cp .env.example .env
```

### Step 3: Install Python dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Claude Code local settings

The `.claude/mcp.json` is already included (Notion MCP config). You just need the local settings file:

```bash
# Create settings file (Claude Code will populate it on first run)
echo '{}' > .claude/settings.local.json
```

Or just open Claude Code in this directory — it will create the file automatically.

### Step 5: Configure API keys

Fill in your `.env` with your credentials:

| Variable | Where to get it |
|----------|----------------|
| `NOTION_API_SECRET` | [notion.so/my-integrations](https://www.notion.so/my-integrations) → Internal Integration Secret |
| `ZOTERO_API_KEY` | [zotero.org/settings/keys/new](https://www.zotero.org/settings/keys/new) → create key with read/write access |
| `ZOTERO_USER_ID` | [zotero.org/settings/keys](https://www.zotero.org/settings/keys) → user ID shown on page |
| `OBSIDIAN_API_KEY` | Obsidian → Settings → Community Plugins → Local REST API → copy API key |

Or type `project_setup` in Claude Code to be guided through the full setup interactively (system checks, dependency install, API keys, connection tests).

### Step 6: Verify connections

```bash
python zotero/api.py recent 1       # Test Zotero API
python obsidian/api.py status        # Test Obsidian Local REST API (Obsidian must be running)
```

### Step 7 (Optional): Install superpowers framework

```bash
git clone https://github.com/obra/superpowers.git superpowers
```

### What's included vs what you create locally

| File | In repo? | Notes |
|------|----------|-------|
| `.env.example` | Yes | Template with empty keys |
| `.env` | **No** — create from `.env.example` | Your actual API keys (never committed) |
| `.claude/mcp.json` | Yes | Notion MCP server config |
| `.claude/settings.local.json` | **No** — auto-created by Claude Code | Machine-specific permissions |
| `superpowers/` | **No** — optional clone | External development framework |
| `node_modules/` | **No** — installed at runtime | Auto-installed by `npx` when needed |

## API Scripts

### Zotero (`zotero/api.py`)

```bash
python zotero/api.py search "machine learning"    # Search papers
python zotero/api.py recent 10                     # Latest N items
python zotero/api.py item ITEM_KEY                 # Full item details
python zotero/api.py annotations ITEM_KEY          # Highlights & notes
python zotero/api.py collections                   # List collections
python zotero/api.py collection COLLECTION_KEY     # Items in collection
python zotero/api.py tags                          # List all tags
python zotero/api.py items_by_tag "tag_name"       # Items by tag
```

### Obsidian (`obsidian/api.py`)

```bash
python obsidian/api.py status                              # Check connection
python obsidian/api.py read "path/to/note.md"              # Read note
python obsidian/api.py create "path/note.md" "# Content"   # Create/overwrite note
python obsidian/api.py append "path/note.md" "new content" # Append to note
python obsidian/api.py delete "path/note.md"               # Delete note
python obsidian/api.py search "query"                      # Search notes
python obsidian/api.py list                                # List all notes
python obsidian/api.py list "Research/"                    # List notes in folder
python obsidian/api.py daily                               # Get today's daily note
python obsidian/api.py daily_append "- task from Claude"   # Append to daily note
```

## Project Structure

```
Daily_Agent/
├── CLAUDE.md                 # Claude Code instructions (workflow logic, commands, conventions)
├── workflow.md               # Detailed workflow specs
├── requirements.txt          # Python + system dependencies
├── .env                      # API keys (not committed)
├── overall_memory.md         # Session memories — problems, solutions, decisions
├── overall_knowledge.md      # Accumulated knowledge — facts, patterns, by topic
│
├── .claude/
│   ├── mcp.json              # Notion MCP server config
│   └── settings.local.json   # Claude Code permission settings
│
├── zotero/
│   ├── api.py                # Zotero REST API client (search, items, annotations, collections, tags)
│   ├── knowledge.md          # Zotero concepts, API details
│   └── skills.md             # Zotero how-to guides
│
├── obsidian/
│   ├── api.py                # Obsidian Local REST API client (CRUD, search, daily notes, literature notes)
│   ├── knowledge.md          # Obsidian concepts, plugin ecosystem
│   └── skills.md             # Obsidian how-to guides
│
├── heptabase/
│   ├── knowledge.md          # Heptabase concepts, limitations
│   └── skills.md             # Heptabase workarounds
│
├── notion/
│   └── travel_plan_template.md  # Notion travel plan database schema & template
│
├── docs/
│   └── multi_agent_roadmap.md   # Future multi-agent architecture plan
│
├── journal/
│   ├── diary_log.md             # Plain diary — user's own words (rolling 150 entries)
│   ├── journal_log.md           # Compact analysis summaries (rolling 10, for pattern recognition)
│   ├── research_questions.md    # Persistent research question tracker
│   └── entries/                 # Permanent full analysis files per session
│
├── rosebud/
│   ├── overview.md              # Template index with therapeutic frameworks
│   ├── journal_intelligence.md  # Intelligence layer: auto-analysis, patterns, tracking
│   ├── journal_personas.md      # Persona overview + structured response format
│   ├── personas/                # Persona soul files (enforce distinct behavior)
│   │   ├── guide.md             # 🧭 引導者
│   │   ├── gardener.md          # 🌿 園丁
│   │   ├── coach.md             # 🔥 教練
│   │   ├── mirror.md            # 🪞 鏡子
│   │   ├── anchor.md            # 🌊 錨
│   │   └── companion.md         # 💬 夥伴
│   └── rosebud_*.md             # 16 journal templates (ACT, IFS, CBT, NVC, etc.)
│
├── findings/                    # Fallback storage when Notion is unreachable
└── superpowers/              # obra/superpowers development framework (cloned)
```

## How to Use — Commands Reference

Open Claude Code in the project directory. You can start using it immediately — **Q&A mode is the default**, no command needed. Just ask Claude anything.

For the full workflow system, use these commands:

### `start` — Launch the workflow picker

Type `start` to see the main menu:

```
你好！請選擇今天要使用的工作流：

1. 📝 日記／反思 — 引導式日記、情緒反思、自我覺察
2. 📚 學術工作流 — 文獻搜尋、整理、研究筆記、知識沉澱
3. 💬 問答型 AI — 問答、摘要、轉格式、文件整理、任務拆解

請輸入數字 (1/2/3)：
```

**Picking 1 (Journal):** Claude will ask you to choose a template (or free dialogue) and a persona, then guide you through a journaling session. At the end, it auto-generates an analysis with emotion tags, people tags, patterns, and action items.

**Picking 2 (Academic):** Claude checks your API connections, then asks for a research topic. It automatically searches Zotero, creates Obsidian notes, synthesizes across papers, and creates a Notion summary page.

**Picking 3 (Q&A):** Same as default mode. Claude handles whatever you ask — Q&A, summarization, format conversion, file organization, task breakdown.

**Not typing `start`?** That's fine. Claude defaults to Q&A mode and responds to whatever you say.

---

### `project_setup` — First-time setup (works after fresh clone)

Type `project_setup` for guided installation. Claude handles everything automatically — including post-clone environment setup:

0. **Environment setup** — Creates `.env` from `.env.example`, creates missing directories (`journal/entries/`, `findings/`), creates `.claude/settings.local.json` if needed
1. **System check** — Verifies Python 3.6+ and Node.js/npm are installed
2. **Dependencies** — Runs `pip install -r requirements.txt` and verifies
3. **API keys** — Asks for each key one by one, with instructions on where to find them:
   - Notion API secret
   - Zotero API key + user ID
   - Obsidian Local REST API key
4. **Connection test** — Tests each service and reports what's working

**After cloning, just open Claude Code and type `project_setup` — that's it.** Claude will detect what's missing and set everything up.

---

### `past_record` — Browse past journal entries

Type `past_record` to browse your diary history:

```
📖 你的日記紀錄：

1. 2026-03-28 21:30 — 晚間回顧 | 引導者
2. 2026-03-28 08:15 — 每日意圖 | 教練
3. 2026-03-27 22:00 — 自由對話 | 夥伴
...

請輸入編號查看內容，或輸入日期（如 2026-03-28）查看該天所有紀錄：
```

- **Pick a number** → see that entry's diary content (your own words)
- **Type a date** → see all entries from that day
- **After viewing** → Claude offers to show the analysis record too (emotion tags, patterns, action items)

The diary stores your last 150 entries. Full analysis records are kept permanently in `journal/entries/`.

---

### Quick Reference

| Command | What it does |
|---------|-------------|
| *(just talk)* | Q&A mode (default) — ask Claude anything |
| `help` | Show all available commands with explanations (in Chinese) |
| `start` | Show workflow picker: Journal / Academic / Q&A |
| `project_setup` | Guided setup: system check, dependencies, API keys, connection test |
| `past_record` | Browse and read past journal entries |

**Note:** `help` only triggers when typed alone. "help me with X" is treated as a normal Q&A question.

### During a Journal Session

| Prompt | What happens |
|--------|-------------|
| Pick template (or say "自由對話") | Choose structured template or free-form conversation |
| Pick persona | Choose AI personality: 引導者/園丁/教練/鏡子/錨/夥伴 |
| *(just journal)* | Claude guides you, adapts to your emotional state, tracks goals |
| *(session ends)* | Auto-analysis generated: summary, emotion tags, people tags, insight, actions, patterns |

### During an Academic Session

| Prompt | What happens |
|--------|-------------|
| Give a topic | Full pipeline runs: Zotero search → Obsidian notes → cross-paper synthesis → Notion page |
| *(after results)* | Claude offers writing support: literature review summary or outline |

## Session Memory

Claude maintains two files across sessions:

- **`overall_memory.md`** — Chronological log of problems, solutions, and decisions from past sessions
- **`overall_knowledge.md`** — Accumulated facts and patterns organized by topic, updated as understanding deepens

Both are read at session start and updated at session end. They stay concise — entries are consolidated and merged, not endlessly appended.

## Journal Storage

Every journal session saves to 4 layers:

| Storage | What | Retention | Purpose |
|---------|------|-----------|---------|
| `journal/entries/` | Full analysis + key quotes | Permanent | Archival record |
| `journal/diary_log.md` | Your own words | Last 150 | Browsable via `past_record` |
| `journal/journal_log.md` | Compact analysis | Last 10 | Cross-entry pattern recognition |
| Notion | Full + database tags | Permanent | Cloud copy with structured properties |

## Conventions

- **Language:** User-facing content in Traditional Chinese (繁體中文) unless specified otherwise
- **File scope:** All configs and files stay inside the project directory
- **Paths:** Generic placeholders discovered at runtime per machine
- **API keys:** Stored in `.env`, never hardcoded
- **Notion styling:** Section headers `green_bg`, callouts `gray_bg` with bulb icon

## License

Personal project. Not currently published for distribution.
