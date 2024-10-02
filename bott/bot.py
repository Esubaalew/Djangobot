from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from os import getenv
import logging
from telegram import Update
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command"""
    await update.message.reply_text("Hey Welcome!!")


async def bot_tele(text):
    # Create application
    application = (
        Application.builder().token(os.getenv('TOKEN')).build()
    )

    
    # Register handlers
    application.add_handler(CommandHandler("start", start))

    # Start application
    await application.bot.set_webhook(url=os.getenv('webhook'))
    await application.update_queue.put(
        Update.de_json(data=text, bot=application.bot)
    )
    async with application:
        await application.start()
        await application.stop()
