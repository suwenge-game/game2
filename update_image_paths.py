#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 JSON 文件中的圖片路徑為新的 SEO 友好結構
"""

import json
import os

def update_image_paths():
    """更新圖片路徑"""
    try:
        # 讀取 games.json 文件
        with open('data/games.json', 'r', encoding='utf-8') as f:
            games_data = json.load(f)
        
        print(f"📖 讀取到 {len(games_data)} 個遊戲")
        
        # 更新每個遊戲的圖片路徑
        for game in games_data:
            if game.get('image_url', '').startswith('images/'):
                old_path = game['image_url']
                new_path = old_path.replace('images/', 'assets/images/')
                game['image_url'] = new_path
                print(f"✅ 更新路徑: {old_path} -> {new_path}")
        
        # 保存更新後的文件
        with open('data/games.json', 'w', encoding='utf-8') as f:
            json.dump(games_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 成功更新 data/games.json")
        return True
        
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
        return False

def main():
    """主函數"""
    print("🔄 開始更新圖片路徑...")
    
    if update_image_paths():
        print("\n🎉 圖片路徑更新成功！")
    else:
        print("\n❌ 圖片路徑更新失敗")

if __name__ == "__main__":
    main()
