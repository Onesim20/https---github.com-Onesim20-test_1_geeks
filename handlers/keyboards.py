from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☕ Меню")],
        [KeyboardButton(text="/menu")],
    ],
    resize_keyboard=True,
)


about_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="О нас", callback_data="about")],
    ]
)