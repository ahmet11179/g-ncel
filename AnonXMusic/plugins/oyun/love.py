from pyrogram import filters
import random
from AnonXMusic import app

def get_random_message(love_percentage):
    # Aynı fonksiyonunuz
    ...

@app.on_message(filters.command("love", prefixes="/"))
async def love_command(client, message):
    if message.chat.type != "private":
        members = []
        try:
            async for member in client.iter_chat_members(message.chat.id):
                user = member.user
                if user.is_bot:
                    continue
                if user.username:
                    mention = f"@{user.username}"
                else:
                    mention = user.mention
                members.append(mention)
        except Exception as e:
            await message.reply_text(f"Üye listesine erişim hatası: {e}")
            return

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
