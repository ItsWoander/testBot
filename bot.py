from aiogram import Bot,Dispatcher, F,types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
from app.func.stack_test import create_json 
create_json()
from app.handlerq import router
import code
import app.Keyboard
from app.admin_handler import admin_router
import datetime
from app.fun import fun_router
import logging
from app.owner_command import owner_command_rout
from app.ru_filt import ru_filt 
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.DEBUG)
create_json() # перевірка наявності players.json при не наявності создає його
try:
    load_dotenv('config.env')
    bot = Bot(token=os.getenv("API_TOK"))
    dp = Dispatcher()
except:
     raise FileNotFoundError("Немає config.env")


@dp.message(Command("gif"))
async def gif_handler(message: Message):
    if message.reply_to_message and message.reply_to_message.animation:
        gif_id = message.reply_to_message.animation.file_id
        await message.reply(f"ID цієї GIF: {gif_id}")
        print(gif_id)
    else:
        await message.reply("Будь ласка, відповідайте на GIF, щоб отримати його ID.")


async def main():

        try:
            dp.include_router(admin_router)
            dp.include_router(router)
            dp.include_router(fun_router)
            dp.include_router(owner_command_rout)
            dp.include_router(ru_filt)
            await dp.start_polling(bot)
        except Exception as e:
            print(e)




if __name__ == "__main__":
    create_json() # перевірка наявності players.json при не наявності создає його
    asyncio.run(main())

