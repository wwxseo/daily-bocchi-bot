import requests
import os
import random

# 1. 从 GitHub Secrets 获取配置
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def get_random_bocchi_image():
    """
    去 Safebooru 抓取一张后藤一里的图片
    """
    # Safebooru 的 API 地址，tags=gotou_hitori 表示只搜波奇酱
    url = "https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1&tags=gotou_hitori&limit=100"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                # 随机选一张
                image_data = random.choice(data)
                # 拼凑图片 URL (Safebooru 的目录结构)
                image_url = f"https://safebooru.org/images/{image_data['directory']}/{image_data['image']}"
                return image_url
    except Exception as e:
        print(f"找图失败: {e}")
    
    # 如果失败了，返回一张保底图（比如经典的承认欲求怪兽）
    return "https://media1.tenor.com/m/oxsD2MwZD8IAAAAd/bocchi-the-rock-hitori-gotou.gif"

def send_to_telegram(image_url):
    """
    发送图片给你的 Telegram
    """
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": "🎸 早上好！今天的波奇酱请查收~ #BocchiDaily"
    }
    
    try:
        res = requests.post(send_url, data=payload)
        print(f"发送状态: {res.status_code}")
        print(res.text)
    except Exception as e:
        print(f"发送失败: {e}")

if __name__ == "__main__":
    # 执行主流程
    if not BOT_TOKEN or not CHAT_ID:
        print("错误：未检测到 Secrets 配置，请在 GitHub 设置中添加。")
    else:
        print("正在寻找波奇酱...")
        pic = get_random_bocchi_image()
        print(f"找到图片: {pic}")
        send_to_telegram(pic)
