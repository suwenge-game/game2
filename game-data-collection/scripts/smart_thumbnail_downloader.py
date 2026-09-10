#!/usr/bin/env python3
"""
智能缩略图下载脚本
基于网站结构分析，智能下载游戏缩略图
"""

import json
import os
import re
import requests
import time
from urllib.parse import urlparse

def clean_filename(filename):
    """清理文件名，移除特殊字符"""
    cleaned_filename = re.sub(r'[^\w\s.-]', '', filename)
    return cleaned_filename.replace(' ', '_')

def extract_game_slug_from_url(game_url):
    """从游戏URL提取slug"""
    game_url = game_url.rstrip('/')
    slug = game_url.split('/')[-1]
    return slug

def get_post_id_from_game_page(game_url):
    """从游戏页面获取post_id"""
    try:
        print(f"正在获取 {game_url} 的post_id...")
        response = requests.get(game_url, timeout=10)
        if response.status_code == 200:
            # 查找图片URL模式
            img_pattern = r'https://www\.onlinegames\.io/media/posts/(\d+)/'
            matches = re.findall(img_pattern, response.text)
            if matches:
                post_id = matches[0]  # 取第一个匹配的post_id
                print(f"找到post_id: {post_id}")
                return post_id
        print(f"无法获取post_id")
        return None
    except Exception as e:
        print(f"获取post_id时出错: {e}")
        return None

def download_thumbnail(game_name, game_url, output_dir):
    """下载游戏缩略图"""
    cleaned_game_name = clean_filename(game_name)
    game_slug = extract_game_slug_from_url(game_url)
    
    # 获取post_id
    post_id = get_post_id_from_game_page(game_url)
    if not post_id:
        print(f"❌ 无法获取 {game_name} 的post_id")
        return False
    
    # 构建可能的图片URL
    base_url = f"https://www.onlinegames.io/media/posts/{post_id}"
    
    # 尝试不同的文件名模式
    filename_patterns = [
        f"{game_slug}-game.webp",
        f"{game_slug}-game.jpg", 
        f"{game_slug}.webp",
        f"{game_slug}.jpg",
        f"{game_slug}-online.webp",
        f"{game_slug}-online.jpg",
        f"{game_slug}-play.webp",
        f"{game_slug}-play.jpg"
    ]
    
    # 尝试响应式图片
    responsive_patterns = [
        f"responsive/{game_slug}-game-sm.webp",
        f"responsive/{game_slug}-game-md.webp",
        f"responsive/{game_slug}-game-lg.webp",
        f"responsive/{game_slug}-game-xs.webp"
    ]
    
    all_patterns = filename_patterns + responsive_patterns
    
    for pattern in all_patterns:
        image_url = f"{base_url}/{pattern}"
        try:
            print(f"尝试下载: {image_url}")
            response = requests.get(image_url, stream=True, timeout=10)
            if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
                # 确定文件扩展名
                if '.webp' in pattern:
                    file_extension = 'webp'
                elif '.jpg' in pattern:
                    file_extension = 'jpg'
                else:
                    file_extension = 'webp'  # 默认
                
                output_filename = f"{cleaned_game_name}.{file_extension}"
                output_path = os.path.join(output_dir, output_filename)
                
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"✅ 成功下载 {game_name} 的缩略图到 {output_path}")
                return True
            else:
                print(f"❌ 无效响应 ({response.status_code}): {image_url}")
        except requests.exceptions.RequestException as e:
            print(f"❌ 请求错误: {image_url} - {str(e)}")
    
    print(f"❌ 无法找到 {game_name} 的缩略图")
    return False

def process_game_files():
    """处理所有游戏文件"""
    base_dir = os.getcwd()
    output_dir = os.path.join(base_dir, "game-thumbnails")
    os.makedirs(output_dir, exist_ok=True)
    
    # 查找所有JSON文件
    json_files = []
    
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
    
    # 统计信息
    total_games = 0
    successful_downloads = 0
    failed_downloads = 0
    
    # 处理每个文件
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                games = json.load(f)
                print(f"\n处理文件: {json_file} ({len(games)} 个游戏)")
                
                for game in games:
                    game_name = game.get("game_name")
                    game_link = game.get("game_link")
                    
                    if game_name and game_link:
                        total_games += 1
                        if download_thumbnail(game_name, game_link, output_dir):
                            successful_downloads += 1
                        else:
                            failed_downloads += 1
                        
                        # 添加延迟避免请求过快
                        time.sleep(1)
                        
        except Exception as e:
            print(f"处理文件 {json_file} 时发生错误: {e}")
    
    # 输出统计信息
    print(f"\n=== 下载完成 ===")
    print(f"总游戏数: {total_games}")
    print(f"成功下载: {successful_downloads}")
    print(f"下载失败: {failed_downloads}")
    print(f"成功率: {(successful_downloads/total_games*100):.1f}%" if total_games > 0 else "0%")

def test_single_game():
    """测试单个游戏的下载"""
    test_game = {
        "game_name": "Italian Brainrot Survive Parkour",
        "game_link": "https://www.onlinegames.io/italian-brainrot-survive-parkour/"
    }
    
    output_dir = os.path.join(os.getcwd(), "game-thumbnails")
    os.makedirs(output_dir, exist_ok=True)
    
    print("测试单个游戏下载...")
    download_thumbnail(test_game["game_name"], test_game["game_link"], output_dir)

def main():
    """主函数"""
    print("智能缩略图下载工具")
    print("=" * 50)
    
    # 检查是否有命令行参数
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_single_game()
    else:
        process_game_files()

if __name__ == "__main__":
    main()
