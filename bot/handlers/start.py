from aiogram import types


async def bot_start(msg: types.Message):
    print(msg.from_user.id)
    await msg.answer("Hi there! Confirm the registration (/regis)")

