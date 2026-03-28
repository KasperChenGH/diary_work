# Daily Agent

Personal automation project using Claude Code as a **unified entry point** for three core workflows: journaling/reflection, academic research, and general AI-assisted tasks. Integrates with Notion, Zotero, Obsidian, Heptabase, and Rosebud-style journaling.

**Full workflow details:** See `workflow.md`

## On Every Session Start

**At the beginning of EVERY conversation (not just when user types `start`):**
1. Read `overall_memory.md` — recall past session problems, solutions, and decisions
2. Read `overall_knowledge.md` — recall accumulated facts, patterns, and reusable solutions
3. Use this context silently to inform the current session (do NOT dump it to the user)

## Three Core Workflows

### 1. 日記／反思 (Journal & Reflection)
Claude replaces Rosebud as guided journaling AI → saves to Notion / Heptabase Journal
- **Templates:** `rosebud/overview.md` (index) + `rosebud/rosebud_*.md` files
- **Goal:** Stable, low-maintenance daily reflection system

### 2. 學術工作流 (Academic Research)
```
Elicit (manual) → Zotero (source library) → Obsidian (research notes) → Notion (metadata DB)
                                          → Heptabase (visual thinking, via Zotero sync, manual)
```
- **Zotero** = source library (full API via pyzotero)
- **Obsidian** = research note library (Local REST API plugin)
- **Notion** = metadata database (MCP)
- **Heptabase** = visual thinking workspace (no write API, manual)
- **Agent automates:** Zotero → Obsidian notes, Zotero → Notion metadata

### 3. 問答型 AI (Q&A & General) — **DEFAULT**
Claude Code as default mode for: Q&A, summarization, format conversion, file organization, task breakdown
**This is the default workflow.** If the user never types `start`, operate in this mode automatically. No menu needed — just respond to whatever the user asks.

## Tool Connections

| Tool | Access Method | Auth | Setup |
|---|---|---|---|
| **Notion** | MCP server (`mcp__claude_ai_Notion__*`) | API key in `.env` (`NOTION_API_SECRET`) | Configured in `.claude/mcp.json` |
| **Zotero** | REST API (`https://api.zotero.org`) | API key + userID in `.env` | `pip install pyzotero` |
| **Obsidian** | Local REST API plugin (`https://127.0.0.1:27124`) | Bearer token in `.env` | Install plugin, Obsidian must be running |
| **Heptabase** | No write API | N/A | Zotero sync connected inside app, manual use only |
| **Rosebud** | Replaced by Claude | N/A | Templates in `rosebud/` folder |

**Paths:** All tool paths (vault location, export folders) use generic placeholders — discover at runtime per machine.

## Project Structure

