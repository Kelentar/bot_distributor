from aiogram.dispatcher import FSMContext
from aiogram import types


async def enter_password(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = msg.text
        print(data.get('email'))
        print(data.get('password'))
    await state.finish()
    await msg.reply("Complete")
