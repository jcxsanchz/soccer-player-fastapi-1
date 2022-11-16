from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String
from api.database import Base


class Player(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True, nullable=False)
    player_name = Column(String, nullable=False)
    player_age = Column(Integer, nullable=False)
    player_nationality = Column(String, nullable=False)
    player_rating = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
