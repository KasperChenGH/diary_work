# Overall Memory

Session-level memories: problems encountered, how they were solved, user preferences discovered, and decisions made. Claude reads this at the start of every session and appends to it at the end.

---

<!-- Entries are added automatically by Claude at the end of each session. Format:
## [YYYY-MM-DD] Session Topic
- **Problem:** What happened
- **Solution:** How it was resolved
- **Takeaway:** What to remember for next time
-->

## [2026-03-29] Zotero User ID
- **Problem:** Used wrong user ID (124302) — all API calls returned 403
- **Solution:** Correct ID is 8834826 (found at zotero.org/settings/keys)
- **Takeaway:** Always confirm user ID from the settings page, not from memory

## [2026-03-29] Obsidian Literature Note Folder & Naming
- **Problem:** Created notes in `Literature/Epistemic_Agency/` with Zotero-key filenames (e.g. `KGMP5P52.md`)
- **Solution:** Correct folder is `PhD_vault/Research/Literature/`, correct naming is truncated Zotero title (replace `:` and `/` with `_`)
- **Takeaway:** Always check `PhD_vault/Research/Literature/` first; never create a new top-level folder

## [2026-03-29] Zotero get_annotations() Missing PDF Highlights
- **Problem:** `get_annotations()` only fetched direct children of item — missed all PDF highlights
- **Solution:** Added second-level fetch: item → PDF attachment children → annotation items
- **Takeaway:** Zotero annotations live under the PDF attachment, not directly under the parent item

## [2026-03-29] Notion 📚 研究文獻資料庫 Integration Permission
- **Problem:** All 28 PATCH requests to Notion returned 404 — database existed but integration had no access
- **Solution:** User shared the database with the "Diary" integration in Notion settings → all 28 succeeded
- **Takeaway:** When Notion returns 404 on a known DB, check integration sharing permissions first

## [2026-03-29] YAML Frontmatter Parsing — notion_id Key
- **Problem:** Regex `r'^([\w\s/\(\)]+?):\s*(.*)'` failed to capture `notion_id` from Obsidian frontmatter
- **Solution:** Used targeted regex `r'^notion_id:\s*["\']?([0-9a-f\-]+)["\']?'` for that specific field
- **Takeaway:** Generic YAML regex is fragile; use field-specific patterns for critical keys like notion_id
