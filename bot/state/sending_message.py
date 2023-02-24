import asyncio
import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import exceptions

from bot.dispatcher import bot
from bot.handlers.user_request import EMOJI_STATUS
from data.config import settings


async def send_message_to_users_handler(
    user_id: int, text: dict, disable_notification: bool = False
) -> bool:
    try:
        await bot.send_message(
            user_id,
            "New task",
            disable_notification=disable_notification,
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text=f'ID: {text["id"]} | СТАТУС: {EMOJI_STATUS[text["status"]]} | ТИП: {text["subject_type"]}',
                                            url=f'{settings.DEVAPI_ROOT}{settings.ASSISTANT_ROOT}/{text["id"]}'))
        )
    except exceptions.BotBlocked:
        logging.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        logging.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        logging.error(
            f"Target [ID:{user_id}]: Flood limit is exceeded. "
            f"Sleep {e.timeout} seconds."
        )
        await asyncio.sleep(e.timeout)
        return await bot.send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        logging.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        logging.exception(f"Target [ID:{user_id}]: failed")
    else:
        logging.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def send_message_to_users(text):
        await send_message_to_users_handler(settings.SUPERUSER_CHAT, text)
