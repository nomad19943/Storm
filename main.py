from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = f"""
<b>Новый торговый сигнал</b>

<b>Актив:</b> {data.get("symbol", "Не указан")}
<b>Тип ордера:</b> {data.get("order_type", "Не указан")}
<b>Направление:</b> {data.get("direction", "Не указано")}
<b>Цена входа:</b> {data.get("entry", "–")}
<b>Stop Loss:</b> {data.get("sl", "–")}
<b>Take Profit:</b> {data.get("tp", "–")}
<b>Плечо:</b> x{data.get("leverage", "–")}
<b>Уверенность:</b> {data.get("confidence", "–")}%
<b>Сумма входа:</b> {data.get("amount", "–")} TON
"""
    send_telegram_message(message.strip())
    return {"status": "ok"}, 200
