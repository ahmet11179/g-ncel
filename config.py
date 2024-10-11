import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "26400244")) #ASİSTAN APİ İD
API_HASH = getenv("API_HASH", "5e69daaa3668a56fe9b72319b280c071") #ASİSTAN APİ HASH
BOT_TOKEN = getenv("BOT_TOKEN", "7581401865:AAEZWnrp0M_3igJOALSJ2eHET3JsQiw51xA") #BOT TOKEN
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ahmetcanyaman495:ahmetcanyaman495@cluster0.4ltto.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002478218038")) #LOG GRUBU İD'Sİ -100 İLE BAŞLAMALI
OWNER_ID = int(getenv("OWNER_ID", 7730275029)) #OWNER İD
SAHİB= getenv("SAHİB", "https://t.me/Cankabusunefendisii") #OWNER KULLANICI ADI 
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
STRING1 = getenv("STRING_SESSION", "BAHHpwsAw_FdhSM0VaLPdcuMC4r7i0nBneJ53wcSEwER7LYo3zu_IGoizDBkBrzlrdWc3TeEnayRtbmv61oiFwNNoDaWiBztKZHHoFBaCgUFr3yNWoStvRYAbFMvF0Cd9r_pVLoa2V7LJAlE6EHqNPPF1ub_1PZaZjuEClZSbuLcn7yHHBQ-umkNJkT8AxAa0tMuUfzyDo_kxquqP-LhYlLhqmlORKjZPDDj7cVYIOd9lxLpRXwVuJlW0ZkjHAjXlCcjF2mf0rpEsKTflgR9qLXYaeHjq-BZSbJsKI6KbBUSYMS_rQLJO-zIPx6-I3oz6REqdYHtDhOCC6eWuScCQpixQ2Y15QAAAAHMwqLVAA") #ASİSTAN SESSİON
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