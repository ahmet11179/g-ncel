from pyrogram import Client, filters
from pyrogram.enums import ChatType
import random

from AnonXMusic import app  # app kesin Pyrogram Client olmalı

def get_random_message(love_percentage: int) -> str:
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

@app.on_message(filters.command("love", prefixes="/") & ~filters.private)
async def love_command(client, message):
    members = []
    async for member in client.iter_chat_members(message.chat.id):
        if member.user.is_bot:
            continue
        if member.user.username:
            mention = f"@{member.user.username}"
        else:
            mention = member.user.mention
        members.append(mention)

    if len(members) < 2:
        await message.reply("Yeterli üye yok.")
        return

    user1, user2 = random.sample(members, 2)
    love_percentage = random.randint(10, 100)
    love_message = get_random_message(love_percentage)

    response = f"{user1} 💕 + {user2} 💕 = {love_percentage}%\n\n{love_message}"
    await message.reply(response)
