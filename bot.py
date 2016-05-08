from telegram.ext import Updater
from telegram.ext import CommandHandler

TELEGRAM_TOKEN = "130757743:AAGbbBfXDNGnmpYqvbfC4-mXlDcD1V4i2tQ"

updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher

def echo(bot, update):
  message_text = update.message.text
  chat_id = update.message.chat_id

  bot.sendMessage(chat_id=chat_id, text=message_text)

echo_handler = CommandHandler('', echo)
dispatcher.addHandler(echo_handler)
updater.start_polling()
