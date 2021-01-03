from aiogram import types
from aiogram.dispatcher import FSMContext
from decouple import config
from app import dp, bot

ADMIN_TELEGRAM_ID = config("ADMIN_ID")


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
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

