import requests
import pandas
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def check_the_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    items = city.split()
    print(items[1])
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={items[1]}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
    a = response.json()
    print(a)
    weather = a['weather'][0]['description']
    print(a['weather'][0]['description'])
    #print(a['main'][0]['temp'])
    #print(weather)
    #['main'][0]

    await update.message.reply_text(f'{weather}')
    #await update.message.reply_text(print(a['weather'][0]['description']))
