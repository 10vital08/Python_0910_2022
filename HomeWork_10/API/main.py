from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from weather import *

# Создание объекта бот
app = ApplicationBuilder().token("5754059861:AAHyA5F2agLPYC-SpWC6cybcTVqtAesMsqY").build()

# Регистрация обработчика на текстовые сообщения,
app.add_handler(CommandHandler("weather", check_the_weather))

print('server start')
app.run_polling()