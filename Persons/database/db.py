import os

from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from fastapi_sqlalchemy import DBSessionMiddleware

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')



def init_db(app):
    app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)