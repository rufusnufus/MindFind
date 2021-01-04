"""This script defines general commands for interaction with bot"""

import os
from aiogram import types
from bot import dp, bot, codeword_kb
from db_worker import check_and_add_user

ADMIN_TELEGRAM_ID = os.environ.get("ADMIN_ID")


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    check_and_add_user(message.from_user.id)
    answer = "Hi!\nAdd the codeword typing /add_codeword or pressing the button that has appeared💫"
    await message.reply(answer, reply_markup=codeword_kb)


@dp.message_handler(commands="help")
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    answer = ("<bold>What is this bot for?:</bold>\n\n"
            "Assign codewords for stickers you use to easily access them when you need.\n\n"
            "Using this bot allows you to get the sticker you want without leaving the chat "
            "and opening the bot separately. All you need is to type in the chat the codeword "
            "you chose! Do it this way:\n@MindFindBot write_your_codeword_here\n\n"
            "<bold>Usage:</bold>\n\n"
            "1. Add the codeword typing /add_codeword or pressing the button that has appeared💫\n"
            "2. See the list of all your codewords typing /codewords")
    await message.reply(answer, reply_markup=codeword_kb)


@dp.message_handler(commands="set_commands", state="*")
async def set_commands(message: types.Message):
    """
    This handler will be called by admin of the bot to set the commands
    """
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        commands = [types.BotCommand(command="/add_codeword", description="Add new codeword")]
        await bot.set_my_commands(commands)
        await message.answer("Commands are set.")
