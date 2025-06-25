import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import router
from config import TG_TOKEN

async def main():
    # Задаётся токен
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    # Начало приёма запросов
    await dp.start_polling(bot)

# Чтоб не запускалось по несколько раз + Выключение

if __name__ == '__main__':
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Bot off')