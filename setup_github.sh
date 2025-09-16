#!/bin/bash

# 🚀 Game2 GitHub 仓库设置脚本

echo "🎮 Game2 GitHub 仓库设置脚本"
echo "=================================="

# 检查是否在正确的目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误: 请在Game2目录中运行此脚本"
    exit 1
fi

echo "✅ 当前目录: $(pwd)"
echo "✅ Git仓库状态:"
git status --short

echo ""
echo "📋 请按照以下步骤操作："
echo ""
echo "1. 🌐 访问 https://github.com/new"
echo "2. 📝 创建新仓库："
echo "   - Repository name: game2-website"
echo "   - Description: 🎮 Game2 游戏网站 - 166个精选游戏，响应式设计"
echo "   - 选择 Public 或 Private"
echo "   - 不要勾选任何初始化选项"
echo ""
echo "3. 📋 复制仓库URL（类似: https://github.com/CNJock/game2-website.git）"
echo ""
echo "4. 🔗 运行以下命令添加远程仓库："
echo "   git remote add origin <您的仓库URL>"
echo ""
echo "5. 🚀 推送到GitHub："
echo "   git push -u origin main"
echo ""

# 检查是否已有远程仓库
if git remote -v | grep -q "origin"; then
    echo "✅ 远程仓库已配置:"
    git remote -v
    echo ""
    echo "🚀 直接推送代码："
    echo "git push -u origin main"
else
    echo "⚠️  尚未配置远程仓库"
    echo "请先按照上述步骤创建GitHub仓库并添加远程地址"
fi

echo ""
echo "📊 项目统计:"
echo "  - 文件数量: $(find . -type f | wc -l)"
echo "  - 游戏数量: $(grep -c '"id"' data/games.json)"
echo "  - 缩略图数量: $(find assets/images -name "*.jpg" -o -name "*.png" -o -name "*.webp" | wc -l)"
echo "  - 代码行数: $(find . -name "*.html" -o -name "*.css" -o -name "*.js" | xargs wc -l | tail -1)"

echo ""
echo "🎉 设置完成后，您的游戏网站将在GitHub上可见！"
