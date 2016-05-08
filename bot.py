from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import config

updater = Updater(token=config.telegram['token'])

dispatcher = updater.dispatcher

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="Welcome to PickAPlaceBot!");

def echo(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler([Filters.text], echo)
start_handler = CommandHandler('start', start)
dispatcher.addHandler(start_handler)
dispatcher.addHandler(echo_handler)
updater.start_polling()