```
Daily_Agent/
├── CLAUDE.md                    # This file
├── workflow.md                  # Full workflow details & conventions
├── overall_memory.md            # Session memories — problems, solutions, decisions (chronological)
├── overall_knowledge.md         # Accumulated knowledge — facts, patterns, solutions (by topic)
├── .env                         # API keys (NOTION_API_SECRET, ZOTERO_API_KEY, etc.) — DO NOT COMMIT
├── .claude/
│   ├── mcp.json                 # MCP server configs (reads from .env)
│   └── settings.local.json      # Local Claude Code settings
├── notion/                      # Notion docs & templates
│   └── travel_plan_template.md  # MUST use when creating travel plans
├── zotero/                      # Zotero reference management
│   ├── knowledge.md             # Concepts, API details, architecture
│   └── skills.md                # How-to: collecting, citing, API usage
├── obsidian/                    # Obsidian local-first notes
│   ├── knowledge.md             # Concepts, Local REST API, plugin ecosystem
│   └── skills.md                # How-to: vault, linking, API usage
├── heptabase/                   # Heptabase visual knowledge base
│   ├── knowledge.md             # Concepts, limitations, no API
│   └── skills.md                # How-to: whiteboards, cards, export parsing
├── docs/
│   └── multi_agent_roadmap.md   # Future multi-agent architecture plan
├── findings/                    # Fallback storage when Notion is unreachable — named by topic
├── journal/                     # Journal session data
│   ├── diary_log.md             # Plain diary — user's own words, rolling 150 entries (for past_record)
│   ├── journal_log.md           # Compact analysis summaries, rolling 10 entries (for cross-entry intelligence)
│   ├── research_questions.md    # Persistent research question tracker (open/exploring/answered)
│   └── entries/                 # Permanent full analysis files per session (archival)
├── rosebud/                     # Journal prompt templates & intelligence layer
│   ├── overview.md              # Template index with therapeutic frameworks
│   ├── journal_intelligence.md  # Intelligence layer rules (auto-analysis, patterns, tracking)
│   ├── journal_personas.md      # Persona overview + structured response format
│   ├── personas/                # Persona soul files (MUST read chosen persona before session)
│   │   ├── guide.md             # 🧭 引導者 — integrative, structured, 4-part response
│   │   ├── gardener.md          # 🌿 園丁 — IFS parts work, gentle curiosity
│   │   ├── coach.md             # 🔥 教練 — Motivational Interviewing, forward-moving
│   │   ├── mirror.md            # 🪞 鏡子 — CBT, Socratic questioning, distortion flagging
│   │   ├── anchor.md            # 🌊 錨 — Polyvagal, body-first, somatic grounding
│   │   └── companion.md         # 💬 夥伴 — Rogerian, non-directive, just listens
│   └── rosebud_*.md             # Individual templates (ACT, IFS, CBT, NVC, etc.)
└── superpowers/                 # obra/superpowers framework (cloned repo)
```

## Special Commands

### `help`
**Trigger:** User types exactly "help" (no follow-up words — "help me" or "help with X" is NOT this command, treat those as normal Q&A)
**Action:** Display the following help menu in Traditional Chinese:

```
📋 可用指令一覽：

🟢 start — 啟動工作流選單
   開啟三大工作流選擇器：日記／反思、學術工作流、問答型 AI。
   Claude 會先載入過去的學習紀錄，再顯示選單讓你選擇。

🟢 project_setup — 專案初始設定
   引導式設定流程，包含五個階段：
   ⓪ 環境檔案建立（複製 .env、建立必要資料夾）
   ① 檢查系統環境（Python、Node.js）
   ② 安裝 Python 套件
   ③ 逐一設定 API 金鑰（Notion、Zotero、Obsidian）
   ④ 測試各服務連線狀態
   💡 Clone 後第一次使用？直接輸入 project_setup 就好！

🟢 past_record — 查看過去的日記紀錄
   瀏覽你的日記歷史（最近 150 筆）。
   可以用編號或日期查看特定紀錄，也可以查看該天的分析報告。

💡 不輸入任何指令？
   直接跟 Claude 對話即可！預設為問答模式（Q&A），
   支援：問答、摘要、格式轉換、檔案整理、任務拆解。

💡 日記工作流中的選項：
   • 選擇模板（16 種）或「自由對話」
   • 選擇對話角色：引導者／園丁／教練／鏡子／錨／夥伴
   • 結束後自動產生分析：摘要、情緒標籤、人物標籤、洞察、行動項目
```

### `start`
**Trigger:** User types "start"
**Action:** Present the workflow picker. (Memory/knowledge already loaded at session start — see "On Every Session Start" above.)

**On every session end (user says goodbye, exits, or conversation wraps up):**
1. Reflect on what was learned this session
2. Append to `overall_memory.md` if any of these occurred:
   - A problem was encountered and solved (error, workaround, debugging)
   - A user preference was discovered (how they like things done)
   - A decision was made that affects future sessions
   - A workflow step failed and had to be adapted
   - Format: `## [YYYY-MM-DD] Topic` → Problem / Solution / Takeaway
3. Update `overall_knowledge.md` if any of these occurred:
   - A new reusable fact, pattern, or solution was learned
   - An existing knowledge entry needs correction or refinement
   - A new tool behavior, API quirk, or integration detail was discovered
   - Format: `## Topic Name` → bullet points, `Last updated: YYYY-MM-DD`
   - Merge/update existing entries rather than duplicating
