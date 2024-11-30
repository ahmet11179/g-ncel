import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "27606753")) #ASİSTAN APİ İD
API_HASH = getenv("API_HASH", "b060babef6dd4a784ea36ac9a3387de1") #ASİSTAN APİ HASH
BOT_TOKEN = getenv("BOT_TOKEN", "7922147139:AAGaDkmCpHUa7Ry29bb0eefXIBIsqHAnNvI") #BOT TOKEN
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sonsuzmango:sonsuz@sonsuz.plikp.mongodb.net/?retryWrites=true&w=majority&appName=Sonsuz")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002292728756")) #LOG GRUBU İD'Sİ -100 İLE BAŞLAMALI
OWNER_ID = int(getenv("OWNER_ID", 7730275029)) #OWNER İD
SAHİB= getenv("SAHİB", "https://t.me/Cankabusower") #OWNER KULLANICI ADI 
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AHMET1346z/karars-z", #REPO LİNKİ
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sonsuzduyuru") #DESTEK KANALI LİNKİ
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sonsuzmuzikdestek") #DESTEK GRUBU LİNKİ
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
STRING1 = getenv("STRING_SESSION", "AQGlPuEAPJZUjJ1ckPntWArM9dAefXxApOUkCS6YTJmFmnzbZ3wFTbFH8dexDmNhivTVjaajqxJux_dcqpprP4I760ban-MKutoh-ohDesiEfgjUDeeay-uE8Us3zpMVWeJc_-3PB9rew8HBeEErgmEnR90MV5D-GJRF45wuHQxizQOBSG_aom3m9Gn3LGXdiK4ZjTP93hVJmZnWg0jxH4422jhRUKKGTP--mRkz5MR58oTPRVu4dUp5uegGc4a7N86og9TOYiFCuZheoD85MtsnmlvoA4IC_tv6EFcj6g5V8trb49EEjox26rVoTPO2hwe_Lq18bjK6xp-YnHvxIfU_yKz1hQAAAAHiXvUSAA") #ASİSTAN SESSİON
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/b79290e357a600dc3ab43.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/b79290e357a600dc3ab43.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
