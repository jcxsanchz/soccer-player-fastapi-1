from pydantic import BaseModel, EmailStr
from datetime import datetime


class PlayerBase(BaseModel):
    player_name: str
    player_age: int
    player_nationality: str
    player_rating: int


class CreatePlayer(PlayerBase):
    pass


class PlayerResponse(PlayerBase):
    player_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
