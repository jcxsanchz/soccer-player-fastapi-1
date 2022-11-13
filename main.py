from fastapi import FastAPI

import models.table
from api import soccer_api
import uvicorn
from api.database import engine
models.table.Base.metadata.create_all(bind=engine)


# instance
api = FastAPI()

api.include_router(soccer_api.router)

if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
