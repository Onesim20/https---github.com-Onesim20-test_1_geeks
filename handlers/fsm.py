from html import escape

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database import db
from handlers.states import AddDrink

router = Router()


@router.message(Command("cancel"), StateFilter(AddDrink.name, AddDrink.price))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    """Доп. команда: позволяет прервать диалог добавления напитка."""
    await state.clear()
    await message.answer("Добавление напитка отменено.")


@router.message(Command("add_product"))
async def cmd_add_product(message: Message, state: FSMContext) -> None:
    await state.set_state(AddDrink.name)
    await message.answer("Введите название напитка:")


@router.message(StateFilter(AddDrink.name))
async def process_drink_name(message: Message, state: FSMContext) -> None:
    
    if message.text is None:
        await message.answer(
            "Название должно быть текстом, а не фото/стикером. "
            "Попробуйте ещё раз — введите название напитка:"
        )
        return

    name = message.text.strip()
    if not name:
        await message.answer("Название не может быть пустым. Введите название напитка:")
        return

    await state.update_data(name=name)
    await state.set_state(AddDrink.price)
    await message.answer("Введите цену напитка (только число, в рублях):")


@router.message(StateFilter(AddDrink.price))
async def process_drink_price(message: Message, state: FSMContext) -> None:
    
    if message.text is None or not message.text.isdigit():
        await message.answer("Цена должна быть числом. Попробуйте ещё раз:")
        return

    data = await state.get_data()
    name = data["name"]
    price = int(message.text)

    db.add_drink(name, price)
    await state.clear()
    await message.answer(f"Напиток «{escape(name)}» за {price} руб. добавлен в меню! ✅")