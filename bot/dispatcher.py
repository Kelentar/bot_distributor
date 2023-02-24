from aiogram import Bot, Dispatcher
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.settings.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)