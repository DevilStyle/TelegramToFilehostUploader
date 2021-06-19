
from pyrogram import *
import datetime
from bot import (
    BOT_TOKEN,
    APP_ID,
    API_HASH,
    LOGGER
)

class CloudBot(Client):

    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            }
        )

    async def start(self):
        await super().start()
        LOGGER.info(f"BOT AVVIATO {datetime.datetime.now()}")
        print(f"BOT AVVIATO ")

    async def stop(self, *args):
        LOGGER.info(f"BOT FERMATO {datetime.datetime.now()}")
        await super().stop()
