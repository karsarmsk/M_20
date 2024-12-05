import aiogram
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputMediaPhoto
import os
import config
import database
import datetime
from datetime import date
from datetime import datetime
from test import keyboard_callback

api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    incity_b = State()
    country_b = State()
    vzr_b = State()
    deti_b = State()
    hotel_b = State()
    pitanie_b = State()
    nochi_b = State()
    name_b = State()
    email_b = State()

import handlers.Start
import handlers.Category
import handlers.Admin
d = date.today()
day = d.strftime("%d/%m/%Y")
current_time = datetime.now().time()

text = open("files\Zayavka.txt",'w',encoding='utf-8')
text.write(f'{day} Заявка для подбора тура\n ')
text.close()
dp.message_handler(lambda m: database.check_block(m.from_user.id))(handlers.Start.ban_message)
dp.callback_query_handler(lambda c: database.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)

dp.message_handler(commands=['start'])(handlers.Start.start)

dp.message_handler(Text(equals=['ℹ️ О нас']))(handlers.Start.about_as)

dp.message_handler(Text(equals=['✈️Поехали']))(handlers.Category.incity)

dp.message_handler(state= UserState.incity_b)(handlers.Category.handle_city_input)
# dp.message_handler(Text(equals=['✉️ Подать заявку']))(handlers.Category.zajavka)

dp.callback_query_handler(Text(equals='Москва'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Санкт Петербург'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Нижний Новгород'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Екатеринбург'),state= UserState.incity_b)(handlers.Category.country)

dp.message_handler(state= UserState.country_b)(handlers.Category.handle_country_input)

dp.callback_query_handler(Text(equals='Турция'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Египет'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Тайланд'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='ОАЭ'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Россия'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Китай'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Абхазия'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Вьетнам'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Шри-Ланка'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals='Мальдивы'),state= UserState.country_b)(handlers.Category.vzr)
#
#
dp.callback_query_handler(Text(equals='🧍1 человек'),state= UserState.vzr_b)(handlers.Category.deti)
dp.callback_query_handler(Text(equals='2 человека'),state= UserState.vzr_b)(handlers.Category.deti)
dp.callback_query_handler(Text(equals='3 человека'),state= UserState.vzr_b)(handlers.Category.deti)
dp.callback_query_handler(Text(equals='4 человека'),state= UserState.vzr_b)(handlers.Category.deti)
dp.callback_query_handler(Text(equals='5 человек'),state= UserState.vzr_b)(handlers.Category.deti)
dp.callback_query_handler(Text(equals='6 человек'),state= UserState.vzr_b)(handlers.Category.deti)


dp.callback_query_handler(Text(equals='Без детей'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='1 человечек'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='2 человечка'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='3 человечка'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='4 человечка'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='5 человечков'),state= UserState.deti_b)(handlers.Category.hotel)
dp.callback_query_handler(Text(equals='6 человечков'),state= UserState.deti_b)(handlers.Category.hotel)


dp.callback_query_handler(Text(equals='*'),state= UserState.hotel_b)(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals='**'),state= UserState.hotel_b)(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals='***'),state= UserState.hotel_b)(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals='****'),state= UserState.hotel_b)(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals='*****'),state= UserState.hotel_b)(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['🔙Назад']))(handlers.Category.country)

dp.callback_query_handler(Text(equals='любое'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals='все включено'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals='завтрак'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals='завтрак, ужин'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals='завтрак, обед, ужин'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals='ультра все включено'),state= UserState.pitanie_b)(handlers.Category.nochi)
dp.callback_query_handler(Text(equals=['🔙Назад']))(handlers.Category.country)

dp.callback_query_handler(Text(equals='6-8'),state= UserState.nochi_b)(handlers.Category.nochi_v)
dp.callback_query_handler(Text(equals='9-11'),state= UserState.nochi_b)(handlers.Category.nochi_v)
dp.callback_query_handler(Text(equals='12-14'),state= UserState.nochi_b)(handlers.Category.nochi_v)
dp.callback_query_handler(Text(equals=['🔙Назад']))(handlers.Category.country)

dp.message_handler(state= UserState.nochi_b)(handlers.Category.handle_name_input)

dp.message_handler(state= UserState.name_b)(handlers.Category.handle_email_input)



dp.message_handler(Text(equals=['Подать заявку']))(handlers.Category.zayavka)

dp.message_handler(Text(equals=['Редактировать']))(handlers.Category.incity)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)