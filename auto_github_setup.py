#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动GitHub设置脚本
帮助用户完成GitHub仓库创建和代码推送
"""

import webbrowser
import time
import subprocess
import sys
from pathlib import Path

def open_github_create_repo():
    """打开GitHub创建仓库页面"""
    url = "https://github.com/new"
    print(f"🌐 正在打开GitHub创建仓库页面: {url}")
    webbrowser.open(url)
    return url

def check_git_status():
    """检查Git状态"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd='.')
        if result.returncode == 0 and not result.stdout.strip():
            print("✅ Git工作区干净，可以推送")
            return True
        else:
            print("⚠️  Git工作区有未提交的更改")
            return False
    except Exception as e:
        print(f"❌ 检查Git状态失败: {e}")
        return False

def check_remote_config():
    """检查远程仓库配置"""
    try:
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            print("🔗 远程仓库配置:")
            print(result.stdout)
            return True
        else:
            print("❌ 无法获取远程仓库配置")
            return False
    except Exception as e:
        print(f"❌ 检查远程仓库配置失败: {e}")
        return False

def get_project_stats():
    """获取项目统计信息"""
    try:
        # 文件数量
        files_result = subprocess.run(['find', '.', '-type', 'f'], 
                                    capture_output=True, text=True, cwd='.')
        file_count = len(files_result.stdout.strip().split('\n')) if files_result.stdout.strip() else 0
        
        # 游戏数量
        try:
            with open('data/games.json', 'r', encoding='utf-8') as f:
                import json
                games_data = json.load(f)
                game_count = len(games_data)
        except:
            game_count = 0
        
        # 缩略图数量
        images_result = subprocess.run(['find', 'assets/images', '-name', '*.jpg', '-o', '-name', '*.png', '-o', '-name', '*.webp'], 
                                     capture_output=True, text=True, cwd='.')
        image_count = len(images_result.stdout.strip().split('\n')) if images_result.stdout.strip() else 0
        
        return file_count, game_count, image_count
    except Exception as e:
        print(f"❌ 获取项目统计失败: {e}")
        return 0, 0, 0

def main():
    """主函数"""
    print("🎮 Game2项目GitHub自动设置")
    print("=" * 50)
    
    # 检查当前目录
    if not Path('index.html').exists():
        print("❌ 错误: 请在Game2目录中运行此脚本")
        return
    
    print("✅ 当前目录: Game2项目目录")
    
    # 检查Git状态
    if not check_git_status():
        print("⚠️  请先提交所有更改")
        return
    
    # 检查远程仓库配置
    check_remote_config()
    
    # 获取项目统计
    file_count, game_count, image_count = get_project_stats()
    print(f"\n📊 项目统计:")
    print(f"  - 文件数量: {file_count}")
    print(f"  - 游戏数量: {game_count}")
    print(f"  - 缩略图数量: {image_count}")
    
    print(f"\n📋 GitHub仓库创建步骤:")
    print("1. 🌐 访问 https://github.com/suwenge-game")
    print("2. 📝 创建新仓库:")
    print("   - Repository name: game2-website")
    print("   - Description: 🎮 Game2 游戏网站 - 166个精选游戏，响应式设计")
    print("   - 选择 Public 或 Private")
    print("   - 不要勾选任何初始化选项")
    print("3. 🚀 点击 'Create repository'")
    
    # 询问是否打开GitHub页面
    response = input("\n是否现在打开GitHub创建仓库页面? (y/n): ")
    if response.lower() in ['y', 'yes', '是']:
        open_github_create_repo()
        print("\n⏳ 请在浏览器中完成仓库创建...")
        
        # 等待用户创建仓库
        input("创建仓库完成后，按Enter键继续...")
        
        # 尝试推送代码
        print("\n🚀 尝试推送代码到GitHub...")
        try:
            result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], 
                                  capture_output=True, text=True, cwd='.')
            if result.returncode == 0:
                print("✅ 代码推送成功!")
                print("🌐 您的网站将在以下地址可见:")
                print("   https://suwenge-game.github.io/game2-website")
            else:
                print("❌ 代码推送失败:")
                print(result.stderr)
        except Exception as e:
            print(f"❌ 推送代码时出错: {e}")
    else:
        print("\n📝 请手动访问 https://github.com/new 创建仓库")
        print("创建完成后运行: git push -u origin main")

if __name__ == "__main__":
    main()
