from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes , ConversationHandler, MessageHandler, filters
from datetime import datetime, timedelta

PERIOD_LENGTH, CYCLE_LENGTH, LAST_DATE = range(3)
user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Welcome to HerDay period tracker.")
    await update.message.reply_text("Please answer a few questions to help personalise your experience.")
    await update.message.reply_text(
        "What's your period length?\n\n"
        "Please enter a number in days (Example :5)"
    )
    return PERIOD_LENGTH

async def period_length(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_data
    try:
        user_data["user_period_length"] = int(update.message.text)
    except:
        await update.message.reply_text("Please enter a numeric value")
        return PERIOD_LENGTH
    await update.message.reply_text(
        "What is your cycle length? (Days from the first day of your period to a day before the next period)\n\n"
        "Enter a number in days (Example: 28)")
    return CYCLE_LENGTH

async def cycle_length(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_data
    try:
        user_data["user_cycle_length"] = int(update.message.text)
    except:
        await update.message.reply_text("Please enter a numeric value")
    await update.message.reply_text(
        "When did your last period start?\n\n"
        "Please enter date in the format DD/MM/YYYY")
    return LAST_DATE

async def last_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_data
    user_data["user_last_date"] = str(update.message.text)
    await update.message.reply_text(
        "Here are your results\n\n"
        f"Period Length: {user_data['user_period_length']}\n"
        f"Cycle Length: {user_data['user_cycle_length']}\n"
        f"Last Period: {user_data['user_last_date']}\n")
    LD=datetime.strptime(user_data["user_last_date"], '%d/%m/%Y')
    user_data["next_period"]=LD+ timedelta(days= user_data['user_cycle_length'])
    NEXT_PERIOD=user_data["next_period"].strftime('%d/%m/%Y')
    await update.message.reply_text("Your next period date is expected to be on:")
    await update.message.reply_text(NEXT_PERIOD)
    user_data = {}
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thankyou for using HerDay!")
    return ConversationHandler.END

def main():
    print("HerDay is Online!")
    application = Application.builder().token("5846504367:AAExULz3yuXK_lhRKKKORvh6-bHPOMk3n5w").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PERIOD_LENGTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, period_length)],
            CYCLE_LENGTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, cycle_length)],
            LAST_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, last_date)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()