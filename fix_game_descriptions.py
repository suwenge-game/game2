#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
游戏描述修复脚本
修复games.json中所有中文描述为英文描述
"""

import json
import re

def translate_game_descriptions():
    """修复游戏描述"""
    
    # 游戏描述翻译映射
    game_translations = {
        # 动作游戏
        "几何箭头游戏，控制箭头在几何世界中飞行": "Navigate through stunning geometric landscapes in this precision-based action game. Master the art of arrow physics as you guide your projectile through increasingly complex mazes and obstacles.",
        "方块io游戏，在方块世界中与其他玩家战斗": "Enter the competitive world of Bloxd io, where strategy meets action in this multiplayer battle royale game. Build your base, collect resources, and eliminate opponents.",
        "蒙面特种部队，第一人称射击游戏": "Join the elite Masked Special Forces in this intense first-person shooter. Experience tactical combat with realistic weapons and challenging missions.",
        "GTA模拟器，体验犯罪世界的刺激生活": "Experience the thrill of the criminal underworld in this GTA-style simulator. Drive cars, complete missions, and explore an open world full of action.",
        "射击类问答游戏，通过射击来回答问题": "Test your knowledge and shooting skills in this unique quiz game. Answer questions by shooting the correct targets in this innovative educational shooter.",
        "玩具熊的五夜后宫，恐怖生存游戏": "Survive five terrifying nights at Freddy's in this spine-chilling horror survival game. Monitor security cameras and defend against animatronic attacks.",
        "极限跑酷3D，在3D世界中奔跑和跳跃": "Experience adrenaline-pumping parkour action in stunning 3D environments. Run, jump, and perform incredible stunts in this fast-paced adventure.",
        "兰博基尼罪恶城市，驾驶超跑在犯罪城市中行动": "Drive luxury supercars through the dangerous streets of Vice Crime City. Experience high-speed chases and criminal adventures in this action-packed racing game.",
        "奶奶，恐怖逃脱游戏，避开奶奶的追捕": "Escape from Granny's house in this terrifying horror game. Solve puzzles, avoid detection, and find a way out before time runs out.",
        "DTA系列第6代，体验激烈的战斗": "Experience intense combat action in DTA 6, the latest installment of this popular fighting series. Master various fighting techniques and defeat your opponents.",
        "火柴人战士3D，3D格斗游戏": "Engage in epic 3D stickman combat in this action-packed fighting game. Master different fighting styles and defeat challenging opponents.",
        "火柴人跑酷，在跑酷中展现技巧": "Show off your parkour skills in this exciting stickman adventure. Run, jump, and perform amazing stunts across challenging obstacle courses.",
        "火柴人GTA城市，在像素城市中进行射击战斗": "Experience GTA-style action in a pixelated stickman world. Drive vehicles, engage in shootouts, and complete missions in this retro-style adventure.",
        "红灯绿灯，鱿鱼游戏经典关卡": "Test your reflexes in this classic Red Light Green Light challenge from Squid Game. Move when the light is green, freeze when it's red!",
        "爬到顶部，物理格斗游戏": "Climb to the top in this physics-based fighting game. Use strategy and skill to overcome opponents and reach the summit.",
        "第一人称射击模拟器，体验真实的射击感觉": "Experience realistic first-person shooting action in this immersive FPS simulator. Master different weapons and complete challenging missions.",
        "城市警车，驾驶警车维护治安": "Take on the role of a city police officer in this action-packed driving game. Patrol the streets, chase criminals, and maintain law and order.",
        "疯狂打击力量，多人第一人称射击游戏": "Join the Crazy Strike Force in this intense multiplayer FPS game. Team up with friends and engage in epic battles against other players.",
        "鸡蛋壳射击io游戏，控制鸡蛋进行射击战斗": "Control an egg in this unique io-style shooter game. Battle against other players in this quirky and fun multiplayer experience.",
        "奶奶2，续作恐怖逃脱游戏": "Return to Granny's house in this sequel to the popular horror escape game. Face new challenges and escape routes in this terrifying adventure.",
        "神枪手io游戏，精准射击击败对手": "Test your marksmanship skills in this precision-based io shooter. Take down opponents with accurate shots and climb the leaderboard.",
        "黑帮城市游戏，在犯罪都市中进行射击战斗": "Enter the dangerous world of Mob City in this action-packed shooter. Engage in gang warfare and fight for control of the criminal underworld.",
        "疯狂射击手，快节奏的射击游戏": "Experience fast-paced shooting action in this intense arcade-style game. Survive waves of enemies and test your reflexes.",
        "反恐精英在线版，经典FPS射击游戏": "Play the classic Counter-Strike experience in this online FPS game. Choose your side and engage in tactical team-based combat.",
        "雪地骑手3D，在雪地中骑行的3D游戏": "Ride through beautiful snowy landscapes in this stunning 3D snowboarding game. Perform tricks and enjoy the winter scenery.",
        "只能向上障碍赛，向上攀爬的障碍游戏": "Climb your way up in this challenging obstacle course game. Navigate through increasingly difficult levels and reach the top.",
        "醉酒决斗，醉酒状态下的格斗游戏": "Experience hilarious combat in this unique fighting game where characters are under the influence. Master the unpredictable movements and win battles.",
        
        # 益智游戏
        "麻将，中国传统益智游戏": "Play the classic Chinese tile-matching game of Mahjong. Clear all tiles by matching pairs in this traditional puzzle game.",
        "国际象棋，策略性棋类游戏": "Master the ancient game of chess in this strategic board game. Plan your moves carefully and checkmate your opponent.",
        "纸牌接龙，单人纸牌游戏": "Enjoy the classic solitaire card game. Arrange cards in descending order by suit to clear the tableau.",
        "井字棋，经典的两人对战游戏": "Play the timeless game of Tic-Tac-Toe. Get three in a row to win in this simple yet engaging strategy game.",
        "贪吃蛇，控制蛇吃食物的经典游戏": "Control the snake and eat food to grow longer in this classic arcade game. Avoid hitting walls or your own tail.",
        "2048数字拼图游戏，合并相同数字达到2048": "Combine numbered tiles to reach 2048 in this addictive puzzle game. Use strategy and planning to achieve the highest score.",
        "俄罗斯方块，经典的方块消除游戏": "Play the legendary Tetris game. Arrange falling blocks to create complete lines and clear them from the screen.",
        "数独，数字逻辑推理游戏": "Solve the classic Sudoku puzzle by filling in numbers 1-9 in each row, column, and 3x3 box without repetition.",
        
        # 赛车游戏
        "城市停车决斗，在城市中进行停车挑战": "Master the art of parallel parking in this challenging city driving game. Navigate tight spaces and park perfectly.",
        "高速公路赛车手专业版，专业高速赛车游戏": "Experience high-speed racing action on the highway in this professional racing simulator. Compete against other drivers and win races.",
        "燃烧城市，在城市中进行激烈赛车": "Race through the city streets in this intense driving game. Burn rubber and leave your opponents in the dust.",
        "Edys汽车模拟器，真实汽车驾驶模拟": "Experience realistic car driving simulation in Edys Car Simulator. Master different vehicles and driving conditions.",
        "吉普车司机，驾驶吉普车进行越野": "Take on challenging off-road terrain in this Jeep driving simulator. Navigate through rough landscapes and obstacles.",
        "超级汽车驾驶，驾驶超级跑车": "Drive exotic supercars in this high-performance racing game. Experience the thrill of speed and luxury vehicles.",
        "漂移城市，在城市中进行漂移比赛": "Master the art of drifting in this exciting racing game. Slide through corners and perform spectacular drifts.",
        "疯狂摩托车，驾驶摩托车进行特技表演": "Perform amazing motorcycle stunts in this action-packed riding game. Show off your skills and complete challenging courses.",
        "迷你汽车赛车，小型汽车竞速游戏": "Race in tiny cars in this fun and fast-paced mini racing game. Compete against other players in exciting races.",
        "终极飞行汽车，驾驶会飞的汽车": "Drive a flying car in this futuristic racing game. Soar through the skies and race against other flying vehicles.",
        "高速公路竞速，在高速公路上进行赛车": "Race at high speeds on the highway in this thrilling racing game. Overtake opponents and reach the finish line first.",
        "摩托车之旅，驾驶摩托车进行旅行": "Embark on a motorcycle journey in this scenic riding game. Explore beautiful landscapes and enjoy the freedom of the open road.",
        
        # 体育游戏
        "足球经理，管理足球俱乐部": "Take control of a football club in this strategic management game. Build your team, manage finances, and lead your club to victory.",
        "篮球投篮，练习篮球投篮技巧": "Practice your basketball shooting skills in this fun sports game. Improve your accuracy and become a shooting champion.",
        "网球比赛，体验网球运动": "Play tennis in this realistic sports simulation. Master different shots and compete in exciting matches.",
        "高尔夫球，在美丽球场打高尔夫": "Play golf on beautiful courses in this relaxing sports game. Master your swing and aim for the perfect shot.",
        "拳击比赛，体验拳击运动": "Step into the ring in this intense boxing game. Master different punches and defeat your opponents.",
        "滑雪比赛，在雪山上滑雪": "Race down snowy mountains in this exciting skiing game. Navigate through challenging slopes and obstacles.",
        "游泳比赛，体验游泳运动": "Compete in swimming races in this aquatic sports game. Master different strokes and beat your opponents to the finish.",
        "田径比赛，体验各种田径项目": "Compete in various track and field events in this comprehensive athletics game. Test your speed, strength, and endurance.",
        
        # 模拟游戏
        "城市建造，建设自己的城市": "Build and manage your own city in this strategic simulation game. Plan infrastructure, manage resources, and watch your city grow.",
        "农场经营，经营自己的农场": "Run your own farm in this relaxing simulation game. Plant crops, raise animals, and build a successful agricultural business.",
        "餐厅经营，经营自己的餐厅": "Manage your own restaurant in this business simulation game. Serve customers, create menus, and build a culinary empire.",
        "医院管理，管理医院运营": "Take charge of a hospital in this medical management simulation. Treat patients, manage staff, and ensure smooth operations.",
        "学校管理，管理学校运营": "Run your own school in this educational management game. Hire teachers, manage students, and create a successful learning environment.",
        "动物园管理，经营动物园": "Build and manage your own zoo in this animal simulation game. Care for animals, attract visitors, and create the ultimate wildlife experience.",
        "机场管理，管理机场运营": "Take control of an airport in this aviation management simulation. Handle flights, manage passengers, and ensure smooth operations.",
        "酒店管理，经营酒店": "Run your own hotel in this hospitality management game. Serve guests, manage rooms, and build a successful hospitality business.",
        
        # 更多遗漏的游戏
        "F1漂移赛车手，F1赛车的漂移版本": "Experience Formula 1 racing with a drifting twist in this exciting racing game. Master F1 cars and perform spectacular drifts.",
        "Hurakan城市司机HD，高清城市驾驶游戏": "Drive through the stunning city of Hurakan in this high-definition urban driving simulator. Experience realistic city traffic and beautiful graphics.",
        "障碍赛：绘制和跳跃，绘制路径进行跳跃": "Draw your own path and jump through obstacles in this creative platformer game. Use your drawing skills to navigate challenging levels.",
        
        # 更多赛车游戏
        "终极飞行汽车2，续作飞行汽车游戏": "Experience the sequel to the ultimate flying car adventure. Drive advanced flying vehicles and race through futuristic landscapes.",
        "疯狂漂移者，进行疯狂的漂移表演": "Become a master drifter in this intense racing game. Perform spectacular drifts and stunts on challenging tracks.",
        "警察真实追车模拟器，体验警察追车": "Experience realistic police chase simulation. Drive police cars and pursue criminals through city streets.",
        "赛车地平线，地平线主题赛车游戏": "Race across stunning horizons in this beautiful racing game. Experience breathtaking landscapes and exciting races.",
        "漂移狂怒，激烈的漂移比赛": "Engage in furious drifting competitions in this high-intensity racing game. Master the art of controlled slides.",
        "汽车特技之王，进行各种汽车特技": "Become the king of car stunts in this action-packed driving game. Perform incredible tricks and stunts.",
        
        # 更多动作游戏
        "疯狂射击手，快节奏的射击游戏": "Experience fast-paced shooting action in this intense arcade-style game. Survive waves of enemies and test your reflexes.",
        "反恐精英在线版，经典FPS射击游戏": "Play the classic Counter-Strike experience in this online FPS game. Choose your side and engage in tactical team-based combat.",
        "雪地骑手3D，在雪地中骑行的3D游戏": "Ride through beautiful snowy landscapes in this stunning 3D snowboarding game. Perform tricks and enjoy the winter scenery.",
        "只能向上障碍赛，向上攀爬的障碍游戏": "Climb your way up in this challenging obstacle course game. Navigate through increasingly difficult levels and reach the top.",
        "醉酒决斗，醉酒状态下的格斗游戏": "Experience hilarious combat in this unique fighting game where characters are under the influence. Master the unpredictable movements and win battles.",
        
        # 更多益智游戏
        "麻将，中国传统益智游戏": "Play the classic Chinese tile-matching game of Mahjong. Clear all tiles by matching pairs in this traditional puzzle game.",
        "国际象棋，策略性棋类游戏": "Master the ancient game of chess in this strategic board game. Plan your moves carefully and checkmate your opponent.",
        "纸牌接龙，单人纸牌游戏": "Enjoy the classic solitaire card game. Arrange cards in descending order by suit to clear the tableau.",
        "井字棋，经典的两人对战游戏": "Play the timeless game of Tic-Tac-Toe. Get three in a row to win in this simple yet engaging strategy game.",
        "贪吃蛇，控制蛇吃食物的经典游戏": "Control the snake and eat food to grow longer in this classic arcade game. Avoid hitting walls or your own tail.",
        "2048数字拼图游戏，合并相同数字达到2048": "Combine numbered tiles to reach 2048 in this addictive puzzle game. Use strategy and planning to achieve the highest score.",
        "俄罗斯方块，经典的方块消除游戏": "Play the legendary Tetris game. Arrange falling blocks to create complete lines and clear them from the screen.",
        "数独，数字逻辑推理游戏": "Solve the classic Sudoku puzzle by filling in numbers 1-9 in each row, column, and 3x3 box without repetition."
    }
    
    # 读取游戏数据
    with open('data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)
    
    # 修复中文描述
    fixed_count = 0
    for game in games:
        # 修复game_description
        if 'game_description' in game and re.search(r'[\u4e00-\u9fff]', game['game_description']):
            chinese_desc = game['game_description']
            if chinese_desc in game_translations:
                game['game_description'] = game_translations[chinese_desc]
                fixed_count += 1
            else:
                # 如果没有直接匹配，尝试部分匹配
                for chinese, english in game_translations.items():
                    if chinese in chinese_desc:
                        game['game_description'] = english
                        fixed_count += 1
                        break
        
        # 修复description
        if 'description' in game and re.search(r'[\u4e00-\u9fff]', game['description']):
            chinese_desc = game['description']
            if chinese_desc in game_translations:
                game['description'] = game_translations[chinese_desc]
                fixed_count += 1
            else:
                # 如果没有直接匹配，尝试部分匹配
                for chinese, english in game_translations.items():
                    if chinese in chinese_desc:
                        game['description'] = english
                        fixed_count += 1
                        break
        
        # 修复game_category
        if 'game_category' in game and re.search(r'[\u4e00-\u9fff]', game['game_category']):
            category_map = {
                '动作游戏': 'Action Games',
                '益智游戏': 'Puzzle Games', 
                '赛车游戏': 'Racing Games',
                '体育游戏': 'Sports Games',
                '模拟游戏': 'Simulation Games',
                '射击游戏': 'Shooting Games'
            }
            if game['game_category'] in category_map:
                game['game_category'] = category_map[game['game_category']]
                fixed_count += 1
    
    # 保存修复后的数据
    with open('data/games.json', 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 修复完成！共修复了 {fixed_count} 个中文描述")
    return fixed_count

if __name__ == "__main__":
    translate_game_descriptions()
