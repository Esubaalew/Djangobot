# bot/views.py

import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = "6836849964:AAEfW1ir-IHZKYgx7HO1uIxkf4Z9jidm27w"

# Initialize bot and application
bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).build()

# Asynchronous start command handler
async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm your bot.")

# Asynchronous echo message handler
async def echo(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Add handlers to the dispatcher
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        # Process the incoming update from Telegram
        update = Update.de_json(json.loads(request.body), bot)
        application.update_queue.put_nowait(update)
    return JsonResponse({"status": "ok"}, status=200)

# index
def index(request):
    return JsonResponse({"status": "ok"}, status=200)