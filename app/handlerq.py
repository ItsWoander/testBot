from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
#from app.Keyboard import phone_skam
import code
router = Router()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer('КУ! для використання напиши "Хто я"')



@router.message(Command('code'))
async def help(message: Message):
    with open('code.txt', 'r',encoding='utf-8') as file:
        code_content = file.read()
        await message.reply(f"Мій код:\n <pre>{code_content}</pre>", parse_mode="HTML")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer('допомога')

@router.message(F.text.upper() == 'Хто я'.upper())
async def info(message:Message):
    try:
        with open("players.txt", "a") as file:
            
            file.write(f"{message.from_user.id},  {"@"+ message.from_user.username if message.from_user.username != None else None} {message.from_user.first_name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
            await message.bot.send_message(config.OWNER, f"{message.from_user.id},  {"@"+ message.from_user.username if message.from_user.username != None else None} {message.from_user.first_name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except BaseException as e:
        await message.answer(f'Помилка логування{e}')

        await message.bot.send_message(config.OWNER, f"{message.from_user.id},  {"@"+ message.from_user.username if message.from_user.username != None else None} {message.from_user.first_name} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n помилка логування: {e}" )


    


     # Беремо останню доступну якість
    photo_userss = await message.bot.get_user_profile_photos(message.from_user.id)
    photo_a = (photo_userss.photos[0][-1].file_id if photo_userss.total_count > 0 else "https://durdom.in.ua/public/main/photos2/2011-03/photo_23045.jpg")
    await message.answer_photo(photo=photo_a, caption = f"""Ось ти:
username:{"@"+ message.from_user.username if message.from_user.username != None else None}
Імя:{message.from_user.first_name}
id:{message.from_user.id}
Бот:{"ні" if message.from_user.is_bot == False else "Так"}
Прізвище:{message.from_user.last_name}
Мова:{message.from_user.language_code}
Преміум:{message.from_user.is_premium}
Чи було вас додано: {message.from_user.added_to_attachment_menu}
"""
        
        )