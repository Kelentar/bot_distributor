from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    email = State()
    password = State()