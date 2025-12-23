from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
import asyncio

bot = Bot('8208985752:AAFQaRe8fqZNXAd_-qLdS0os2TyjXJlNNLM')
dp = Dispatcher()
router = Router()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())