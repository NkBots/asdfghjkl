from telethon import TelegramClient
from telethon import events

#pyrogram

import pyrogram
import random
from pyrogram import Client, filters
from pyrogram import Client, emoji, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Message, CallbackQuery 
from pyrogram.types import Message
import os
from telegraph import upload_file
import json, requests, os, shlex, asyncio, uuid, shutil
from typing import Tuple
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import json, requests, os, shlex, asyncio, uuid, shutil
from typing import Tuple
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
import sys
import os
import time
from pyrogram.types import Message
from pyrogram.types import Message, User
import openai
import logging
import json

from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)


MENTION = "[{}](tg://user?id={})"
MESSAGE = "Salam! {}, Əyləncə Dolu Qrupumuza Xoş Gəldin🥳!Qaydalara riaət etdikcə səndə favori userlərimizdən biri olacaqsan🤩!Əminəmki Nümunəvi Userlərdən biri olacaqsan!🥰"

DUR = False
SORGU = None
WSORGU = None
WDUR = False

GRUP = []


logging.basicConfig(filename='chatgpt-bot-errors.txt', level=logging.ERROR,
                    format='[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def btag():
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻Sahibim", url="https://t.me/Teamabasov")]]
	BUTTON=[[InlineKeyboardButton(text="Yeniliklər Kanalı📣", url="https://t.me/teamabasofcom")]]
	return InlineKeyboardMarkup(BUTTON)





openai.api_key = "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"



@rehim.on_message(filters.command('gpt') & filters.private)
async def start(client, msj):
    chat_id = msj.chat.id
    reply = msj.reply_to_message
    
    
    
    if reply:
        yazi = reply.text
        yazi = yazi.lower()
        if "kod" in yazi or "kodu" in yazi:
                    z = await client.send_message(chat_id, f"🤩 **ChatGPT cavab hazırlayır...**\n⚠️ **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=2048,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"`{text}`")
                    await client.send_message(chat_id, f"🌌 **Kodu daha rahat görmək üçün /carbon əmrindən istifadə et**")
        else:
                    z = await client.send_message(chat_id, f"🤩 **ChatGPT cavab hazırlayır...**\n⚠️ **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=3072,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"{text}")
    elif not reply:
        try:
            yazi = msj.text.split(" ", 1)[1]
            yaziVar = True
            if yaziVar == True:
                yazi = yazi.lower()
                if "kod" in yazi or "kodu" in yazi:
                    z = await client.send_message(chat_id, f"🤩 **ChatGPT cavab hazırlayır...**\n⚠️ **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=2048,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"`{text}`")
                    await client.send_message(chat_id, f"🌌 **Kodu daha rahat görmək üçün /carbon əmrindən istifadə et**")
                else:
                    z = await client.send_message(chat_id, f"🤩 **ChatGPT cavab hazırlayır...**\n⚠️ **Bu sənin nə istədiyindən asılı olaraq vaxt ala bilər**")
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=yazi,
                        temperature=0.9,
                        max_tokens=3072,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=["###"]
                    )
                    text = response['choices'][0]['text']
                    await client.delete_messages(chat_id, z.id)
                    await client.send_message(chat_id, f"{text}")
        except Exception as e:
            print(e)
            await client.send_message(chat_id, f"⚠️ **Mənə düzgün bir mətn ver.**")

@rehim.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Salam {message.from_user.mention} Xoş gəldin @{message.chat.username} ,  Groupuna",chat_id=chatid)
	
@rehim.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Sağol ,  {message.from_user.mention} , Görüşmək ümüdü ilə",chat_id=chatid)
	


@rehim.on_message(filters.command("rules"))
async def _rules(_, message: Message):
    replied = message.reply_to_message
    if replied:
        msg_id = replied.message_id
    else:
        msg_id = message.message_id
    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Read Rules",
                    url="https://t.me/usergeot/537063"
                )
            ]
        ]
    )
    await rehim.send_message(chat_id=message.chat.id,
                           text="**⚠️ Here Our RULES ⚠️**",
                           reply_to_message_id=msg_id,
                           reply_markup=markup)





