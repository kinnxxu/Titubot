# 📰 News Tweet Bot 🤖

A fully automated bot that **fetches the latest news** from top media sources and **tweets it on X (formerly Twitter)** — all controlled via **Telegram**!  
Deploy-ready for **Heroku + GitHub** with custom interval scheduling via Telegram commands.

---

## ⚙️ Features

✅ Automatically fetches and tweets top news headlines  
✅ Customizable tweet interval (e.g. every 30, 60 minutes) via Telegram commands  
✅ Simple Telegram Bot control interface  
✅ Powered by [NewsAPI](https://newsapi.org), [Telegram Bot API](https://core.telegram.org/bots/api), and [Twitter API v2](https://developer.twitter.com/)  
✅ Easily deployable on **Heroku** using GitHub integration  

---

## 🚀 Live Workflow

[Telegram Commands] → [Bot Scheduler] → [Fetch News] → [Post on X/Twitter]

yaml
Copy
Edit

---

## 🔧 Tech Stack

- **Python 3.11+**
- `python-telegram-bot`
- `tweepy`
- `schedule`
- `requests`
- `Heroku` + `Procfile`

---

## 📦 Setup Instructions

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/news-twitter-bot.git
cd news-twitter-bot
2. 🧪 Local Development (Optional)
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file:

env
Copy
Edit
TELEGRAM_TOKEN=your_telegram_bot_token
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_token_secret
NEWS_API_KEY=your_newsapi_key
Run locally:

bash
Copy
Edit
python bot.py
☁️ Heroku Deployment Guide
📁 Files to Have:
Ensure your repo has:

bot.py

config.py

news.py

Procfile

requirements.txt

runtime.txt

🚀 Deploy on Heroku
Go to Heroku Dashboard

Create a new app

Connect your GitHub repo

Go to Settings → Config Vars, add the following:

Key	Value
TELEGRAM_TOKEN	your Telegram bot token
TWITTER_API_KEY	your Twitter API key
TWITTER_API_SECRET	your Twitter API secret
TWITTER_ACCESS_TOKEN	your Twitter access token
TWITTER_ACCESS_SECRET	your Twitter access secret
NEWS_API_KEY	your NewsAPI key

Go to Resources, enable the Worker dyno

Done! Your bot is now live and tweeting 🚀

💬 Telegram Bot Commands
Command	Description
/start	Starts the bot and confirms it's active
/setinterval 60	Sets tweet interval to 60 minutes (customizable)

🛡️ Notes
Avoid hitting Twitter or NewsAPI rate limits by setting reasonable intervals (e.g., 30–60 mins)

Prevent duplicate tweets by caching article URLs (can be implemented in future updates)

You can extend to support categories, filters, multiple news sources, etc.
