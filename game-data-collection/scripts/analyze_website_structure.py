#!/usr/bin/env python3
"""
网站结构分析脚本
分析OnlineGames.io网站的图片URL模式
"""

import json
import os
import re
import requests
from urllib.parse import urlparse

def analyze_url_patterns():
    """分析URL模式"""
    print("=== 网站结构分析 ===")
    
    # 基于用户提供的HTML元素分析
    example_html = '''
    <figure class="c-card__image is-loaded" style="position: relative;">
        <img src="https://www.onlinegames.io/media/posts/885/obby-but-your-on-a-bike.jpg" 
             srcset="https://www.onlinegames.io/media/posts/885/responsive/obby-but-your-on-a-bike-xs.jpg 384w, 
                     https://www.onlinegames.io/media/posts/885/responsive/obby-but-your-on-a-bike-sm.jpg 600w" 
             sizes="(min-width: 600px) 14.285vw, 100vw" 
             loading="lazy" height="512" width="512" 
             alt="Obby But You're on A Bike Play Free Online Game" class="is-loaded">
    </figure>
    '''
    
    print("1. 图片URL模式分析:")
    print("   - 基础URL: https://www.onlinegames.io/media/posts/{post_id}/{filename}")
    print("   - 响应式URL: https://www.onlinegames.io/media/posts/{post_id}/responsive/{filename}")
    print("   - 示例: https://www.onlinegames.io/media/posts/885/obby-but-your-on-a-bike.jpg")
    print("   - 响应式示例: https://www.onlinegames.io/media/posts/885/responsive/obby-but-your-on-a-bike-xs.jpg")
    
    print("\n2. 关键发现:")
    print("   - post_id: 885 (从URL中提取)")
    print("   - filename: obby-but-your-on-a-bike.jpg (基于游戏slug)")
    print("   - 游戏slug: obby-but-your-on-a-bike (从游戏链接提取)")
    
    print("\n3. URL构建策略:")
    print("   - 从游戏链接提取slug: /obby-but-you-re-on-a-bike/ -> obby-but-you-re-on-a-bike")
    print("   - 需要找到post_id (可能是动态的)")
    print("   - 构建图片URL: /media/posts/{post_id}/{slug}.jpg")

def extract_game_slug_from_url(game_url):
    """从游戏URL提取slug"""
    # 移除末尾的斜杠
    game_url = game_url.rstrip('/')
    # 提取最后一部分作为slug
    slug = game_url.split('/')[-1]
    return slug

def test_image_url_patterns():
    """测试不同的图片URL模式"""
    print("\n=== 测试图片URL模式 ===")
    
    # 测试已知的游戏
    test_games = [
        {
            "name": "Obby But You're on a Bike",
            "url": "https://www.onlinegames.io/obby-but-you-re-on-a-bike/",
            "known_post_id": "885"
        }
    ]
    
    for game in test_games:
        slug = extract_game_slug_from_url(game["url"])
        post_id = game["known_post_id"]
        
        print(f"\n测试游戏: {game['name']}")
        print(f"Slug: {slug}")
        print(f"Post ID: {post_id}")
        
        # 测试不同的URL模式
        url_patterns = [
            f"https://www.onlinegames.io/media/posts/{post_id}/{slug}.jpg",
            f"https://www.onlinegames.io/media/posts/{post_id}/{slug}-game.jpg",
            f"https://www.onlinegames.io/media/posts/{post_id}/{slug}-online.jpg",
            f"https://www.onlinegames.io/media/posts/{post_id}/{slug}-play.jpg",
            f"https://www.onlinegames.io/media/posts/{post_id}/{slug}.webp",
            f"https://www.onlinegames.io/media/posts/{post_id}/responsive/{slug}-xs.jpg",
            f"https://www.onlinegames.io/media/posts/{post_id}/responsive/{slug}-sm.jpg"
        ]
        
        for url in url_patterns:
            try:
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    print(f"✅ 有效: {url}")
                else:
                    print(f"❌ 无效 ({response.status_code}): {url}")
            except Exception as e:
                print(f"❌ 错误: {url} - {str(e)}")

def analyze_collected_games():
    """分析已收集的游戏数据"""
    print("\n=== 分析已收集的游戏数据 ===")
    
    # 查找所有JSON文件
    json_files = []
    base_dir = os.getcwd()
    
    # 根目录的JSON文件
    for file in os.listdir(base_dir):
        if file.startswith("games-batch-") and file.endswith(".json"):
            json_files.append(os.path.join(base_dir, file))
    
    # 分类目录的JSON文件
    for category_dir in ["action-games", "racing-games", "puzzle-games", "sports-games", "simulator-games"]:
        full_category_dir = os.path.join(base_dir, category_dir)
        if os.path.exists(full_category_dir):
            for file in os.listdir(full_category_dir):
                if file.endswith(".json"):
                    json_files.append(os.path.join(full_category_dir, file))
    
    print(f"找到 {len(json_files)} 个JSON文件")
    
    # 分析游戏数据
    all_games = []
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                games = json.load(f)
                all_games.extend(games)
        except Exception as e:
            print(f"读取文件 {json_file} 时出错: {e}")
    
    print(f"总共收集了 {len(all_games)} 个游戏")
    
    # 分析URL模式
    url_patterns = {}
    for game in all_games:
        game_url = game.get("game_link", "")
        if game_url:
            slug = extract_game_slug_from_url(game_url)
            if slug not in url_patterns:
                url_patterns[slug] = []
            url_patterns[slug].append(game)
    
    print(f"发现 {len(url_patterns)} 个唯一的游戏slug")
    
    # 显示前10个示例
    print("\n前10个游戏slug示例:")
    for i, (slug, games) in enumerate(list(url_patterns.items())[:10]):
        print(f"{i+1}. {slug} ({len(games)} 个游戏)")

def main():
    """主函数"""
    print("OnlineGames.io 网站结构分析工具")
    print("=" * 50)
    
    analyze_url_patterns()
    test_image_url_patterns()
    analyze_collected_games()
    
    print("\n=== 分析完成 ===")
    print("基于分析结果，可以创建更智能的缩略图下载脚本")

if __name__ == "__main__":
    main()
