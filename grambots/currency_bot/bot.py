from telegram import Bot
import requests

TELEGRAM_TOKEN = "<TELEGRAM_TOKEN>"
bot = Bot(token=TELEGRAM_TOKEN)
eur_to_inr_chat_id = 123456


exchange_rate_url = "https://api.exchangerate.host/latest?symbols=EUR,INR"
response = requests.get(exchange_rate_url)
data = response.json()
exchange_rate = round(data["rates"]["INR"], 2)

msg_text = f"1 EUR = {exchange_rate} INR"


bot.send_message(chat_id=eur_to_inr_chat_id, text=msg_text)
