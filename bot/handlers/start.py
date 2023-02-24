import requests

from aiogram import types
from api.backend_request import client_request


async def bot_start(msg: types.Message):
    try:
        args = msg.get_args()
        if not args:
            await msg.answer(text=f"Прив'яжіть ваш акаунт!")
            return
        user_id, token = args.split("_")
        result = client_request(user_id, msg.chat.id, str(token))
        print(result.content)
        result.raise_for_status()
        await msg.answer('Реєстрація успішна')
    except requests.exceptions.HTTPError:
        await msg.answer(f'Реєстрація не вдалася')





