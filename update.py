from datetime import datetime

# 转换到北京时间 (UTC+8)
hour = (datetime.utcnow().hour + 8) % 24

if 5 <= hour < 11:
    greeting = "☀️ 早上好！又是新的一天"
elif 11 <= hour < 13:
    greeting = "🍜 中午好！别忘了休息"
elif 13 <= hour < 18:
    greeting = "🌤 下午好呀！欢迎来到我的主页"
elif 18 <= hour < 23:
    greeting = "🌙 晚上好呀！今天过得怎么样？"
else:
    greeting = "🌌 夜深了，早点休息吧"

content = f"""
# Hi, I'm MonsterTower 👋

{greeting}

🎮 独立游戏开发者 Indie Game Developer | Unity + C#  
🌌 RimWorld 社区 Modder |  

## 🛠 Tech Stack
![C#](https://img.shields.io/badge/C%23-239120?logo=c-sharp&logoColor=white)
![Unity](https://img.shields.io/badge/Unity-000000?logo=unity&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## 🔗 Links
- [Bilibili](https://space.bilibili.com/17463438)
- [CSDN](https://blog.csdn.net/qq_58145131)

---

> 本页面会根据时间自动更新  
> 更新时间：{datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")} UTC
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
