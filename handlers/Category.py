import tb
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

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
    name_b = State() # имя путешественика
    email_b = State() # email путешественика
    # дата


async def incity(message):
    with open('files/media/city_of_departure.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Выберите город вылета или напишите свой</b>', parse_mode='HTML',reply_markup=incity_kb)
        await UserState.incity_b.set()
async def handle_city_input(message: types.Message, state):
    incity = message.text  # Получаем текст, введенный пользователем
    await state.update_data(ic=incity)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'        Город вылета {incity}    ')
    text.close
    print(f'Город вылета {incity}')
    data = await state.get_data()
    incity = data['ic']
    with open('files/media/strana.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Выберите страну или напишите свою</b>', parse_mode='HTML', reply_markup=country_kb)
        await UserState.country_b.set()
        await message.answer(f'Вы ввели город: {incity}')
        # await message.answer()


async def country(call:types.CallbackQuery, state):
    incity = call.data
    await state.update_data(ac=incity)
    text = open("files\Zayavka.txt",'a',encoding='utf-8')
    text.write(f'Город вылета {incity}\n')
    text.close
    print(f'Город вылета {incity}')
    data = await state.get_data()
    incity = data['ac']
    with open('files/media/strana.jpg', "rb") as img:
        await call.message.answer_photo(img,'<b>Выберите страну или напишите свою</b>', parse_mode='HTML',reply_markup=country_kb)
        await UserState.country_b.set()
        await call.answer(f'Город вылета {incity}')
        await call.answer()


async def handle_country_input(message: types.Message, state):
    country = message.text  # Получаем текст, введенный пользователем
    await state.update_data(uc=country)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Страна для путешествия {country} ')
    text.close
    print(f'Страна для путешествия {country}')
    data = await state.get_data()
    country = data['uc']
    with open('files/media/vzr.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Выберите количество взрослых путешествеников</b>', parse_mode='HTML', reply_markup=vzr_kb)
        await UserState.vzr_b.set()
        await message.answer(f'Вы ввели Страну для путешествия: {country}')
        # await message.answer()


async def vzr(call:types.CallbackQuery, state):
    country = call.data
    await state.update_data(bc=country)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Страна для путешествия {country} ')
    text.close
    print(f'Страна для путешествия {country}')
    data = await state.get_data()
    country = data['bc']
    with open('files/media/vzr.jpg', "rb") as img:
        await call.message.answer_photo(img,'<b>Выберите количество взрослых путешествеников</b>', parse_mode='HTML',reply_markup=vzr_kb)
        await UserState.vzr_b.set()
        await call.answer(f'Стана для путешествия {country}')
        await call.answer()
async def deti(call:types.CallbackQuery, state):
    vzr = call.data
    await state.update_data(cc=vzr)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Количество взрослых {vzr}\n')
    text.close
    print(f'Количество взрослых {vzr}')
    data = await state.get_data()
    vzr = data['cc']
    with open('files/media/deti.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите количество детей в поездке</b>',parse_mode='HTML',reply_markup=deti_kb)
        await UserState.deti_b.set()
        await call.answer(f'Количество взрослых {vzr}')
        await call.answer()
async def hotel(call:types.CallbackQuery, state):
    deti = call.data
    await state.update_data(dc=deti)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Количество детей {deti}\n')
    text.close
    print(f'Количество детей {deti}')
    data = await state.get_data()
    deti = data['dc']
    with open('files/media/hotel.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите минимальную категорию отеля</b>',parse_mode='HTML', reply_markup=hotel_kb)
        await UserState.hotel_b.set()
        await call.answer(f'Количество детей {deti}')
        await call.answer()
async def pitanie(call:types.CallbackQuery, state):
    hotel = call.data
    await state.update_data(ec=hotel)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Минимальная категория отеля {hotel}\n')
    text.close
    print(f'Минимальная категория отеля {hotel}')
    data = await state.get_data()
    hotel = data['ec']
    with open('files/media/pitanie.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите питание</b>',
                                   parse_mode='HTML', reply_markup=pitanie_kb)
        await UserState.pitanie_b.set()
        await call.answer(f'Минимальная категория отеля {hotel}')
        await call.answer()

async def nochi(call:types.CallbackQuery, state):
    pitanie = call.data
    await state.update_data(cc=pitanie)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Категория питания {pitanie}\n')
    text.close
    print(f'Категория питания {pitanie}')
    data = await state.get_data()
    pitanie= data['cc']
    with open('files/media/nochi.jpg', "rb") as img:
        await call.message.answer_photo(img, '<b>Выберите количество ночей</b>',
                                   parse_mode='HTML', reply_markup=nochi_kb)
        await UserState.nochi_b.set()
        await call.answer(f'Категория питания {pitanie}')
        await call.answer()
async def nochi_v(call:types.CallbackQuery, state):
    nochi = call.data
    await state.update_data(dc=nochi)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Количество ночей {nochi}\n')
    text.close
    print(f'Количество ночей {nochi}')
    with open('files/media/name.jpg', "rb") as img:
        await call.message.answer_photo(img,'<b>Напишите свое имя для обратной связи </b>', parse_mode='HTML')
    data = await state.get_data()
    nochi= data['dc']
    await UserState.nochi_b.set()
    await call.answer(f'Количество ночей {nochi}')
    await call.answer()

async def handle_name_input(message: types.Message, state):
    name = message.text  # Получаем текст, введенный пользователем
    await state.update_data(uc=name)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'Имя путешественика {name}\n')
    text.close
    print(f'Имя путешественика {name}')
    data = await state.get_data()
    name = data['uc']
    with open('files/media/email.jpg', "rb") as img:
        await message.answer_photo(img, '<b>Напишите email для связи</b>', parse_mode='HTML')
        await UserState.name_b.set()
        await message.answer(f'Имя путешественика: {name}')

async def handle_email_input(message: types.Message, state):
    email = message.text  # Получаем текст, введенный пользователем
    await state.update_data(xc=email)
    text = open("files\Zayavka.txt", 'a', encoding='utf-8')
    text.write(f'email путешественика {email}')
    text.close
    print(f'email путешественика {email}')
    data = await state.get_data()
    email = data['xc']
    await UserState.email_b.set()
    await message.answer(f'email путешественика: {email}')
    list = []
    with open("files\Zayavka.txt", 'r', encoding='utf-8') as file:
        for line in file:
            list.append(line)
            print(list)
    await message.answer(list)
    # await message.answer(f'<b>Город вылета - {incity}, Страна прилета - {country},'
    #                      f'Количество взрослых -{vzr}, Количество детей - {deti} Категория отеля -{hotel},'
    #                      f'Категория питания -{pitanie},Количество ночей - {nochi}, '
    #                      f'Имя путешественика -{name}, email путешественика - {email}',parse_mode='HTML')

    await message.answer('<b>Проверьте данные и если все верно- нажмите кнопку "Подать заявку", что-то не так - "Редактировать"</b>',
                         parse_mode='HTML', reply_markup=zayavka_kb)

    # await message.answer(f'email путешественика: {email}')

async def zayavka(message):
    # url = "https://t.me/skarsar"
    with open('files/Zayavka.txt', 'rb') as doc:
        # url = "https://t.me/skarsar"
        bot.send_document(chat_id=message.chat.id, document=doc)
        await message.answer('Заявка отправлена, с вами скоро свяжусь. Алена')
        # tb.send_document(url, doc)
        # tb.send_document(url,"FILEID")
    # await message.answer('Заявка отправлена, с вами скоро свяжусь. Алена')


