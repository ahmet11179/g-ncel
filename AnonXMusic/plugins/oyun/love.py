from pyrogram import filters
from random import choice, randint
from AnonXMusic import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return choice([
            "Aşk havada ama biraz kıvılcım lazım.",
            "İyi bir başlangıç ama daha gelişmeli.",
            "Güzel bir şeyin sadece başlangıcı."
        ])
    elif love_percentage <= 70:
        return choice([
            "Güçlü bir bağ var. Beslemeye devam et.",
            "İyi bir şansın var. Üzerinde çalış.",
            "Aşk filizleniyor, devam et."
        ])
    else:
        return choice([
            "Vay! Cennet tarafından yazılmış bir eşleşme!",
            "Mükemmel uyum! Bu bağı koru.",
            "Birlikte olmaya yazılmışsınız. Tebrikler!"
        ])

@app.on_message(filters.command("love", prefixes="/") & filters.group)
async def love_command(client, message):
    try:
        # Grup üyelerini getir
        members = []
        async for member in client.iter_chat_members(message.chat.id):
            # Botu ve kanal üyelerini dışla, sadece gerçek kullanıcıları al
            if not member.user.is_bot:
                members.append(member.user.first_name)
        
        if len(members) < 2:
            await message.reply("Yeterli kullanıcı yok.")
            return
        
        # Rastgele 2 farklı isim seç
        name1, name2 = None, None
        while name1 == name2:
            name1 = choice(members)
            name2 = choice(members)
        
        love_percentage = randint(10, 100)
        love_message = get_random_message(love_percentage)
        
        response = f"{name1}💕 + {name2}💕 = %{love_percentage}\n\n{love_message}"
        await message.reply(response)
    
    except Exception as e:
        await message.reply(f"Bir hata oluştu: {e}")
