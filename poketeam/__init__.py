from typing import Optional

import dotenv
from peewee import SqliteDatabase


db: Optional[SqliteDatabase] = None


def init_db(dbname: str) -> None:
    global db
    db = SqliteDatabase(dbname)


dotenv.load_dotenv('./.env.local')
dotenv.load_dotenv('./.env.dev')
