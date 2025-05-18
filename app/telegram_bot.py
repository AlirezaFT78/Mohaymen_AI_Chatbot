import os
import requests
import asyncio
from dotenv import load_dotenv
from telegram import Update
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
        response = requests.post(API_URL, json={"query": user_input})
        answer = response.json().get("answer", "خطایی رخ داده است.")
    except Exception as e:
        answer = f"مشکلی پیش آمد: {str(e)}"

    await update.message.reply_text(answer)

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
    
    
    
if __name__ == "__main__":
    run_bot()