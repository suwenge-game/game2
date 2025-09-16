#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
創建本地遊戲縮略圖腳本
使用 PIL 創建美觀的遊戲縮略圖
"""

import json
import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_images_folder():
    """創建 images 文件夾"""
    if not os.path.exists('images'):
        os.makedirs('images')
        print("✅ 創建 images 文件夾")

def create_game_thumbnail(game_name, game_id):
    """創建遊戲縮略圖"""
    # 圖片尺寸
    width, height = 300, 200
    
    # 隨機選擇背景顏色
    colors = [
        ('#FF6B6B', '#FF8E8E'),  # 紅色系
        ('#4ECDC4', '#7EDDD6'),  # 青色系
        ('#45B7D1', '#6BC5D8'),  # 藍色系
        ('#96CEB4', '#A8D5BA'),  # 綠色系
        ('#FFEAA7', '#FFF0C7'),  # 黃色系
        ('#DDA0DD', '#E6B3E6'),  # 紫色系
        ('#98D8C8', '#A8E0D0'),  # 薄荷綠
        ('#F7DC6F', '#F9E79F'),  # 金黃色
        ('#82E0AA', '#9AE6C1'),  # 淺綠色
        ('#E17055', '#E88A73'),  # 橙色系
    ]
    
    # 根據遊戲 ID 選擇顏色
    color_pair = colors[game_id % len(colors)]
    bg_color = color_pair[0]
    accent_color = color_pair[1]
    
    # 創建圖片
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 添加漸變效果（簡單的圓形漸變）
    for i in range(50):
        alpha = int(255 * (1 - i / 50))
        color = tuple(int(bg_color[j:j+2], 16) for j in (1, 3, 5))
        draw.ellipse([width//2-i*3, height//2-i*2, width//2+i*3, height//2+i*2], 
                    fill=(*color, alpha) if len(color) == 3 else color)
    
    # 添加裝飾性圓圈
    for i in range(3):
        x = random.randint(20, width-20)
        y = random.randint(20, height-20)
        radius = random.randint(10, 30)
        alpha = random.randint(50, 150)
        color = tuple(int(accent_color[j:j+2], 16) for j in (1, 3, 5))
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                    fill=(*color, alpha) if len(color) == 3 else color)
    
    # 添加遊戲手柄圖標（簡單的矩形和圓圈）
    icon_size = 40
    icon_x = width // 2 - icon_size // 2
    icon_y = height // 2 - icon_size // 2 - 10
    
    # 手柄主體
    draw.rectangle([icon_x, icon_y, icon_x + icon_size, icon_y + icon_size//2], 
                  fill='white', outline='#333', width=2)
    
    # 手柄按鈕
    draw.ellipse([icon_x + 5, icon_y + 5, icon_x + 15, icon_y + 15], fill='#333')
    draw.ellipse([icon_x + 25, icon_y + 5, icon_x + 35, icon_y + 15], fill='#333')
    
    # 手柄握把
    draw.rectangle([icon_x - 5, icon_y + icon_size//2, icon_x + 5, icon_y + icon_size//2 + 15], 
                  fill='white', outline='#333', width=2)
    draw.rectangle([icon_x + icon_size - 5, icon_y + icon_size//2, icon_x + icon_size + 5, icon_y + icon_size//2 + 15], 
                  fill='white', outline='#333', width=2)
    
    # 添加遊戲名稱
    try:
        # 嘗試使用系統字體
        font_size = 16
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # 如果沒有找到字體，使用默認字體
        font = ImageFont.load_default()
    
    # 計算文字位置
    text_bbox = draw.textbbox((0, 0), game_name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = icon_y + icon_size + 20
    
    # 添加文字陰影
    draw.text((text_x + 1, text_y + 1), game_name, fill='#333', font=font)
    # 添加文字
    draw.text((text_x, text_y), game_name, fill='white', font=font)
    
    # 添加裝飾性邊框
    draw.rectangle([0, 0, width-1, height-1], outline='white', width=2)
    
    return img

def main():
    """主函數"""
    print("🎮 開始創建本地遊戲縮略圖...")
    
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
    
    # 創建每個遊戲的縮略圖
    success_count = 0
    
    for i, game in enumerate(games_data, 1):
        game_name = game.get('game_name', f'game_{i}')
        
        try:
            # 創建縮略圖
            img = create_game_thumbnail(game_name, i)
            
            # 保存圖片
            filename = f"{game_name.replace(' ', '_').replace('.', '_')}.png"
            filepath = os.path.join('images', filename)
            img.save(filepath, 'PNG')
            
            print(f"✅ 創建成功: {filename}")
            success_count += 1
            
        except Exception as e:
            print(f"❌ 創建失敗: {game_name} - {str(e)}")
    
    # 輸出結果
    print("\n" + "="*50)
    print("📊 創建完成統計:")
    print(f"✅ 成功: {success_count} 個")
    print(f"📁 圖片保存在: images/ 文件夾")
    
    if success_count > 0:
        print("\n🎉 本地縮略圖創建成功！")
        print("💡 現在可以更新 JSON 文件使用本地圖片路徑")

if __name__ == "__main__":
    main()
