from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
import config

import asyncio

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer_invoice(
        title="Buying the course",
        description="Buying the David`s course",
        payload="invoice",
        provider_token=config.PAYMENT_TOKEN,
        currency="USD",
        prices=[
            types.LabeledPrice(label="Buying the course", amount=5 * 100)
        ]
    )

@router.message(F.successful_payment)
async def success(message: types.Message):
    await message.answer(f'Success:{message.successful_payment.order_info}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())