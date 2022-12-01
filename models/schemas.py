from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


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
    owner_id: int

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


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
