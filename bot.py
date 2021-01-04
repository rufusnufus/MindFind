"""This script defines Bot object, Dispatcher object and Memory for monitoring the states"""

import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

API_TOKEN=os.environ.get("API_TOKEN")


bot = Bot(token=API_TOKEN, parse_mode="HTML")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.DEBUG)

button_assoc = KeyboardButton("Add association 😉")
assoc_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_assoc)