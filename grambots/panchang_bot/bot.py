import json
import os
from argparse import ArgumentParser

from telegram import Bot


def main(pred_path: str):
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    bot = Bot(token=TELEGRAM_TOKEN)
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    with open(pred_path, "r") as f:
        predictions = json.load(f)
        for p in predictions:
            msg = f"{p['title']}\n\n{p['prediction']}"
            bot.send_message(chat_id=chat_id, text=msg)


if __name__ == "__main__":
    parser = ArgumentParser("Panchang Telegram bot")
    parser.add_argument("pred_json_path", type=str)

    args, _ = parser.parse_known_args()

    main(pred_path=args.pred_json_path)
