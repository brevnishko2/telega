from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from qwe import get_text, add_brat
import random
import datetime


TOKEN = "6109198023:AAFpGVo-FFNeY2l4JvreXrNgnsx249wmli4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
keyboard = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='Дай цитату, брат')],
        [types.KeyboardButton(text='Сколько время, брат?')],
        [types.KeyboardButton(text='Битва ебланов')]])


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(
        f'Привет, я первый бот, которого сделал Серго Сергоевич. {msg.from_user.first_name},'
        f' мне очень приятно с тобой познакомиться. Уверен, мы поладим с тобой.', reply_markup=keyboard)


@dp.message_handler(regexp='Битва ебланов')
async def send_welcome(msg: types.Message):
    await msg.answer(
        f'Пока не реализовано', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Дарова, заэбал!')
    elif msg.text == 'Дай цитату, брат':
        await msg.answer(random.choice(add_brat(get_text('text.txt'))), reply_markup=keyboard)
    elif msg.text == 'Сколько время, брат?':
        d = datetime.datetime.now()
        await msg.answer(f"{d.hour}:{d.minute}, Брат!", reply_markup=keyboard)
    else:
        await msg.answer("казахстан, брат!", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
