import requests


def post_log(Form):
    result = requests.post("https://devapi-v2.assist.systems/systems/auth/login",
                           headers={'accept': 'application/json',
                       'Content-Type': 'application/json'},
                           json={'email': Form['email'], 'password': Form['password']})
    return result.content


def get_task():
    identify = requests.get("https://devapi-v2.assist.systems/systems/task/980",
                            headers={'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbklkIjoyOCwic2Vzc2lvbklkIjoiM2Q0NzZhM2QtMDY5MC00MzlkLTg4NTQtOTMxNjVhMGRjMTBiIiwiaWF0IjoxNjc2MzIzOTAzfQ.-AN0ELTn3b7CuuNHLjJkMGfittKtszILv1KrcZ4CIq8'})
    return identify.content
