import telegram.ext

Token = "5842652460:AAE4dEbP0g6a0mC74CFqmiEk7Lm2PpqMDdY"

updater = telegram.ext.Updater("5842652460:AAE4dEbP0g6a0mC74CFqmiEk7Lm2PpqMDdY", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello")

