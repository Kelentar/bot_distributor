from aiogram import types
from api.models import Form


async def cmd_start(msg: types.Message):
    Form.id = msg.from_user.id
    await Form.email.set()
    await msg.reply("Hi there! What's your name?")
