from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from datetime import datetime
from AnonXMusic import app as app
import requests

@app.on_message(filters.command("sayfa"))
async def handwrite(bot, message: Message):
    try:
        await message.delete()  # Komut mesajını sil
    except Exception:
        pass  # Yetki yoksa hata vermez

    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            await message.reply_text("Lütfen yazılacak metni belirtin! Örnek: /sayfa Merhaba dünya")
            return
        text = parts[1]

    m = await message.reply_text("Lütfen bekleyin...,\n\nMetniniz yazılıyor...")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
Başarıyla yazılmış metin 💘
🥀 yazan: {message.from_user.mention} ✨
"""
    await m.delete()
    await message.reply_photo(photo=write, caption=caption)