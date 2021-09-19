import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Rdbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Rdbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Rdbot.send_message(
               chat_id=message.chat.id,
               text="""<b>👋 Hey There, Welcome To RoyalPhotoGraphBot.</b>

<i> Can Upload Photos or Videos To Telegraph. Made by @Royal_Devendra

Press The Help Button For More Information On How To Use Me.</i>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "📝 Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "🌐 Support", url="https://t.me/RoyalDevendra")
                                    ],[
                                      InlineKeyboardButton(
                                            "🧑🏻‍💻 Developer", url="https://t.me/Royal_Devendra")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Rdbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Rdbot.send_message(
               chat_id=message.chat.id,
               text="""<b>RoyalPhotoGraphBot Help!</b>

<i>Just send a photo or video less than 5mb file size, I'll upload it to telegraph.</i>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "⁉️About", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Rdbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Rdbot.send_message(
               chat_id=message.chat.id,
               text="""<b>About RoyalPhotoGraphBot!</b>

<b>♞ Developer:</b> <a href="http://t.me/Royal_Devendra">Devendra</a>

<b>♞ Support:</b> <a href="https://t.me/RoyalDevendra">Royal Bot Support</a>

<b>~ @Royal_Devendra</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "🧑🏻‍💻 Developer", url="https://t.me/Royal_Devendra")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Rdbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("⏳ Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n🖼 Uploaded By @RoyalPhotoGraphBot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Rdbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("⏳ Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n📹 Uploaded By @RoyalPhotoGraphBot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Rdbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("⏳ Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\n🆔 Uploaded By @RoyalPhotoGraphBot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Rdbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!! 
"""
)

Rdbot.run()
