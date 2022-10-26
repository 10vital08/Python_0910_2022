from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from bot_commands import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help!\n/complex')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 456
    complex_number_1 = complex(int(items[1]), int(items[2]))
    complex_number_2 = complex(int(items[4]), int(items[5]))
    operation = items[3]

    if operation == '+':
        string = str(complex_number_1) + ' + ' + str(complex_number_2) + ' = ' + str(complex_number_1 + complex_number_2)
    elif operation == '-':
        string = str(complex_number_1) + ' - ' + str(complex_number_2) + ' = ' + str(complex_number_1 - complex_number_2)
    elif operation == '*':
        string = str(complex_number_1) + ' * ' + str(complex_number_2) + ' = ' + str(complex_number_1 * complex_number_2)
    elif operation == '/':
        string = str(complex_number_1) + ' / ' + str(complex_number_2) + ' = ' + str(complex_number_1 / complex_number_2)
    else:
        string = 'Wrong data'
        print('Неправильно введен знак операции')

    await update.message.reply_text(f'{string}')
    