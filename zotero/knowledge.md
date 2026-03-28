# Zotero -- Knowledge

## Identity
- Free, open-source reference management software (AGPL license)
- Developed by Corporation for Digital Scholarship (nonprofit, George Mason University)
- Tagline: "Your personal research assistant"
- Latest major release: Zotero 8

## Core Concepts
- **Library:** Central database of all your saved references (items) and attachments
- **Items:** Individual references (journal articles, books, web pages, etc.) with bibliographic metadata
- **Collections:** Folder-like groupings of items (an item can belong to multiple collections)
- **Tags:** Labels for cross-cutting categorization across collections
- **Saved Searches / Smart Collections:** Dynamic collections based on search criteria
- **Attachments:** Files linked to items -- PDFs, ePUBs, HTML snapshots, images
- **Notes:** Rich-text notes linked to items or standalone
- **Annotations:** Highlights, sticky notes, and area selections made within the built-in reader
- **Group Libraries:** Shared libraries separate from personal libraries for team collaboration
- **CSL (Citation Style Language):** Open standard powering 9,000+ citation styles

## Architecture
- Desktop app is the primary client (Windows, macOS, Linux)
- Mobile apps for iOS/iPadOS and Android (stable since June 2025)
- Web library at zotero.org for browser access
- Browser connectors (Chrome, Firefox, Edge, Safari) communicate with desktop client or fall back to web API
- Zotero Web API v3 (REST) for programmatic read/write access
- Local SQLite database stores metadata; attachments stored as files on disk

## Data & Formats
- **Import/Export:** BibTeX, BibLaTeX, RIS, CSL JSON, MODS, RDF, NBIB, CSV, Wikipedia templates
- **Attachments:** PDFs, ePUBs, HTML snapshots, images, any file type
- **Built-in reader:** Supports PDF, ePUB, and HTML snapshots with annotation

## Pricing
| Tier | Storage | Cost |
|------|---------|------|
| Free | 300 MB | $0 |
| 2 GB | 2 GB | $20/year |
| 6 GB | 6 GB | $60/year |
| Unlimited | Unlimited | $120/year |

Software is fully free. Storage costs only for cloud file syncing. Metadata sync is free and unlimited.

## Target Audience
- Academic researchers across all disciplines
- Graduate and undergraduate students
- Librarians
- Journalists, lawyers, professionals organizing source materials
- Collaborative research teams and lab groups

## API Access
- **Zotero Web API v3** -- full REST API at `https://api.zotero.org`
- **Auth:** API key via `Zotero-API-Key` header (or OAuth 1.0a for third-party apps)
- **Get a key:** https://www.zotero.org/settings/keys/new (select per-library read/write permissions)
- **User ID:** Found at https://www.zotero.org/settings/keys
- **API version header:** `Zotero-API-Version: 3`
- **Endpoints scoped to** `/users/{userID}/` or `/groups/{groupID}/`:
  - `/items` -- CRUD on items, `/items/top`, `/items/trash`, `/items/{key}/children`
  - `/collections` -- CRUD on collections, `/collections/{key}/items`
  - `/tags` -- list all tags
  - `/searches` -- saved searches CRUD
  - `/groups` -- list user's groups
  - Schema endpoints (no auth): `/itemTypes`, `/itemFields`, `/creatorTypes`
- **Query params:** `format` (json/atom/bib/keys), `limit`, `start`, `sort`, `q`, `tag`, `itemType`, `since`
- **Rate limits:** ~10 req/s; respect `Backoff` and `Retry-After` headers. Writes more tightly limited.
- **Write operations:** JSON request bodies, optimistic concurrency via `If-Unmodified-Since-Version` header
- **Best library:** pyzotero (Python) -- `pip install pyzotero`
- **Other libraries:** `zotero-api-client` (npm/JS), zotero-ruby (Ruby)
- **Docs:** https://www.zotero.org/support/dev/web_api/v3/start

## Plugin Ecosystem
- **Better BibTeX** -- fine-grained citation key control (essential for LaTeX)
- **ZotMoov** -- automated file renaming and management
- **Zotero OCR** -- OCR for scanned PDFs
- **AI plugins** -- PapersGPT, Aria, Beaver for summarization and Q&A
- **Cross-tool integrations** -- Obsidian, Logseq, Notion, Heptabase connectors

## Collaboration Model
- Group libraries with unlimited members
- Three visibility types: private, closed-membership public, open public
- Roles: Member, Administrator, Owner
- Group file storage counts against the owner's quota
- No real-time co-editing (sync-based)

## Strengths
- Completely free and open-source, no paywalled features
- Cross-platform (desktop + mobile + web)
- 9,000+ citation styles
- Browser connector works with thousands of sites
- Strong plugin ecosystem
- Unlimited local storage; you own your data
- Standard export formats, no vendor lock-in

## Limitations
- Free cloud storage only 300 MB
- No real-time collaborative editing
- Interface can feel cluttered
- Note-taking is basic compared to Obsidian/Notion
- No built-in AI features (requires plugins)
- Learning curve for syncing, groups, and plugin configuration
