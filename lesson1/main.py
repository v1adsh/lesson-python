from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

bot = Bot(token='7968373203:AAHV_utO29R5yupoK2S40y5XapWcfGTmGoM')
dp = Dispatcher(bot = bot)

@dp.message(Command('Start'))
async def echo(message: types.Message):
    await  message.answer(message.text)

if __name__ == '__main__':
    dp.start_polling(bot, skip_updates=True)

