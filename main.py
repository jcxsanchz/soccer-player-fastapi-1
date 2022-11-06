from fastapi import FastAPI
from api import soccer_api
import uvicorn


# instance
api = FastAPI()

api.include_router(soccer_api.router)


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')


