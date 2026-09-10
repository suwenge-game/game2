# 射击类游戏采集总结报告

## 采集概述
- **采集时间**: 2025年1月13日
- **采集来源**: https://www.onlinegames.io/t/shooting/
- **采集总数**: 90款射击类游戏
- **数据格式**: JSON（每批10款游戏）
- **采集方式**: 浏览器自动化采集

## 文件结构
```
/Users/Shared/game2025/game-website-template-v2/
├── games-batch-1.json    # 第1批：10款游戏
├── games-batch-2.json    # 第2批：10款游戏
├── games-batch-3.json    # 第3批：10款游戏
├── games-batch-4.json    # 第4批：10款游戏
├── games-batch-5.json    # 第5批：10款游戏
├── games-batch-6.json    # 第6批：10款游戏
├── games-batch-7.json    # 第7批：10款游戏
├── games-batch-8.json    # 第8批：10款游戏
├── games-batch-9.json    # 第9批：10款游戏
└── GAMES_COLLECTION_SUMMARY.md  # 本总结文件
```

## 数据字段说明
每个游戏记录包含以下字段：
- **game_name**: 游戏名称
- **game_link**: 游戏链接
- **game_description**: 游戏描述（中文）
- **game_category**: 游戏分类（统一为"射击游戏"）

## 游戏分类统计
- **射击游戏**: 90款
- **io游戏**: 约15款
- **模拟器游戏**: 约10款
- **大逃杀游戏**: 约8款
- **狙击游戏**: 约12款
- **僵尸游戏**: 约8款
- **特警/军事游戏**: 约15款
- **其他射击游戏**: 约22款

## 热门游戏类型
1. **第一人称射击(FPS)**: Masked Special Forces, ArmedForces.io, FPS Simulator
2. **第三人称射击(TPS)**: Mini Shooters, Squad Shooter
3. **io射击游戏**: Bloxd io, Shell Shockers.io, Deadshot io
4. **狙击游戏**: Legendary Sniper, Urban Sniper, Sniper Elite
5. **大逃杀游戏**: Fortnite Z, Su Battle Royale, Battle Royale Simulator
6. **僵尸射击**: Zombie Apocalypse Shooter, FNaF Shooter, Zombie Sniper
7. **军事射击**: Army Combat, Tank War Simulator, ArmedForces.io

## 技术特点
- **多人在线**: 大部分游戏支持多人在线对战
- **无需下载**: 所有游戏均可在线直接游玩
- **跨平台**: 支持PC、手机、平板等设备
- **实时对战**: 支持实时多人对战功能

## 使用建议
1. **数据导入**: 可以将JSON文件导入到数据库或表格中
2. **网站集成**: 可以用于游戏网站的游戏列表展示
3. **数据分析**: 可以分析射击游戏的流行趋势
4. **内容管理**: 可以用于游戏内容管理系统

## 后续扩展
- 可以继续采集其他分类的游戏
- 可以添加游戏评分、玩家数量等更多信息
- 可以定期更新游戏数据
- 可以添加游戏缩略图信息

## 注意事项
- 所有游戏链接均为在线游戏，无需下载
- 游戏描述为中文，便于中文用户理解
- 数据采集时间为2025年1月13日，游戏信息可能随时间变化
- 建议定期更新游戏数据以保持信息的准确性

---
*采集完成时间: 2025年1月13日*
*总游戏数量: 90款射击类游戏*
*数据格式: JSON (9个批次文件)*
