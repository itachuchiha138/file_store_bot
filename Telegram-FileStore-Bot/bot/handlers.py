from pyrogram import filters
from pyrogram.types import Message
from .database import save_file, get_file
from . import bot

def register_handlers(bot):
    @bot.on_message(filters.command("start"))
    def start(client, message: Message):
        message.reply_text("Hello! Send me any file, and I'll store it for you.")

    @bot.on_message(filters.document | filters.video | filters.audio | filters.photo)
    def save_file_handler(client, message: Message):
        file_id = message.document.file_id if message.document else message.video.file_id if message.video else message.audio.file_id if message.audio else message.photo.file_id
        file_name = message.document.file_name if message.document else "No Name"
        
        save_file(file_id, file_name, message.from_user.id)
        message.reply_text(f"File saved! Use /get {file_id} to retrieve it.")

    @bot.on_message(filters.command("get"))
    def get_file_handler(client, message: Message):
        args = message.text.split()
        if len(args) < 2:
            message.reply_text("Usage: /get <file_id>")
            return
        
        file_data = get_file(args[1])
        if file_data:
            client.send_document(chat_id=message.chat.id, document=file_data["file_id"], caption=file_data["file_name"])
        else:
            message.reply_text("File not found!")
