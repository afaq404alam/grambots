import json
import os

from telegram import Bot

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

with open("pred.json", "r") as f:
    predictions = json.load(f)
    for p in predictions:
        msg = f"{p['title']}\n\n{p['prediction']}"
        bot.send_message(chat_id=chat_id, text=msg)
