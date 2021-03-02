import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

PORT = int(os.environ.get('PORT', 5000))
TOKEN = "TELEGRAM_TOKEN_BOT"

# Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Messages

def message_handler(update: Update, context: CallbackContext) -> None:

    chat_id = update.message.chat_id
    message = update.message.text.lower()

    # You can find more information about attributes here: https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html

    if("hello" in message):
        update.bot.send_message(chat_id=chat_id, text=f"Hi there!")

# Commands

def start(update: Update, context: CallbackContext) -> None:

    user_first_name = update.message.from_user.first_name
    chat_id = update.message.chat_id

    update.bot.send_message(chat_id=chat_id, text=f"Hello, {user_first_name}!")

# Errors

def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"L'update {update} ha causato l'errore: {context.error}")

# Main

def main():

    # Initial steps
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    # Commands handler
    dispatcher.add_handler(CommandHandler("start", start)

    # Error Handler
    dispatcher.add_error_handler(error)

    # Starting the bot
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://APPNAME.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
