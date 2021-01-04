"""This script defines general commands for interaction with bot"""

import os
from aiogram import types
from bot import dp, bot, assoc_kb
from db_worker import check_and_add_user

ADMIN_TELEGRAM_ID = os.environ.get("ADMIN_ID")


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    check_and_add_user(message.from_user.id)
    answer = ("Hi!\nСreate your association here.\nAdd the association tapping "
            "/add_association or pressing the button that has appeared")
    await message.reply(answer, reply_markup=assoc_kb)


@dp.message_handler(commands="help")
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    answer = ("You can add word/phrase -> sticker associations by /add_association command or button below.\n"
            "Afterwards you can use this bot in inline mode to send stickers fast instead of searching them.\n"
            "Example of using in inline mode: @MindFindBot text_association")
    await message.reply(answer, reply_markup=assoc_kb)


@dp.message_handler(commands="set_commands", state="*")
async def set_commands(message: types.Message):
    """
    This handler will be called by admin of the bot to set the commands
    """
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        commands = [types.BotCommand(command="/add_association", description="Add new association")]
        await bot.set_my_commands(commands)
        await message.answer("Commands are set.")
