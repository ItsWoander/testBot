from aiogram import Bot,Dispatcher, F,types,Router
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ChatMember, ChatPermissions, InputFile
import config
from datetime import datetime
import datetime
from app.Keyboard import kb_report
from app.func.stack_test import Filter_type, Filter_admin
import code
#from aiogram.types import ParseMode


admin_router = Router()

@admin_router.message(Command('ban'),Filter_type(["group", "supergroup"]),Filter_admin())
async def ban(message:Message):

        if message.reply_to_message != None: #перевірка чи є реплай

            try:
                await message.message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await message.reply(f'Кориcтувача {message.reply_to_message.from_user.first_name} було заблоковано')
                try:
                    await message.message.bot.send_message(message.reply_to_message.from_user.id, f"Вас було заблоковано у чаті {message.chat.title}\n Посилання:{"@"+str(message.chat.username) if message.chat.username != None else 'None' }")
                except:
                    pass
                # обробник помилки, якщо блокнуть бота, або користувач немає пп з цим ботом
            except Exception as e:
                
                await message.reply('Не можна заблокувати адміна')


            #відсилаємо користувачу повідомлення в лс
            try:
                await message.message.bot.send_message(message.reply_to_message.from_user.id, f"Вас було заблоковано у чаті {message.chat.title}\n Посилання:{"@"+str(message.chat.username) if message.chat.username != None else 'None' }")
            except Exception as r:
                pass # обробник помилки, якщо блокнуть бота, або користувач немає пп з цим ботом
        else:
            await message.reply('Команда /ban - додасть користувача у чорний список')

@admin_router.message(Command('unban'),Filter_type(["group", "supergroup"]),Filter_admin())
async def unban(message:Message):
    if message.reply_to_message != None: #перевірка чи є реплай

            
        

            try:
                await message.bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id, only_if_banned=True)
                await message.reply(f'Користувача {message.reply_to_message.from_user.first_name} було розблковано')
            
            except BaseException as e:
                await message.reply(f'Не можна заблокувати адміна')
            
            try:
                await message.bot.send_message(message.reply_to_message.from_user.id, f"Вас було розблоковано у чаті {message.chat.title}\n Посилання:{"@"+str(message.chat.username) if message.chat.username != None else 'None' }")
            except Exception as r:
                pass # обробник помилки, якщо блокнуть бота, або користувач немає пп з цим ботом
    else:
            
            await message.reply('Команда /unban - видалить користувача з чорного списку')




'''
Мут
'''










@admin_router.message(Command('mute'),Filter_type(["group", "supergroup"]),Filter_admin())
async def mute(message:Message):
    if message.reply_to_message != None: #перевірка чи є реплай

            id_user_reply =  message.reply_to_message.from_user.id #юзер користувача в реплаї
            # Отримуємо інформацію про адмінів
            

            #якшо реплайнули на бота
            infobot = await message.bot.get_me()
            if id_user_reply == infobot.bot.id:
                await message.reply_animation('CgACAgIAAxkBAAICuGesk9DsFcsEXkTcOMYvXkMR75QjAAKdcAACxnwoSINS985tgdYCNgQ')
                return
        
                
                
            text = message.text
            text = text.split()
            text = list(text)
            if len(text) == 1:
                print("вхід")
                time_mute_format = 283939393
            elif len(text) == 2:
                int_mute = text[1][:-1]
                if any(letter in text[1] for letter in ['h', 's', 'm', 'd']):
                    if int(int_mute) <= 0:
                        await message.reply('Час повинен бути додатнім')
                        return
                            
                    if 'h' in text[1] :
                        print(1)
                        time_mute_format = 60 * 60 * int(int_mute)
                    elif 'd' in text[1] :
                        time_mute_format = 60 * 60 * 24 * int(int_mute)
                    elif 'm' in text[1]:
                        time_mute_format = 60 * int(int_mute)
                    elif 's' in text[1]:
                        if int(int_mute) <= 31:
                            time_mute_format = 31
                        else:
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
            try:
                    


                        
                
                
                
                untill_date = datetime.datetime.now() + datetime.timedelta(seconds=time_mute_format)
                

                permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,)
                
                await message.bot.restrict_chat_member(message.chat.id, id_user_reply, permissions, until_date=untill_date)
                await message.reply(f'Користувачу заборонено розмовляти \nТривалість:{text[1] if len(text) == 2 else "∞"}')
            except:
                await message.reply_animation('CgACAgIAAxkBAAICuGesk9DsFcsEXkTcOMYvXkMR75QjAAKdcAACxnwoSINS985tgdYCNgQ', caption='Не можна замутити адміна')
  




            else:
                await message.reply("У вас немає прав ")
                return
            

    else:
            await message.reply("Затулити пельку: Заборонить користувачу розмовляти:\n s-секунда m-хвилина h-години d-дні \n/mute 1s /mute 2m /mute 3h /mute 4d")




