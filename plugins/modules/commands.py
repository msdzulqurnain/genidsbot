from plugins import app
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import ChatType

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

@app.on_message(filters.command("id"))
async def idCommand(app: Client, m: Message):
    text = """
<b>Your Id :</b> <code>{}</code>
<b>Chat Id :</b> <code>{}</code>
"""
    textChannel = """
<b>Chat Id :</b> <code>{}</code>
"""
    textChannel2 = """
<b>Reply details 🔱

<b>Chat Id :</b> <code>{}</code>
<b>Replied Msg Id :</b> <code>{}</code>"""
    textGroup = """
<b>Your Id :</b> <code>{}</code>
<b>Chat Id :</b> <code>{}</code>
"""
    textGroup2 = """
<b>Reply details 🔱

Replied User Id :</b> <code>{}</code>
<b>Replied Msg Id :</b> <code>{}</code>
<b>Chat Id :</b> <code>{}</code>
<b>Your Id :</b> <code>{}</code>"""
    if m.chat.type == ChatType.CHANNEL:
        if m.reply_to_message:
            chat_id = m.chat.id
            replied_msg = m.reply_to_message.id
            await m.reply_text(
                textChannel2.format(
                    chat_id,
                    replied_msg
                )
            )
        else:
            chat_id = m.chat.id
            await m.reply_text(
                textChannel.format(
                    chat_id
                )
            )
    elif m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        if m.reply_to_message:
            replied_user = m.reply_to_message.from_user.id
            replied_msg = m.reply_to_message.id
            chat_id = m.chat.id
            from_user = m.from_user.id
            await m.reply_text(
                textGroup2.format(
                    replied_user,
                    replied_msg,
                    chat_id,
                    from_user
                )
            )
        else:
            chat_id = m.chat.id
            from_user = m.from_user.id
            await m.reply_text(
                textGroup.format(
                    from_user,
                    chat_id
                )
            )
    else:
        if m.reply_to_message:
            replied_user = m.reply_to_message.from_user.id
            replied_msg = m.reply_to_message.id
            chat_id = m.chat.id
            from_user = m.from_user.id
            await m.reply_text(
                textGroup2.format(
                    replied_user,
                    replied_msg,
                    chat_id,
                    from_user
                )
            )
        else:
            chat_id = m.chat.id
            from_user = m.from_user.id
            await m.reply_text(
                text.format(
                    from_user,
                    chat_id
                )
            )

@app.on_message(filters.forwarded & filters.private)
async def forwarded(app: Client, m: Message):
    forward = """
<b>Forward details 🔱

Forwarded User Id :</b> <code>{}</code>
<b>Forwarded DC id :</b> <code>{}</code>
<b>Your Id :</b> <code>{}</code>"""
    forward2 = """
<b>Forward details 🔱

Forwarded Chat Title :</b> {}
<b>Forwarded Chat Id :</b> <code>{}</code>
<b>Forwarded Msg Id :</b> <code>{}</code>
<b>Forwarded DC id :</b> <code>{}</code>
<b>Your Id :</b> <code>{}</code>"""
    if m.forward_from:
        chat_id = m.forward_from.id
        user_id = m.from_user.id
        dc_id = m.forward_from.dc_id
        await m.reply_text(
            forward.format(
                chat_id,
                dc_id,
                user_id
            )
        )
    elif m.forward_from_chat:
        forward_chat_title = m.forward_from_chat.title 
        forward_chat_id = m.forward_from_chat.id
        forward_msg = m.forward_from_message_id
        forward_dc_id = m.forward_from_chat.dc_id
        user_id = m.from_user.id
        await m.reply_text(
            forward2.format(
                forward_chat_title,
                forward_chat_id,
                forward_msg,
                forward_dc_id,
                user_id
            )
        )
    else:
        await m.reply_text("<b>Cannot get ID from hidden account🥷🏻</b>")