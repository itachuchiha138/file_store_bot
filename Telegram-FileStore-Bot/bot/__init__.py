import os
from pyrogram import Client
from .config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "FileStoreBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def start_bot():
    from .handlers import register_handlers
    register_handlers(bot)
    print("Bot is running...")
    bot.run()
