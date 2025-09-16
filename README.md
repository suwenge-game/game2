# GameHub 遊戲站

一個遵循 Google SEO 最佳實踐的響應式網頁遊戲平台。

## 🎮 功能特色

- **10+ 款精選射擊遊戲**：包括 Bloxd io、GTA Simulator、FPS Simulator 等
- **響應式設計**：完美適配桌面、平板、手機
- **即點即玩**：使用 iframe 嵌入，無需跳轉
- **智能搜索**：即時搜索和分類篩選
- **SEO 優化**：遵循 Google 官方 SEO 建議

## 📁 項目結構

```
GameHub/
├── index.html              # 主頁面
├── 404.html               # 404 錯誤頁面
├── robots.txt             # 搜索引擎爬蟲規則
├── sitemap.xml            # 網站地圖
├── .htaccess              # Apache 服務器配置
├── assets/                # 靜態資源
│   ├── css/
│   │   └── style.css      # 樣式文件
│   ├── js/
│   │   └── script.js      # JavaScript 邏輯
│   └── images/            # 遊戲縮略圖
├── data/
│   └── games.json         # 遊戲數據
└── pages/                 # 未來擴展頁面
```

## 🚀 SEO 優化特性

### 1. 結構化數據
- **JSON-LD 格式**：網站和遊戲集合的結構化標記
- **Schema.org 標準**：符合 Google 推薦的數據格式
- **豐富摘要**：提升搜索結果展示效果

### 2. Meta 標籤優化
- **標題標籤**：包含關鍵詞和品牌名稱
- **描述標籤**：吸引點擊的詳細描述
- **Open Graph**：社交媒體分享優化
- **Twitter Cards**：Twitter 分享優化

### 3. 技術 SEO
- **XML Sitemap**：完整的網站地圖
- **Robots.txt**：搜索引擎爬蟲指導
- **.htaccess 配置**：URL 重寫、緩存、安全頭
- **404 錯誤頁面**：用戶友好的錯誤處理

### 4. 性能優化
- **圖片壓縮**：本地生成的優化縮略圖
- **CSS/JS 壓縮**：減少文件大小
- **緩存策略**：合理的資源緩存設置
- **響應式設計**：移動優先的設計理念

## 🛠️ 技術棧

- **HTML5**：語義化標記
- **CSS3**：現代樣式和動畫
- **JavaScript ES6+**：模塊化代碼
- **JSON**：結構化數據存儲
- **Python**：輔助腳本（圖片生成、數據處理）

## 📱 響應式設計

- **桌面端**：1200px+ 寬屏優化
- **平板端**：768px-1199px 適配
- **手機端**：320px-767px 移動優化
- **觸控友好**：大按鈕和手勢支持

## 🎯 遊戲特色

### 射擊遊戲類別
1. **Bloxd io** - 多人射擊 io 遊戲
2. **Masked Special Forces** - 第一人稱射擊
3. **GTA Simulator** - GTA 風格模擬器
4. **Fragen** - 射擊類問答遊戲
5. **DTA 6** - DTA 系列第 6 代
6. **Stickman GTA City** - 火柴人 GTA
7. **FPS Simulator** - 第一人稱射擊模擬器
8. **Crazy Strike Force** - 多人射擊
9. **Shell Shockers.io** - 雞蛋殼射擊
10. **Deadshot io** - 神槍手射擊

## 🔧 本地開發

### 啟動服務器
```bash
# Python 3
python -m http.server 8000

# 或使用 Node.js
npx http-server -p 8000
```

### 訪問網站
打開瀏覽器訪問：`http://localhost:8000`

## 📊 SEO 監控

### Google Search Console
- 提交 sitemap.xml
- 監控搜索表現
- 檢查結構化數據

### 性能監控
- Core Web Vitals
- 頁面加載速度
- 移動友好性

## 🔄 更新維護

### 添加新遊戲
1. 在 `data/games.json` 中添加遊戲數據
2. 將縮略圖放入 `assets/images/` 目錄
3. 更新 `sitemap.xml` 中的 URL

### SEO 優化
- 定期更新 sitemap.xml
- 監控 Google Search Console
- 優化 Core Web Vitals

## 📄 許可證

MIT License - 可自由使用和修改

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request 來改進項目！

---

**GameHub 遊戲站** - 讓遊戲更簡單，讓快樂更純粹！🎮
