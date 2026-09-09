from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

#Агай из за того что мы кнопки не проходили мне было сложно изучал одновременно и исправлял другие команды из за этого 
#в вторнике я не успел и пошел домой и дом долеко и даже до 12 я не смог потомучто хотел спасть из за этого я сделал
#в среду сейчас
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
