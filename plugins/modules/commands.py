# Framework and Tools
from pyrogram import *
from pyrogram.types import *

# Bot
from plugins import app
from plugins.core import *

@app.on_message(filters.command("start") & filters.private)
async def startCommand(app: Client, m: Message):
    await startCmdCore(app, m)

@app.on_message(filters.command("id"))
async def idCommand(app: Client, m: Message):
    await idCmdCore(app, m)

@app.on_message(filters.forwarded & filters.private)
async def forwarded(app: Client, m: Message):
    await forwardedCmdCore(app, m)