from pyrogram import filters
from pyrogram.types import Message
from gtts import gTTS
from AnonXMusic import app

@app.on_message(filters.command('ses'))
async def text_to_speech(client, message: Message):
    try:
        if len(message.text.split()) < 2:
            return await message.reply("Lütfen dönüştürülecek metni yazın. Örnek: `/tts Merhaba dünya`")

        text = message.text.split(' ', 1)[1]
        tts = gTTS(text=text, lang='tr')  # Türkçe konuşsun istersen 'tr' yaz
        tts.save('speech.mp3')
        await message.reply_audio('speech.mp3', title="dönüştürdüm", caption="İşte sesli mesajınız 🎧")
    except Exception as e:
        await message.reply(f"Hata oluştu: {str(e)}")
