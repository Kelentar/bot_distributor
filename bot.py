from aiogram import executor
from bot.dispetcher import dp
from api.models import Form

from bot.state import cancel_handler
from bot.state import enter_password
from bot.state import enter_login
from bot.state import cmd_start
from bot.handlers import bot_start


def setup():
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(cmd_start, commands=['regis'])
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(enter_login, state=Form.email)
    dp.register_message_handler(enter_password, state=Form.password)


if __name__ == '__main__':
    setup()
    executor.start_polling(dp, skip_updates=True)