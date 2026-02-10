import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#---------- ---------- ---------- ----------
from pyrogram import *
from pyromod import listen
from plugins.config import API_ID, API_HASH, TOKEN

class app(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=TOKEN, 
            plugins={
                "root": "plugins/modules"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.LOGGER(__name__).info(f"{me.first_name} {me.last_name or ''} | @{me.username}  started!")
        self.LOGGER(__name__).info("Created by </DZ C0DE> | https://t.me/DZC0de")
        self.bot_details = me

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
