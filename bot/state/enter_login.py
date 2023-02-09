from api.models import Form
from aiogram.dispatcher import FSMContext
from aiogram import types


async def enter_login(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = msg.text
    await Form.password.set()
    await msg.reply("Enter your Password")