from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import (KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup)
BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(
        'Hi! My hame is Echo-bot!'
    )


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'White me something and i will send the reply'
    )


@dp.message()
async def send_echo(message: Message):
    await message.reply(text='bugaga')

if __name__ == '__main__':
    dp.run_polling(bot)
