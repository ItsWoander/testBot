from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
import code
router = Router()
import json

@router.message(CommandStart())
async def start(message:Message):
    with open(r"D:\pyth\BOTT\app\players.json", 'r+') as data:
        bd = json.load(data)
        bd['players'].setdefault(str(message.from_user.id), {'rep': 5, 'money': 1000})
        data.seek(0)
        json.dump(bd,data,indent=2)




    await message.answer('Я вмію банить і мутить)))) Ну і інформація про тебе "Хто я" ')


@router.message(Command('code'))
async def help(message: Message):
    await message.reply(f"Github : https://github.com/ItsWoander/testBot ")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer('допомога')




@router.message(Command('send'))
async def send(message:Message):
    #адмінська команда
    if message.from_user.id in config.Owner_players:
        print(1)
        if message.reply_to_message != None:
            from bot import bot
            comand = message.text
            comand = comand.split()
            comand = list(comand)
            if len(comand) == 2:
                print(2)
                id_chat = comand[1]
                print(id_chat)
                #повідомлення яке треба переслати
                replyy = message.reply_to_message
                #при просто тексті текст міститься в text, а якшо це опис фото то caption
                if not(replyy.text is None):
                    print(replyy.text)
                    await bot.send_message(chat_id=id_chat, text=replyy.text)
                elif not(replyy.photo is None ):
                    await bot.send_photo(chat_id=id_chat,photo=replyy.photo[-1].file_id, caption=replyy.caption)
                elif not(replyy.video is None):
                    await bot.send_video(chat_id=id_chat,video=replyy.video.file_id, )
                   
                else:
                    await message.reply('Не підтримуємий формат')
                await message.reply_animation('CgACAgQAAyEFAASNcZgUAAIC92euVxroffStwY2Pl2JhlWgoJCO2AAItAwACQYIMUxqAY7aLlNjMNgQ')
            else:
                await message.reply('Не правильний формат\nПравильний формат:\n/send 12345')
        else:
            await message.reply('Немає реплаю')
    else:
        await message.reply('Ви не адмін. ФУУУУУУ🤮🤮🤮🤮🤮🤮🤮')
        


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