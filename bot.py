from aiogram import executor

from bot.dispatcher import dp
from bot.handlers import bot_start, items_index


def setup():
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(items_index, commands=['done_shop'])
    dp.register_message_handler(items_index, commands=['wait_shop'])
    dp.register_message_handler(items_index, commands=['work_shop'])
    dp.register_message_handler(items_index, commands=['stop_shop'])


if __name__ == '__main__':
    setup()
    executor.start_polling(dp, skip_updates=True)
