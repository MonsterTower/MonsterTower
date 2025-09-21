from datetime import datetime

# 转换到北京时间 (UTC+8)
hour = (datetime.utcnow().hour + 8) % 24

if 5 <= hour < 11:
    greeting = "☀️ 早上好！又是新的一天"
elif 11 <= hour < 13:
    greeting = "🍜 中午好！不考虑休息一下？"
elif 13 <= hour < 18:
    greeting = "🌤 下午好呀！干劲十足呢"
elif 18 <= hour < 23:
    greeting = "🌙 晚上好呀！今天过得怎么样？"
else:
    greeting = "🌌 夜深了，早点休息吧"

content = f"""

# {greeting}
# 您好，我是旋风！ 欢迎来到我的主页
# Hello! I'm XVI-Tower. Welcome to my homepage.

🎮 独立游戏开发者 |Indie Game Developer | Unity + C#  
🌌 《边缘世界》社区内容创作者&教程作者 | 'Rimwolrd' modder & guider

🎓 厦门大学 电子信息科学与技术系 2024级本科生 | XMU.School of Electronic Science and Engineering 

## 🛠 技术栈 / Tech Stack

![C#](https://img.shields.io/badge/C%23-239120?logo=c-sharp&logoColor=white) 
![Unity](https://img.shields.io/badge/Unity-000000?logo=unity&logoColor=white) 

## 📚 学习中 / Studying

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?logo=java&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?logo=cplusplus&logoColor=white)

## 🔗 链接 / Links

- [Bilibili](https://space.bilibili.com/17463438)
- [CSDN](https://blog.csdn.net/qq_58145131)【含Rimworld Mod开发教程】
- [爱发电](https://afdian.com/a/MonsterTower)

## 📬 联系方式 / Contact

- QQ: 1394869809
- E-Mail: 1394869809@qq.com


---

> 本页面会根据时间自动更新  
> 更新时间：{datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")} UTC
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
