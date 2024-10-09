import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8050915888:AAHn-idxXQ_21LSeN9Nk7J4GLSxkFrAUQ44")
API_ID = int(os.environ.get("API_ID", "22768311"))
API_HASH = os.environ.get("API_HASH", "702d8884f48b-42e865425391432b3794")


OWNER_ID = int(os.environ.get("OWNER_ID", "6040503076"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://imh203356:qsc6pCJ6z6jaTrVP@cluster0.fisr5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "imh203356")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002436399053"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001999825163"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot of @CrunchyRollOfficialChannel !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI am A File Sharing Bot Of @CrunchyRollOfficialChannel.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Devil Developer 
# Don't Remove Credit 🥺
# Telegram Channel @CrunchyRollOfficialChannel
# Backup Channel @CrunchyRollOfficialChannel
# Developer @IamRealDevil
