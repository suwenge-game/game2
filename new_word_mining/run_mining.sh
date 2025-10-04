#!/bin/bash

# 游戏行业新词挖掘系统 - 快速启动脚本
# 使用方法: ./run_mining.sh

echo "🎮 游戏行业新词挖掘系统启动"
echo "=================================="

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 检查脚本文件
if [ ! -f "new_word_mining_script.py" ]; then
    echo "❌ 错误: 未找到new_word_mining_script.py文件"
    exit 1
fi

# 创建结果目录
mkdir -p results
echo "📁 创建结果目录: results/"

# 运行挖掘脚本
echo "🔍 开始挖掘新词..."
python3 new_word_mining_script.py

# 检查运行结果
if [ $? -eq 0 ]; then
    echo "✅ 挖掘完成！"
    
    # 移动结果文件到results目录
    if [ -f "new_words_*.json" ]; then
        mv new_words_*.json results/ 2>/dev/null
        echo "📊 数据文件已保存到 results/"
    fi
    
    if [ -f "mining_report_*.md" ]; then
        mv mining_report_*.md results/ 2>/dev/null
        echo "📋 报告文件已保存到 results/"
    fi
    
    echo ""
    echo "🎯 下一步行动建议:"
    echo "1. 查看 results/ 目录中的挖掘结果"
    echo "2. 选择高潜力关键词开始应用"
    echo "3. 更新网站SEO策略"
    echo "4. 监控关键词效果"
    
else
    echo "❌ 挖掘过程中出现错误，请检查脚本和配置"
    exit 1
fi

echo ""
echo "📚 更多信息请查看:"
echo "- README.md - 系统说明"
echo "- 使用指南.md - 详细使用说明"
echo "- 游戏行业新词挖掘体系.md - 策略框架"
echo "- 新词挖掘执行计划.md - 执行计划"

