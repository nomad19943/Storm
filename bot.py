
import os
from fastapi import FastAPI, Request
import httpx

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.post("/")
async def send_signal(request: Request):
    data = await request.json()
    message = f"📈 TradingView Signal\nSymbol: {data.get('symbol')}\nAction: {data.get('action')}\nEntry: {data.get('entry')}\nSL: {data.get('sl')}\nTP: {data.get('tp')}\nLeverage: {data.get('leverage')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)
    return {"status": "sent"}
@app.get("/")
def home():
    return {"status": "online"}
