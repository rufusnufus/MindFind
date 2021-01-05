# MindFind
Assign codewords for stickers you use to easily access them when you need in Telegram.
Demo: [@MindFindBot](https://t.me/MindFindBot)

## What you should do to run the application locally
1. You need to install [Docker](https://www.docker.com/):
2. `git clone https://github.com/rufusnufus/MindFind`
3. `cd MindFind`
4. This command creates an image for this project
```bash
sudo docker build -t app .
```
5. This command runs the application in the background
```bash
sudo docker run -d --env-file .env app
```

### Variables in .env file need to be specified:
* API_TOKEN - API token of the bot given by [@BotFather in Telegram](https://t.me/BotFather)
* DB_USER - MongoDB username to access your cluster on [Atlas](https://www.mongodb.com/cloud/atlas)
* DB_PASS - MongoDB password to access your cluster on [Atlas](https://www.mongodb.com/cloud/atlas)
* DB_NAME - database name
* ADMIN_ID - Telegram ID of the bot owner

## Support
Write to [@rufusnufus](https://t.me/rufusnufus) if you have any questions.
