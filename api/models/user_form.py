import enum

from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    email = State()
    password = State()


class SubjectTypeEnum(enum.Enum):
    admin = "admin"
    found = "found"
    shop = "shop"
    dialog = "dialog"
    order = "order"
    product = "product"


class SubjectStatusEnum(enum.Enum):
    wait = "wait"
    work = "work"
    stop = "stop"
    done = "done"


