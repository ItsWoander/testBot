from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phone_skam = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/start', request_contact=True)]],resize_keyboard=True)