from pyrogram import Client, enums, filters
import asyncio
from AnonXMusic import app as app

@app.on_message(filters.command("zar"))
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç

    x = await bot.send_dice(message.chat.id)  # Zar atılır
    m = x.dice.value  # Zarın sonucu alınır

@app.on_message(filters.command("dart"))
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç
    x = await bot.send_dice(message.chat.id, "🎯")  # Dart oyunu
    m = x.dice.value  # Sonuç alınır

@app.on_message(filters.command("basket"))
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç
    x = await bot.send_dice(message.chat.id, "🏀")  # Basketbol oyunu
    m = x.dice.value  # Sonuç alınır

@app.on_message(filters.command("slot"))
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç
    x = await bot.send_dice(message.chat.id, "🎰")  # Jackpot (slot makinesi)
    m = x.dice.value  # Sonuç alınır

@app.on_message(filters.command("Bowling"))
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç
    x = await bot.send_dice(message.chat.id, "🎳")  # Bowling oyunu
    m = x.dice.value  # Sonuç alınır

@app.on_message(filters.command("Bowling
async def dice(bot, message):
    try:
        # Botun mesaj silme yetkisini kontrol et ve silme işlemi yap
        await message.delete()  # Kullanıcının yazdığı komutu sil
    except Exception:
        pass  # Hata olursa hiçbir şey yapma ve geç
    x = await bot.send_dice(message.chat.id, "⚽")  # Futbol oyunu
    m = x.dice.value  # Sonuç alınır

__help__ = """
Emoji ile Oyun Oynayın:
/zar - Zar 🎲
/dart - Dart 🎯
/basket - Basketbol 🏀
/Bowling - Bowling 🎳
/football - Futbol ⚽
/slot - Slot makinesi döndür 🎰
"""

__mod_name__ = "Dɪᴄᴇ"
