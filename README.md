Markdown

# 🎸 Daily Bocchi Bot (每日波奇酱推送机器人)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **"这里的波奇酱全是野生的！"**

这是一个基于 GitHub Actions 的自动化脚本。它每天会自动去 Safebooru 抓取一张 **后藤一里 (Bocchi the Rock!)** 的美图，并通过 Telegram 机器人发送给你。无需服务器，完全免费，配置简单。

![运行效果截图](screenshot.jpg)

## ✨ 功能特点

- **💸 零成本**：利用 GitHub Actions 的免费额度运行，无需购买任何服务器。
- **⏰ 全自动**：默认每天早上 **8:00** (北京时间) 准时推送，唤醒元气满满的一天。
- **🛡️ 防社死**：默认使用 Safebooru API (Safe 模式)，图片内容相对安全，适合工作群或日常使用。
- **🧩 易扩展**：代码结构清晰，只需改动一个单词，就能变成其他角色的推送机器人。

---

## 🚀 快速开始 (Quick Start)

你只需要 3 步就能拥有自己的波奇机器人：

### 1. Fork 本仓库
点击页面右上角的 **Fork** 按钮，将本项目完整复制到你的 GitHub 账号下。

### 2. 配置 Secrets (详细指南)
为了保护账户安全，我们需要将敏感信息存储在 GitHub 的保险箱 (Secrets) 中。

#### 2.1 获取 Telegram 机器人信息
如果你还没有机器人，请按以下步骤获取：
1.  **获取 Bot Token**:
    - 在 Telegram 搜索 `@BotFather` 并发送 `/newbot`。
    - 按提示设置名字，成功后你会收到一串红色的 **HTTP API Token**。
    - **⚠️ 重要**：获取 Token 后，请务必在 Telegram 搜索你的机器人用户名并点击 **Start**，否则它无法给你发消息。
2.  **获取 Chat ID (你的用户ID)**:
    - 在 Telegram 搜索 `@userinfobot` 并点击 Start。
    - 它回复的那串数字就是你的 `ID`。

#### 2.2 填入 GitHub 仓库
回到你 Fork 后的仓库页面：
1.  点击顶部菜单的 **⚙️ Settings**。
2.  在左侧栏找到 **Secrets and variables** -> **Actions**。
3.  点击 **New repository secret**，依次添加以下两个变量：
    - Name: `TELEGRAM_BOT_TOKEN`
      - Value: *粘贴你的 Token*
    - Name: `TELEGRAM_CHAT_ID`
      - Value: *粘贴你的 Chat ID*

### 3. 启用并运行
1. 点击仓库顶部的 **Actions** 选项卡。
2. 点击绿色的 **I understand my workflows, go ahead and enable them** 按钮。
3. 在左侧选择 **波奇酱每日推送**，点击右侧的 **Run workflow** 手动测试一次。
4. 如果手机收到消息，恭喜你，配置成功！以后它会自动运行。

---

## ⚙️ 进阶配置 (自定义)

想看别的角色？或者想改时间？这里教你怎么改：

### 1. 修改推送角色
打开 `main.py` 文件，找到第 **14** 行左右：
```python
# tags=gotou_hitori 表示只搜波奇酱
url = "[https://safebooru.org/index.php?...&tags=gotou_hitori](https://safebooru.org/index.php?...&tags=gotou_hitori)&..."
```
将 gotou_hitori 修改为其他角色的英文标签即可。

例如：喜多郁代 -> kita_ikuyo

例如：伊地知虹夏 -> ijichi_nijika

2. 修改推送时间
打开 .github/workflows/daily_push.yml 文件，找到 cron 表达式：

YAML

- cron: '0 0 * * *' # UTC 0点 = 北京时间 8点
改成 '0 23 * * *' -> 北京时间早上 7 点

改成 '30 0 * * *' -> 北京时间早上 8:30

❓ 常见问题 (FAQ)
Q: 运行显示成功 (绿色对勾)，但手机没收到消息？ A: 99% 的原因是你忘记点击机器人的 Start 了。Telegram 规定机器人不能主动向陌生人发起对话。请先给你的机器人发一句 "hello"。

Q: 图片加载失败或者发了一张奇怪的 GIF？ A: 脚本里写了“保底机制”。如果网络波动或者 API 没找到图，为了不让你失望，机器人会发一张默认的表情包。这属于正常现象。

Q: 我想把仓库设为私有 (Private) 可以吗？ A: 完全可以。GitHub Actions 在私有仓库里也能免费运行（每月有 2000 分钟额度，足够用几百年了）。

🤝 贡献与支持
如果你觉得这个项目有趣，欢迎点击右上角的 ⭐️ Star 支持一下！

📄 开源协议
本项目基于 MIT License 开源。
