import asyncio
from AnonXMusic import app
from pyrogram import filters, enums

# Kullanıcı bilgisi mesaj şablonu
INFO_TEXT = """✨───────────────✨
         ✦ ᴋᴜʟʟᴀɴıᴄı ʙɪʟɢɪsɪ ✦

🆔  • Kullanıcı ID: {}
👤  • İsim: {}
👥  • Soyisim: {}
🔖  • Kullanıcı Adı: {}
📢  • Tanıtım: {}
⏰  • Son Görülme: {}
📝  • Biyografi: {}

✨───────────────✨
"""

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

# /info veya /userinfo komutu işlendiğinde çalışacak fonksiyon
@app.on_message(filters.command(["info", "userinfo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        elif len(message.command) == 2:
            user_id = message.text.split(None, 1)[1]

        user_info = await app.get_chat(user_id)
        user = await app.get_users(user_id)
        status = await userstatus(user.id)

        id = user_info.id
        first_name = user_info.first_name 
        last_name = user_info.last_name if user_info.last_name else "Soyadı yok"
        username = user_info.username if user_info.username else "Kullanıcı adı yok"
        mention = user.mention
        bio = user_info.bio if user_info.bio else "Biyografi ayarlanmamış"

        await app.send_message(
            chat_id,
            INFO_TEXT.format(id, first_name, last_name, username, mention, status, bio),
            reply_to_message_id=message.id
        )

    except Exception as e:
        await message.reply_text(str(e))
