from telegram import Updater

TELEGRAM_TOKEN = "INSERT_YOUR_TOKEN_HERE"

updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher

def echo(bot, update):
  message_text = update.message.text
  chat_id = update.message.chat_id

  bot.sendMessage(chat_id=chat_id, text=message_text)


dispatcher.addTelegramMessageHandler(echo)
updater.start_polling
