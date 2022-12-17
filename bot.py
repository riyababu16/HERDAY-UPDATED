from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to HERDAY Period Tracker!")


app = ApplicationBuilder().token("5846504367:AAExULz3yuXK_lhRKKKORvh6-bHPOMk3n5w").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("Start",start))

app.run_polling()