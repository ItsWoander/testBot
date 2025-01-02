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
async def mute(message:Message):
    if message.chat.type != 'private':
        if message.reply_to_message != None:
            id_useer = message.reply_to_message.from_user.id
            chat_id_group = message.chat.id
            await message.answer(f"{id_useer, chat_id_group}")
            await bot.ban_chat_member(chat_id_group, id_useer)


    else:
        await message.answer("Використання є можливим тільки в чатах")
    
@admin_router.message(Command('unban'))
async def mute(message:Message):

    if message.chat.type != 'private': #перевірка чи є група
        
        chat_id_group = message.chat.id #АЙДИ ЧАТА
        # chat_member = await bot.get_chat_administrators(message.chat.id) 
        #await message.reply(chat_member)
        
        chat_admins = await bot.get_chat_administrators(chat_id_group)
        print(chat_admins)
        print(message.from_user.id in chat_admins)
        for admin in chat_admins:
            if admin.status == 'creator':
                print('yes create')
                pass
                # Якщо адміністратор є власником чату
            elif admin.status == 'administrator':
                print('yes admin')
                pass
                # Якщо адміністратор є звичайним адміністратором


        if message.reply_to_message != None: #перевірка чи є реплай
            user_admin = message.from_user.id #юзер користувача який розмутив
            id_useer =  message.reply_to_message.from_user.id #юзер користувача якого замутили
            await message.reply(f"{id_useer, chat_id_group}")
            await bot.unban_chat_member(chat_id_group, id_useer)
            await message.bot.send_message(id_useer,f"Ви були розблокані у чаті:{message.chat.title} \n Посилання:" + f"{"t.me/"+ str(message.chat.username) if {message.chat.username} != None else str(message.chat.title)}")