@rehim.on_message(filters.command("ids"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = f"👥 **Söhbət ID** : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f"💬 **Mesaj ID** : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f"🙋‍♂️ **İstdifadəçi ID** : `{msg.from_user.id}`\n"
    file_id, file_unique_id = None, None
    if msg.audio:
        type_ = "audio"
        file_id = msg.audio.file_id
        file_unique_id = msg.audio.file_unique_id
    elif msg.animation:
        type_ = "animation"
        file_id = msg.animation.file_id
        file_unique_id = msg.animation.file_unique_id
    elif msg.document:
        type_ = "document"
        file_id = msg.document.file_id
        file_unique_id = msg.document.file_unique_id
    elif msg.photo:
        type_ = "photo"
        file_id = msg.photo.file_id
        file_unique_id = msg.photo.file_unique_id
    elif msg.sticker:
        type_ = "sticker"
        file_id = msg.sticker.file_id
        file_unique_id = msg.sticker.file_unique_id
    elif msg.voice:
        type_ = "voice"
        file_id = msg.voice.file_id
        file_unique_id = msg.voice.file_unique_id
    elif msg.video_note:
        type_ = "video_note"
        file_id = msg.video_note.file_id
        file_unique_id = msg.video_note.file_unique_id
    elif msg.video:
        type_ = "video"
        file_id = msg.video.file_id
        file_unique_id = msg.video.file_unique_id
    if (file_id and file_unique_id) is not None:
        out_str += f"● **Növ:** `{type_}`\n"
        out_str += f"📄 **Fayıl ID:** `{file_id}`\n"
        out_str += f"📄 **Fayil UNİKAL ID:** `{file_unique_id}`"
    await message.reply(out_str)





@rehim.on_message(
	filters.command(["admin", "all"])
	& filters.private
)
async def priw(client, message):
	await message.reply_text("Hmm burada 2miz olduğumuz üçün və 2 mizdə online olduğumuz üçün bu əmri qruplarda işlət!🤠")


@rehim.on_message(
	filters.command("all")
	& filters.group
	)
async def tag(client: rehim, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in rehim.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Tag Prosesini Başlatdı! Hərkəsi Tag Edirəm Boss!⚡️",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in rehim.iter_chat_members(chat_id=chat.id, filter="all"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await rehim.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass
		
@rehim.on_message(
	filters.command("admin")
	& filters.group
	)
async def ta(client: rehim, message: Message):
	global DUR
	global SORGU
	msg = " ".join(message.command[1:])
	chat = message.chat
	async for mem in rehim.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			await message.reply_text(f"{message.from_user.mention} Adminləri tag etməyimi istədi⚡️ Adminləri Tag Edirəm Boss!🥳",
				reply_markup=btag()
				)
			time.sleep(1)
			SORGU = True
			async for member in rehim.iter_chat_members(chat_id=chat.id, filter="administrators"):
				if DUR:
					DUR=False
					SORGU = None
					break
				time.sleep(1)
				await rehim.send_message(chat_id=chat.id, text=f"{member.user.mention} {msg}")
				time.sleep(1.5)
		if message.from_user.id != mem.user.id:
			pass


		
@rehim.on_message(
	filters.group
	& filters.command("cancel")
)
async def stop(client: rehim, message: Message):
	global DUR
	chat = message.chat
	async for mem in rehim.iter_chat_members(chat_id=chat.id, filter="administrators"):
		if message.from_user.id == mem.user.id:
			if SORGU == None:
				await message.reply_text("Aktiv bir all prosesi yoxdur😕👍🏻")
				return

			DUR = True
			await message.reply_text(f"{message.from_user.mention} Tag prosesini dayandırdı❌ Tamam heçkəsi tag etmirəm😒")	
		if message.from_user.id != mem.user.id:
			pass


@rehim.on_message(filters.command('adminlist', prefixes='/'))
def admin_list(app, message):
    admins = rehim.get_chat_administrators(chat_id=message.chat.id)

    msgString = ""
    for i in range(len(admins)):
        user_name = admins[i].user.first_name
        if admins[i].user.last_name is not None:
            user_name += " " + admins[i].user.last_name
        msgString += "{}) {} \n".format(i+1, user_name)
    
    message.reply_text(msgString)



@rehim.on_message(filters.command("shib"))
def shib(client, message):
    # Get the users to "ship"
    user_a = message.reply_to_message.from_user
    user_b = message.mentions[0]

    # Build the string with the Love
    ship_str = "{} & {}".format(
        user_a.id, user_a.first_name, user_b.id, user_b.first_name)

    # Send the message with the users
    client.send_message(
        chat_id=message.chat.id,
        text="🚢 {} are perfect for each other!".format(ship_str),
        parse_mode="html"
    )


@rehim.on_message(filters.command("shipp"))
def ship(client, message):
    words = message.command[1:]
    if len(words) != 2:
        message.reply_text("Üzgünüm, Lütfen iki kelime girin")
        return

    first_word = words[0]
    second_word = words[1]

    score = 0
    for char in first_word:
        if char in second_word and char != " ":
            score += 1

    final_score = score * 100 / (len(first_word) + len(second_word))
    final_score = round(final_score)

    if final_score == 100:
        message.reply_text("Sonuç: PERFECT MATCH! 💕")
    elif final_score > 80:
        message.reply_text("Sonuç: Çok uyumlu! 👍")
    elif final_score > 60:
        message.reply_text("Sonuç: Uyumlu 🤝")
    elif final_score > 40:
        message.reply_text("Sonuç: Orta 🤔")
    elif final_score > 20:
        message.reply_text("Sonuç: Yetersiz 🤨")
    elif final_score >= 0:
        message.reply_text("Sonuç: Hiç uymuyor 😒")
    else:
        message.reply_text("Bir hata oluştu. Lütfen tekrar deneyin")



@rehim.on_message(filters.command(["ship"]))
def ship(client, message):
    parts = message.text.split()  #mesajı parçalara ayırır

    if len(parts) == 1:  #fonksiyonu çağıran komutun argümanları olup olmadığını kontrol eder
        client.send_message(
            chat_id=message.chat.id, 
            text="Kullanım:\n/ship  \nYazılan isimleri bir arada gösterir")  #geçersiz argümanları belirtir
        return
    
    name1 = parts[1]  #argümanları alır
    name2 = parts[2]
 
    client.send_message(  #mesaj gönderir
        chat_id=message.chat.id,
        text=name1 + " ♥ " + name2 )


@rehim.on_message(filters.command('tlink'))
async def get_link_group(client, message):
    try:
        text = await message.reply("Emal edilir...")
        async def progress(current, total):
            await text.edit_text(f"📥 Media yüklənir... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 Telegrapha yüklənir...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Linki**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | Fayl yükləmə uğursuz oldu**\n\n<i>**Səbəb**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass



@rehim.on_message(filters.command('id', prefixes="!"))
async def get_id(client, message):
    try:

        if (not message.reply_to_message) and (message.chat):
            await message.reply(f"İstdifadəçi {message.from_user.first_name}'idisi <code>{message.from_user.id }</code>.\nChat id: <code>{message.chat.id}</code>.") 

        elif not message.reply_to_message:
            await message.reply(f"İstdifadəçi {message.from_user.first_name}'ID <code>{message.from_user.id }</code>.") 

        elif message.reply_to_message.forward_from_chat:
            await message.reply(f"Yönləndirilmiş Kanal {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title} İdisi <code>{message.reply_to_message.forward_from_chat.id}</code>.") 

        elif message.reply_to_message.forward_from:
            await message.reply(f"Yönləndirilmiş İstdifadəçi, {message.reply_to_message.forward_from.first_name} İdisi <code>{message.reply_to_message.forward_from.id   }</code>.")

        elif message.reply_to_message.forward_sender_name:
            await message.reply("Üzr istəyirik, məxfilik parametrlərinə görə yönləndirilmiş istifadəçi ID-sini əldə edə bilməzsiniz")

        else:
            await message.reply(f"İstdifadəçi {message.reply_to_message.from_user.first_name}'İdisi <code>{message.reply_to_message.from_user.id}</code>.")   

    except Exception:
            await message.reply("ID-ni əldə edərkən xəta baş verdi.")




@rehim.on_message(filters.command('məzələnmə', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACKclj6oQmuLyLtOWks7vlpCYmJKp4JgAC9QIAAheWPVEZhr74w1bcwx4E', caption="Mözölönməəə")




@rehim.on_message(filters.command('küsdüm', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACKbtj6oNL_cuVNf1Y6UB3lvZJ_YwujwACywIAAhpPZFB2pPAE6XYVjx4E', caption="Küsdümmm")




@rehim.on_message(filters.command('töbə', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACKaZj6oJrs_Mn6Ni2Zc-VkzSAl0RD_wACsgIAAj4SDVB5nKQR2qqChB4E', caption="AY TÖBBƏƏƏƏƏƏƏƏ")




@rehim.on_message(filters.command('aleykum', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgIAAx0Cb5j5qAACKaFj6oC30P3qeRCVsZr5JV-pdmRTYAACNiMAAn-7WEuTKmDWoWhDyh4E', caption="ALEYKUMMM SALAM")




@rehim.on_message(filters.command("purge", prefixes="!"))
def purge_my_messages(client, message):
 to_delete = message.reply_to_message.message_id
 
 for message in client.iter_history(message.chat.id, limit=100):
  if message.message_id < to_delete:
   client.delete_messages(message.chat.id, message.message_id)
  



@rehim.on_message(filters.command("sill"))
def text_delete(client, message):
    # İlgili mesajı almak
    reply_msg = message.reply_to_message

    # Mesajı güncelleme
    if reply_msg:
        message.edit("Mesaj silindi!",
            reply_to_message_id=reply_msg.message_id,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Mesaj Geri Al",
                                    callback_data="undo_delete")
            ]]))
        # Mesajı silme
        reply_msg.delete()


@rehim.on_callback_query("undo_delete")
def on_undelete(client, query):
    # İlgili mesajı almak
    reply_msg = query.message.reply_to_message

    # Mesaj geri alma
    reply_msg.restore()

    # Mesajı güncelleme
    query.message.edit("Mesaj geri alındı!",
            reply_to_message_id=reply_msg.message_id)




@rehim.on_message(filters.command('salam', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACJg1j6hzo4r2ZWfnHhM6h1TFVKMjGbwACcAMAAtUEBVKM8iMEgl-FfR4E', caption="SALAM ALEYKUMMM")




@rehim.on_message(filters.command("zer", prefixes="!"))
def send_dice(client, message):
    result = random.randint(1, 6)
    dice = str(result)
    if message.chat.type in ["group", "supergroup"]:
        client.send_message(message.chat.id, f"{message.from_user.first_name} sanırım {dice} 🎲 geldi!", parse_mode="html")


@rehim.on_message(filters.command('list', prefixes="!"))
def chat_members(client, message):
    members = client.get_chat_members(message.chat.id)

    # Gruplardaki üyeleri listeleme
    text = "Gruptaki Üyeler:\n\n"
    for x in members:
        text += f"""\U0001f464 {x.user.username}\n"""
    message.reply_text(text)






@rehim.on_message(filters.command(["promote"], prefixes="!"))
def promote_member(client, message):
    if len(message.command) == 2:
        member_id = message.command[1]
        status = client.promote_chat_member(chat_id=message.chat.id, user_id=member_id)
        message.reply(f"{member_id} Başarıyla Yükseltildi.")







@rehim.on_message(filters.command("unpinall", prefixes="!"))
def unpin_all_chat_messages(client, message):
    chat_id = message.chat.id
    client.unpin_all_chat_messages(chat_id)
    message.reply("Tüm mesajlar başarıyla unpin edildi.")



@rehim.on_message(filters.command('aye', prefixes="."))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACITpj6VD0_jjbXkOZ307AwYF8rNw5UwACswIAAs0m_VKAQ7xZ5hdPpx4E', caption="Test")




@rehim.on_message(filters.command("botlist", prefixes="!"))
def botlist(client, message):
    bots = [     # List of Bots
        {
            "name": "OldMulti",
            "username": "OldMultiBot"
        },
        {
            "name": "Robbie",
            "username": "RobbieBot"
        },
        {
            "name": "Cally",
            "username": "CallyBot"
        }
    ]
    response_text = ""
    for bot in bots:
        response_text += f"{bot['name']}: @{bot['username']}\n"
    message.reply(response_text)






@rehim.on_message(filters.command('pin', prefixes="!")) 
def pin_message(client, message): 
    if not message.reply_to_message: 
        message.reply("Lütfen bir mesaj yanıtlayarak pinleme yapın!") 
    else: 
        message.reply_to_message.pin() 
        message.reply("Mesajınız başarıyla pinlendi!") 





@rehim.on_message(filters.command("unpin", prefixes="!"))
def unpin_message(client, message):
 reply_to = message.reply_to_message
 
 if reply_to != None:
  client.unpin_chat_message(message.chat.id, reply_to.message_id)
  client.send_message(message.chat.id, "Mesaj başarıyla kaldırıldı.")
 else:
  client.send_message(message.chat.id, "Bir mesaj seciniz")



@rehim.on_message(filters.command('info', prefixes="!"))
def user_info(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else :
        user = message.from_user

    user_id = user.id 
    first_name = user.first_name 
    last_name = user.last_name 
    user_name = user.username
    language_code = user.language_code  

    message.reply_text(
        f"User ID : {user_id}\n"
        f"First Name : {first_name}\n"
        f"Last Name : {last_name}\n"
        f"User Name : {user_name}\n"
        f"Language Code : {language_code}"        
    )





@rehim.on_message(filters.command("ses", prefixes="!"))
def get_voice(client, message):
    if message.audio:
        message.download_media(file_name="voice.ogg")
        print("Voice code saved.")








@rehim.on_message(filters.command(["sil"], prefixes="!"))
def delete_message(client, message):
    # silinecek mesajın ID'si
    message_to_delete = message.reply_to_message.message_id

    client.delete_messages(
        chat_id=message.chat.id,
        message_ids=message_to_delete
    )

    message.reply_text("Mesaj başarıyla silindi!")



@rehim.on_message(filters.text)
def delete_text(client, message):
    soz = ["Sik", "sik", "Sikdir", "sikdir", "Qəhbə", "qəhbə", "Göt", "göt", "31", "Peysər", "peysər", "Peyser", "peyser", "seks", "Seks", "sikərəm", "69", "sxoy"]
    if message.text in soz:
        rehim.delete_messages(message.chat.id, message.message_id)
        rehim.send_message(message.chat.id, "Söz Bot sahibi tərəfindən botdan bloklanıb söyüş söyməyin !")

     




@rehim.on_message(filters.voice)
def anything(client, message):
    message.reply(message.voice.file_id)


#TELETHON SETRİ

abasov = TelegramClient('abasov', api_id, api_hash).start(bot_token=bot_token)

@abasov.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@abasov.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Davay gelme day")

userjoin = (

    "Xoş gəlmisininiz",
    "",
)




print(">> Bot işləyir <<")
rehim.run()
abasov.run_until_disconnected()
