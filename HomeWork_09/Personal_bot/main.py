# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

app = ApplicationBuilder().token("5688069639:AAHOTQsWYMD_0K9GmPCpAOg0-YGaGtO0KiY").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("complex", complex_command))

print('server start')
app.run_polling()