from aiogram import types
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
import os
from bot import dp, bot
from db_worker import check_and_add_user

ADMIN_TELEGRAM_ID = os.environ.get("ADMIN_ID")


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    check_and_add_user(message.from_user.id)
    await message.reply("Hi!\nHere you can create associations between phrases and stickers.\nTo start send me association first, then sticker that is suitable.")


@dp.message_handler(commands="set_commands", state="*")
async def set_commands(message: types.Message):
    """
    This handler will be called by admin of the bot to set the commands
    """
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        commands = [types.BotCommand(command="/add_association", description="Add new association")]
        await bot.set_my_commands(commands)
        await message.answer("Commands are set.")

