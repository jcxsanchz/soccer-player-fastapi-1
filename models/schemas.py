from pydantic import BaseModel
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
