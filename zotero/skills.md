# Zotero -- Skills

## Collecting References
- Install Zotero Connector browser extension (Chrome/Firefox/Edge/Safari)
- Click connector icon on any supported site to save reference + full-text PDF in one click
- Drag PDFs directly into Zotero -- it auto-detects bibliographic metadata
- Use ISBN, DOI, or PubMed ID lookup to add items manually
- Subscribe to RSS feeds to monitor new publications from journals

## Organizing Your Library
- Create **collections** (like folders) to group items by project, topic, or course
- Apply **tags** for cross-cutting labels (e.g., `#methodology`, `#to-read`)
- Use **saved searches** for dynamic smart collections based on criteria
- Use **duplicate detection** to find and merge duplicate entries
- Drag items between collections (items can live in multiple collections)
- Use colored tags (up to 9) for quick visual identification

## Reading & Annotating
- Open PDFs, ePUBs, or HTML snapshots in Zotero's built-in reader
- **Highlight text** in multiple colors for different purposes
- Add **sticky notes** for inline commentary
- Use **area selection** tool to capture figures/tables
- All annotations are searchable and appear as child items in your library
- Extract annotations into a standalone note for review

## Citing in Documents
- Install the word processor plugin (Word, LibreOffice, Google Docs, OnlyOffice)
- Use the citation dialog to search and insert in-text citations as you write
- Zotero 8 citation dialog has two modes:
  - **List mode** -- quick search across all libraries
  - **Library mode** -- hierarchical browsing within specific collections
- Switch citation styles at any time -- Zotero reformats the entire document
- Bibliography is auto-generated and auto-updated at the end of the document

## Syncing Across Devices
- Create a free Zotero account at zotero.org
- Metadata sync is free and unlimited
- File sync uses your storage quota (300 MB free, upgradeable)
- Alternative: use WebDAV for file storage to avoid Zotero storage costs
- Mobile apps sync with the same account

## Collaborating with Groups
- Create a group library from zotero.org
- Invite members by Zotero username or email
- Choose visibility: private, closed-public, or open-public
- Assign roles (Member, Admin, Owner) to control edit permissions
- Group items are separate copies from personal library -- copy items between them
- File sharing only available in private and closed-membership groups

## LaTeX Workflow (Better BibTeX)
- Install Better BibTeX plugin for fine-grained citation key control
- Auto-export `.bib` files that stay in sync with your Zotero library
- Use `\cite{citekey}` in LaTeX documents
- Configure citation key format (e.g., `[auth:lower][year]`)

## Integrating with Other Tools
- **Obsidian:** Use Zotero Integration plugin to pull references and annotations into notes
- **Logseq/Notion:** Community connectors available
- **Heptabase:** Beta Zotero integration
- **API access:** Use Zotero Web API v3 for custom integrations and automation

## Using the Zotero API
- Get an API key at https://www.zotero.org/settings/keys/new
- Find your userID at https://www.zotero.org/settings/keys

### curl example
```bash
curl -H "Zotero-API-Version: 3" \
     -H "Zotero-API-Key: YOUR_API_KEY" \
     "https://api.zotero.org/users/YOUR_USER_ID/items/top?limit=5&format=json"
```

### Python with pyzotero
```python
from pyzotero import zotero

zot = zotero.Zotero("YOUR_USER_ID", "user", "YOUR_API_KEY")

# Get top 5 items
items = zot.top(limit=5)
for item in items:
    print(item["data"]["title"])

# Search by tag
tagged = zot.items(tag="machine-learning")

# Create an item
template = zot.item_template("journalArticle")
template["title"] = "My New Article"
template["creators"] = [{"creatorType": "author", "firstName": "Jane", "lastName": "Doe"}]
zot.create_items([template])
```

### Common API operations
- **List items:** `GET /users/{id}/items/top?limit=25`
- **Get single item:** `GET /users/{id}/items/{itemKey}`
- **Create items:** `POST /users/{id}/items` with JSON body
- **Update item:** `PATCH /users/{id}/items/{itemKey}` with `If-Unmodified-Since-Version` header
- **Delete item:** `DELETE /users/{id}/items/{itemKey}`
- **List collections:** `GET /users/{id}/collections`
- **Items in collection:** `GET /users/{id}/collections/{collKey}/items`
- **Search:** `GET /users/{id}/items?q=search+term`
- **Filter by tag:** `GET /users/{id}/items?tag=tagname`

## Power User Tips
- Use the **Quick Copy** feature (Ctrl/Cmd+Shift+C) to copy formatted citations to clipboard
- Set up **auto-file-renaming** rules with ZotMoov plugin
- Use **Related Items** to manually link connected references
- Use the **Timeline** view for chronological browsing
- Enable **Zotero OCR** plugin for searchable scanned PDFs
