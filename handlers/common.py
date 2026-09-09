from html import escape

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database import db
from handlers.keyboards import about_keyboard, main_buttons

router = Router()


COMMANDS = [
    ("start", "запустить бота и открыть главное меню"),
    ("menu", "показать список доступных команд"),
    ("drinks", "показать список напитков в меню кафе"),
    ("add_product", "добавить новый напиток в меню (диалог)"),
]

ABOUT_TEXT = (
    "☕ <b>Кафе «Уютный уголок»</b>\n\n"
    "Мы варим кофе и готовим авторские напитки с 2015 года. "
    "У нас тепло, уютно и всегда свежая выпечка — заходите в гости!"
)


def build_menu_text() -> str:
    lines = ["<b>Доступные команды:</b>", ""]
    lines += [f"/{cmd} — {desc}" for cmd, desc in COMMANDS]
    return "\n".join(lines)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
   
    await state.clear()
    await message.answer(
        "Привет! Я бот кафе ☕\n"
        "Воспользуйтесь кнопками ниже или командой /menu, чтобы увидеть все возможности.",
        reply_markup=main_buttons,
    )
    await message.answer("Хотите узнать больше о нас?", reply_markup=about_keyboard)


@router.message(Command("menu"))
async def cmd_menu(message: Message) -> None:
    await message.answer(build_menu_text())


@router.message(Command("drinks"))
async def cmd_drinks(message: Message) -> None:
    drinks = db.get_all_drinks()
    if not drinks:
        await message.answer("Меню пока пустое")
        return

    lines = ["<b>Меню напитков:</b>"]
    lines += [f"• {escape(name)} — {price} руб." for name, price in drinks]
    await message.answer("\n".join(lines))


@router.message(F.text == "☕ Меню")
async def button_menu_alias(message: Message) -> None:
   
    await cmd_drinks(message)


@router.callback_query(F.data == "about")
async def callback_about(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(ABOUT_TEXT)


@router.message(F.text.lower() == "пока")
async def farewell_handler(message: Message) -> None:
    await message.answer("До встречи!")
