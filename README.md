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
