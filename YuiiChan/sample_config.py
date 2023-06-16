# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/YuiiChan/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27776767"
    API_HASH = "e7b0d8f7b037df9ff8b300816e90080b"
    API_KEY = "6038308153:AAHSpZ3aHzr0yQtVA4Uz5AoVUpuIPOrPr8M"
    OWNER_ID = "6044333279"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "kazumikazo"
    SUPPORT_CHAT = "@coldbloodnation"

    # RECOMMENDED

    SQLALCHEMY_DATABASE_URI = "postgres://cpdrwphc:LXuKxTftoPMnZ575JTP479F9Sf7f8XXg@tyke.db.elephantsql.com/cpdrwphc"  # needed for any database modules
    MESSAGE_DUMP = -1001848461536  # needed to make sure 'save from' messages persist
    GBAN_LOGS = -1001646756467
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = 1952067206 5007562506 1178572412("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 1952067206 5007562506 1178572412("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = 1952067206 5007562506 1178572412("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGER_USERS = 1952067206 5007562506 1178572412("elevated_users.json", "tigers")
    WHITELIST_USERS = 1952067206 5007562506 1178572412("elevated_users.json", "whitelists")
    DONATION_LINK = Https://t.me/kazumikazo  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = "awoo"
    TIME_API_KEY = "awoo"
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
