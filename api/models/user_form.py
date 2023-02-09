from aiogram.dispatcher.filters.state import State, StatesGroup
from pydantic import BaseModel


class Form(StatesGroup):
    email = State()
    password = State()