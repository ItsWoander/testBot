from aiogram import Bot,Dispatcher, F,types
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import config
from datetime import datetime
from app.handlerq import router
import code
import app.Keyboard
from app.admin_handler import admin_router
import datetime

import logging


bot = Bot(token=config.API_TOK)
dp = Dispatcher()




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