import telegram.ext
from telegram import Update
from telegram.ext import CommandHandler,ContextTypes

Token="5842652460:AAE4dEbP0g6a0mC74CFqmiEk7Lm2PpqMDdY"

updater=telegram.ext.Updater("5842652460:AAE4dEbP0g6a0mC74CFqmiEk7Lm2PpqMDdY", update_queue=True)
dispatcher=

def start(update,context):
    update.message.reply_text("HELLO! Welcome to HERDAY.\n We are herte to help you track your menstruation cycle\n Please answer a few questions to help personalise your experience")

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))

updater.start_polling()
updater.idle()