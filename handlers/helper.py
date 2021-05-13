from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 Merhaba! Aşağıdaki komutlar şunlardır: **{bn}** - __A Grup Sesli Sohbet Müzik Çaları__.
Şu anda desteklediğim komutlar şunlardır:

👤 **Kullanıcı Komutları :**
▶️ /oynat - **[ Yalnızca Gruplar ]** > __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
🔎 /bul - **[ Gruplar & İçinde]** > __Sohbette aranan şarkıyı yükler.__
⏩ /ytplay - **[ Yalnızca Gruplar]** > __Şarkıyı doğrudan YouTube Arama'dan çalar.__
🇹🇷 /düzenleyen - **[ Bilgi ]** > __Düzenleyen kişi bilgisini gösterir.__


👮‍♂️ **Yönetici ve Özel Kullanıcıları Komutları :**
⏸️ /durdur - **[Yalnızca Gruplar ]** > __Sesli Sohbet Müziğini Duraklat.__
⏩ /devam - **[Yalnızca Gruplar ]** > __Sesli Sohbet Müziğine Devam Et.__
⏭️ /atla - **[Yalnızca Gruplar ]** > __sesli sohbette çalan mevcut müziği geçer.__
🛑 /dur - **[Yalnızca Gruplar ]** > __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__""")

@Client.on_message(command("help") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** selam! Tüm komutları almak için beni PM bakınız 😉")
