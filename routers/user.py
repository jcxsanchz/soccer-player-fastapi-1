import fastapi
from fastapi import status, HTTPException, Depends
import models.table
from api.database import get_db
from models.schemas import CreateUser, UserOut
from sqlalchemy.orm import Session
import utils

router = fastapi.APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # hash the password - user.password
    hashed_password = utils.hash_user_password(user.password)
    user.password = hashed_password

    new_user = models.table.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/users/{id}', response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.table.User).filter(models.table.User.user_id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")

    return user
