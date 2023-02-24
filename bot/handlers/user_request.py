import json
import math

import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from api.backend_request import get_task, get_admin_id
from data.config import settings
from bot.dispatcher import dp


EMOJI_STATUS = {'done': '\U00002705',
                'stop': '\U0000274C',
                'wait': '\U0001F634',
                'work': '\U0000270F'}

items_callback = CallbackData("Items", "page")


class Items(StatesGroup):
    items = State()


def get_item(user_id: int, status: str):
    response = get_task(user_id=user_id, status=status)
    back_request = json.loads(response.content.decode())
    items = back_request["items"]
    for item in items:
        if item["id"] != 'null':
            return items


def get_item_count(user_id: int, status: str):
    response = get_task(user_id=user_id, status=status)
    back_request = json.loads(response.content.decode())
    items_count = back_request["total_count"]
    return items_count


def get_items_keyboard(items: list, page_count: int, page: int = 0) -> InlineKeyboardMarkup:

    keyboard = InlineKeyboardMarkup(row_width=1)
    has_next_page = page_count > page + 1

    for i in range(0, len(items)):
        task_request = InlineKeyboardButton(
            text=f'ID: {items[i]["id"]} | СТАТУС: {EMOJI_STATUS[items[i]["status"]]} | ТИП: {items[i]["subject_type"]}',
            url=f'{settings.DEVAPI_ROOT}{settings.TASK_ROOT}/{items[i]["id"]}')
        keyboard.add(task_request)

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=items_callback.new(page=page - 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=f"{page + 1}",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text="Вперед >",
                callback_data=items_callback.new(page=page + 1)
            )
        )

    return keyboard


async def items_index(msg: Message, state: FSMContext):
    try:
        response = get_admin_id(msg.from_user.id)
        back_request = json.loads(response.content.decode())

        if not back_request['total_count']:
            raise requests.exceptions.HTTPError

        user_id = back_request['items'][0]['id']
        term = msg.text

        match term:
            case '/work_shop':
                term = 'work'
            case '/wait_shop':
                term = 'wait'
            case '/stop_shop':
                term = 'stop'
            case '/done_shop':
                term = 'done'
            case _:
                await msg.answer('Команда не вірна')
        print(term)

        async with state.proxy() as data:
            data['items'] = get_item(user_id=user_id, status=term)
            data['total_count'] = get_item_count(user_id=user_id, status=term)

        if not data['total_count']:
            raise requests.exceptions.HTTPError

        items_data = data['items'][:10]
        items_count_data = data['total_count']
        page_count = math.ceil(len(data["items"]) / 10)
        keyboard = get_items_keyboard(items_data, page_count)

        await msg.answer(
            f'Кількість завдань: {items_count_data}',
            reply_markup=keyboard
        )
    except requests.exceptions.HTTPError:
        await msg.answer('Завдання не знайдені')


@dp.callback_query_handler(items_callback.filter())
async def item_page_handler(query: CallbackQuery, callback_data: dict, state: FSMContext):
    page = int(callback_data.get('page'))
    async with state.proxy() as data:
        items_data = data['items'][page * 10: (page + 1) * 10]
        items_count_data = data['total_count']
    page_count = math.ceil(len(data['items']) / 10)
    get_items_keyboard(items_data, page_count, page)

    await query.message.edit_text(f'Кількість завдань: {items_count_data}", reply_markup=keyboard')
