import aiogram
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputMediaPhoto

import config
import database


api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Ответы на сообщения
# _______________________________________________________________________________________
# @dp.message_handler(text= ['Urban','ff'])
# async def urban_message(message):
#     print('urban_message')
#     await message.answer('urban_message!!!')
#
@dp.message_handler(commands= ['start'])
async def start_message(message):
    print("start_message")
    await message.answer('Рады вас видеть в нашем боте')

# @dp.message_handler()
# async def all_message(message):
#     print("Мы получили сообщение")
#     await message.answer(message.text.upper())
# _________________________________________________________________________________________

# машина состояний позволяет собирать данные с пользователей сохранять и использовать далее
# __________________________________________________________________
class UserState(StatesGroup):
    adress = State()


# dp.callback_query_handler(CommandHandler("Москва", sity))
# dp.callback_query_handler(Text(equals=['Москва']))(handlers.Category.country)
# dp.callback_query_handler(CallbackQueryHandler(keyboard_callback))
async def sity(update, context):
    keyboard = [
        [InlineKeyboardButton("Москва", callback_data='Москва')],
        [InlineKeyboardButton("Санкт петербург 1", callback_data='Санкт петербург')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_reply_text = 'Нажмите на клавишу'
    update.message.reply_text(message_reply_text, reply_markup=reply_markup)


async def keyboard_callback(update, context):
    query = update.callback_query
    print('query.data:', query.data)
    query.answer(f'Выберите: {query.data}')


@dp.message_handler(text= "Заказать")
async def buy(message):
    await message.answer("Отправь нам свой адрес, пожалуйста")
    await UserState.adress.set()

@dp.message_handler(state= UserState.adress)
async def fsm_handler(message, state):
    await state.update_data(first = message.text)
    data = await state.get_data()
    ad = data['first']
    print(ad)
    await message.answer(f"Доставка будет отправлена на {data['first']}")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)