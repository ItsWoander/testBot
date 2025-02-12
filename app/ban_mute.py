from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMember, ChatPermissions
import config
from datetime import datetime
import datetime

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




'''
Мут
'''










@admin_router.message(Command('mute'))
async def mute(message:Message):
    if message.chat.type != 'private': #перевірка чи є група
        if message.reply_to_message != None: #перевірка чи є реплай

            id_user_reply =  message.reply_to_message.from_user.id #юзер користувача в реплаї
            # Отримуємо інформацію про адмінів
            admins = await bot.get_chat_administrators(message.chat.id)

            if any(admin.user.id == message.from_user.id for admin in admins):
                
                
                text = message.text
                text = text.split()
                text = list(text)
                if len(text) == 1:
                    print("вхід")
                    time_mute_format = 283939393
                elif len(text) == 2:
                    int_mute = text[1][:-1]
                    if any(letter in text[1] for letter in ['h', 's', 'm', 'd']):
                        if 'h' in text[1] :
                            print(1)
                            time_mute_format = 60 * 60 * int(int_mute)
                        elif 'd' in text[1] :
                            time_mute_format = 60 * 60 * 24 * int(int_mute)
                        elif 'm' in text[1]:
                            time_mute_format = 60 * int(int_mute)
                        elif 's' in text[1]:
                            time_mute_format = int(int_mute)
                        else:
                            await message.reply('Невірний формат')
                            return 
                    else:
                        await message.reply("Невірний формат")
                        return
                           
  
                else:
                    await message.reply("Невірний формат муту")
                    return
                await message.reply(f'Користувачу заборонено розмовляти \n Тривалість:{text[1] if len(text) == 2 else "inf"}')


                        
                
                print(text)
                
                untill_date = datetime.datetime.now() + datetime.timedelta(seconds=time_mute_format)
                

                permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,)
                
                await bot.restrict_chat_member(message.chat.id, id_user_reply, permissions, until_date=untill_date)




            else:
                await message.reply("У вас немає прав ")
                return

        else:
            await message.reply("Затикати щелепу треба за таким форматом:\n /mute 1h /mute 2d /mute 3m /mute 4s")
    else:
        await message.reply("Команда не доступна в пп")




@admin_router.message(Command('unmute'))
async def unmute(message:Message):
    if message.chat.type != 'private': #перевірка чи є група
        if message.reply_to_message != None: #перевірка чи є реплай

            id_user_reply =  message.reply_to_message.from_user.id #юзер користувача в реплаї
            # Отримуємо інформацію про адмінів
            admins = await bot.get_chat_administrators(message.chat.id)

            if any(admin.user.id == message.from_user.id for admin in admins):
                permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,)
                await bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id, permissions)
                await message.reply('Користувачу дозволено розмовляти')
            else:
                await message.reply('У вас немає прав')
        else:
            await message.reply('Немає реплаю')
    else:
        await message.reply('Команда в пп не доступна')






