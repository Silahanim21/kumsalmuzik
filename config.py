import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21194358"))
API_HASH = getenv("API_HASH", "9623f07eca023e4e3c561c966513a642")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7563580567:AAHdItwB78m3OBWJ8SdbfpiRv5TWQMO0h7k")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:DLArCT171SF9wRKJ@alexsoza.xpoqv.mongodb.net/?retryWrites=true&w=majority&appName=Alexsoza")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002065943011"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7268753735"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Meyit47zade/MYTGRUPBOT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeceSohbettr")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFDZnYAft8X7GUG1Hzvbk_iiVKhaDMrafD4AT_TkglkxsYMcB88b2EMqZxj-5B3pa-3BdIOIwjE2kofB0yh0MDiFgUHXNfiKj7csV-NfWfmVk1Fghov2j5rFdT-_1xcg28ECKxjvLsnDx1U2dlH9mBgSnWF9aVNrD9vM8yJkoEQ18ZzZe5FDd_tcO0oPVoBrKgFI6-vZt6jJY4RsZFKDSX0hOCCqjLhuZlJ4uT0bNCSghE_tKxp0Vqc6tVRDNdUNdFQOQgJF4Txu2SzjbvVjR29PpQ3WgPTSUaILRt8w2Bdc9yBVbtEm1oAb_b1EKfesgrCLxorkPjWqhVbicepUeo63XoqogAAAAG17kjxAA")
STRING2 = getenv("STRING_SESSION2", "BAE6FqgArsjPO0POHPvXUYKiobN_8ZPb43cyxZRziCXbm5X1obHqzbJtlY57ZFGYodLNfk4XtH9xtzO-JF8tmivw3ofGOsenetSxqCjtr1nCh5xjJnDLACFYgbSLbQE2qNBKinkGE8iJGkd2kuqT8F2PVnDW7T-IGWt1y0g7UjVfxQMAI9GksZ1xbqydczjJ-WEhn88C51LFRp9DJhpkeBWJK3PXjc8UPQ1IqUcDvlKIo17wUOAL7oUj3xKO48X0xz7DrDkjMaRDbWW0-Cfg35gwKZWUvoRTx2YLtZNUs0iih_5TnuhiySzP55iGpXY5WoHzmfC0Mzj1Tes-XFhQo_vRFnANKgAAAAG9qjszAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/869297aef3b5dd030ea33.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/869297aef3b5dd030ea33.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
STATS_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
STREAM_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/869297aef3b5dd030ea33.jpg "


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
