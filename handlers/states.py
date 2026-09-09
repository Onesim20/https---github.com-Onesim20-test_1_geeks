from aiogram.fsm.state import State, StatesGroup


class AddDrink(StatesGroup):
    """Состояния диалога добавления напитка (/add_product)."""

    name = State()
    price = State()