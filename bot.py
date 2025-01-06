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




bot = Bot(token=config.API_TOK)
dp = Dispatcher()



async def main():
    dp.include_router(admin_router)
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())