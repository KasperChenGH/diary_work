# Obsidian -- Skills

## Setting Up a Vault
- Create a new vault by choosing a folder on your filesystem
- Obsidian creates a `.obsidian` config folder inside it
- Each vault is independent with its own settings, plugins, and themes
- Use multiple vaults to separate work/personal/projects

## Writing & Editing Notes
- Write in Markdown with **live preview** (WYSIWYG) or **source mode**
- Use `#`, `##`, `###` for headings, `**bold**`, `*italic*`, `- ` for lists
- Add YAML frontmatter at the top for metadata:
  ```yaml
  ---
  tags: [research, pkm]
  date: 2026-03-28
  status: draft
  ---
  ```
- Use split panes and tabs to work on multiple notes at once
- Command palette (Ctrl/Cmd+P) for quick access to all commands

## Linking & Building Knowledge
- Create links with `[[Note Name]]` -- works even if target note doesn't exist yet
- Link to specific headings: `[[Note Name#Heading]]`
- Custom display text: `[[Note Name|Display Text]]`
- Embed entire notes or sections: `![[Note Name]]` or `![[Note#Heading]]`
- Use **backlinks panel** to see all notes linking to the current note
- Check **unlinked mentions** to find implicit connections and convert to links
- Use **tags** (`#topic`) and **nested tags** (`#project/active`) for categorization

## Using Graph View
- Open graph view to see your entire vault as a network
- Filter by tags, folders, or search queries
- Color-code groups of notes for visual distinction
- Adjust forces (repulsion, link distance) for layout
- Use **local graph** to see connections for just the current note
- Identify orphan notes (unlinked) and cluster patterns

## Using Canvas
- Create a canvas file for spatial arrangement of ideas
- Add note cards, image cards, web link cards, or text-only cards
- Draw connections between cards
- Group and arrange cards freely on the infinite canvas
- Useful for brainstorming, project planning, and visual mapping

## Daily Notes & Journaling
- Enable the **Daily Notes** core plugin
- Configure a template for consistent daily entries
- Set a folder for daily notes (e.g., `Journal/Daily/`)
- Click the calendar icon or use hotkey to create today's note
- Use the **Calendar** community plugin for a visual calendar interface

## Templates & Automation
- **Core Templates plugin:** Define template files and insert them into new notes
- **Templater plugin (community):** Advanced templating with:
  - Dynamic dates, titles, cursor placement
  - JavaScript execution for custom logic
  - Auto-apply templates on note creation based on folder
- Create templates for meeting notes, project pages, literature notes, etc.

## Querying Notes with Dataview
- Install **Dataview** community plugin
- Query notes using a SQL-like language:
  ```dataview
  TABLE status, date FROM #research
  WHERE status = "active"
  SORT date DESC
  ```
- Create dynamic tables, lists, and task views that auto-update
- Use inline fields (`Key:: Value`) for structured metadata
- Combine with frontmatter properties for powerful filtering

## Task Management
- Use `- [ ]` for tasks, `- [x]` for completed
- **Tasks plugin (community):** Query and filter tasks across the vault
  ```tasks
  not done
  due before next week
  sort by due
  ```
- **Kanban plugin:** Turn a note into a Kanban board with draggable cards

## Syncing & Publishing
- **Obsidian Sync:** Enable in settings, sign in, choose vaults to sync
- **Third-party sync:** iCloud (simple), Git (version control), Syncthing (P2P)
- **Obsidian Publish:** Select notes to publish as a read-only website
- Avoid Dropbox/Google Drive for sync -- can cause file conflicts

## Integrating with Other Tools
- **Zotero:** Zotero Integration plugin pulls references and annotations into notes
- **Readwise:** Official plugin syncs highlights from Kindle, articles, podcasts
- **Todoist:** Sync tasks between Obsidian and Todoist
- **Anki:** Flashcard export for spaced repetition
- **Excalidraw:** Embedded drawings and diagrams within notes

## Customization
- Install community themes from Settings > Appearance
- Add **CSS snippets** in `.obsidian/snippets/` for fine-grained style tweaks
- Remap hotkeys in Settings > Hotkeys
- Configure workspace layouts and save/restore them
- Enable/disable core plugins as needed
- Optional Vim keybindings for keyboard-driven editing

## Using the Local REST API
- Install **Local REST API** from community plugins
- Enable it and copy the API key from plugin settings
- Default: `https://127.0.0.1:27124` (HTTPS) or `http://127.0.0.1:27123` (HTTP)

### curl examples
```bash
# Read a note
curl -k -H "Authorization: Bearer YOUR_API_KEY" \
     "https://127.0.0.1:27124/vault/Projects/my-note.md"

# Create/overwrite a note
curl -k -X PUT -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: text/markdown" \
     -d "# New Note\nContent here" \
     "https://127.0.0.1:27124/vault/Projects/new-note.md"

# Append to a note
curl -k -X PATCH -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: text/markdown" \
     -d "\n## Appended Section\nMore content" \
     "https://127.0.0.1:27124/vault/Projects/my-note.md"

# List all files
curl -k -H "Authorization: Bearer YOUR_API_KEY" \
     "https://127.0.0.1:27124/vault/"

# Search by filename
curl -k -X POST -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"query": "project plan"}' \
     "https://127.0.0.1:27124/search/simple/"

# Get today's daily note
curl -k -H "Authorization: Bearer YOUR_API_KEY" \
     "https://127.0.0.1:27124/periodic/daily/"
```

### Python example
```python
import requests

API_KEY = "your-api-key"
BASE = "https://127.0.0.1:27124"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Read a note
resp = requests.get(f"{BASE}/vault/Projects/my-note.md", headers=HEADERS, verify=False)
print(resp.text)

# Create a note
requests.put(f"{BASE}/vault/Projects/new-note.md",
             headers={**HEADERS, "Content-Type": "text/markdown"},
             data="# Hello\nNew note content", verify=False)

# Append to daily note
requests.patch(f"{BASE}/periodic/daily/",
               headers={**HEADERS, "Content-Type": "text/markdown"},
               data="\n- Task added via API", verify=False)
```

### Direct file access (when Obsidian is closed)
```python
from pathlib import Path

# Locate the vault path first -- search common locations or ask the user
# e.g. look in ~/Documents, ~/ObsidianVault, or find .obsidian folders on disk
vault = Path("<VAULT_PATH>")

# Read a note
content = (vault / "Projects" / "my-note.md").read_text(encoding="utf-8")

# Write a note
(vault / "Projects" / "new-note.md").write_text("# New Note\nContent", encoding="utf-8")

# List all markdown files
for note in vault.rglob("*.md"):
    print(note.relative_to(vault))
```

## PKM Methodologies in Obsidian
- **Zettelkasten:** Atomic notes with unique IDs, linked together, no hierarchy
- **PARA:** Organize folders as Projects, Areas, Resources, Archive
- **MOCs (Maps of Content):** Hub notes that link to related notes on a topic
- **Daily Notes + Periodic Reviews:** Capture daily, review weekly/monthly
- **Progressive Summarization:** Layer highlights and bold text over time
