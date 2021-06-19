#!/usr/bin/env python3
# This is bot coded by DevilStyle and used for educational purposes only
# https://github.com/DevilStyle
# Copyright DevilStyle
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():
    upload_selection = [
        [
            InlineKeyboardButton(
                "transfer.sh",
                callback_data="transfersh"
            ),
            InlineKeyboardButton(
                "File.io",
                callback_data="File.io"
            )
        ],
        [
            InlineKeyboardButton(
                "gofile.io",
                callback_data="gofileio"
            ),
            InlineKeyboardButton(
                "anonymfiles.com",
                callback_data="anonymfiles"
            )
        ]
    ]
    return InlineKeyboardMarkup(upload_selection)


def completedKeyboard(dl):
    replayMarkup = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "DOWNLOAD URL",
                url=f"{dl}"
            )
        ],
            [
            InlineKeyboardButton(
                "DONATE",
                url=""
            )
        ]])

    return replayMarkup
