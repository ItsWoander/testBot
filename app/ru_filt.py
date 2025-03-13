from aiogram import Router,types,F
import asyncio
from aiogram.types import Message, ChatPermissions
from aiogram.filters import Command,Filter
from app.func.stack_test import Chat
from app.Keyboard import rusofilt_kb
from app.func.stack_test import Filter_admin,Filter_type,Filter_admin_kb
import datetime
ru_filt = Router()




@ru_filt.message(Command('rufilt'),Filter_type(['group','supergroup']),Filter_admin())
async def ru_on(message:Message):
    c = Chat(message.chat.id)
    print(c.check_mode())
    await message.reply(f"РУСОФІЛЬТР - Забороніть користувачам з російским інтерфейсом писати повідомлення\n Статус:{"Увімкнено" if c.check_mode() else "Вимкнено" }", reply_markup=rusofilt_kb(c.check_mode()))


@ru_filt.callback_query(F.data.startswith('off_rusofilter'))
async def ru_off(callback: types.CallbackQuery):
    user = callback.from_user.id
    a = (Filter_admin_kb(user,callback.message.chat.id))
    result = await a(callback=callback)
    if not result:
        return 
    c = Chat(callback.message.chat.id)
    c.set_rufilt(False)
    print(c.check_mode())
    await callback.bot.edit_message_text(text=f'РУСОФІЛЬТР - Забороніть користувачам з російским інтерфейсом писати повідомлення\n Статус:Вимкнен', chat_id=callback.message.chat.id,message_id=callback.message.message_id)
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=rusofilt_kb(c.check_mode()))
    await callback.answer()
@ru_filt.callback_query(F.data.startswith('on_rusofilter'))
async def ru_on(callback: types.CallbackQuery):
    user = callback.from_user.id
    a = (Filter_admin_kb(user,callback.message.chat.id))
    result = await a(callback=callback)
    if not result:
        return     
    c = Chat(callback.message.chat.id)
    c.set_rufilt(True)
    print(c.check_mode())
    await callback.bot.edit_message_text(text=f'РУСОФІЛЬТР - Забороніть користувачам з російским інтерфейсом писати повідомлення\n Статус:Увімкнен', chat_id=callback.message.chat.id,message_id=callback.message.message_id)
    await callback.bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=rusofilt_kb(c.check_mode()))
    await callback.answer()

@ru_filt.message(F.text)
async def filt(message:Message):
    print(1)
    if message.chat.type != 'private':
        a = Chat(message.chat.id)
        if a.check_mode():
            print(1)
            if message.from_user.language_code == 'ru':
                await message.reply(f'{"@" + str(message.from_user.username) if message.from_user.username != None else message.from_user.full_name} спрацював русофільт. В вас виявлений інтерфейс роснявої\nВам заборонено розмовляти:10 хв')
                print(message)
                try:
                    untill_date = datetime.datetime.now() + datetime.timedelta(seconds=60*10)
                    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,)
                    print(message)
                    await message.bot.restrict_chat_member(message.chat.id, message.from_user.id, permissions, until_date=untill_date)
                    await message.bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
                except Exception as e:
                    await message.reply('Не вдалося заборонити')
                    print(e)
            