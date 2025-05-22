from pyrogram import Client, filters
import random

# Bot client'ınızı burada tanımlayın (api_id, api_hash ve token'u kendi bilgilerinizle değiştirin)
app = Client(
    "my_bot_session",
    api_id=1234567,
    api_hash="your_api_hash_here",
    bot_token="your_bot_token_here"
)

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

@app.on_message(filters.command("love") & ~filters.private)
async def love_command(client, message):
    # Sadece grup ve süpergruplarda çalışacak
    if message.chat.type not in ["group", "supergroup"]:
        await message.reply_text("Bu komut sadece grup sohbetlerinde kullanılabilir.")
        return

    members = []
    try:
        async for member in client.iter_chat_members(message.chat.id):
            user = member.user
            if user.is_bot:
                continue  # Botları atla
            if user.username:
                mention = f"@{user.username}"
            else:
                mention = user.mention  # İsim ile mention
            members.append(mention)
    except Exception as e:
        await message.reply_text(f"Üye listesine erişim hatası: {e}")
        return

    if len(members) < 2:
        await message.reply_text("Yeterli üye yok veya üyeler gizli.")
        return

    user1, user2 = random.sample(members, 2)
    love_percentage = random.randint(10, 100)
    love_message = get_random_message(love_percentage)

    response = f"{user1} 💕 + {user2} 💕 = {love_percentage}%\n\n{love_message}"
    await message.reply_text(response)

if __name__ == "__main__":
    print("Bot başlatılıyor...")
    app.run()
