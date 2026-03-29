# Overall Knowledge

Accumulated facts, patterns, and reusable solutions Claude has learned across sessions. Unlike memory (which is chronological), knowledge is organized by topic and kept up to date — older entries get refined or merged as understanding deepens.

---

<!-- Entries are added/updated by Claude. Format:
## Topic Name
- Key facts and patterns
- Reusable solutions
- Last updated: YYYY-MM-DD
-->

## Zotero → Obsidian 工作流程
- **抓資料夾:** 用 collection key（`python zotero/api.py collection KEY`），不用關鍵字搜尋
- **抓標註:** `python zotero/api.py annotations KEY` — 已修正為兩層查詢（item children + PDF attachment children），可抓 PDF 高亮、行內筆記、頂層筆記
- **建立筆記前先確認:** 查 `PhD_vault/Research/Literature/` 的 `zotero_key` frontmatter，避免重複
- **命名規則:** Zotero 標題截短（非 key），e.g. `Agency as a joint endeavor_ making sense...md`
- **儲存位置:** 永遠存到 `PhD_vault/Research/Literature/`，勿建新頂層資料夾
- **模板:** `PhD_vault/Templates/Zotero_Template.md`
- **標註格式:** `> 引文 ([p.X](zotero://open-pdf/library/items/ATT_KEY?page=X&annotation=ANN_KEY))` + `📝 筆記：comment`
- **綜合筆記:** `_Synthesis_[Topic].md`，存同一資料夾
- Last updated: 2026-03-29

## Epistemic Agency（知識能動性）
- **定義:** 個人/群體在知識建構中主動參與、質疑、協商並主導信念形成與修正的能力
- **理論基礎:** Damşa et al. (2010) — agency 是 joint endeavor，在社會互動中共同構成
- **主要張力:** AI 是工具 vs. AI 是「認知模式改變者」（削弱人的主動性）
- **可培養性:** 可透過設計任務激活，但過程非線性（Zhou 2025, Baze 2025）
- **AI 脈絡:** 需主動教育設計以保護人類能動性（Wu 2025, Yan 2025, Coeckelbergh 2025）
- **研究缺口:** 測量工具不足、長期效果未知、跨文化研究缺乏
- **Zotero 資料夾:** Epistemic Agency collection key `28EDHVUZ`（26 篇）
- **Obsidian:** `PhD_vault/Research/Literature/` — 25 篇個別筆記 + `_Synthesis_Epistemic_Agency.md`
- **Notion:** 頁面 ID `332d3914-55cd-8172-9850-e9a6e99a1e80`
- Last updated: 2026-03-29
