from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
import code
import json
import random
from app.func.stack_test import Player,Chat,Filter_type, Filter_admin


fun_router = Router()

@fun_router.message(Command('profile'))
async def profile(message:Message):
    
    if message.reply_to_message != None:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user
    a = Player(user.id, user.full_name)
    check = a.check()
    try:
        money = check["money"]
        rep = check["rep"]
        await message.reply(f"""Профіль <a href="tg://user?id={user.id}">{user.full_name}</a>
Грошей : {money:,}
Репутація: {rep} \n В всесвіті кавуняки:{(datetime.now() - datetime.strptime(check['date_first'], "%d %m %Y")).days} Днів
                            """, parse_mode='HTML')
    except Exception as a:
        print(a)

@fun_router.message(Command('pay'))
async def pay(message:Message):
    print(len(list(message.text)), list(message.text))
    if len(message.text.split()) == 2:
        text = message.text.split()
        money_pay = int(text[1])
        if money_pay <= 0:
            await message.reply('Це все? Не витрачай мій час, гандон')
            return
        try:
            a = Player(message.from_user.id, message.from_user.full_name)
            b = Player(message.reply_to_message.from_user.id, message.reply_to_message.from_user.full_name)
            a_status = a.check()
            if a_status['money'] >= money_pay :
                a.minus(money_pay)
                b.plus(money_pay)
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
                a = Player(message.from_user.id, message.from_user.full_name)
                if a.check("money") >= money:
                    a = Player(message.from_user.id, message.from_user.full_name)
                    dicee = await message.reply_dice()
                    if dicee.dice.value == number:
                        await asyncio.sleep(4)
                        await message.reply(f'Випало число:{number}\nВи перемогли\nЗараховано:{int(money* 10)}')
                        a.plus(int(money * 10))
                    else:
                        await asyncio.sleep(4)
                        await message.reply(f'Випало число:{dicee.dice.value}\nВи програли')
                else:
                    await message.reply('В тебе немає стільки Грошей.\n Хочеш в борги залізти?')
        else:
            await message.reply('Цифра кубика повинна бути в діапозоні 1-6')
    elif len(text) == 1:
        await message.reply("Гра в кості, яка зробить тебе МІЛЬЙОНЕРОМ\n Формат гри:\n /dice (цифри кості) (ставка) \n /dice 5 100 ")
    
    else:
        await message.reply("Неправильний формат")
        
@fun_router.message(F.text.upper() == 'Бас'.upper())
async def ball(message:Message):
    data = await message.reply_dice(emoji='🏀')
    await asyncio.sleep(4)
    if data.dice.value == 3:
        await message.reply('Почти')
    elif data.dice.value == 5 or data.dice.value == 4:
        a = Player(message.from_user.id, message.from_user.full_name)
        num = random.randint(3400,8600)
        a.plus(num)
        await message.reply(f'Бінго\n +{num}')
    print(data.dice.value)

@fun_router.message(F.text.upper() == 'Фут'.upper())
async def football(message:Message):
    data = await message.reply_dice(emoji='⚽️')
    print( data.dice.value )
    await asyncio.sleep(4)

    if data.dice.value == 2 or data.dice.value==3 :
        await message.reply('Почти')
    elif data.dice.value == 5 or data.dice.value == 4:
        a = Player(message.from_user.id, message.from_user.full_name)
        num = random.randint(4000,7500)
        a.plus(num)
        await message.reply(f'Бінго\n +{num}')


@fun_router.message(F.text.upper() == 'Дар'.upper())
async def darts(message:Message):
    data = await message.reply_dice(emoji='🎯')
    print( data.dice.value )
    await asyncio.sleep(4)

    if data.dice.value == 5:
        await message.reply('Почти')
    elif data.dice.value == 6:
        a = Player(message.from_user.id, message.from_user.full_name)
        num = random.randint(3000,9500)
        a.plus(num)
        await message.reply(f'Ну ти снайпер\n +{num}')



@fun_router.message(F.text.upper() == 'Боу'.upper())
async def bole(message:Message):
    data = await message.reply_dice(emoji='🎳')
    print( data.dice.value )
    await asyncio.sleep(4)

    if data.dice.value == 5:
        await message.reply('Почти')
    elif data.dice.value == 6:
        a = Player(message.from_user.id, message.from_user.full_name)
        num = random.randint(4000,6000)
        a.plus(num)
        await message.reply(f'БІНГО\n +{num}')






