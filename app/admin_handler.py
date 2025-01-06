from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMember
import config
from datetime import datetime
from app.Keyboard import phone_skam
import code
#from aiogram.types import ParseMode

bot = Bot(token=config.API_TOK)
admin_router = Router()

@admin_router.message(Command('ban'))
async def ban(message:Message):
    if message.chat.type != 'private': #перевірка чи є група
        
        chat_id_group = message.chat.id #АЙДИ ЧАТА
        admins = await bot.get_chat_administrators(message.chat.id) #отримуємо список адмінів

    # Перевіряємо, чи є відправник серед адмінів
        if any(admin.user.id == message.from_user.id for admin in admins):
            pass

        else:
            await message.reply("У вас немає прав ")
            return
        
        if message.reply_to_message != None: #перевірка чи є реплай
            
            id_useer =  message.reply_to_message.from_user.id #юзер користувача якого замутили

            try:
                await bot.ban_chat_member(chat_id_group, id_useer)
                await message.reply(f'Коричтувача {message.reply_to_message.from_user.first_name} було заблоковано')
            
            except BaseException as e:
                await message.reply(f'Щось пішло не так \n Переконайтесь що ви не блокуете адміністатора{e}')


            #відсилаємо користувачу повідомлення в лс
            try:
                await bot.send_message(message.reply_to_message.from_user.id, f"Вас було заблоковано у чаті {message.chat.title}\n Посилання:{"@"+str(message.chat.username) if message.chat.username != None else 'None' }")
            except Exception as r:
                pass # обробник помилки, якщо блокнуть бота, або користувач немає пп з цим ботом
        else:
            await message.reply('Ви повинні написати цю команду в реплаї порушника')
    else:
        await message.reply('Команда не працює в пп')








@admin_router.message(Command('unban'))
async def unban(message:Message):

    if message.chat.type != 'private': #перевірка чи є група

        chat_id_group = message.chat.id #АЙДИ ЧАТА

        if message.reply_to_message != None: #перевірка чи є реплай

            id_useer =  message.reply_to_message.from_user.id #юзер користувача якого замутили
            # Отримуємо інформацію про адмінів
            admins = await bot.get_chat_administrators(message.chat.id)

            if any(admin.user.id == message.from_user.id for admin in admins):
                pass
            else:
                await message.reply("У вас немає прав ")
                return

            try:
                await bot.unban_chat_member(chat_id_group, id_useer)
                await message.reply(f'Коричтувача {message.reply_to_message.from_user.first_name} було розблковано')
            
            except BaseException as e:
                await message.reply(f'Щось пішло не так \n Переконайтесь що ви не розблокуете адміністатора{e}')
            
            try:
                await bot.send_message(message.reply_to_message.from_user.id, f"Вас було розблоковано у чаті {message.chat.title}\n Посилання:{"@"+str(message.chat.username) if message.chat.username != None else 'None' }")
            except Exception as r:
                pass # обробник помилки, якщо блокнуть бота, або користувач немає пп з цим ботом
        else:
            await message.reply('Ви повинні написати цю команду в реплаї порушника')
    else:
        await message.reply('Команда не працює в пп')



