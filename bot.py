from aiogram import Bot,Dispatcher, F,types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
from app.handlerq import router
import app.Keyboard
from app.admin_handler import admin_router
import datetime

import logging


bot = Bot(token=config.API_TOK)
dp = Dispatcher()




@dp.message(Command("gif"))
async def gif_handler(message: Message):
    if message.reply_to_message and message.reply_to_message.animation:
        gif_id = message.reply_to_message.animation.file_id
        await message.reply(f"ID цієї GIF: {gif_id}")
        print(gif_id)
    else:
        await message.reply("Будь ласка, відповідайте на GIF, щоб отримати його ID.")


async def main():
    while True:
        try:
            dp.include_router(admin_router)
            dp.include_router(router)
            await dp.start_polling(bot)
        except Exception as e:
            print(e)
    



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            logging.exception("Критична помилка, перезапускаємо бот...")
            asyncio.sleep(5)  # Затримка перед перезапуском