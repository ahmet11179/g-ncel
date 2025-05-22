import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from AnonXMusic import app
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from typing import Union, Optional
import random

# Rastgele kullanılacak profil fotoğrafı linkleri (profil resmi olmayan kullanıcılar için)
random_photo = [
    "https://telegra.ph/file/b79290e357a600dc3ab43.jpg",
]

# --------------------------------------------------------------------------------- #

# Yazı tipi alma fonksiyonu
get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)

# Uzun yazıyı kesip büyük harfe çevirme
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

# Kullanıcı bilgisi görseli oluşturma fonksiyonu
async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    # Arka plan resmini aç
    bg = Image.open(bg_path)

    if profile_path:
        # Profil resmi varsa, daire şeklinde kırp ve yapıştır
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    # Kullanıcı ID'sini yaz
    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    # Görseli kaydet ve yolunu döndür
    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

# Arka plan ve yazı tipi dosya yolları
bg_path = "AnonXMusic/assets/userinfo.png"
font_path = "AnonXMusic/assets/font.ttf"

# --------------------------------------------------------------------------------- #

# Kullanıcı bilgisi mesaj şablonu
INFO_TEXT = """**
❅─────✧❅✦❅✧─────❅
            ✦ ᴋᴜʟʟᴀɴıᴄı ʙɪʟɢɪsɪ ✦

➻ ᴋᴜʟʟᴀɴıᴄı ɪᴅsɪ ‣ **`{}`
**➻ ɪsɪᴍ ‣ **{}
**➻ sᴏʏɪsɪᴍ ‣ **{}
**➻ ᴋᴜʟʟᴀɴıᴄı ᴀᴅı ‣ **`{}`
**➻ ᴛᴀɴıᴛɪᴍ (ᴍᴇɴᴛɪᴏɴ) ‣ **{}
**➻ sᴏɴ ɢöʀüʟᴍᴇ ‣ **{}
**➻ ᴅᴄ ɪᴅ ‣ **{}
**➻ ʙɪʏᴏɢʀᴀғɪ ‣ **`{}`

**❅─────✧❅✦❅✧─────❅**
"""

# --------------------------------------------------------------------------------- #

# Kullanıcının çevrimiçi durumunu döndür
async def userstatus(user_id):
   try:
      user = await app.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "Son zamanlarda çevrimiçiydi."
      elif x == enums.UserStatus.LAST_WEEK:
          return "Geçen hafta çevrimiçiydi."
      elif x == enums.UserStatus.LONG_AGO:
          return "Uzun zaman önce çevrimiçiydi."
      elif x == enums.UserStatus.OFFLINE:
          return "Çevrimdışı."
      elif x == enums.UserStatus.ONLINE:
         return "Şu an çevrimiçi."
   except:
        return "**Bir hata oluştu!**"

# --------------------------------------------------------------------------------- #

# /info veya /userinfo komutu işlendiğinde çalışacak fonksiyon
@app.on_message(filters.command(["info", "userinfo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Komutla birlikte bir kullanıcı adı/id verilmişse
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "Soyadı yok"
            username = user_info.username if user_info.username else "Kullanıcı adı yok"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "Biyografi ayarlanmamış"
            
            if user.photo:
                # Kullanıcının profil fotoğrafı varsa
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # Kullanıcının profil fotoğrafı yoksa rastgele bir fotoğraf kullan
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))        
      
    # Komut sadece yazıldıysa (örneğin: /info)
    elif not message.reply_to_message:
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "Soyadı yok"
            username = user_info.username if user_info.username else "Kullanıcı adı yok"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "Biyografi ayarlanmamış"
            
            if user.photo:
                # Kullanıcının profil fotoğrafı varsa
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # Kullanıcının profil fotoğrafı yoksa rastgele bir fotoğraf kullan
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))

    # Komut bir mesaja cevap olarak verildiyse
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "Soyadı yok"
            username = user_info.username if user_info.username else "Kullanıcı adı yok"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "Biyografi ayarlanmamış"
            
            if user.photo:
                # Kullanıcının profil fotoğrafı varsa
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # Kullanıcının profil fotoğrafı yoksa rastgele bir fotoğraf kullan
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))
