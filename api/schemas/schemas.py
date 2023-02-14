from pydantic import BaseModel


class TaskCreate(BaseModel):
    user_id: int
    subject_id: int
    subject_type: str
    status: str
    details: str


class TaskUpdate(TaskCreate):
    id: int


class UserCreate(BaseModel):
    email: str
    token: str


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: str


# class json_load():
#     json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)