@admin_router.message(Command('unmute'),Filter_type(["group", "supergroup"]),Filter_admin())
async def unmute(message:Message):
        if message.reply_to_message != None: #перевірка чи є реплай

            id_user_reply =  message.reply_to_message.from_user.id #юзер користувача в реплаї
            # Отримуємо інформацію про адмінів
            admins = await message.bot.get_chat_administrators(message.chat.id)

            
            permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,)
            await message.bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id, permissions)
            await message.reply('Користувачу дозволено базікати')
        else:
            await message.reply('Немає реплаю')




@admin_router.message(Command('report'),Filter_type(["group", "supergroup"]))
async def report(message:Message):
    text = message.text
    text = text.split()
    if len(text) == 1 or len(text) >= 2:
        if len(text) == 1:
            comment = 'Немає'
        elif len(text) >= 2:
            comment = text[1:]
            comment = " ".join(comment)
        else:
            await message.reply('Неправильний формат')
            return
        if message.chat.type != 'private': #перевірка чи є група
            if message.reply_to_message != None: #перевірка чи є реплай
                us1 = message.reply_to_message.from_user # той на кого відправили
                us2 = message.from_user #той хто відправив
                infobot = await message.bot.get_me()
                if us2.id == us1.id:
                        await message.reply('Навіщо відправляти репорт на самого себе?')
                        return
                if us1.id == infobot.bot.id:
                    await message.reply('...')
                    return
                admins = await message.bot.get_chat_administrators(message.chat.id)
                id_message = message.reply_to_message.message_id
                for admin in admins:
                    if admin.user.id == us1:
                        await message.reply('Помилка: Переконайтесь що ви не відправляєте репорт на адміністрацію')
                        return
                    


                await message.reply('Скарга на порушника відправлена.Очікуйте розгляд адміністрації')
            
                for admin in admins:
                    if not admin.user.is_bot:
                        try:
                            admin_id = admin.user.id  # Отримуємо ID адміністратора
                            await message.message.bot.forward_message(admin_id, message.chat.id, id_message)

                            await message.message.bot.send_message(chat_id=admin_id, text=f"""
                                                           📢 <b>Отримана скарга:</b>\n
👤 <b>Відправник:</b> {us2.full_name}\n
⚠ <b>Порушник:</b> {us1.full_name}\n
📝 <b>Коментар:</b> {comment}""",
                                parse_mode="HTML",
                                reply_markup = kb_report(us1.id, us2.id, message.chat.id))
                        except Exception as e:
                            print(f"❌ Адміністратор {admin_id} заблокував бота. Пропускаємо.{e}")
                    
                await message.message.bot.delete_message(message.chat.id ,id_message)
#, reply_markup = kb_report(us1, us2, message.chat.id)



@admin_router.callback_query(lambda c: c.data.startswith("bankb1"))
#бан порушника
async def rep_ban_1(callback: types.CallbackQuery):
    print(callback.data)
    try:
        _, user1, user2,chat_id =  callback.data.split("_")
        user1 = int(user1) # ПОРУШНИК
        user2 = int(user2) # ВІДПРАВНИК
        #chat_id = int(chat_id)
        admins = await callback.bot.get_chat_administrators(chat_id)
        print(user1,user2,chat_id)
        for admin in admins:
            admin_check = admin.user.id
            if admin_check == user1:
                await callback.answer(F'Неможливо видати вирок адміністратору', show_alert=True)
                return
        await callback.message.bot.ban_chat_member(chat_id, user1)
        await callback.message.bot.send_message(chat_id=chat_id, text=f'Вирок затверджен адміністатором:<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>. Порушник отримав БАН',parse_mode='HTML')
        for admin in admins:
            if not admin.user.is_bot:
                await callback.message.bot.send_message(chat_id=admin.user.id, text=f'Вирок затверджен адміністатором:<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>. Порушник отримав БАН',parse_mode='HTML')


        await callback.answer()  # Закриваємо анімацію завантаження
    except Exception as a:
        print(a)

