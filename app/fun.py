from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
import code
import json
fun_router = Router()

@fun_router.message(Command('profile'))
async def profile(message:Message):
    
    if message.reply_to_message != None:
        user = message.reply_to_message.from_user.id 
    else:
        user = message.from_user.id
    with open(r"D:\pyth\BOTT\app\players.json", 'r', encoding='UTF-8') as data:
        try:
            bd["players"][str(message.from_user.id)]['money']
        except:
            await message.reply('Ваш профіль не активований\nДля активації напишість /start')
            return
        try:
            bd = json.load(data)
            await message.reply(f"""
                            Грошей : {bd['players'][str(user)]['money']}
Репутація: {bd['players'][str(user)]['rep']}
                            """)
        except:
            await message.reply('Профіль не активований\nдля активації введи /start')

@fun_router.message(Command('pay'))
async def pay(message:Message):
    print(len(list(message.text)), list(message.text))
    if len(message.text.split()) == 2:
        text = message.text.split()
        money_pay = int(text[1])
        if money_pay <= 0:
            await message.reply('Це все? Не витрачай мій час, гандон')
            return
        
        with open(r"D:\pyth\BOTT\app\players.json", 'r+', encoding='UTF-8') as data:
            bd = json.load(data)
            print(1)
            try:
                bd["players"][str(message.from_user.id)]['money']
                print(2)
            except:
                await message.reply('Ваш профіль не активований\nДля активації напишість /start')
                return
            try:
                    
                if bd["players"][str(message.from_user.id)]['money'] >= money_pay :
                    bd["players"][str(message.from_user.id)]['money'] -= money_pay
                    bd['players'][str(message.reply_to_message.from_user.id)]['money'] += money_pay
                
                    data.seek(0)
                    data.truncate()
                    json.dump(bd,data,indent=2)
                
                    await message.reply("Успішно")
                else:
                    await message.reply_animation('CgACAgIAAxkBAAICuGesk9DsFcsEXkTcOMYvXkMR75QjAAKdcAACxnwoSINS985tgdYCNgQ', caption='У вас немає стільки грошей')
            except Exception as e:
                await message.reply(f'Щось пішло не так:{e}')
    else:
        await message.reply('Неправильний формат')



@fun_router.message(Command('dice'))
async def profile(message:Message):
    text = message.text.split() 
    
    if len(text) == 3:
        money = int(text[2])
        if money < 10:
            await message.reply('Мінімальна ставка:10')
            return
        number = int(text[1])
        if number <=6:
            with open(r"D:\pyth\BOTT\app\players.json", 'r+', encoding='UTF-8') as data:
                bd = json.load(data)
                try:
                    bd["players"][str(message.from_user.id)]['money']
                except:
                    await message.reply('Ваш профіль не активований\nДля активації напишість /start')
                    return
                if bd["players"][str(message.from_user.id)]['money'] >= money:
                    bd["players"][str(message.from_user.id)]['money'] -= money
                    data.seek(0)
                    data.truncate()
                    json.dump(bd,data,indent=2)
                    dicee = await message.reply_dice()
                    if dicee.dice.value == number:
                        await asyncio.sleep(4)
                        await message.reply(f'Випало число:{number}\nВи перемогли\nЗараховано:{int(money* 10)}')
                        bd["players"][str(message.from_user.id)]['money'] += int(money * 10)
                    else:
                        await asyncio.sleep(4)
                        await message.reply(f'Випало число:{dicee.dice.value}\nВи програли')
                        
                    data.seek(0)
                    data.truncate()
                    json.dump(bd,data,indent=2)
                else:
                    await message.reply('В тебе немає стільки Грошей.\n Хочеш в борги залізти?')
        else:
            await message.reply('Цифра кубика повинна бути в діапозоні 1-6')
    elif len(text) == 1:
        await message.reply("Гра в кості, яка зробить тебе МІЛЬЙОНЕРОМ\n Формат гри:\n /dice (цифри кості) (ставка) \n /dice 5 100 ")
    
    else:
        await message.reply("Неправильний формат")
        
