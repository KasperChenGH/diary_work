# Notion API & Integrations

## Notion API

### Overview
- RESTful API for programmatic access to pages, databases, blocks, users, and comments
- Two integration types: **Internal** (private workspace automations) and **Public** (shareable, OAuth 2.0-based)
- SCIM API for enterprise user/group provisioning
- Docs: https://developers.notion.com/

### What Developers Can Do
- Create, read, update, and delete pages and databases
- Query databases with filters and sorts
- Manage blocks (content elements) within pages
- Automated notifications monitoring database changes
- Build custom integrations and workflows

### Recent API Updates (2026)
- **/v1/views API (2026):** 8 new endpoints for programmatic database view management
- **API version 2026-03-11:** Modernized surface with changes to block placement, trash fields, and meeting note block naming
- **Status properties** now creatable/updatable via API and MCP
- **Webhook support** for real-time updates between apps

## MCP (Model Context Protocol)
- First-party MCP integrations with partners like Lovable, Perplexity, Mistral, and HubSpot
- External tools can read context from Notion workspace and write back
- Custom agents can leverage MCP for multi-source access

## Native Integrations
- Slack
- Google Drive
- GitHub
- Microsoft Teams
- Jira
- Google Calendar and Outlook (two-way sync)
- 100+ third-party app connections

## Automation Platforms
- Zapier
- Make
- Relay
- Native automations within Notion databases

## AI Connectors
- Slack, Google Drive, Microsoft Teams, Jira for AI context
- Circleback for meeting notes (95%+ accuracy, 100 languages)