4. If nothing meaningful was learned, skip — don't write filler entries

**IMPORTANT — Keep both files concise:**
- Both `overall_memory.md` and `overall_knowledge.md` must stay **summarised at all times**
- Each memory entry: max 3-4 lines (problem → solution → takeaway, no lengthy explanations)
- Each knowledge entry: max 5-6 bullet points per topic
- When a file grows too long, **consolidate**: merge related entries, remove outdated ones, compress verbose entries
- Prefer updating/refining existing entries over adding new ones that overlap
- These files should be quick to scan — if Claude needs more than 30 seconds to read them, they're too long

**Display this menu (in Traditional Chinese):**
```
你好！請選擇今天要使用的工作流：

1. 📝 日記／反思 — 引導式日記、情緒反思、自我覺察
2. 📚 學術工作流 — 文獻搜尋、整理、研究筆記、知識沉澱
3. 💬 問答型 AI — 問答、摘要、轉格式、文件整理、任務拆解

請輸入數字 (1/2/3)：
```

**After user picks:**

**If 1 (日記／反思):**

**Setup phase:**
1. Read `rosebud/journal_intelligence.md` for the intelligence layer rules
2. Read `rosebud/journal_personas.md` for available personas
3. Read `journal/journal_log.md` for recent entry context (last 10 entries)
4. Read `rosebud/overview.md` for the template index

**Start phase:**
5. If previous entry had a **tracking reminder**, ask it naturally as an opening check-in
6. If morning: reference last evening's themes. If evening: reference morning's intention/goals
7. Present a **numbered list** of all templates for the user to pick by number. Also include **free dialogue** ("自由對話") as the last option. Example:
   ```
   請選擇今天的日記模板：
   1. 🌅 每日意圖
   2. 🌙 晚間回顧
   3. 🙏 感恩日記
   ...
   16. 🗣️ 自由對話
   請輸入數字（1-16）：
   ```
8. Present a **numbered list** of personas for the user to pick by number. Example:
   ```
   請選擇對話角色：
   1. 🧭 引導者（預設）
   2. 🌿 園丁
   3. 🔥 教練
   4. 🪞 鏡子
   5. 🌊 錨
   6. 💬 夥伴
   請輸入數字（1-6）：
   ```
9. **Read the chosen persona's soul file** from `rosebud/personas/<persona>.md` — follow its hard rules strictly
10. If a template was chosen, read the relevant `rosebud/rosebud_*.md` template. If free dialogue, skip template and follow the user's lead
11. Ask the user how they want to start:
    ```
    你想怎麼開始？
    1. ✍️ 直接寫日記 — 你寫，我最後分析
    2. 💬 對話引導 — 我用問題帶你寫
    請輸入數字（1/2）：
    ```
    - **If 1 (直接寫):** Let the user write freely. Don't ask questions. Just acknowledge briefly when they send messages ("嗯，收到了" or similar). When they signal they're done (e.g., "寫完了", "就這樣", or stop sending), proceed to the analysis phase.
    - **If 2 (對話引導):** Proceed with guided conversation as defined below.

