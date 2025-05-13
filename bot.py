import logging, asyncio, schedule, time
import tweepy
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import *
from news import get_latest_news
import logging

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Twitter API Setup
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
twitter_api = tweepy.API(auth)

# Globals
tweet_interval = 3600  # Default: 1 hour

# Logging
logging.basicConfig(level=logging.INFO)

# Telegram Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 News Bot is running! Use /setinterval <minutes> to change post frequency.")

async def set_interval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global tweet_interval
    try:
        mins = int(context.args[0])
        tweet_interval = mins * 60
        await update.message.reply_text(f"⏰ Tweet interval set to {mins} minutes.")
    except:
        await update.message.reply_text("⚠️ Invalid input. Use `/setinterval 60`")

def post_news():
    news = get_latest_news()
    if news:
        try:
            twitter_api.update_status(news)
            print("✅ Tweeted:", news)
        except Exception as e:
            print("❌ Tweet error:", e)

# Background job runner
async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setinterval", set_interval))

    schedule.every(tweet_interval).seconds.do(post_news)

    async with application:
        await asyncio.gather(application.start(), scheduler())

if __name__ == '__main__':
    asyncio.run(main())
