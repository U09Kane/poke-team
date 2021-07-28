from typing import Optional

from peewee import SqliteDatabase


db: Optional[SqliteDatabase] = None


def init_db(dbname: str) -> None:
    global db
    db = SqliteDatabase(dbname)
