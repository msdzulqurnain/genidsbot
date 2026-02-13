# Framework and Tools
from pyrogram.enums import ChatType

async def idCmdCore(app, m):
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