from bot_commands import *

# Создание объекта бот
app = ApplicationBuilder().token("5688069639:AAHOTQsWYMD_0K9GmPCpAOg0-YGaGtO0KiY").build()

# Регистрация обработчиков на текстовые сообщения,
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("complex", complex_command))
app.add_handler(CommandHandler("rational", rational_number))

print('server start')
app.run_polling()