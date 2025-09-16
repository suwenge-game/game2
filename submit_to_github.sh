#!/bin/bash

# 🚀 Game2项目GitHub提交脚本

echo "🎮 Game2项目GitHub提交脚本"
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
echo "📋 请按照以下步骤操作："
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
if git remote -v | grep -q "suwenge-game"; then
    echo "✅ 远程仓库已配置:"
    git remote -v
    echo ""
    echo "🚀 如果GitHub仓库已创建，直接运行："
    echo "git push -u origin main"
else
    echo "⚠️  远程仓库配置:"
    git remote -v
    echo ""
    echo "🔗 如果远程仓库配置不正确，运行："
    echo "git remote remove origin"
    echo "git remote add origin https://github.com/suwenge-game/game2-website.git"
fi

echo ""
echo "📊 项目统计:"
echo "  - 文件数量: $(find . -type f | wc -l)"
echo "  - 游戏数量: $(grep -c '"id"' data/games.json)"
echo "  - 缩略图数量: $(find assets/images -name "*.jpg" -o -name "*.png" -o -name "*.webp" | wc -l)"
echo "  - 代码行数: $(find . -name "*.html" -o -name "*.css" -o -name "*.js" | xargs wc -l | tail -1)"

echo ""
echo "🎉 提交完成后，您的游戏网站将在GitHub上可见！"
echo "🌐 启用GitHub Pages后，可访问: https://suwenge-game.github.io/game2-website"
