import time

from aiogram import types
from api.backend_request import get_task


async def bot_start(msg: types.Message):
    print(msg.from_user.id)
    await msg.answer("Hi there! Confirm the registration (/regis)")


async def make_request(msg: types.Message):
    print(get_task())
    await msg.answer("Request +")


