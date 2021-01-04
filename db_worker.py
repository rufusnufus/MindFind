"""Script that does interaction with MongoDB in Atlas"""

import os
import pymongo


DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_NAME=os.environ.get("DB_NAME")


serv = (f"mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.vfsgh.mongodb.net/{DB_NAME}?"
        "retryWrites=true&w=majority")
client = pymongo.MongoClient(serv)
db = client[DB_NAME]

def check_and_add_user(user_id):
    """
    Checks whether user is present in DB or not by id. If not, adds user in DB
    Parameter:
        user_id: Telegram ID of the user
    """
    if db.users.find_one({'user_id': user_id}) is None:
        new_user = {
            'text_to_sticks': {},
            'user_id': user_id
        }
        db.users.insert_one(new_user)


def add_codeword(user_id, sticker_id, text):
    """
    Adds new text-sticker binding of specified user
    Parameters:
        user_id: Telegram ID of the user
        sticker_id: file_id of the Sticker in Telegram
        text: text that user entered as association
    """
    user = db.users.find_one({'user_id':user_id})
    if text in user['text_to_sticks']:
        user['text_to_sticks'][text].append(sticker_id)
    else:
        user['text_to_sticks'][text] = [sticker_id]
    db.users.update_one({'user_id':user_id}, {"$set": {"text_to_sticks": user['text_to_sticks']}})


def find_stickers(user_id, text):
    """
    Finds all stickers associated with specified text
    Parameters:
        user_id: Telegram ID of the user
        text: text that user entered as association to find sticker
    Returns:
        result: list of file_ids of all stickers with specified codeword
    """
    user = db.users.find_one({'user_id':user_id})
    result = user['text_to_sticks'][text]
    return result


def find_codewords(user_id):
    """
    Finds all codewords of the user
    Parameter:
        user_id: Telegram ID of the user
    Returns:
        result: list of all codewords
    """
    user = db.users.find_one({'user_id':user_id})
    result = user['text_to_sticks'].keys()
    return result
