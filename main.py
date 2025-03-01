import logging
import os
import requests

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ApplicationBuilder, MessageHandler, filters
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get bot token from environment variables
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError('Please set the TELEGRAM_BOT_TOKEN environment variable')



def get_joke():
    site_link = "https://icanhazdadjoke.com/"
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Telegram Bot (https://github.com/ianburke/telegram-bot-fly-io-starter)'
    }
    
    try:
        response = requests.get(site_link, headers=headers)
        if response.status_code == 200:
            joke_data = response.json()
            joke_text = joke_data['joke']
            return joke_text
    except Exception as e:
        logging.error(f"Error fetching joke: {e}")
    return "Sorry, I couldn't fetch a joke right now!"

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.warning(f'Got message from {update.effective_chat.username}')
    joke_text = get_joke()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=joke_text)



# Bot command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    welcome_message = "👋 Hello! I'm your friendly Telegram bot. Try these commands:\n" \
                     "/start - Show this welcome message\n" \
                     "/joke - Get a friendly greeting"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle non-command messages"""
    user_message = update.message.text
    response = f"You said: {user_message}\nI'm a bot and still learning how to chat! Try /start or /joke commands."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == '__main__':
    try:
        application = ApplicationBuilder().token(TOKEN).build()
    except:
        raise ValueError('Please, set environment var TELEGRAM_BOT_TOKEN with your bot token')

    # Bot command handlers
    start_handler = CommandHandler('start', start)
    joke_handler = CommandHandler('joke', joke)
    
    
    # handle non-command messages
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    

    # add handlers to the application
    application.add_handler(start_handler)
    application.add_handler(joke_handler)
    application.add_handler(message_handler)

    # run the bot
    print("Bot is starting...")
    application.run_polling()