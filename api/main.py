from fastapi import FastAPI, Body
from bot.state.sending_message import send_message_to_users

app = FastAPI()


@app.post("/manager_bot/")
async def new_task(request: dict = Body()):
    task_list = request["items"]
    for task in task_list:
      await send_message_to_users(task)

