import uvicorn

from fastapi import FastAPI

from database.db import init_db
from persons.controllers import client

app = FastAPI()
app.include_router(client)

init_db(app)

if __name__ == '__main__':
    uvicorn.run(app)