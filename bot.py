"""This script defines Bot object, Dispatcher object and Memory for monitoring the states"""

import logging
import os
import pymongo
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


load_dotenv()

API_TOKEN=os.environ.get("API_TOKEN")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_NAME=os.environ.get("DB_NAME")


bot = Bot(token=API_TOKEN, parse_mode="HTML")
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.DEBUG)

serv = (f"mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.vfsgh.mongodb.net/{DB_NAME}?"
        "retryWrites=true&w=majority")
client = pymongo.MongoClient(serv)
db = client[DB_NAME]
