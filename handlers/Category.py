from aiogram.types import InputMediaPhoto
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import *
# from main import *

class UserState(StatesGroup):
    incity_b = State() #город вылета
    country_b = State() # Страна прилета
    vzr_b = State() # Количество взрослых
    deti_b = State()# количество детей
    hotel_b = State()# категория отеля
    pitanie_b = State()# каегория питания
    nochi_b = State() # количество ночей
    # дата


async def incity(message):
    with open('files/media/city_of_departure.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Выберите город вылета </b>', parse_mode='HTML',reply_markup=incity_kb)
        await UserState.incity_b.set()

# async def country(call, state ):
async def country(callback: types.CallbackQuery, state):
    await state.update_data(ic=callback)
    incity = callback
    print(f'Город вылета {incity}')
    # with open('files/media/strana.jpg', "rb") as img:
    #     await call.message.answer_photo(img,'<b>Выберите страну </b>', parse_mode='HTML',reply_markup=country_kb)
    #     await UserState.country_b.set()
    #     # await call.answer(f'Город вылета {incity}')
    #     await call.answer()

async def vzr(call, state):
    await state.update_data(bc=call.message)
    data = await state.get_data()
    country = data['bc']
    print(f'Стана для путешествия {country}')
    with open('files/media/vzr.jpg', "rb") as img:
        await call.message.answer_photo(img,'<b>Выберите количество взрослых путешествеников</b>', parse_mode='HTML',reply_markup=vzr_kb)
        await UserState.vzr_b.set()
        # await call.answer(f'Стана для путешествия {country}')
        await call.answer()

async def deti(call, state ):

    with open('files/media/deti.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите количество детей в поездке</b>',
                                        parse_mode='HTML',reply_markup=deti_kb)
        await call.answer()
async def hotel(call, state):
    with open('files/media/hotel.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите минимальную категорию отеля</b>',parse_mode='HTML', reply_markup=hotel_kb)
        await call.answer()

async def pitanie(call,state ):
    with open('files/media/pitanie.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите питание</b>',
                                   parse_mode='HTML', reply_markup=pitanie_kb)
        await call.answer()

async def nochi(call, state):
    with open('files/media/nochi.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите количество ночей</b>',
                                   parse_mode='HTML', reply_markup=nochi_kb)
        await call.answer()

async def back(call, state):
    with open('files/media/strana.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите страну или напишите свою</b>', parse_mode='HTML',reply_markup=nochi_kb)
        await call.answer()

async def proverka(message):
    with open('files/media/d.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Проверка</b>',
                                   parse_mode='HTML', reply_markup=proverka_kb)
        await call.answer()

async def zajavka(message):
    with open('files/media/deti.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Заявка</b>',
                                   parse_mode='HTML', reply_markup=zajavka_kb)
        await message.answer()


