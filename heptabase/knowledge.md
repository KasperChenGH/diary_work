# Heptabase -- Knowledge

## Identity
- Intelligent, visual knowledge base for learning, research, and deep thinking
- Founded by Alan Chan
- Spatial, canvas-based approach: ideas as cards on infinite whiteboards
- Mission: help users make sense of complex topics through visual organization
- Reached v1.0 status

## Core Concepts
- **Whiteboards:** Infinite spatial canvases for arranging cards. Support nesting (sub-whiteboards) for hierarchical depth.
- **Cards:** Atomic, self-contained notes (text, images, links). The fundamental knowledge unit. A single card can appear on multiple whiteboards and stays synced everywhere.
- **Card Library:** Central repository of all cards, searchable and filterable. Includes AI-powered card suggestions.
- **Connections:** Visual lines drawn between cards on a whiteboard to show relationships.
- **Sections:** Named groupings of cards on a whiteboard for visual clustering.
- **Tags & Properties:** Metadata for organizing and filtering cards across the library.
- **Daily Journal:** Automatic daily note for diary-style quick capture.
- **Web Tab:** Built-in browser for reading websites and chatting with AI about content.

## Architecture
- Offline-first: data stored locally on your device
- Background cloud sync across devices when online
- Desktop apps for macOS, Windows, Linux
- Mobile apps for iOS and Android (home screen widgets)
- Web app (browser-based, beta)
- No public API or plugin system yet

## AI Features
- Chat with AI using individual cards or entire whiteboards as context
- AI actions on cards: summarize, translate, create mind maps, extract key points
- AI filter in card library suggests related cards
- Drag AI responses onto whiteboards as new cards
- Supports OpenAI, Anthropic Claude, Google Gemini via user-provided API keys
- Built-in AI credits included with subscription

## Pricing
No free tier. 7-day free trial.

| Plan | Cost | AI Credits |
|------|------|------------|
| Pro | $11.99/mo or $8.99/mo annually | 100/month |
| Premium | $17.99/mo annually | 1,800/month |
| Premium+ | Higher tier | More AI capacity |

BYOK (bring your own key) for AI models does not consume Heptabase credits.

## Target Audience
- Students learning complex academic subjects
- Researchers synthesizing literature
- Lifelong learners exploring new domains
- Knowledge workers managing complex projects
- Writers and content creators organizing ideas
- Positioned for sense-making, not general project management

## Integrations
- **Readwise** -- auto-sync highlights from Kindle, Instapaper, web articles
- **Google Calendar** -- in-app calendar
- **Zotero** -- beta integration for academic references
- **PDF/Markdown** -- import and export
- **Obsidian export** -- migration and backup path
- **MCP Server** -- external tools (ChatGPT, Claude) can create cards and interact with data
- No public API or plugin ecosystem yet

## Collaboration Model
- Whiteboard sharing via email invitation
- Permission levels: Can View, Can Chat, Can Edit, Full Access
- Real-time collaboration on shared whiteboards
- Built-in chat/discussion on whiteboards
- Single card sharing with specific permissions
- Public links for publishing whiteboards
- Collaborators do not need a paid subscription

## API Access
- **No public API exists.** Most requested feature but no announced timeline.
- **No native integrations** with Zapier, Make, n8n, or similar automation platforms
- **No browser extension API** or plugin system

### Available Programmatic Methods

| Method | Read | Write | Live Data | Official |
|---|---|---|---|---|
| Public API | No | No | N/A | N/A |
| MCP Server (community) | Yes | No | No (export snapshot) | No |
| JSON/MD Export + scripts | Yes | No | No (manual re-export) | Partially |

### Community MCP Server
- **Name:** `heptabase-mcp` (GitHub/npm)
- Does NOT use an API -- reads from Heptabase's **local data export** (JSON files)
- **Read-only:** search/list whiteboards and cards, read card content
- **Static snapshot:** data goes stale on any change in Heptabase; must re-export to refresh
- Not officially supported by the Heptabase team

### Manual Data Export
- Export all data via Settings > Export
- Format: **JSON + Markdown** (cards as `.md`, JSON for whiteboard structure, relationships, tags)
- Can be parsed with Python/Node scripts for analysis, graph visualization, or syncing to other tools

### Team's Position on API
- Demand acknowledged on community forums and roadmap
- Not a near-term priority; focus remains on core product features
- When built, they want stable endpoints, proper auth -- not a rushed release

## Comparison with Alternatives
| Aspect | Heptabase | Obsidian | Notion |
|---|---|---|---|
| Core strength | Visual spatial thinking | Text-centric + graph view | Databases + collaboration |
| Data storage | Local-first + cloud sync | Fully local (plain markdown) | Cloud-based |
| Customization | Limited (opinionated UX) | Extremely extensible | Moderate |
| Free tier | No (trial only) | Free for personal use | Free tier available |
| API/Plugins | No public API yet | Rich plugin ecosystem | Extensive API |
| Best for | Learning and research | Technical users, full control | Teams and project management |

## Strengths
- Unique visual-spatial approach unmatched by competitors
- Excellent for deep learning and complex, interconnected topics
- Offline-first with fast local search (10,000+ notes in <1 second)
- Cross-platform (desktop, mobile, web)
- AI deeply integrated into the visual workflow
- Cards-on-whiteboards paradigm intuitive once learned
- Active development with frequent updates
- Real-time collaboration on whiteboards

## Limitations
- Steep learning curve
- No free tier -- subscription only
- Limited integrations, no public API yet
- No multi-workspace support yet (in development)
- Mobile experience lags behind desktop
- Performance can slow on very large whiteboards
- Smaller community and ecosystem vs Obsidian/Notion
