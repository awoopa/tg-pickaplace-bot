from telegram import Updater
import config

updater = Updater(token=config.telegram['token'])
dispatcher = updater.dispatcher


def echo(bot, update):
  message_text = update.message.text
  chat_id = update.message.chat_id

  bot.sendMessage(chat_id=chat_id, text=message_text)


dispatcher.addTelegramMessageHandler(echo)
updater.start_polling
