from plugins import app
from pyrogram import *
from pyrogram.types import *

# Help Callback
@app.on_callback_query(filters.regex("help"))
async def help_cb(app: Client, query: CallbackQuery):
    text = 'hi, this is callback help'
    await query.message.edit_text(text)

# Debug Callback Checker
@app.on_callback_query()
async def debug_callback(client, callback_query):
    print("Callback received:", callback_query.data)