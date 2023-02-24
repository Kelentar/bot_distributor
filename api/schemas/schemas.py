from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: int
    email: str
    token: str


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True