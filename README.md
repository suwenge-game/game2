# 🎮 Game2 游戏网站

一个遵循 Google SEO 最佳实践的响应式网页游戏平台，包含166个精选游戏。

## ✨ 功能特色

- **166个精选游戏**：包括动作、射击、竞速、解谜、模拟、运动等各类游戏
- **响应式设计**：完美适配桌面、平板、手机
- **幻灯片播放**：英雄区域自动播放和手动控制
- **智能搜索**：即时搜索和分类筛选
- **100%缩略图覆盖**：所有游戏都有高质量缩略图
- **SEO优化**：遵循 Google 官方 SEO 建议

## 📊 项目统计

- **总文件数**: 722个
- **游戏数量**: 166个
- **缩略图数量**: 197个
- **代码行数**: 2,785行

## 📁 项目结构

```
Game2/
├── index.html              # 主页面
├── 404.html               # 404错误页面
├── robots.txt             # 搜索引擎爬虫规则
├── sitemap.xml            # 网站地图
├── assets/                # 静态资源
│   ├── css/
│   │   └── style.css      # 样式文件
│   ├── js/
│   │   └── script.js      # JavaScript逻辑
│   └── images/            # 游戏缩略图 (197个)
├── data/
│   └── games.json         # 游戏数据 (166个游戏)
├── game-data-collection/  # 数据收集工具
│   ├── data/              # 原始游戏数据
│   ├── docs/              # 文档
│   ├── scripts/           # 采集脚本
│   └── thumbnails/        # 缩略图资源 (156个)
└── pages/                 # 未来扩展页面
```

## 🎯 游戏分类

### 动作游戏 (27个)
- Bloxd io、Masked Special Forces、GTA Simulator等

### 射击游戏 (90个)
- Fragen、DTA 6、FPS Simulator、Crazy Strike Force等

### 竞速游戏 (39个)
- 各种驾驶、漂移、赛车游戏

### 解谜游戏 (8个)
- 益智类、解谜类游戏

### 模拟游戏 (1个)
- 模拟器类游戏

### 运动游戏 (1个)
- 体育类游戏

## 🚀 技术特性

### 前端技术
- **HTML5**：语义化标记
- **CSS3**：现代样式和动画
- **JavaScript ES6+**：模块化代码
- **响应式设计**：移动优先设计理念

### 功能特性
- **幻灯片播放**：自动播放和手动控制
- **游戏搜索**：实时搜索功能
- **分类筛选**：按游戏类型筛选
- **懒加载**：优化页面加载速度

## 🔧 本地开发

### 启动服务器
```bash
# Python 3
python3 -m http.server 8080

# 访问网站
# http://localhost:8080
```

### 项目脚本
```bash
# 运行GitHub连接脚本
./connect_github.sh

# 运行自动化设置脚本
python3 auto_github_setup.py
```

## 🌐 部署选项

### GitHub Pages
- 仓库地址: https://github.com/suwenge-game/game2
- 访问地址: https://suwenge-game.github.io/game2

### 其他平台
- **Netlify**: 连接GitHub仓库自动部署
- **Vercel**: 连接GitHub仓库自动部署
- **Firebase Hosting**: 使用Firebase CLI部署

## 📈 SEO优化

### 结构化数据
- **JSON-LD格式**：网站和游戏集合的结构化标记
- **Schema.org标准**：符合Google推荐的数据格式

### 技术SEO
- **XML Sitemap**：完整的网站地图
- **Robots.txt**：搜索引擎爬虫指导
- **Meta标签优化**：标题、描述、Open Graph等

## 🔄 更新维护

### 添加新游戏
1. 在 `data/games.json` 中添加游戏数据
2. 将缩略图放入 `assets/images/` 目录
3. 更新 `sitemap.xml` 中的URL

### 数据管理
- 使用 `game-data-collection/` 中的脚本管理游戏数据
- 定期更新缩略图和游戏信息
- 监控游戏链接的有效性

## 📄 许可证

MIT License - 可自由使用和修改

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进项目！

---

**Game2 游戏网站** - 让游戏更简单，让快乐更纯粹！🎮