**Conversation phase (only if user chose 對話引導):**
12. Guide user through the prompts conversationally in Traditional Chinese, **behaving as the chosen persona** (follow its soul file's hard rules, tone, signature moves)
13. During the conversation, apply intelligence layer rules:
    - Adapt questioning style to user's response length and emotional state
    - Scan for cognitive distortions and gently flag them
    - Track goals mentioned and create If-Then strategies
    - Reference previous entries when relevant patterns appear

**Analysis phase (automatic, after conversation or direct writing ends):**
14. Generate the auto-analysis block (as defined in `rosebud/journal_intelligence.md`):
    - 📝 摘要 (summary of conversation)
    - 🏷️ 情緒標籤 (detected emotion tags)
    - 👥 提及的人 (people mentioned, as tags)
    - 💡 核心洞察 (key insight or shift)
    - ✅ 行動項目 (action items with time/place)
    - 🔄 模式觀察 (patterns across recent entries)
    - 📌 追蹤提醒 (follow-up question for next session)
15. Present the analysis to the user for review

**Save phase:**
16. **Always save full analysis locally** to `journal/entries/[YYYY-MM-DD]_[type].md` — this is the permanent record (includes full auto-analysis block + key quotes from conversation)
17. **Append plain diary entry** to `journal/diary_log.md` — the user's own words from the session (what they shared, felt, experienced — NOT Claude's questions or analysis). Include date/time header `## [YYYY-MM-DD HH:MM] [Template] | [Persona]`. Keep max 150 entries, delete oldest.
18. Append compact entry to `journal/journal_log.md` (keep max 10 entries, delete oldest — this is for cross-entry intelligence, not archival)
19. Offer to save the full entry + analysis to Notion
20. If Notion fails → local file from step 16 already exists, no extra fallback needed

**If 2 (學術工作流):**
1. First check API connections: run `python zotero/api.py recent 1` and `python obsidian/api.py status`
2. If any connection fails, suggest running `project_setup`
3. Read `journal/research_questions.md` for open research questions
4. If connected, ask: `學術工作流已啟動！請告訴我你想研究什麼主題？`
   - If there are open research questions, mention them: "你之前有這些未解的研究問題：[list]. 要繼續其中一個嗎？"
5. Once user gives a topic/query, **run the full pipeline automatically — no sub-menus, no confirmations:**
   - Search Zotero for relevant papers (`zotero/api.py search`)
   - For each result, pull full details + annotations (`zotero/api.py item` + `annotations`)
   - Create structured literature notes in Obsidian (`obsidian/api.py create` / `create_literature_note()`)
   - **Cross-paper comparison:** After collecting all papers, synthesize across them:
     - Identify common themes, conflicting findings, methodological differences
     - Note which papers agree/disagree on key points
     - Highlight research gaps (what no paper addresses)
   - **Create a new Notion page for the topic** via MCP (`mcp__claude_ai_Notion__notion-create-pages`):
     - Page title = user's topic (e.g., "Transformer Architectures")
     - Content: summary of findings, cross-paper synthesis, list of papers found (title, authors, year, DOI), key themes, connections, research gaps
     - Each paper's metadata (title, authors, year, tags, status) listed in the page
   - **If Notion fails** (API error, MCP error, any exception) → save findings to `findings/[YYYY-MM-DD]_<topic>.md` as fallback. Naming convention: date prefix + topic sanitised for filename (e.g., `findings/2026-03-28_transformer_architectures.md`). Include all metadata that would have gone to Notion.
   - **Present findings to the user** — summarise what was found, key themes, notable papers, cross-paper insights
6. **Writing support:** After presenting findings, offer:
   - "需要我幫你寫研究摘要嗎？" — generate a structured summary suitable for literature review sections
   - "需要幫你整理成寫作大綱嗎？" — create an outline with argument structure, evidence mapping, and citation placement
   - If the user accepts, produce the draft in Traditional Chinese with proper academic style
7. **Update research questions:** Check `journal/research_questions.md`:
   - If the search answered or partially answered an existing question, update its status and add paper links
   - If new questions emerged during the search, add them as 🔴 open
8. **Save what was learned** to the appropriate files:
   - New academic knowledge → update relevant `knowledge.md` or `skills.md` in the tool folder (zotero/, obsidian/, etc.)
   - Research findings, patterns, or topic summaries → append to `overall_knowledge.md`
   - Problems encountered during the pipeline → append to `overall_memory.md`

**If 3 (問答型 AI):**
1. Simply respond: "問答模式已啟動！請告訴我你需要什麼幫助。"
2. Proceed normally — handle Q&A, summaries, format conversion, file organization, task breakdown as requested

