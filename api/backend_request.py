import requests

from data.config import settings


def get_task(user_id: int, status="work"):
    authorization = requests.get(f'{settings.DEVAPI_ROOT}{settings.TASK_ROOT}',
                                 headers={'x-app-auth': f'{settings.ASSIST_TOKEN}'},
                                 params={'admin_id': user_id, 'limit': 500, 'status': status})
    return authorization


def get_admin_id(telegram_id: int):
    authorization = requests.get(f'{settings.DEVAPI_ROOT}{settings.ADMIN_ROOT}',
                                 headers={'x-app-auth': f'{settings.ASSIST_TOKEN}'},
                                 params={'telegram_id': telegram_id, 'is_active': 'true', 'is_verified': 'true'})
    return authorization


def client_request(id: int, telegram_id: int, code: str):
    identify = requests.put(f'{settings.DEVAPI_ROOT}{settings.ADMIN_ROOT}/{id}/telegram',
                            headers={'x-app-auth': f'{settings.ASSIST_TOKEN}'},
                            json={'telegram_id': telegram_id, 'code': code})
    return identify
