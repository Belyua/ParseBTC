import os

import ccxt
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


we = ccxt.wavesexchange()
we.load_markets()
ticker = we.fetch_ticker('BTC/USDT')
last_price = ticker['last']

token = os.environ.get("TOKEN")
#token = ''
bot = Bot(token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot,
                storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message):
    await message.answer(
        "Hi there! I am a BTC parser bot.\n"
        "Use the /check_price command to check \n"
        "BTC/USDT price.")


@dp.message_handler(commands=["check_price"])
async def send_text(message):

    try:
        await message.answer(f'{last_price}$')

    except Exception as ex:
        print(ex)
        await message.answer(
                "Damn...Something was wrong...")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

