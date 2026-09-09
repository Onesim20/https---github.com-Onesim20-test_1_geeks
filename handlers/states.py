from aiogram.fsm.state import State, StatesGroup


class AddDrink(StatesGroup):


    name = State()
    price = State()
