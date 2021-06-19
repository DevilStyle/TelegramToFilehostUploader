#!/usr/bin/env python3
# This is bot coded by DevilStyle and used for educational purposes only
# https://github.com/DevilStyle
# Copyright DevilStyle
# Thank you https://github.com/pyrogram/pyrogram

import pyrogram
from bot.filetocloud import CloudBot
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    CloudBot().run()

