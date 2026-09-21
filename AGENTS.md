# 專案說明（給 AI coding agent 看）

kc09393 的個人作品集網站。

## 基本資訊

- **正式網站**：https://kc09393.github.io/kc-portfolio/
- **後台管理**：目前未部署；`admin.html` 不存在，不要使用舊的 `/portfolio/admin.html` 網址
- **Repo**：`kc09393/portfolio`，branch `main`
- **本機路徑**：`D:\Projects\網站\portfolio`（已 clone 到本機，走一般 `git` 流程）

## 日常新增／編輯內容（作品、照片、證照、簡介）

目前走純靜態流程：在本機修改 `index.html` 與 `imgs/` 內的素材，確認預覽無誤後再使用一般 `git` 流程發布。`imgs/state.json` 與舊版 `admin.html` 後台流程不是目前前台的內容來源，不要重新接回舊後台。

## 修改網站程式碼（index.html / admin.html）

本機直接編輯檔案 → `git add` → `git commit` → `git push`。**改完程式碼直接 push，不用每次先問**——使用者已明確要求這樣，不用每次改完都停下來確認要不要推上線。但如果改動涉及會員資料隱私、大規模刪除等本質上高風險的操作，仍應該講清楚在做什麼。

⚠️ `index.html` 和 `admin.html` 各自有獨立的資料同步邏輯，改一邊要記得檢查另一邊是否有同樣的問題。

## 安全與授權原則

- 不要要求使用者把 admin.html 用的 PAT 貼到對話裡；引導他們自己貼到後台欄位，也不要把讀到的 token 值印出來。

## 使用者要求的規則

- 聊天回覆用繁體中文，除非使用者改用英文。
- 長時間自主工作，不要每 10-30 分鐘就停下回報。
- 使用者做這個網站（以及其他個人專案）的目標是吸引真實外部使用者，不只是自用/作品集展示——規劃新功能時也要考慮曝光/發現管道。

## 已知還沒處理的事

- **證照隱私（使用者尚未決定）**：Credentials 區塊有政府核發證照，身分證字號/生日等個資完整可見，是否裁切/馬賽克由使用者自行決定。
- **CDN 快取約 10 分鐘**：`state.json` 走 GitHub Pages CDN，更新後最多等到 10 分鐘才全域生效。
- **驗證是否真的更新時，不要只重整同一分頁**：舊分頁背景的自動同步可能把舊資料寫回去；改用全新分頁 + `?cb=`時間戳，或 `fetch(url,{cache:'no-store'})` 檢查。
- **GitHub Pages 偶爾卡 build error**：通常幾分鐘到十幾分鐘會自己好，一直不好可以用 no-op commit 觸發重試。

## 效能／SEO 優化紀錄（避免重複踩同一個坑）

- Studio／Lens／Credentials 三區塊曾經在 `index.html` 裡 hardcode 22 張 base64 內嵌圖片，但頁面一載入就會用 `state.json` 的資料整個覆蓋掉——使用者實際上從來看不到這些內嵌圖片，純粹是被下載又立刻丟棄。已刪除，`index.html` 從 4.2MB 降到約 110KB。改動前先確認新增的內嵌內容會不會有同樣的問題。
- About 區塊的大頭照是唯一真正會顯示的內嵌圖片，已抽成獨立檔案 `imgs/about-photo.jpg`。
- SEO / 社群分享 meta（`og:image`、`twitter:card`、canonical URL、favicon、JSON-LD Person schema）、`robots.txt`、`sitemap.xml` 都已補上。
