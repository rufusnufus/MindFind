# MindFind
Assign codewords for stickers you use to easily access them when you need in Telegram.
Demo: [@MindFindBot](https://t.me/MindFindBot)

### Installation:
1. `git clone https://github.com/rufusnufus/MindFind`
2. `cd MindFind`
3. `source venv/bin/python`
4. `pip install -r requirements.txt`
5. `chmod +x start.py`

### Variables in .env file need to be specified:
* API_TOKEN - API token of the bot given by [@BotFather in Telegram](https://t.me/BotFather)
* DB_USER - MongoDB username to access your cluster on [Atlas](https://www.mongodb.com/cloud/atlas)
* DB_PASS - MongoDB password to access your cluster on [Atlas](https://www.mongodb.com/cloud/atlas)
* DB_NAME - database name
* ADMIN_ID - Telegram ID of the bot owner
