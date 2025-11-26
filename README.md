# 🎸 Daily Bocchi Bot (每日波奇酱推送机器人)

这是一个基于 GitHub Actions 的自动化脚本。它每天会自动去 Safebooru 抓取一张 **后藤一里 (Bocchi the Rock!)** 的美图，并通过 Telegram 机器人发送给你。

![运行效果截图](https://github.com/wwxseo/daily-bocchi-bot/blob/main/screenshot.jpg)
*(建议把你刚才那张 Telegram 收到消息的截图传到仓库里，替换上面这个链接，有图才有真相！)*

## ✨ 功能特点
- **零成本**：完全基于 GitHub Actions 免费运行，无需购买服务器。
- **自动化**：每天早上 8:00 (北京时间) 自动推送。
- **防社死**：默认使用 Safebooru 的 API，图片相对安全。
- **易扩展**：代码简单，可轻松修改成抓取其他角色。

## 🚀 如何使用 (Quick Start)

你只需要 3 步就能拥有自己的波奇机器人：

### 1. Fork 本仓库
点击右上角的 **Fork** 按钮，将项目复制到你的 GitHub 账号下。

### 2. 配置 Secrets
进入你 Fork 后的仓库，点击 `Settings` -> `Secrets and variables` -> `Actions`，添加以下两个变量：
- `TELEGRAM_BOT_TOKEN`: 你的 Telegram 机器人 Token。
- `TELEGRAM_CHAT_ID`: 你的用户 ID。

### 3. 启用并运行
1. 点击 `Actions` 选项卡。
2. 允许 Workflows 运行 (Enable Workflow)。
3. 手动点击 `Run workflow` 测试一次，或者等待第二天早上自动运行。

## 🛠️ 技术栈
- Python 3.9
- GitHub Actions (Cron Schedule)
- Telegram Bot API

## 📄 开源协议
MIT License
