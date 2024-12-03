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


import handlers.Start
import handlers.Category



dp.message_handler(lambda m: database.check_block(m.from_user.id))(handlers.Start.ban_message)
dp.callback_query_handler(lambda c: database.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)

dp.message_handler(commands=['start'])(handlers.Start.start)

dp.message_handler(Text(equals=['ℹ️ О нас']))(handlers.Start.about_as)

dp.message_handler(Text(equals=['✈️Поехали']))(handlers.Category.incity)


dp.callback_query_handler(Text(equals='m'),state= UserState.incity_b)(handlers.Category.country)
# dp.callback_query_handler(Text(equals='Москва'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Санкт Петербург'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Нижний Новгород'),state= UserState.incity_b)(handlers.Category.country)
dp.callback_query_handler(Text(equals='Екатеринбург'),state= UserState.incity_b)(handlers.Category.country)

dp.callback_query_handler(Text(equals='Турция'),state= UserState.country_b)(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['Турция']))(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['Египет']))(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['Тайланд']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['ОАЭ']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Россия']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Китай']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Абхазия']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Вьетнам']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Шри-Ланка']))(handlers.Category.country)
dp.callback_query_handler(Text(equals=['Мальдивы']))(handlers.Category.country)
#
#
dp.callback_query_handler(Text(equals=['🧍1 человек']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['2 человека']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['3 человека']))(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['4 человека']))(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['5 человек']))(handlers.Category.vzr)
dp.callback_query_handler(Text(equals=['6 человек']))(handlers.Category.vzr)

dp.callback_query_handler(Text(equals=['Без детей']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['1 человечек']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['2 человечка']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['3 человечка']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['4 человечка']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['5 человечков']))(handlers.Category.deti)
dp.callback_query_handler(Text(equals=['6 человечков']))(handlers.Category.deti)

dp.callback_query_handler(Text(equals=['*']))(handlers.Category.hotel)
dp.callback_query_handler(Text(equals=['**']))(handlers.Category.hotel)
dp.callback_query_handler(Text(equals=['***']))(handlers.Category.hotel)
dp.callback_query_handler(Text(equals=['****']))(handlers.Category.hotel)
dp.callback_query_handler(Text(equals=['*****']))(handlers.Category.hotel)
dp.callback_query_handler(Text(equals=['🔙Назад']))(handlers.Category.back)

dp.callback_query_handler(Text(equals=['любое']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['все включено']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['завтрак']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['завтрак, ужин']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['завтрак, обед, ужин']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['ультра все включено']))(handlers.Category.pitanie)
dp.callback_query_handler(Text(equals=['🔙Назад']))(handlers.Category.back)
# dp.message_handler(commands=['admin'])(handlers.Admin.start)
# dp.callback_query_handler(text="statistick")(handlers.Admin.statistick)
# dp.callback_query_handler(text="users")(handlers.Admin.users)
# dp.callback_query_handler(text="mailing")(handlers.Admin.mailing)
# dp.message_handler(state=handlers.Admin.admins.mailing_step1)(handlers.Admin.mailing1)
# dp.message_handler(content_types=types.ContentTypes.PHOTO, state=handlers.Admin.admins.mailing_step2)(handlers.Admin.mailing2)
# dp.callback_query_handler(text="block")(handlers.Admin.block)
# dp.message_handler(state=handlers.Admin.admins.ban)(handlers.Admin.ban1)
# dp.callback_query_handler(text="back_to_admin")(handlers.Admin.back_admin)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)