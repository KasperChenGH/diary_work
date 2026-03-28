# Heptabase -- Skills

## Getting Started
- Sign up and start with 7-day free trial
- Create your first whiteboard as a workspace for a topic or project
- Create cards directly on the whiteboard or from the card library
- Arrange cards spatially to reflect how ideas relate to each other

## Creating & Managing Cards
- Click on a whiteboard to create a new card
- Write rich text content inside cards (headings, lists, images, links)
- A card is an atomic unit -- keep each card focused on one idea
- Cards live in the **Card Library** and can be placed on multiple whiteboards
- Use the card library search to find any card across your entire knowledge base
- Apply **tags** and **properties** for structured metadata and filtering

## Working with Whiteboards
- Create whiteboards for different topics, projects, or research areas
- Drag cards freely to arrange them spatially
- Group related cards into **sections** with labels
- Draw **connections** (lines) between cards to show relationships
- Create **sub-whiteboards** by nesting whiteboards inside whiteboards for depth
- Use zoom and pan to navigate large whiteboards
- Color-code cards and sections for visual distinction

## Capture Workflow
- Create cards directly from thoughts and notes
- Use **Daily Journal** for quick daily capture
- Import PDFs and annotate them -- highlights become extractable cards
- Use the **Web Tab** to browse and capture from websites
- Sync highlights from **Readwise** (Kindle, Instapaper, articles)
- Drag AI chat responses onto whiteboards as new cards

## PDF Research Workflow
- Import PDF documents into Heptabase
- Read and highlight text directly in the built-in PDF viewer
- Add notes alongside highlights
- Export highlights as individual cards onto a whiteboard
- Arrange extracted cards spatially to synthesize findings

## Using AI Features
- Open AI chat and select cards or whiteboards as context
- Ask AI to explain, summarize, or compare ideas from your cards
- Run **AI actions** on individual cards:
  - Summarize content
  - Translate to another language
  - Generate mind maps
  - Extract key points
- Drag valuable AI responses onto whiteboards for further development
- Use AI filter in card library to discover related cards you may have missed
- Bring your own API keys (OpenAI, Claude, Gemini) to avoid using built-in credits

## Collaboration
- Click **Share** on a whiteboard to invite collaborators via email
- Set permission levels per person: Can View, Can Chat, Can Edit, Full Access
- Collaborators can join without a paid subscription
- Use built-in **chat/discussion** on whiteboards for team communication
- Share individual cards with specific permission levels
- Generate **public links** to publish whiteboards for wider viewing

## Integrating with Other Tools
- **Readwise:** Connect in settings to auto-sync reading highlights
- **Google Calendar:** View calendar events within Heptabase
- **Zotero:** Beta integration for pulling academic references
- **Markdown export:** Export cards and whiteboards as Markdown files
- **Obsidian migration:** Export data for use in Obsidian
- **MCP Server:** Connect external AI tools (ChatGPT, Claude) to create cards and interact with your data programmatically

## Sense-Making Methodology
1. **Capture broadly** -- Collect cards from reading, lectures, ideas, and conversations
2. **Cluster on whiteboards** -- Group related cards and label the clusters
3. **Draw connections** -- Identify and visualize relationships between clusters
4. **Nest for depth** -- Create sub-whiteboards to drill into complex sub-topics
5. **Synthesize** -- Use AI and your own writing to create summary cards that bridge clusters
6. **Revisit and reorganize** -- As understanding deepens, rearrange the spatial layout

## Programmatic Access (Limited)

### Exporting Data
- Go to Settings > Export to download all data as JSON + Markdown
- Cards export as `.md` files with content
- JSON metadata contains whiteboard structure, card positions, relationships, tags
- Re-export manually whenever you need fresh data

### Parsing Exports with Python
```python
import json
from pathlib import Path

# Locate the export folder -- ask the user or search for the most recent Heptabase export
export_dir = Path("<HEPTABASE_EXPORT_PATH>")

# Read whiteboard metadata
with open(export_dir / "whiteboards.json") as f:
    whiteboards = json.load(f)

for wb in whiteboards:
    print(f"Whiteboard: {wb['name']}")

# Read card markdown files
for card_file in export_dir.glob("cards/*.md"):
    content = card_file.read_text(encoding="utf-8")
    print(f"Card: {card_file.stem}")
    print(content[:200])
```

### Using the Community MCP Server
- Install `heptabase-mcp` from npm/GitHub
- Export your Heptabase data and point the MCP server to the export folder
- Enables LLM agents (Claude, ChatGPT) to search and read your cards/whiteboards
- **Read-only** -- cannot write back to Heptabase
- Must re-export data to refresh what the MCP server sees

### Workarounds for Writing
- No programmatic write path exists
- Manual import of Markdown files is possible but not API-driven
- For automation, consider using Heptabase alongside a tool with API access (Zotero, Obsidian) and manually syncing

## Manual Integration with Daily Agent Workflows

Heptabase has no write API, so all integration is manual. Here's how to use it alongside the automated tools.

### Connecting Zotero to Heptabase (One-Time Setup)
1. Open Heptabase → Settings → Integrations
2. Find **Zotero** (beta integration) and click Connect
3. Sign in with your Zotero account and authorize access
4. Once connected, your Zotero references will appear in Heptabase's import panel
5. You can pull references onto whiteboards as cards with metadata

### Academic Workflow: After the Automated Pipeline
After Claude runs the Zotero → Obsidian → Notion pipeline:
1. Open Heptabase and create a whiteboard for your research topic
2. Pull relevant Zotero references onto the whiteboard (via the Zotero integration)
3. Arrange papers spatially — group by theme, methodology, or argument
4. Draw connections between papers that build on, contradict, or extend each other
5. Create summary cards that synthesize findings across clusters
6. Use sub-whiteboards for deep dives into specific sub-topics
7. Use AI features to compare and explain ideas from your cards

### Journal Workflow: Visual Reflection
1. After a journal session, open Heptabase's Daily Journal
2. Create cards from key insights or patterns Claude identified
3. Place them on a personal growth whiteboard to track themes over time
4. Connect related insights across days — see your emotional/behavioral patterns visually

### When to Use Heptabase vs Obsidian
| Use Case | Heptabase | Obsidian |
|---|---|---|
| Structured literature notes | ❌ Use Obsidian (automated) | ✅ Created by pipeline |
| Visual thinking / spatial arrangement | ✅ Whiteboards | ❌ Not spatial |
| Discovering connections between papers | ✅ Draw lines between cards | ⚠️ Manual linking |
| Writing drafts / pre-writing | ✅ Arrange argument visually, then write | ✅ Write in vault |
| Quick daily capture | ✅ Daily Journal | ✅ Daily note |
| Searchable research archive | ⚠️ Card library search | ✅ Full-text search via API |

### Keeping Data in Sync
- **Zotero → Heptabase:** Automatic via integration (references sync when connected)
- **Obsidian → Heptabase:** Manual. Export Obsidian notes as Markdown, import into Heptabase if needed
- **Heptabase → Obsidian:** Manual. Use Heptabase export (Settings → Export) to get Markdown files

## Tips for Effective Use
- Keep cards atomic -- one idea per card for maximum flexibility
- Use whiteboards as thinking spaces, not just storage
- Start messy and refine -- spatial arrangement is an iterative process
- Use sections to create visual boundaries between related groups
- Leverage AI to surface connections you might miss manually
- Use daily journal for quick capture, then promote entries to cards on whiteboards
- Use sub-whiteboards to prevent any single whiteboard from getting too crowded
