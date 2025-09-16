#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
遊戲縮略圖下載腳本
從 1.json 文件中讀取圖片 URL，下載到本地 images 文件夾
"""

import json
import os
import requests
from urllib.parse import urlparse
import time

def create_images_folder():
    """創建 images 文件夾"""
    if not os.path.exists('images'):
        os.makedirs('images')
        print("✅ 創建 images 文件夾")

def download_image(url, filename):
    """下載單個圖片"""
    try:
        print(f"📥 正在下載: {filename}")
        
        # 設置請求頭，模擬瀏覽器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.onlinegames.io/',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 保存圖片
        filepath = os.path.join('images', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ 下載成功: {filename} ({len(response.content)} bytes)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 下載失敗: {filename} - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 下載錯誤: {filename} - {str(e)}")
        return False

def get_filename_from_url(url, game_name):
    """從 URL 生成文件名"""
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # 獲取文件擴展名
    if '.' in path:
        ext = os.path.splitext(path)[1]
    else:
        ext = '.webp'  # 默認擴展名
    
    # 清理遊戲名稱作為文件名
    safe_name = "".join(c for c in game_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_name = safe_name.replace(' ', '_')
    
    return f"{safe_name}{ext}"

def main():
    """主函數"""
    print("🎮 開始下載遊戲縮略圖...")
    
    # 創建 images 文件夾
    create_images_folder()
    
    # 讀取 1.json 文件
    try:
        with open('1.json', 'r', encoding='utf-8') as f:
            games_data = json.load(f)
        print(f"📖 讀取到 {len(games_data)} 個遊戲")
    except FileNotFoundError:
        print("❌ 找不到 1.json 文件")
        return
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析錯誤: {e}")
        return
    
    # 下載統計
    success_count = 0
    failed_count = 0
    
    # 下載每個遊戲的縮略圖
    for i, game in enumerate(games_data, 1):
        game_name = game.get('game_name', f'game_{i}')
        thumbnail_url = game.get('thumbnail_url', '')
        
        if not thumbnail_url:
            print(f"⚠️  跳過 {game_name}: 沒有縮略圖 URL")
            continue
        
        # 生成文件名
        filename = get_filename_from_url(thumbnail_url, game_name)
        
        # 檢查文件是否已存在
        filepath = os.path.join('images', filename)
        if os.path.exists(filepath):
            print(f"⏭️  跳過 {filename}: 文件已存在")
            success_count += 1
            continue
        
        # 下載圖片
        if download_image(thumbnail_url, filename):
            success_count += 1
        else:
            failed_count += 1
        
        # 添加延遲避免請求過於頻繁
        time.sleep(1)
    
    # 輸出結果
    print("\n" + "="*50)
    print("📊 下載完成統計:")
    print(f"✅ 成功: {success_count} 個")
    print(f"❌ 失敗: {failed_count} 個")
    print(f"📁 圖片保存在: images/ 文件夾")
    
    if success_count > 0:
        print("\n🎉 部分或全部圖片下載成功！")
        print("💡 現在可以更新 JSON 文件使用本地圖片路徑")

if __name__ == "__main__":
    main()
