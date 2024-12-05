from aiogram.types import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton)

win_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '📝 Start'),
        ],
    ],resize_keyboard=True
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '✈️Поехали'),
            KeyboardButton(text = 'ℹ️ О нас')
        ],
    ],resize_keyboard=True
)
zayavka_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Подать заявку'),
            KeyboardButton(text = 'Редактировать')
        ],
    ],resize_keyboard=True
)
# 💬📝
incity_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Москва', callback_data = 'Москва'),
        ],
        [
            InlineKeyboardButton(text = 'Санкт Петербург', callback_data = 'Санкт Петербург'),
        ],
        [
            InlineKeyboardButton(text = 'Нижний Новгород', callback_data = 'Нижний Новгород'),
        ],
        [
            InlineKeyboardButton(text = 'Екатеринбург', callback_data = 'Екатеринбург'),
        ],
    ],resize_keyboard=True
)

country_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Турция', callback_data = 'Турция'),
            InlineKeyboardButton(text = 'Египет', callback_data = 'Египет'),
        ],
        [
            InlineKeyboardButton(text = 'Тайланд', callback_data = 'Тайланд'),
            InlineKeyboardButton(text = 'ОАЭ', callback_data = 'ОАЭ'),
        ],
        [
            InlineKeyboardButton(text = 'Россия', callback_data = 'Россия'),
            InlineKeyboardButton(text = 'Китай', callback_data = 'Китай'),
        ],
        [
            InlineKeyboardButton(text = 'Абхазия', callback_data = 'Абхазия'),
            InlineKeyboardButton(text = 'Вьетнам', callback_data = 'Вьетнам'),
        ],
        [
            InlineKeyboardButton(text = 'Шри-Ланка', callback_data = 'Шри-Ланка'),
            InlineKeyboardButton(text = 'Мальдивы', callback_data = 'Мальдивы'),
        ],

],resize_keyboard=True
)

vzr_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = '🧍1 человек', callback_data = '🧍1 человек'),
            InlineKeyboardButton(text = '2 человека', callback_data = '2 человека'),
        ],
        [
            InlineKeyboardButton(text = '3 человека', callback_data = '3 человека'),
            InlineKeyboardButton(text = '4 человека', callback_data = '4 человека'),
        ],
        [
            InlineKeyboardButton(text = '5 человек', callback_data = '5 человек'),
            InlineKeyboardButton(text = '6 человек', callback_data = '6 человек'),
        ],

],resize_keyboard=True
)
deti_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [   InlineKeyboardButton(text='Без детей', callback_data='Без детей')],
        [
            InlineKeyboardButton(text='1 человечек', callback_data='1 человечек'),
            InlineKeyboardButton(text='2 человечка', callback_data='2 человечка'),
        ],
        [
            InlineKeyboardButton(text='3 человечка', callback_data='3 человечка'),
            InlineKeyboardButton(text='4 человечка', callback_data='4 человечка'),
        ],
        [
            InlineKeyboardButton(text='5 человечков', callback_data='5 человечков'),
            InlineKeyboardButton(text='6 человечков', callback_data='6 человечков'),
        ],

    ], resize_keyboard=True
)
hotel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='*', callback_data='*'),
            InlineKeyboardButton(text='**', callback_data='**'),
            InlineKeyboardButton(text='***', callback_data='***'),
        ],
        [
            InlineKeyboardButton(text='****', callback_data='****'),
            InlineKeyboardButton(text='*****', callback_data='*****'),
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='🔙 Назад'),
        ],

    ], resize_keyboard=True
)
pitanie_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='любое', callback_data='любое'),
            InlineKeyboardButton(text='все включено', callback_data='все включено'),
        ],
        [
            InlineKeyboardButton(text='завтрак', callback_data='завтрак'),
        ],
        [
            InlineKeyboardButton(text='завтрак, ужин', callback_data='завтрак, ужин'),

        ],
        [
            InlineKeyboardButton(text='завтрак, обед, ужин', callback_data='завтрак, обед, ужин'),

        ],
        [
            InlineKeyboardButton(text='ультра все включено', callback_data='ультра все включено'),
        ],
        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='🔙 Назад'),
        ],

    ], resize_keyboard=True
)

nochi_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='6-8', callback_data='6-8'),
            InlineKeyboardButton(text='9-11', callback_data='9-11'),
            InlineKeyboardButton(text='12-14', callback_data='12-14'),
        ],

        [
            InlineKeyboardButton(text='🔙 Назад', callback_data='🔙 Назад'),
        ],

    ], resize_keyboard=True
)




AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Пользователи", callback_data = "users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data = "statistick"),
        ],
        [
            InlineKeyboardButton(text="✉️ Рассылка", callback_data = "mailing"),
        ],
        [
            InlineKeyboardButton(text="❌ Блокировка", callback_data = "block"),
        ],
    ]
)

back_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data = "back_to_admin"),
        ],
    ]
)