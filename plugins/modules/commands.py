from plugins import app
from pyrogram import *
from pyrogram.types import *

@app.on_message(filters.command("start") & filters.private)
async def startCommand(app: Client, m: Message):
    text = "hi, can i help you?"
    await m.reply_text(text)