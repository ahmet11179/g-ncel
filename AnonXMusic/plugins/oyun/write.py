from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from datetime import datetime
from AnonXMusic import app as app
import requests

@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "Lütfen bekleyin...,\n\nMetniniz yazılıyor...")  # Burada kullanıcıya yazı yazma işleminin yapıldığını belirtiyoruz.
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
Başarıyla yazılmış metin 💘
✨ Yazılan: [𝐘ᴜᴍɪᴋᴏᴏ](https://t.me/{BOT_USERNAME})  # Yazıyı yazan kişinin adı, botun username'i.
🥀 İstek yapan: {message.from_user.mention}  # Kullanıcının adı veya mesajda etiketlenen kişi
"""
    await m.delete()  # Kullanıcıya, yazma işlemi tamamlandığında gönderilen "Lütfen bekleyin..." mesajını sileriz.
    await message.reply_photo(photo=write, caption=caption)  # Kullanıcıya yazılan metnin görselini göndeririz.

mod_name = "Yazı Aracı"  # Modül ismi Türkçeye çevrildi

help = """
Verilen metni beyaz bir sayfada kalemle yazılmış gibi gösterir 🖊

❍ /write <Metin> *:* Verilen metni beyaz bir sayfada yazılmış olarak gösterir.
"""  # Yardım kısmındaki açıklamalar Türkçeye çevrildi.


#----------

@app.on_message(filters.command("day"))
def date_to_day_command(client: Client, message: Message):
    try:
        # Komut mesajından tarihi çıkarma işlemi...
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            input_date = command_parts[1].strip()
            date_object = datetime.strptime(input_date, "%Y-%m-%d")  # Girilen tarihi belirli bir formata çeviriyoruz.
            day_of_week = date_object.strftime("%A")  # Haftanın gününü alıyoruz.

            # Haftanın günüyle birlikte yanıt veriyoruz.
            message.reply_text(f"{input_date} tarihinin haftanın günü: {day_of_week}.")

        else:
            message.reply_text("Lütfen geçerli bir tarih girin. Format: `/day 1947-08-15`")

    except ValueError as e:
        message.reply_text(f"Hata: {str(e)}")  # Eğer tarih formatı yanlışsa hata mesajı gösteririz.
