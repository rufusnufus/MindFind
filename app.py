#!venv/bin/python
import logging
import pymongo
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
# from decouple import config
from dotenv import load_dotenv
import os
import handlers

load_dotenv()

API_TOKEN=os.environ.get("API_TOKEN")
# DB_USER=os.environ.get("DB_USER")
# DB_PASS=os.environ.get("DB_PASS")
# DB_NAME=os.environ.get("DB_NAME")


logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN, parse_mode="HTML")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Hi!")

# client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.vfsgh.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
# db = client[DB_NAME]


# @dp.message_handler(chat_type=types.ChatType.PRIVATE, content_types=types.ContentTypes.STICKER)
# async def echo(message: types.Message):
#     """
#     This handler will be called whenever any sticker is sent.
#     """
#     await message.answer(f"Sticker ID\n <code>{message.sticker.file_id}</code>")

# @dp.inline_handler()
# async def inline_echo(inline_query: InlineQuery):
#     # id affects both preview and content,
#     # so it has to be unique for each result
#     # (Unique identifier for this result, 1-64 Bytes)
#     # you can set your unique id's
#     # but for example i'll generate it based on text because I know, that
#     # only text will be passed in this example
#     text = inline_query.query or 'echo'
#     input_content = InputTextMessageContent(text)
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     item = InlineQueryResultArticle(
#         id=result_id,
#         title=f'Result {text!r}',
#         input_message_content=input_content,
#     )
#     # don't forget to set cache_time=1 for testing (default is 300s or 5m)
#     await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)