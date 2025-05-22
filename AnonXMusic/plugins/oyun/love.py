from pyrogram import filters
import random
from AnonXMusic import app  # app burada Pyrogram Client olmalı

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "Aşk havada ama biraz kıvılcım lazım.",
            "İyi bir başlangıç ama gelişmeye açık.",
            "Güzel bir şeyin başlangıcı."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "Güçlü bir bağ var. Beslemeye devam et.",
            "İyi bir şansın var. Üzerinde çalış.",
            "Aşk filizleniyor, devam et."
        ])
    else:
        return random.choice([
            "Vay be! Cennet gibi bir uyum!",
            "Mükemmel eşleşme! Bu bağı koru.",
            "Birlikte olmaya yazgılısınız. Tebrikler!"
        ])

@app.on_message(filters.command("love", prefixes="/"))
async def love_command(client, message):
    # Özel mesaj değilse (private dışı)
    if message.chat.type != "private":
        members = []
        try:
            async for member in client.iter_chat_members(message.chat.id):
                user = member.user
                if user.is_bot:
                    continue  # Botları atla
                if user.username:
                    mention = f"@{user.username}"
                else:
                    mention = user.mention  # Kullanıcının ismine göre mention
                members.append(mention)
        except Exception:
            # Eğer üye listesine erişim olmazsa boş bırak
            members = []

        if len(members) < 2:
            await message.reply_text("Bu sohbette yeterli üye yok ya da üye listesine erişilemiyor.")
            return

        user1, user2 = random.sample(members, 2)
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{user1} 💕 + {user2} 💕 = {love_percentage}%\n\n{love_message}"
        await message.reply_text(response)
    else:
        await message.reply_text("Bu komut özel mesajlarda kullanılamaz.")
