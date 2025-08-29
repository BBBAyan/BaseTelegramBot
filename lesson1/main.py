import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.database.models import async_main

from config import TOKEN_API
from app.handlers import router

async def main():
    await async_main()
    bot = Bot(TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
