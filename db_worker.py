"""Script that does interaction with MongoDB in Atlas"""
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_NAME=os.environ.get("DB_NAME")


serv = (f"mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.vfsgh.mongodb.net/{DB_NAME}?"
        "retryWrites=true&w=majority")
client = pymongo.MongoClient(serv)
db = client[DB_NAME]

def check_and_add_user(user_id):
    if db.users.find_one({'user_id': user_id}) == None:
        new_user = {
            'text_to_sticks': {},
            'user_id': user_id
        }
        db.users.insert_one(new_user)
    return

def add_assoc(user_id, sticker_id, text):
    print(type(sticker_id))
    print(type(text))
    user = db.users.find_one({'user_id':user_id})
    if text in user['text_to_sticks']:
        user['text_to_sticks'][text].append(sticker_id)
    else:
        user['text_to_sticks'][text] = [sticker_id]
    db.users.update_one({'user_id':user_id}, {"$set": {"text_to_sticks": user['text_to_sticks']}})

def find_stickers(user_id, text):
    user = db.users.find_one({'user_id':user_id})
    return user['text_to_sticks'][text]
