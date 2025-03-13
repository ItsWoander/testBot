from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
import code
owner_command_rout = Router()
import json

@owner_command_rout.message(Command('send'))
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
                players_id = list([comand[1]])
                if players_id == ['all']:
                    with open('players.json', 'r') as file:
                        players = json.load(file)
                        print(players)
                        players_id = list(players['players'].keys())
                        players_chat = list(players['chats'].keys())
                        players_id += players_chat
                        print("                                         ")
                        print(players_id)
                        
                print(players_id)
                #повідомлення яке треба переслати
                replyy = message.reply_to_message
                wrong = 0
                right = 0
                #при просто тексті текст міститься в text, а якшо це опис фото то caption
                for player in players_id:
                    
                    try:
                        if not(replyy.text is None):
                            
                            await bot.send_message(chat_id=player, text=replyy.text)
                        elif not(replyy.photo is None ):
                            await bot.send_photo(chat_id=player,photo=replyy.photo[-1].file_id, caption=replyy.caption)
                        elif not(replyy.video is None):
                            await bot.send_video(chat_id=player,video=replyy.video.file_id, )
                   
                        else:
                            await message.reply('Не підтримуємий формат')
                        print(1)
                        right +=1
                    except Exception as e:
                        wrong +=1
                        print(e)
                await message.reply_animation('CgACAgQAAyEFAASNcZgUAAImjme8Y9XVzw1nAcCEiqCaerAE2WeLAAItAwACQYIMU0GpXC68J_7ONgQ')
                await message.reply(f"Вдало{right}\nНевдало:{wrong}")
            else:   
                await message.reply('Не правильний формат\nПравильний формат:\n/send 12345')
                
        else:
            await message.reply('Немає реплаю')
    else:
        await message.reply('Ви не розробник')
        
