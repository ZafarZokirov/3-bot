import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5289904004:AAEiZ8ow_3WbVbz_5CWkqt-2w-9c6XWINsA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5289904004:AAEiZ8ow_3WbVbz_5CWkqt-2w-9c6XWINsA")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("bizning menu\nSomsa\nManti\nShashlik")


@dp.message_handler(text="somsa")
async def somsa(message: types.Message):
    await  message.reply("Somsa 3000 som")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)