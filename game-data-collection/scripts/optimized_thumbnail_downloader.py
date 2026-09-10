#!/usr/bin/env python3
"""
优化版缩略图下载脚本
通过分析HTML页面直接提取真实的图片URL
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

def extract_image_urls_from_page(game_url):
    """从游戏页面提取所有图片URL"""
    try:
        print(f"正在分析 {game_url} 的图片URL...")
        response = requests.get(game_url, timeout=10)
        if response.status_code == 200:
            # 查找所有图片URL模式
            img_patterns = [
                r'https://www\.onlinegames\.io/media/posts/(\d+)/([^"\s]+\.(?:jpg|jpeg|png|webp))',
                r'https://www\.onlinegames\.io/media/posts/(\d+)/responsive/([^"\s]+\.(?:jpg|jpeg|png|webp))'
            ]
            
            image_urls = []
            for pattern in img_patterns:
                matches = re.findall(pattern, response.text, re.IGNORECASE)
                for match in matches:
                    post_id, filename = match
                    if 'responsive' in pattern:
                        url = f"https://www.onlinegames.io/media/posts/{post_id}/responsive/{filename}"
                    else:
                        url = f"https://www.onlinegames.io/media/posts/{post_id}/{filename}"
                    image_urls.append(url)
            
            # 去重并排序（优先选择非响应式图片）
            unique_urls = []
            seen = set()
            for url in image_urls:
                if url not in seen:
                    seen.add(url)
                    unique_urls.append(url)
            
            # 优先选择非响应式图片
            non_responsive = [url for url in unique_urls if '/responsive/' not in url]
            responsive = [url for url in unique_urls if '/responsive/' in url]
            
            final_urls = non_responsive + responsive
            
            print(f"找到 {len(final_urls)} 个图片URL")
            return final_urls
        else:
            print(f"无法访问页面: {response.status_code}")
            return []
    except Exception as e:
        print(f"分析页面时出错: {e}")
        return []

def download_thumbnail_optimized(game_name, game_url, output_dir):
    """优化版缩略图下载"""
    cleaned_game_name = clean_filename(game_name)
    
    # 从页面提取图片URL
    image_urls = extract_image_urls_from_page(game_url)
    
    if not image_urls:
        print(f"❌ 无法找到 {game_name} 的图片URL")
        return False
    
    # 尝试下载每个图片URL
    for i, image_url in enumerate(image_urls):
        try:
            print(f"尝试下载 ({i+1}/{len(image_urls)}): {image_url}")
            response = requests.get(image_url, stream=True, timeout=10)
            
            if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
                # 确定文件扩展名
                file_extension = image_url.split('.')[-1].lower()
                if file_extension not in ['jpg', 'jpeg', 'png', 'webp']:
                    file_extension = 'jpg'  # 默认
                
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
    
    print(f"❌ 无法下载 {game_name} 的缩略图")
    return False

def test_optimized_download():
    """测试优化版下载"""
    test_games = [
        {
            "game_name": "Racing Horizon",
            "game_link": "https://www.onlinegames.io/racing-horizon/"
        },
        {
            "game_name": "Drift Fury", 
            "game_link": "https://www.onlinegames.io/drift-fury/"
        },
        {
            "game_name": "Car Stunt King",
            "game_link": "https://www.onlinegames.io/car-stunt-king/"
        }
    ]
    
    output_dir = os.path.join(os.getcwd(), "game-thumbnails")
    os.makedirs(output_dir, exist_ok=True)
    
    print("测试优化版下载...")
    for game in test_games:
        print(f"\n=== 测试 {game['game_name']} ===")
        download_thumbnail_optimized(game["game_name"], game["game_link"], output_dir)
        time.sleep(2)  # 避免请求过快

def process_game_files_optimized():
    """优化版批量处理"""
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
                        print(f"\n--- 处理 {game_name} ---")
                        if download_thumbnail_optimized(game_name, game_link, output_dir):
                            successful_downloads += 1
                        else:
                            failed_downloads += 1
                        
                        # 添加延迟避免请求过快
                        time.sleep(2)
                        
        except Exception as e:
            print(f"处理文件 {json_file} 时发生错误: {e}")
    
    # 输出统计信息
    print(f"\n=== 下载完成 ===")
    print(f"总游戏数: {total_games}")
    print(f"成功下载: {successful_downloads}")
    print(f"下载失败: {failed_downloads}")
    print(f"成功率: {(successful_downloads/total_games*100):.1f}%" if total_games > 0 else "0%")

def main():
    """主函数"""
    print("优化版缩略图下载工具")
    print("=" * 50)
    
    # 检查是否有命令行参数
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_optimized_download()
    else:
        process_game_files_optimized()

if __name__ == "__main__":
    main()
