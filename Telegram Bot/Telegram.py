from telegram import Bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
token = "5860671160:AAFU7Ww3E8K4xsw6_tssoYrLfgJWcRctB5A"

updater = Updater("5860671160:AAFU7Ww3E8K4xsw6_tssoYrLfgJWcRctB5A",use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("WELCOME..! To The vaccine Registration Bot, Book Your Vaccination Dose Slot here.")
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    print("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))
    Bot.sendMessage(chat_id, 'text')

start_command = CommandHandler('start',start)
updater.dispatcher.add_handler(start_command)
updater.start_polling()
updater.idle()