@admin_router.callback_query(lambda c: c.data.startswith("bankb2"))
#бан відправника
async def  rep_ban_2(callback: types.CallbackQuery):
    print(callback.data, 1)
    try:
        _, user1, user2,chat_id =  callback.data.split("_")
        user1 = int(user1) # ПОРУШНИК
        user2 = int(user2) # ВІДПРАВНИК
        chat_id = int(chat_id)
        print(user1,user2,chat_id)
        admins = await callback.message.bot.get_chat_administrators(chat_id)
        
        for admin in admins:
            admin_check = admin.user.id
            if admin_check == user2:
                await callback.answer(F'Неможливо видати вирок адміністратору', show_alert=True)
                return
        await callback.message.bot.ban_chat_member(chat_id, user2)
        await callback.message.bot.send_message(chat_id=chat_id, text=f'Вирок затверджен адміністратором:<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>. Відправник отримав БАН',parse_mode='HTML')
        for admin in admins:
            if not admin.user.is_bot:
                await callback.message.bot.send_message(chat_id=admin.user.id, text=f'Вирок затверджен адміністратором<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>. Відправник отримав БАН',parse_mode='HTML')

        
        print(user2)
        await callback.answer()  # Закриваємо анімацію завантаження
    except Exception as a:
        print(a)
    
@admin_router.callback_query(lambda c: c.data.startswith("mutekb1"))
#мут порушнику
async def button_1(callback: types.CallbackQuery):
    try:
        _, user1, user2,chat_id =  callback.data.split("_")
        user1 = int(user1) # ПОРУШНИК
        user2 = int(user2) # ВІДПРАВНИК
        chat_id = int(chat_id)
        print(user1,user2,chat_id)
        admins = await callback.message.bot.get_chat_administrators(chat_id)
        
        for admin in admins:
            admin_check = admin.user.id
            if admin_check == user1:
                await callback.answer(F'Неможливо видати вирок адміністратору', show_alert=True)
                return 
        
        permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,)
        
        untill_date = datetime.datetime.now() + datetime.timedelta(seconds=60 * 60 * 12)

        await callback.message.bot.restrict_chat_member(chat_id, user1, permissions, until_date=untill_date)
        await callback.message.bot.send_message(chat_id=chat_id, text=f'Вирок затверджен адміністратором:<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>.Порушник отримав мут', parse_mode='HTML')
        for admin in admins:
            if not admin.user.is_bot:
                await callback.message.bot.send_message(chat_id=admin.user.id, text=f'Вирок затверджен адміністратором:<a href="tg://openmessage?user_id={callback.from_user.id}">{callback.from_user.full_name}</a>.Порушник отримав мут', parse_mode='HTML')
        await callback.answer()  
    except Exception as a:
        print(a)
    await callback.answer()  # Закриваємо анімацію завантаження

@admin_router.callback_query(lambda c:c.data.startswith("mutekb2"))
async def button_1(callback: types.CallbackQuery):
#мут відправнику
    try:
        _, user1, user2,chat_id =  callback.data.split("_")
        user1 = int(user1) # ПОРУШНИК
        user2 = int(user2) # ВІДПРАВНИК
        chat_id = int(chat_id)
        print(user1,user2,chat_id)
        admins = await callback.message.bot.get_chat_administrators(chat_id)
        
        for admin in admins:
            admin_check = admin.user.id
            if admin_check == user2:
                await callback.answer(F'Неможливо видати вирок адміністратору', show_alert=True)
                await callback.answer()  
                return 
        
        permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,)
        
        untill_date = datetime.datetime.now() + datetime.timedelta(seconds=60 * 60 * 12)

        await callback.message.bot.restrict_chat_member(chat_id, user2, permissions, until_date=untill_date)

        await callback.message.bot.send_message(chat_id=chat_id, text='Вирок затверджен.Відправник отримав мут')
        for admin in admins:
            if not admin.user.is_bot:
                await callback.message.bot.send_message(chat_id=admin.user.id, text=f'''Вирок затверджен адміністрацією:<a href='tg://openmessage?user_id={callback.from_user.id}'>{callback.from_user.full_name}</a>.Відправник отримав мут''', parse_mode='HTML')
        await callback.answer()  
    except Exception as a:
        print(a)

    await callback.answer()  # Закриваємо анімацію завантаження # Закриваємо анімацію завантаження 


@admin_router.callback_query(lambda c:c.data.startswith("pass_kb"))
async def button_1(callback: types.CallbackQuery):
    id_message = callback.message.message_id
    await callback.message.bot.delete_message(callback.message.chat.id ,id_message)