
async def startCmdCore(app, m):
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