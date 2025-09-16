#!/bin/bash

# 🚀 GitHub连接和推送脚本

echo "🎮 Game2项目GitHub连接脚本"
echo "=================================="

# 检查是否在正确的目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误: 请在Game2目录中运行此脚本"
    exit 1
fi

echo "✅ 当前目录: $(pwd)"
echo "✅ Git状态:"
git status --short

echo ""
echo "📋 GitHub连接步骤："
echo ""
echo "1. 🌐 访问 https://github.com/suwenge-game"
echo "2. 📝 创建新仓库："
echo "   - Repository name: game2-website"
echo "   - Description: 🎮 Game2 游戏网站 - 166个精选游戏，响应式设计"
echo "   - 选择 Public 或 Private"
echo "   - 不要勾选任何初始化选项"
echo ""
echo "3. 🚀 创建仓库后，运行以下命令推送代码："
echo "   git push -u origin main"
echo ""

# 检查远程仓库配置
echo "🔗 当前远程仓库配置:"
git remote -v

echo ""
echo "📊 项目统计:"
echo "  - 文件数量: $(find . -type f | wc -l)"
echo "  - 游戏数量: $(grep -c '"id"' data/games.json)"
echo "  - 缩略图数量: $(find assets/images -name "*.jpg" -o -name "*.png" -o -name "*.webp" | wc -l)"
echo "  - 代码行数: $(find . -name "*.html" -o -name "*.css" -o -name "*.js" | xargs wc -l | tail -1)"

echo ""
echo "🎯 提交历史:"
git log --oneline -5

echo ""
echo "🎉 准备就绪！创建GitHub仓库后即可推送代码！"
echo "🌐 启用GitHub Pages后，可访问: https://suwenge-game.github.io/game2-website"
