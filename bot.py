"""This script defines Bot object, Dispatcher object and Memory for monitoring the states"""

import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db_worker import db

API_TOKEN=os.environ.get("API_TOKEN")


bot = Bot(token=API_TOKEN, parse_mode="HTML")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.DEBUG)
