from telegram.ext import Updater
from bot.message_handler import handle_message
from config.settings import TELEGRAM_BOT_TOKEN

def start_bot():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()