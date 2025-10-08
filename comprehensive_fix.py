#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面修复游戏描述脚本
修复所有剩余的中文描述
"""

import json
import re

def comprehensive_fix():
    """全面修复所有中文描述"""
    
    # 通用翻译规则
    translation_rules = {
        # 游戏类型翻译
        "射击游戏": "Shooting Game",
        "动作游戏": "Action Game", 
        "赛车游戏": "Racing Game",
        "益智游戏": "Puzzle Game",
        "体育游戏": "Sports Game",
        "模拟器游戏": "Simulator Game",
        "模拟游戏": "Simulation Game",
        "io游戏": "io Game",
        "多人游戏": "Multiplayer Game",
        "单人游戏": "Single Player Game",
        
        # 常见词汇翻译
        "游戏": "Game",
        "模拟器": "Simulator",
        "射击": "Shooting",
        "战斗": "Combat",
        "驾驶": "Driving",
        "赛车": "Racing",
        "漂移": "Drifting",
        "特技": "Stunt",
        "生存": "Survival",
        "战争": "War",
        "狙击": "Sniper",
        "僵尸": "Zombie",
        "警察": "Police",
        "军队": "Army",
        "坦克": "Tank",
        "摩托车": "Motorcycle",
        "汽车": "Car",
        "飞机": "Aircraft",
        "火车": "Train",
        "船": "Ship",
        "城市": "City",
        "高速公路": "Highway",
        "雪地": "Snow",
        "沙漠": "Desert",
        "森林": "Forest",
        "海洋": "Ocean",
        "太空": "Space",
        "未来": "Futuristic",
        "现代": "Modern",
        "古代": "Ancient",
        "经典": "Classic",
        "专业": "Professional",
        "高级": "Advanced",
        "终极": "Ultimate",
        "超级": "Super",
        "疯狂": "Crazy",
        "极限": "Extreme",
        "真实": "Realistic",
        "虚拟": "Virtual",
        "3D": "3D",
        "HD": "HD",
        "在线": "Online",
        "离线": "Offline",
        "免费": "Free",
        "付费": "Paid",
        "多人": "Multiplayer",
        "单人": "Single Player",
        "合作": "Cooperative",
        "竞技": "Competitive",
        "休闲": "Casual",
        "硬核": "Hardcore",
        "简单": "Simple",
        "困难": "Difficult",
        "挑战": "Challenge",
        "冒险": "Adventure",
        "探索": "Exploration",
        "建造": "Building",
        "管理": "Management",
        "经营": "Business",
        "策略": "Strategy",
        "战术": "Tactical",
        "角色扮演": "RPG",
        "第一人称": "First Person",
        "第三人称": "Third Person",
        "俯视角": "Top Down",
        "侧视角": "Side View",
        "横版": "Side Scrolling",
        "竖版": "Vertical Scrolling",
        "像素": "Pixel",
        "卡通": "Cartoon",
        "写实": "Realistic",
        "科幻": "Sci-Fi",
        "奇幻": "Fantasy",
        "恐怖": "Horror",
        "喜剧": "Comedy",
        "动作": "Action",
        "解谜": "Puzzle",
        "益智": "Educational",
        "音乐": "Music",
        "节奏": "Rhythm",
        "体育": "Sports",
        "格斗": "Fighting",
        "平台": "Platform",
        "跑酷": "Parkour",
        "跳跃": "Jumping",
        "飞行": "Flying",
        "游泳": "Swimming",
        "跑步": "Running",
        "走路": "Walking",
        "爬行": "Crawling",
        "攀爬": "Climbing",
        "滑行": "Sliding",
        "滚动": "Rolling",
        "旋转": "Spinning",
        "翻转": "Flipping",
        "弹跳": "Bouncing",
        "爆炸": "Explosion",
        "火焰": "Fire",
        "水": "Water",
        "冰": "Ice",
        "电": "Electric",
        "风": "Wind",
        "土": "Earth",
        "金": "Metal",
        "木": "Wood",
        "火": "Fire",
        "光": "Light",
        "暗": "Dark",
        "彩色": "Colorful",
        "黑白": "Black and White",
        "红色": "Red",
        "蓝色": "Blue",
        "绿色": "Green",
        "黄色": "Yellow",
        "紫色": "Purple",
        "橙色": "Orange",
        "粉色": "Pink",
        "灰色": "Gray",
        "黑色": "Black",
        "白色": "White",
        "棕色": "Brown",
        "银色": "Silver",
        "金色": "Gold",
        "铜色": "Copper",
        "透明": "Transparent",
        "不透明": "Opaque",
        "发光": "Glowing",
        "闪烁": "Blinking",
        "旋转": "Rotating",
        "移动": "Moving",
        "静止": "Static",
        "动态": "Dynamic",
        "静态": "Static",
        "快速": "Fast",
        "慢速": "Slow",
        "高速": "High Speed",
        "低速": "Low Speed",
        "超速": "Super Speed",
        "极速": "Extreme Speed",
        "光速": "Light Speed",
        "音速": "Sound Speed",
        "亚音速": "Subsonic",
        "超音速": "Supersonic",
        "高超音速": "Hypersonic",
        "大": "Big",
        "小": "Small",
        "巨大": "Huge",
        "微小": "Tiny",
        "迷你": "Mini",
        "巨型": "Giant",
        "超大型": "Super Large",
        "超小型": "Super Small",
        "中等": "Medium",
        "平均": "Average",
        "标准": "Standard",
        "正常": "Normal",
        "异常": "Abnormal",
        "特殊": "Special",
        "普通": "Common",
        "稀有": "Rare",
        "史诗": "Epic",
        "传说": "Legendary",
        "神话": "Mythical",
        "神秘": "Mysterious",
        "神奇": "Magical",
        "魔法": "Magic",
        "法术": "Spell",
        "技能": "Skill",
        "能力": "Ability",
        "力量": "Power",
        "能量": "Energy",
        "生命": "Life",
        "健康": "Health",
        "体力": "Stamina",
        "魔法值": "Mana",
        "经验": "Experience",
        "等级": "Level",
        "分数": "Score",
        "金币": "Gold",
        "银币": "Silver",
        "铜币": "Copper",
        "钻石": "Diamond",
        "宝石": "Gem",
        "水晶": "Crystal",
        "珍珠": "Pearl",
        "玉石": "Jade",
        "翡翠": "Emerald",
        "红宝石": "Ruby",
        "蓝宝石": "Sapphire",
        "紫水晶": "Amethyst",
        "黄水晶": "Citrine",
        "绿松石": "Turquoise",
        "玛瑙": "Agate",
        "琥珀": "Amber",
        "珊瑚": "Coral",
        "象牙": "Ivory",
        "骨头": "Bone",
        "皮革": "Leather",
        "布料": "Cloth",
        "丝绸": "Silk",
        "棉花": "Cotton",
        "羊毛": "Wool",
        "亚麻": "Linen",
        "麻": "Hemp",
        "竹子": "Bamboo",
        "木头": "Wood",
        "石头": "Stone",
        "岩石": "Rock",
        "沙子": "Sand",
        "泥土": "Dirt",
        "粘土": "Clay",
        "水泥": "Cement",
        "混凝土": "Concrete",
        "砖块": "Brick",
        "瓦片": "Tile",
        "玻璃": "Glass",
        "金属": "Metal",
        "钢铁": "Steel",
        "铁": "Iron",
        "铜": "Copper",
        "铝": "Aluminum",
        "锌": "Zinc",
        "铅": "Lead",
        "锡": "Tin",
        "银": "Silver",
        "金": "Gold",
        "铂": "Platinum",
        "钛": "Titanium",
        "钨": "Tungsten",
        "铬": "Chromium",
        "镍": "Nickel",
        "锰": "Manganese",
        "钼": "Molybdenum",
        "钒": "Vanadium",
        "铌": "Niobium",
        "钽": "Tantalum",
        "铪": "Hafnium",
        "锆": "Zirconium",
        "铪": "Hafnium",
        "钪": "Scandium",
        "钇": "Yttrium",
        "镧": "Lanthanum",
        "铈": "Cerium",
        "镨": "Praseodymium",
        "钕": "Neodymium",
        "钷": "Promethium",
        "钐": "Samarium",
        "铕": "Europium",
        "钆": "Gadolinium",
        "铽": "Terbium",
        "镝": "Dysprosium",
        "钬": "Holmium",
        "铒": "Erbium",
        "铥": "Thulium",
        "镱": "Ytterbium",
        "镥": "Lutetium",
        "钍": "Thorium",
        "镤": "Protactinium",
        "铀": "Uranium",
        "镎": "Neptunium",
        "钚": "Plutonium",
        "镅": "Americium",
        "锔": "Curium",
        "锫": "Berkelium",
        "锎": "Californium",
        "锿": "Einsteinium",
        "镄": "Fermium",
        "钔": "Mendelevium",
        "锘": "Nobelium",
        "铹": "Lawrencium",
        "钅卢": "Rutherfordium",
        "钅杜": "Dubnium",
        "钅喜": "Seaborgium",
        "钅波": "Bohrium",
        "钅黑": "Hassium",
        "钅麦": "Meitnerium",
        "钅达": "Darmstadtium",
        "钅仑": "Roentgenium",
        "钅哥": "Copernicium",
        "钅夫": "Flerovium",
        "钅立": "Livermorium",
        "钅石": "Tennessine",
        "钅气": "Oganesson"
    }
    
    # 读取游戏数据
    with open('data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)
    
    fixed_count = 0
    
    for game in games:
        # 修复game_description
        if 'game_description' in game and re.search(r'[\u4e00-\u9fff]', game['game_description']):
            original = game['game_description']
            # 使用翻译规则
            translated = original
            for chinese, english in translation_rules.items():
                translated = translated.replace(chinese, english)
            
            # 如果还有中文字符，生成通用描述
            if re.search(r'[\u4e00-\u9fff]', translated):
                # 根据游戏类型生成描述
                if '射击' in original or 'shooting' in original.lower():
                    translated = f"Experience intense shooting action in this exciting {game.get('title', 'game')}. Master weapons and defeat enemies in this action-packed adventure."
                elif '赛车' in original or 'racing' in original.lower() or '驾驶' in original:
                    translated = f"Drive fast cars and race to victory in this thrilling {game.get('title', 'racing game')}. Master the tracks and become the ultimate racing champion."
                elif '动作' in original or 'action' in original.lower():
                    translated = f"Engage in exciting action gameplay in this dynamic {game.get('title', 'action game')}. Experience fast-paced combat and thrilling adventures."
                elif '益智' in original or 'puzzle' in original.lower():
                    translated = f"Challenge your mind with this engaging {game.get('title', 'puzzle game')}. Solve puzzles and test your problem-solving skills."
                elif '体育' in original or 'sports' in original.lower():
                    translated = f"Play exciting sports action in this dynamic {game.get('title', 'sports game')}. Compete and show off your athletic skills."
                elif '模拟' in original or 'simulator' in original.lower():
                    translated = f"Experience realistic simulation gameplay in this immersive {game.get('title', 'simulator')}. Master the controls and enjoy authentic experiences."
                else:
                    translated = f"Enjoy exciting gameplay in this fun {game.get('title', 'game')}. Experience engaging challenges and entertaining adventures."
            
            game['game_description'] = translated
            fixed_count += 1
        
        # 修复description
        if 'description' in game and re.search(r'[\u4e00-\u9fff]', game['description']):
            original = game['description']
            # 使用翻译规则
            translated = original
            for chinese, english in translation_rules.items():
                translated = translated.replace(chinese, english)
            
            # 如果还有中文字符，生成通用描述
            if re.search(r'[\u4e00-\u9fff]', translated):
                # 根据游戏类型生成描述
                if '射击' in original or 'shooting' in original.lower():
                    translated = f"Experience intense shooting action in this exciting {game.get('title', 'game')}. Master weapons and defeat enemies in this action-packed adventure."
                elif '赛车' in original or 'racing' in original.lower() or '驾驶' in original:
                    translated = f"Drive fast cars and race to victory in this thrilling {game.get('title', 'racing game')}. Master the tracks and become the ultimate racing champion."
                elif '动作' in original or 'action' in original.lower():
                    translated = f"Engage in exciting action gameplay in this dynamic {game.get('title', 'action game')}. Experience fast-paced combat and thrilling adventures."
                elif '益智' in original or 'puzzle' in original.lower():
                    translated = f"Challenge your mind with this engaging {game.get('title', 'puzzle game')}. Solve puzzles and test your problem-solving skills."
                elif '体育' in original or 'sports' in original.lower():
                    translated = f"Play exciting sports action in this dynamic {game.get('title', 'sports game')}. Compete and show off your athletic skills."
                elif '模拟' in original or 'simulator' in original.lower():
                    translated = f"Experience realistic simulation gameplay in this immersive {game.get('title', 'simulator')}. Master the controls and enjoy authentic experiences."
                else:
                    translated = f"Enjoy exciting gameplay in this fun {game.get('title', 'game')}. Experience engaging challenges and entertaining adventures."
            
            game['description'] = translated
            fixed_count += 1
        
        # 修复game_category
        if 'game_category' in game and re.search(r'[\u4e00-\u9fff]', game['game_category']):
            category_map = {
                '动作游戏': 'Action Games',
                '益智游戏': 'Puzzle Games', 
                '赛车游戏': 'Racing Games',
                '体育游戏': 'Sports Games',
                '模拟游戏': 'Simulation Games',
                '射击游戏': 'Shooting Games',
                '模拟器游戏': 'Simulator Games'
            }
            if game['game_category'] in category_map:
                game['game_category'] = category_map[game['game_category']]
                fixed_count += 1
    
    # 保存修复后的数据
    with open('data/games.json', 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 全面修复完成！共修复了 {fixed_count} 个中文描述")
    return fixed_count

if __name__ == "__main__":
    comprehensive_fix()
