import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "27606753"))
API_HASH = getenv("API_HASH", "b060babef6dd4a784ea36ac9a3387de1") #ASİSTAN APİ HASH

EVAL = list(map(int, getenv("EVAL", "7716352578 7091230649").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7922147139:AAEIPV5YJbKL5nodzbtvuVOm7cb6INIuh5o") #BOT TOKEN
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Cankabusower")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Sonsuzmuzik_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "ₛₒₙₛᵤz ₘüzᵢₖ")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Sonsuzasistan3")
# ---------------------------------------------------------
SAHİB= getenv("SAHİB", "https://t.me/Cankabusower") #OWNER KULLANICI ADI 
#---------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7730275029)) #OWNER İD
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sonsuzmango:sonsuz@sonsuz.plikp.mongodb.net/?retryWrites=true&w=majority&appName=Sonsuz")
#---------------------------------------------------------------
# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002292728756")) #LOG GRUBU İD'Sİ -100 İLE BAŞLAMALI
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# -----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ahmet11179/g-ncel",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sonsuzduyuru") #DESTEK KANALI LİNKİ
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sonsuzmuzikdestek") #DESTEK GRUBU LİNKİ
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "AQGlPuEAftZfjJYIe1g-NVelgWukGwOW8pwl0ViRUI0G8mnfhLKaUHbG9kXgdR3ih_Vwzpx7XHgyeiUTyL32taRZ4DmhMrQzn9-MkjhD_i-aQA9W_pI7Rar9zEFcVlpGLwDDmrKupYMuz3xPGeNp7D1I9N3EKHXayDVTZbXKYOyozT-cYe2NoS2fTMS6oNdefD6wTJSstkOnhB4ryB-BK1nw6aptd3e2qVRi-wNz8Eg5YnNLK73p5RvSbFLJ-YCqzHS-o4M7E96WmWLrRS71svdxnWRdr4IQiEQYhDIyhVANWU5z7zCgGd0LG4pzHyXUNiqzTPljlRZuh0MTeA3neOk2y7pmbgAAAAHiXvUSAA") #ASİSTAN SESSİON
STRING2 = getenv("STRING_SESSION2", "BAGlPuEALLiqOTkp-xR387CA6hG7LhnhHdxQqzizHyDDK3tNjlo4QtD2B1rKE6vHKxDiMmQvACxHYTqhL3WBAkSc1NPBofOJ7zqgjM81nSs-UkJnp8_MotmjOTd6RKUPQGanJCkmiO1Y1wRQE0XvLkCq5ohmo263NXfBQeSIm9ZbrhPTsm8gAiYu1EdRY7BS8kKynOdqYjWWyak0cZRFxExvCVVM3gcv0oPdd4Ub1tvoZaU6ZM3MKqsEBf3ANNQPO07oJHOmytp43HUpnT24OwWwvIkwz6d_B5d0kPlgq0mu0tgdY8w_3RE9mudL6HzbgQkruhReKrhqiORsmUR4vhBqAwheKQAAAAHSyI2rAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
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
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
