<<<<<<< HEAD
import yfinance as yf
from telegram import Bot
import schedule
import time

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"

bot = Bot(token=TOKEN)

def mercado():

    sp500 = yf.Ticker("^GSPC").history(period="1d")["Close"].iloc[-1]
    nasdaq = yf.Ticker("^IXIC").history(period="1d")["Close"].iloc[-1]
    dow = yf.Ticker("^DJI").history(period="1d")["Close"].iloc[-1]

    oil = yf.Ticker("CL=F").history(period="1d")["Close"].iloc[-1]
    gold = yf.Ticker("GC=F").history(period="1d")["Close"].iloc[-1]

    btc = yf.Ticker("BTC-USD").history(period="1d")["Close"].iloc[-1]

    mensaje = f"""
🌎 GLOBAL MARKET REPORT

📊 INDICES
S&P500: {sp500}
Nasdaq: {nasdaq}
Dow Jones: {dow}

🛢 PETRÓLEO WTI
{oil}

🥇 ORO
{gold}

₿ BITCOIN
{btc}

Buen día Miguel.
"""

    bot.send_message(chat_id=CHAT_ID, text=mensaje)

schedule.every().day.at("08:00").do(mercado)

while True:
    schedule.run_pending()
=======
import yfinance as yf
from telegram import Bot
import schedule
import time

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"

bot = Bot(token=TOKEN)

def mercado():

    sp500 = yf.Ticker("^GSPC").history(period="1d")["Close"].iloc[-1]
    nasdaq = yf.Ticker("^IXIC").history(period="1d")["Close"].iloc[-1]
    dow = yf.Ticker("^DJI").history(period="1d")["Close"].iloc[-1]

    oil = yf.Ticker("CL=F").history(period="1d")["Close"].iloc[-1]
    gold = yf.Ticker("GC=F").history(period="1d")["Close"].iloc[-1]

    btc = yf.Ticker("BTC-USD").history(period="1d")["Close"].iloc[-1]

    mensaje = f"""
🌎 GLOBAL MARKET REPORT

📊 INDICES
S&P500: {sp500}
Nasdaq: {nasdaq}
Dow Jones: {dow}

🛢 PETRÓLEO WTI
{oil}

🥇 ORO
{gold}

₿ BITCOIN
{btc}

Buen día Miguel.
"""

    bot.send_message(chat_id=CHAT_ID, text=mensaje)

schedule.every().day.at("08:00").do(mercado)

while True:
    schedule.run_pending()
>>>>>>> c81f0ab789ce49d7d397815cd3849230d457671a
    time.sleep(60)