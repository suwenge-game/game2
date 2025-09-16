#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 JSON 文件使用本地圖片路徑
"""

import json
import os

def get_local_image_path(game_name):
    """根據遊戲名稱獲取本地圖片路徑"""
    # 清理遊戲名稱
    safe_name = game_name.replace(' ', '_').replace('.', '_')
    return f"images/{safe_name}.png"

def update_games_json():
    """更新 games.json 文件"""
    try:
        # 讀取 1.json 文件
        with open('1.json', 'r', encoding='utf-8') as f:
            games_data = json.load(f)
        
        print(f"📖 讀取到 {len(games_data)} 個遊戲")
        
        # 轉換數據格式並更新圖片路徑
        updated_games = []
        for i, game in enumerate(games_data, 1):
            game_name = game.get('game_name', f'game_{i}')
            local_image_path = get_local_image_path(game_name)
            
            # 檢查本地圖片是否存在
            if os.path.exists(local_image_path):
                print(f"✅ 找到本地圖片: {local_image_path}")
            else:
                print(f"⚠️  本地圖片不存在: {local_image_path}")
            
            # 轉換為網站使用的格式
            updated_game = {
                "id": i,
                "title": game_name,
                "image_url": local_image_path,
                "description": game.get('game_description', ''),
                "category": "射擊遊戲",  # 統一為射擊遊戲
                "tags": ["射擊", "多人", "io遊戲"],  # 默認標籤
                "game_link": game.get('game_link', '')
            }
            
            updated_games.append(updated_game)
        
        # 保存到 data/games.json
        with open('data/games.json', 'w', encoding='utf-8') as f:
            json.dump(updated_games, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 成功更新 data/games.json，包含 {len(updated_games)} 個遊戲")
        return True
        
    except FileNotFoundError as e:
        print(f"❌ 文件未找到: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析錯誤: {e}")
        return False
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
        return False

def main():
    """主函數"""
    print("🔄 開始更新 JSON 文件使用本地圖片路徑...")
    
    if update_games_json():
        print("\n🎉 JSON 文件更新成功！")
        print("💡 現在網站應該能正常顯示本地縮略圖了")
    else:
        print("\n❌ JSON 文件更新失敗")

if __name__ == "__main__":
    main()
