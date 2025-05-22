from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from datetime import datetime
from AnonXMusic import app as app
import requests

@app.on_message(filters.command("sayfa"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = message.text.split(None, 1)[1]
    m = await message.reply_text("Lütfen bekleyin...,\n\nMetniniz yazılıyor...")  # Burada `await` kullanmamız gerekiyor.
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
Başarıyla yazılmış metin 💘
"""
    await m.delete()  # `await` ekledik çünkü bu da bir async işlemi
    await message.reply_photo(photo=write, caption=caption)  # `await` ekledik

mod_name = "Yazı Aracı"  # Modül ismi Türkçeye çevrildi

help = """
Verilen metni beyaz bir sayfada kalemle yazılmış gibi gösterir 🖊

❍ /write <Metin> *:* Verilen metni beyaz bir sayfada yazılmış olarak gösterir.
"""  # Yardım kısmındaki açıklamalar Türkçeye çevrildi.