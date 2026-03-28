# Obsidian -- Knowledge

## Identity
- Private knowledge management and note-taking application
- Developed by Dynalist Inc. (Shida Li and Erica Xu)
- Launched public beta March 2020, reached v1.0 October 2022
- Built on Electron (desktop), native apps for mobile
- Philosophy: local-first, privacy-focused, future-proof plain text

## Core Concepts
- **Vault:** A folder on your filesystem that Obsidian opens and indexes. Contains notes + `.obsidian` config folder. Fully self-contained and portable.
- **Notes:** Plain `.md` (Markdown) files -- no proprietary format, no database
- **Wikilinks:** `[[Note Name]]` syntax for creating bidirectional links between notes
- **Backlinks:** Automatic reverse links showing which notes reference the current note
- **Unlinked Mentions:** Detection of note title text in other notes without explicit links
- **Graph View:** Visual network graph of notes (nodes) and links (edges)
- **Canvas:** Infinite spatial canvas for arranging notes, images, and cards visually
- **Frontmatter:** YAML metadata at the top of notes for properties (tags, dates, custom fields)
- **Embeds:** `![[Note Name]]` syntax to embed one note's content inside another
- **Tags:** `#tag` syntax, supports nesting like `#project/active`

## Architecture
- All data is plain Markdown files on local filesystem
- No cloud dependency by default -- data never leaves your machine
- `.obsidian` folder per vault stores settings, themes, plugins, workspace state
- Multiple vaults supported (e.g., work + personal)
- Sync options: Obsidian Sync (paid, E2E encrypted), iCloud, Dropbox, Syncthing, Git

## Platforms
- **Desktop:** Windows, macOS, Linux (Electron)
- **Mobile:** iOS and Android (native apps, not Electron)
- Same core feature set across all platforms

## Pricing
| Product | Cost |
|---------|------|
| Personal use | Free (all features, no restrictions) |
| Commercial license | $50/user/year |
| Obsidian Sync | $4-8/month (E2E encrypted sync) |
| Obsidian Publish | $8-16/month (publish notes as website) |
| Catalyst (supporter) | $25/$50/$100 one-time |

## Target Audience
- Knowledge workers, researchers, academics
- Writers and content creators
- Software developers (local-first, Vim support, extensible)
- Students
- PKM enthusiasts (Zettelkasten, PARA, Building a Second Brain)
- Privacy-conscious users wanting full data ownership

## API Access
- **No built-in API** -- Obsidian is local-first with no official REST API
- **Three ways to access programmatically:**

### 1. Local REST API Plugin (community)
- Plugin: **obsidian-local-rest-api** by coddingtonbear
- Runs HTTPS server on `localhost:27124` (HTTP on `27123`)
- Auth: `Authorization: Bearer <API_KEY>` header (key generated in plugin settings)
- Self-signed certificate (clients must disable cert verification or trust it)
- Auto-generates **OpenAPI spec** at root URL (Swagger-compatible)
- **Endpoints:**
  - `GET/PUT/PATCH/DELETE /vault/{path}` -- read, create, append, delete notes
  - `GET /vault/` -- list all files
  - `GET/PUT/PATCH /periodic/daily/` -- daily note operations
  - `POST /search/simple/` -- filename search
  - `POST /search/` -- Dataview-style queries (JsonLogic)
  - `GET /open/{path}` -- open note in Obsidian UI
  - `POST /commands/{commandId}` -- execute Obsidian commands
  - `GET /active/` -- get currently open file

### 2. Direct File System Access
- Vault is just a folder of `.md` files -- read/write with any language
- Metadata in YAML frontmatter, links use `[[wikilink]]` syntax
- Simplest for batch/offline processing when Obsidian is closed
- Caveat: race conditions possible if Obsidian is open and watching files

### 3. Obsidian URI Protocol
- `obsidian://open?vault=Name&file=path/to/note` -- open a note
- `obsidian://new?vault=Name&file=Name&content=...` -- create a note
- `obsidian://search?vault=Name&query=...` -- open search
- **Advanced URI plugin** extends with write, append, navigate to headings
- Limitation: fire-and-forget, no response returned

### MCP Server
- Community MCP servers exist (e.g., `obsidian-mcp`) wrapping the Local REST API
- Enables LLM agents (Claude, etc.) to interact with vaults via MCP tools

### No Official SDKs
- Use `requests`/`httpx` (Python) or `fetch` (JS) against Local REST API endpoints
- OpenAPI spec can generate client libraries via `openapi-generator`

## Plugin Ecosystem
- **25+ core plugins** shipped with Obsidian (toggleable individually)
- **1,800+ community plugins** via built-in browser:
  - **Dataview** -- query notes like a database (SQL-like language)
  - **Templater** -- advanced templating with JavaScript execution
  - **Kanban** -- Kanban boards from notes
  - **Excalidraw** -- embedded drawing and whiteboarding
  - **Calendar** -- calendar view for daily notes
  - **Tasks** -- advanced task management and queries
  - **Linter** -- auto-format Markdown
  - **Advanced Tables** -- better table editing
  - **Zotero, Readwise, Todoist, Anki** integrations
- **Hundreds of community themes** + CSS snippet customization
- Active community: Discord, official Forum, Reddit (r/ObsidianMD 200k+ subscribers)

## Collaboration Model
- Fundamentally single-user, local-first
- Obsidian Sync: limited vault sharing (not real-time co-editing)
- Obsidian Publish: one-way read-only website publishing
- Teams sometimes use Git, shared drives, or Syncthing (manual conflict resolution)
- No Google Docs-style simultaneous editing

## Strengths
- Data ownership -- plain Markdown, no vendor lock-in, future-proof
- Blazing fast even with tens of thousands of notes
- Massive plugin ecosystem for nearly any use case
- Highly customizable (themes, CSS, hotkeys, layouts)
- Best-in-class bidirectional linking and graph visualization
- Free for personal use with no feature restrictions
- Fully offline capable

## Limitations
- No real-time collaboration
- Learning curve for non-technical users
- Official sync is paid; third-party sync can cause conflicts
- Mobile apps less polished than dedicated mobile note apps
- Markdown tables awkward without plugins
- Workflows can depend on community plugins that may break or go unmaintained
- Electron-based desktop app has higher memory usage than native apps