### `project_setup`
**Trigger:** User types "project_setup"
**Action:** Full project setup — handles everything needed after a fresh clone, including environment setup, dependencies, API keys, and connection tests. Safe to run on an existing setup too (skips what's already done).

**Steps:**

**Phase 0 — Environment file setup (post-clone):**
1. Check if `.env` exists. If not, copy from `.env.example`: `cp .env.example .env`
2. Check if `.claude/settings.local.json` exists. If not, create it: `echo '{}' > .claude/settings.local.json`
3. Check if `journal/entries/` directory exists. If not, create it: `mkdir -p journal/entries`
4. Check if `findings/` directory exists. If not, create it: `mkdir -p findings`

**Phase 1 — System prerequisites:**
5. Check Python is installed (`python --version`, need 3.6+)
6. Check Node.js/npm is installed (`node --version`, `npm --version`) — needed for Notion MCP
7. Report any missing prerequisites and stop if critical ones are absent

**Phase 2 — Install Python dependencies:**
8. Run `pip install -r requirements.txt`
9. Verify installation succeeded (import test: `python -c "import requests; import urllib3; print('OK')"`)


**Phase 3 — API key setup:**
10. Read current `.env` to see which keys are already filled
11. For each empty key, ask the user with instructions on where to find it:
   - **NOTION_API_SECRET** — "Go to https://www.notion.so/my-integrations → select your integration → copy the Internal Integration Secret"
   - **ZOTERO_API_KEY** — "Go to https://www.zotero.org/settings/keys/new → create a key with read/write access → copy the key"
   - **ZOTERO_USER_ID** — "Go to https://www.zotero.org/settings/keys → your userID is the number shown on that page"
   - **OBSIDIAN_API_KEY** — "Open Obsidian �� Settings → Community Plugins → Local REST API → copy the API key"
12. Skip keys that already have values (ask user if they want to update them)
13. Write all values to `.env`

**Phase 4 — Connection tests:**
14. Run a quick test for each service:
    - Zotero: `python zotero/api.py recent 1`
    - Obsidian: `python obsidian/api.py status`
    - Notion: try a simple MCP search
15. Report which connections succeeded and which failed

### `past_record`
**Trigger:** User types "past_record"
**Action:** Let the user browse and read past journal entries.

**Steps:**
1. Read `journal/diary_log.md`
2. Extract all entry headers (dates and template types)
3. Present a numbered list of available entries in Traditional Chinese:
   ```
   📖 你的日記紀錄：

   1. 2026-03-28 21:30 — 晚間回顧 | 引導者
   2. 2026-03-28 08:15 — 每日意圖 | 教練
   3. 2026-03-27 22:00 — 自由對話 | 夥伴
   ...

   請輸入編號查看內容，或輸入日期（如 2026-03-28）查看該天所有紀錄：
   ```
4. If user picks a number → show that entry's full diary content from `diary_log.md`
5. If user types a date → show all entries from that date
6. After showing the entry, also offer: "要看這天的分析紀錄嗎？" → if yes, read and show the corresponding `journal/entries/[YYYY-MM-DD]_[type].md` file
7. User can keep browsing or type anything else to exit

## When to Use What

### Notion
**When:** Create, update, search Notion pages/databases (travel plans, journal entries, academic metadata)
**Tools:** `mcp__claude_ai_Notion__*`
**Travel plans:** When the user asks to create or plan a trip/travel itinerary, **MUST read and follow `notion/travel_plan_template.md`** for the database schema, views, sub-pages, and content structure. This triggers automatically when the user mentions travel planning — no special command needed.

### Zotero
**When:** Academic workflow — pull references, annotations, create literature notes
**How:** Run `python zotero/api.py <command>` via Bash tool
**Commands:**
- `search "query"` — search papers
- `recent N` — latest N items
- `item KEY` — full item details
- `annotations KEY` — highlights & notes for an item
- `collections` / `collection KEY` — browse collections
- `tags` / `items_by_tag "tag"` — browse by tags

### Obsidian
**When:** Academic workflow — create/read research notes in vault
**How:** Run `python obsidian/api.py <command>` via Bash tool
**Commands:**
- `status` — check connection
- `read "path"` / `create "path" "content"` / `append "path" "content"` / `delete "path"`
- `search "query"` / `list` / `list "folder/"`
- `daily` / `daily_append "content"`
**Requires:** Obsidian running with Local REST API plugin
**Special:** `create_literature_note()` in `obsidian/api.py` generates structured notes from Zotero data

### Heptabase
**When:** User asks about visual thinking or Heptabase features — **reference only, cannot automate**

### Journaling
**When:** User asks to journal, reflect, check-in, or do guided self-reflection
**How:** Read `rosebud/journal_intelligence.md` + `rosebud/journal_personas.md` + `journal/journal_log.md`, then guide conversationally with chosen persona, auto-generate analysis at end
**Personas:** 引導者(Guide, default), 園丁(Gardener/IFS), 教練(Coach), 鏡子(Mirror/CBT), 錨(Anchor/somatic), 夥伴(Companion) — see `rosebud/journal_personas.md`
**Modes:** Template-guided (pick from 16 templates) OR **free dialogue** (自由對話 — unstructured, user leads)
**Intelligence:** `rosebud/journal_intelligence.md` — adaptive questioning, cognitive distortion scan, emotion/people tagging, pattern recognition, cross-day linking, reading integration, structured response format
**History:** `journal/journal_log.md` — last 10 entries for cross-entry context
**Templates:** Daily intention, evening check-in, gratitude, dream journal, CBT reframing, ACT, IFS, boundary setting, communication repair, conversation prep, motivational interviewing, nervous system regulation, positive psychology, relationship reflection, knowing your needs

## Skill Reference Index

**Do NOT read all skill files at session start.** Only read the relevant file when the task requires it.

| Skill File | Read When |
|---|---|
| `zotero/skills.md` | User asks about Zotero usage, collecting references, citing, organizing, API usage, or LaTeX workflow |
| `obsidian/skills.md` | User asks about Obsidian vault setup, writing notes, linking, Dataview queries, Local REST API, or PKM methods |
| `heptabase/skills.md` | User asks about Heptabase usage, whiteboards, cards, PDF workflow, AI features, or **manual integration with Zotero/Obsidian** |
| `rosebud/journal_intelligence.md` | Journal workflow starts (Workflow 1) |
| `rosebud/journal_personas.md` | Journal workflow starts — persona selection |
| `rosebud/personas/<name>.md` | After user picks a specific persona |
| `rosebud/overview.md` | Journal workflow starts — template selection |
| `rosebud/rosebud_*.md` | After user picks a specific journal template |
| `notion/travel_plan_template.md` | User asks to create a travel plan on Notion |

## Knowledge Reference Index

**Do NOT read all knowledge files at session start.** Only read the relevant file when the topic comes up.

| Knowledge File | Read When |
|---|---|
| `zotero/knowledge.md` | User asks about Zotero concepts, architecture, API details, pricing, plugin ecosystem, or data formats |
| `obsidian/knowledge.md` | User asks about Obsidian architecture, plugin ecosystem, API methods, sync options, or comparison with other tools |
| `heptabase/knowledge.md` | User asks about Heptabase concepts, features, limitations, pricing, AI features, or why it has no API |
| `notion/overview.md` | User asks about Notion features, capabilities, or general usage |
| `notion/api_and_integrations.md` | User asks about Notion API details, MCP setup, or integration methods |
| `notion/features.md` | User asks about specific Notion features or what Notion can do |
| `notion/pricing.md` | User asks about Notion pricing or plans |
| `notion/notion_ai.md` | User asks about Notion's built-in AI features |
| `notion/competitors.md` | User asks to compare Notion with other tools |
| `docs/multi_agent_roadmap.md` | User asks about future architecture, multi-agent plans, or system expansion |

## Conventions

- **Language:** User-facing content in Traditional Chinese (繁體中文) unless specified otherwise
- **Files:** All configs and files inside this project directory, not global
- **Paths:** Generic placeholders — discover at runtime per machine
- **Notion styling:** Section headers `{color="green_bg"}`, callouts `gray_bg` with 💡
- **API keys:** Store in `.env`, never hardcode
