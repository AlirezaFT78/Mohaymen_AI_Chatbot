import os
import requests
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters
)

load_dotenv(override=True)

API_URL = os.getenv("API_URL") if os.getenv("API_URL") else os.getenv("FASTAPI_URL")  
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        response = requests.post(API_URL, json={"query": user_input}, timeout=10)
        response.raise_for_status()
        answer = response.json().get("answer", "خطایی رخ داده است.")
    except requests.exceptions.Timeout:
        answer = "⏱️ زمان پاسخ‌گویی به پایان رسید. لطفاً دوباره تلاش کنید."
    except requests.exceptions.RequestException as e:
        answer = f"❌ خطا در ارتباط با سرور: {str(e)}"
        
    await update.message.reply_text(answer)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من دستیار منابع انسانی مهیمن هستم. لطفا سوال خود را بپرسید.")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
    
if __name__ == "__main__":
    run_bot()