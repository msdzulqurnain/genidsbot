

async def forwardedCmdCore(app, m):
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