@fun_router.message(Command('slot'))
async def slot(message:Message):
    text = message.text.split() 
    
    if len(text) == 2:
        money = int(text[1])
        if money < 10:
            await message.reply('Мінімальна ставка:10')
            return
        a = Player(message.from_user.id, message.from_user.full_name)
        a.minus(money)
        if a.check('money') >= money:
            a.minus(money)
            dicee = await message.reply_dice(emoji='🎰')
            print(dicee.dice.value)
            
            if dicee.dice.value in  [1, 22, 43]:
                await asyncio.sleep(3)
                await message.reply(f'Ви виграли x5\nЗараховано{money * 5}')
                a.plus(int(money * 5)) 
            elif dicee.dice.value in  [48,62,63, 61, 32,16]: #17
                await asyncio.sleep(3)
                await message.reply(f'Майже!\nВи виграли x8\nЗараховано{money * 8}')
                a.plus(int(money * 8))
            elif dicee.dice.value == 64:
                await asyncio.sleep(3)
                await message.reply(f'БІНГОООО! ВИ ВИГРАЛИ х20\nЗараховано{money * 20}')
                a.plus(int(money * 20))
  
                    


                        
        else:
            await message.reply('В тебе немає стільки Грошей.\n Хочеш в борги залізти?')
    elif len(text) == 1:
        await message.reply("Гра в Слоти, яка зробить тебе МІЛЬЯРДЕРОМ\n Формат гри:\n /slot (ставка) \n /dice 10000000 ")
    
    else:
        await message.reply("Неправильний формат")



@fun_router.message(F.text.upper() == '-'.upper())
async def plus_rep(message:Message):

    if message.reply_to_message != None:
        user_reply = message.reply_to_message.from_user.id
        if user_reply != message.from_user.id:
            a = Player(message.from_user.id, message.from_user.full_name)
            a.minus_rep()
            await message.reply(f"Дії {message.reply_to_message.from_user.first_name} не сподобалась народу\nРепутація {message.reply_to_message.from_user.first_name}:{a.check('rep')}")
        else:
            await message.reply_animation('CgACAgQAAyEFAASNcZgUAAIcTmezH-MVxPXm3biAQ3jNfm1D6iDHAAL3AgACVJd1UzDnjQt-fxw0NgQ', caption='.....')


@fun_router.message(F.text.upper() == '+'.upper())
async def minus_rep(message:Message):
    
    if message.reply_to_message != None:
        user_reply = message.reply_to_message.from_user.id
        if user_reply != message.from_user.id:
            print(user_reply,message.from_user.id)
            print(user_reply == message.from_user.id)
            a = Player(message.from_user.id, message.from_user.full_name)
            a.plus_rep()
            await message.reply(f"{message.reply_to_message.from_user.first_name} підіймається в очах народу\nРепутація {message.reply_to_message.from_user.first_name}:{a.check('rep')}")
        else:
            print(1)
            await message.reply_animation('CgACAgQAAyEFAASNcZgUAAIcUWezIAqh2tTuTzqoMjFdZ2nRgJjaAALBsgACthtkBxnPsQ9-GI8KNgQ', caption='Так не можно')

@fun_router.message(F.text.upper().find('+RULES') != -1, )
async def add_rules(message:Message):
    if message.chat.type != 'private': #перевірка чи є група
        rules = message.text
        rules = rules.split()
        rules = rules[1:]
        rules_text = ' '.join(rules)
        a = Chat(int(message.chat.id))
        a.set_rule(rules_text)
        await message.reply('Успішно')

@fun_router.message(F.text.upper() == '-RULES')
async def add_rules(message:Message):
    if message.chat.type != 'private':
        c = Chat(int(message.chat.id))
        c.del_rule()
        await message.reply("Правила прибрані")

    
@fun_router.message(F.text.upper() == 'RULES')
async def rules(message:Message):
    if message.chat.type != 'private':
        c = Chat(int(message.chat.id))
        if not(c.info_rule() is None):
            await message.reply(f"Правила цього чату:\n{c.info_rule()}")
        else:
            await message.reply(f"Правил немає\nЩоб додати правила використовуй +rules (правила)")


@fun_router.message(Command('admins'))

async def admins_list(message:Message):
    try:
        admins = await message.bot.get_chat_administrators(message.chat.id)
        text = 'Адміністрація цього чату:\n'
        for i in admins:
            text += f"""<a href='tg://openmessage?user_id={i.user.id}'>{i.user.full_name}</a>\n"""
        await message.reply(text=text, parse_mode='HTML')
    except Exception as e:
        print(f"адмін {e}")


@fun_router.message(Command('stats'))
async def stats(message:Message):
    a = Player(message.from_user.id, message.from_user.full_name)
    stats = a.stats_money()
    text = 'Топ багачів бота:\n'
    if len(stats) < 10:
        for i in stats:
            text += f"""<a href='tg://openmessage?user_id={i[1]}'>{i[2]}</a> - {i[0]:,} \n"""
        await message.reply(text,parse_mode='HTML')
    else:
        stats = stats[:10]
        for i in stats:
            text += f"""<a href='tg://openmessage?user_id={i[1]}'>{i[2]}</a> - {i[0]:,} \n"""
        await message.reply(text,parse_mode='HTML')


@fun_router.message(F.text == "зп")
async def zp(message:Message):
    a = Player(message.from_user.id,message.from_user.full_name)
    if a.last_using_zp():
        money = random.randint(30000,60000)
        if await a.subscribe(message):  
            a.plus(money*2)
            await message.reply(f'Ви отримали {money*2}')
        else:
            a.plus(money)
            await message.reply(f'Ви отримали {money} \n Підписники республіки отримують х2 нагороди')
    else:
        await message.reply('Нагороду можна отримати раз в день')