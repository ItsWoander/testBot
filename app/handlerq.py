from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
import code
router = Router()
import json
from app.Keyboard import kb
from app.func.stack_test import Player
@router.message(CommandStart())
async def start(message:Message):
    
    await message.reply('Я вмію банить і мутить)))) Ну і інформація про тебе "Хто я" ', reply_markup=kb())


@router.callback_query(lambda c: c.data == "mod_pressed")
async def button_1(callback: types.CallbackQuery):
    await callback.message.edit_text(
            text="Модерація:\n/ban - заблокувати користувача\n/mute - заткнути комусь пельку\n/report - поскаржитись на користувача\n/admins - список адміністрації",
        reply_markup=kb()
    )
    await callback.answer()  # Закриваємо анімацію завантаження

@router.callback_query(lambda c: c.data == "game_pressed")
async def button_1(callback: types.CallbackQuery):
    a = Player(callback.message.reply_to_message.from_user.id, callback.message.reply_to_message.from_user.full_name)
    text="<b>Ігрові команди:</b>\nКости: /dice (число) (ставка)\nСлоти: /slot (ставка)\nКоманди без вкладень:\nФут\nБас\nДар\nБоу "
    if not(await a.subscribe(callback.message)):
        text += f'\n<b>Примітка:</b>\nПідписники каналу <a href="{config.chat_user}">{config.name_chat} </a> мають більшу вдачу)'



    await callback.message.edit_text(
        text=text,
        reply_markup=kb(),parse_mode='HTML'
    )
    await callback.answer()  # Закриваємо анімацію завантаження




@router.callback_query(lambda c: c.data == "fun_pressed")
async def button_1(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Фансервіс:\nПрофіль: /profile\nПередати гроші:/pay (сумма) \nПравила: +rules (правила)\nПрибрати правила -rules \nПодивитись правила rules ",
        reply_markup=kb()
    )
    await callback.answer()  # Закриваємо анімацію завантаження






@router.message(Command('code'))
async def help(message: Message):
    await message.reply(f"Github : https://github.com/ItsWoander/testBot ")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer('допомога')







@router.message(F.text.upper() == 'Хто я'.upper())
async def info(message:Message):

    

     # Беремо останню доступну якість
    photo_userss = await message.bot.get_user_profile_photos(message.from_user.id)
    photo_a = (photo_userss.photos[0][-1].file_id if photo_userss.total_count > 0 else "https://durdom.in.ua/public/main/photos2/2011-03/photo_23045.jpg")
    await message.answer_photo(photo=photo_a, caption = f"""
                               
Ось ти:
username:{"@"+ message.from_user.username if message.from_user.username != None else None}
Імя:{message.from_user.first_name}
id:{message.from_user.id}
Бот:{"ні" if message.from_user.is_bot == False else "Так"}
Прізвище:{message.from_user.last_name}
Мова:{message.from_user.language_code}
Преміум:{message.from_user.is_premium}
Чи було вас додано: {message.from_user.added_to_attachment_menu}
""")
    