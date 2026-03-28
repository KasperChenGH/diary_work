# Travel Plan Template (旅遊行程)

Based on user's Notion template page "旅遊行程"

## How to Use

When asked to create a travel plan on Notion:
1. Create main page with icon �� and title format: "🌴 {Destination} Travel Plan — {Date Range}"
2. Build page content using the Notion Markdown below
3. Create 行程安排 database with schema and views
4. Create sub-pages (行李清單, 行程參考資料, 採購清單)
5. Populate database with itinerary entries
6. Note: API creates default table view first; rename it to "行程時間表格" then create board view "行程圖表"

## Day Label Format

`D{n}.{MM}/{DD}({weekday})` e.g. "D1.04/07(二)", "D2.04/08(三)"
- Weekday in Chinese: 一=Mon, 二=Tue, 三=Wed, 四=Thu, 五=Fri, 六=Sat, 日=Sun

## Page Content (Notion Markdown)

```markdown
<callout icon="💡" color="gray_bg">
	旅遊小約定：
	快快樂樂出門、平平安安回家
</callout>

## 行程安排 {color="green_bg"}

<database url="{DB_URL}" inline="true">行程安排</database>

<columns>
	<column>
		## 行前準備 {color="green_bg"}
		<page url="{行李清單_URL}">行李清單</page>
		<page url="{行程參考資料_URL}">行程參考資料</page>
	</column>
	<column>
		## **代辦事項** {color="green_bg"}
		- [ ] 旅遊保險
		- [ ] eSIM/網卡
		- [ ] 餐廳預約
		- [ ] 門票購買
		- [ ] 住宿預定
	</column>
	<column>
		## 航班資訊 {color="green_bg"}
		**訂位代號：**
		去程
		回程
	</column>
</columns>

## 出發Go! {color="green_bg"}

<page url="{採購清單_URL}">採購清單</page>

---
```

## Database: 行程安排

### SQL Schema

```sql
CREATE TABLE (
  "地點" TITLE,
  "類別" SELECT('🛒 逛街':orange, '⛱ 景點':brown, '🧁 吃喝':yellow, '🚗 移動':blue, '🏡 住宿':green),
  "描述" RICH_TEXT,
  "Google Map" URL,
  "照片" FILES,
  "第幾天" SELECT('{day_labels}'),  -- Dynamic: generate per trip dates with colors blue, yellow, green, brown, pink, red...
  "預計停留時間" DATE
)
```

### Views (create in this order)

1. Rename default table view to **行程時間表格**
   - `SORT BY "預計停留時間" ASC; SHOW "第幾天", "預計停留時間", "類別", "地點", "描述", "Google Map"`

2. **行程圖表** (Board) — main visual view, user should drag this to first tab
   - `GROUP BY "第幾天"; SHOW "地點", "類別", "描述", "Google Map"; COVER "照片"`

3. **景點** (Gallery)
   - `FILTER "類別" = "⛱ 景點"; SHOW "地點", "描述", "第幾天"; COVER "照片"`

4. **逛街** (Gallery)
   - `FILTER "類別" = "🛒 逛街"; SHOW "地點", "描述", "第幾天"; COVER "照片"`

5. **吃喝** (Gallery)
   - `FILTER "類別" = "🧁 吃喝"; SHOW "地點", "描述", "第幾天"; COVER "照片"`

6. **住宿** (Table)
   - `FILTER "類別" = "🏡 住宿"; SHOW "第幾天", "地點", "描述"`

### Entry Format

Each itinerary entry should have:
- 地點: Location/activity name (in Chinese)
- 類別: One of the 5 categories
- 第幾天: Day label
- 描述: Short description
- 預計停留時間: datetime range (start + end, is_datetime=1)

## Sub-page: 行李清單 (🧳)

```markdown
<callout icon="💡" color="gray_bg">
	**行李托運、上機物品規定重點：**
	- 僅能拖運：防狼噴霧劑、大於100ml液體、酒類、**不可**摺疊雨傘。
	- 僅能隨身：行動電源、備用電池、打火機（每人限一個）。
	- 隨身行李液體攜帶規定：容器每個須小於100ml、總共不超過1公升且可重複密封20*20的透明塑膠袋，每名旅客只能攜帶一袋上機。
</callout>
<columns>
	<column>
		## 換洗衣物(行李箱) {color="gray_bg"}
		- [ ] 上衣
		- [ ] 褲子
		- [ ] 洋裝
		- [ ] 襪子
		- [ ] 內衣
		- [ ] 內褲
		- [ ] 鞋子
		## 化妝包(行李箱) {color="gray_bg"}
		- [ ] 防曬
		- [ ] 粉餅
		- [ ] 睫毛夾、膏
		- [ ] 眼影
		- [ ] 眼線筆
		- [ ] 眉筆
		- [ ] 刷具
		- [ ] 蜜粉
		## 盥洗包(行李箱) {color="gray_bg"}
		- [ ] 牙刷牙膏
		- [ ] 卸妝、洗面乳
		- [ ] 隱形眼鏡
		- [ ] 衛生紙
		- [ ] 濕紙巾
		- [ ] 酒精
		- [ ] 保養品
	</column>
	<column>
		## 隨身包 {color="gray_bg"}
		- [ ] 護照
		- [ ] 錢包（身分證、健保卡）
		- [ ] 國際駕照
		- [ ] 行動電源
		- [ ] 衛生紙、濕紙巾
		- [ ] 耳機
		- [ ] 個人藥品
		- [ ] 眼罩
		- [ ] 充氣枕頭
		## 登機箱 {color="gray_bg"}
		- [ ] ��眼
		- [ ] 電池+充電器
		- [ ] 記憶卡
		- [ ] 隨身硬碟
		- [ ] 筆電
		- [ ] 行動電源
		- [ ] 手機+充電器
	</column>
</columns>
```

## Sub-page: 採購清單 (🛍️)

```markdown
<callout icon="💡" color="gray_bg">
	日本退稅：
	大部分為滿5000日圓(不含稅)可退稅
	一般商品不會指定包裝，可以馬上使用(包包、服飾、鞋子、雜貨、生活用品等...)
	消耗品會指定包裝，在日本境內不可開封(食品、飲料、藥妝等...)
	一般商品+消耗品一起退稅時會指定包裝(日本境內不可開封)
</callout>
```

Note: The tax-free callout is Japan-specific. Adapt for other destinations.

## Sub-page: 行程參考資料

Empty page for user to collect reference links, screenshots, bookmarks.

## Color Convention

- All section headers: `{color="green_bg"}`
- Callouts: `gray_bg` with 💡 icon
- Packing list headers: `{color="gray_bg"}`
