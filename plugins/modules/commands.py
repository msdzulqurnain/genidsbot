from plugins import app
from pyrogram import *
from pyrogram.types import *

@app.on_message(filters.command("start") & filters.private)
async def startCommand(app: Client, m: Message):
    text = """
<b>Your Id :</b> <code>{}</code>
<b>Chat Id :</b> <code>{}</code>
"""
    await m.reply_text(
        text.format(
            m.from_user.id,
            m.chat.id
        )
    )