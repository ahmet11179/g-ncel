import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory

from DAXXMUSIC import userbot as us, app
from DAXXMUSIC.core.userbot import assistants

@app.on_message(filters.command("gecmis"))  # /gecmis komutu ile çalışır
async def sg(client: Client, message: Message):
    # Kullanıcı belirtilmemiş ve cevaplanmış bir mesaj da yoksa uyarı ver
    if len(message.text.split()) < 1 and not message.reply_to_message:
        return await message.reply("sg username/id/reply")
    
    # Eğer bir mesaja yanıt verilmişse, yanıtlanan kullanıcının ID'sini al
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]  # Aksi halde komuttan sonraki kullanıcı adı/id alınır

    lol = await message.reply("<code>İşleniyor...</code>")
    
    # Geçerli bir kullanıcıyı almaya çalış
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>Lütfen geçerli bir kullanıcı belirtin!</code>")

    # Kullanılacak stalk botlarından rastgele birini seç
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)

    # Asistan botu kontrol et
    if 1 in assistants:
        ubot = us.one

    try:
        # Stalk botuna kullanıcı ID'sini gönder
        a = await ubot.send_message(sg, f"{user.id}")
        await a.delete()  # Mesajı hemen sil
    except Exception as e:
        return await lol.edit(e)

    await asyncio.sleep(1)  # Kısa bir gecikme ekle

    # Gelen mesajları ara ve ilk uygun olanı göster
    async for stalk in ubot.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await message.reply("Bot cevap vermedi.")
        elif stalk:
            await message.reply(f"{stalk.text}")
            break  # İlk bulduğu mesajı gösterip döngüden çık

    # Sohbet geçmişini temizle (stalk botu ile olan)
    try:
        user_info = await ubot.resolve_peer(sg)
        await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    # "İşleniyor..." mesajını sil
    await lol.delete()
