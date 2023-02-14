import json

from aiogram.dispatcher import FSMContext
from aiogram import types

from api.backend_request import post_log
from api.crud.crud import create_user
from api.schemas.schemas import UserCreate
from api.database import SessionLocal


async def enter_password(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = msg.text
        print(data.get('email'))
        print(data.get('password'))
        token = json.loads(post_log(data).decode())["token"]
        print(token)
        create_user(SessionLocal(), UserCreate(email=data.get("email"), token=token))
    await state.finish()
    await msg.reply("Complete")
