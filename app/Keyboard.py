from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phone_skam = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/start', request_contact=True)]],resize_keyboard=True)



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=" Модерація", callback_data="mod_pressed"),
      InlineKeyboardButton(text="Ігрові", callback_data="game_pressed")],
      [InlineKeyboardButton(text="Фансервіс", callback_data="fun_pressed")]
])


def kb_report(user1, user2, chat_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔨 Бан порушнику", callback_data=f"bankb1_{user1}_{user2}_{chat_id}"),
         InlineKeyboardButton(text="🤐 Мут порушнику", callback_data=f"mutekb1_{user1}_{user2}_{chat_id}")],
        [InlineKeyboardButton(text="🔨 Бан відправнику", callback_data=f"bankb2_{user1}_{user2}_{chat_id}"),
         InlineKeyboardButton(text="🤐 Мут відправнику", callback_data=f"mutekb2_{user1}_{user2}_{chat_id}")],
        [InlineKeyboardButton(text="⏭ Пропустити", callback_data="pass_kb")]
    ])

def rusofilt_kb(mode:bool, ):
    if mode:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"[☒] Вимкнути",callback_data=f"off_rusofilter")]])
    else:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"[☑] Увімкнути",callback_data=f"on_rusofilter")]])

def language():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"🇺🇦",callback_data=f"ua_language"),InlineKeyboardButton(text=f"🏴 Інші",callback_data=f"ua_language")]])
