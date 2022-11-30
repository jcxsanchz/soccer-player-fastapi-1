from fastapi import FastAPI
import models.table
from routers import players, user
import uvicorn
from api.database import engine

models.table.Base.metadata.create_all(bind=engine)


# instance
api = FastAPI()

api.include_router(players.router)
api.include_router(user.router)


# path operation or route. route path
@api.get('/')
def root():
    return {"message": "Welcome to Soccer Manager!"}


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
