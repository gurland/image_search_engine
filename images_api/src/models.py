from peewee import *
from cfg import PG_USER, PG_PASSWORD, PG_DB, PG_HOST


db = PostgresqlDatabase(PG_DB, user=PG_USER, host=PG_HOST, password=PG_PASSWORD)


class BaseModel(Model):
    class Meta:
        database = db


class IndexedImage(BaseModel):
    url = CharField(unique=True)
    is_indexed = BooleanField(default=False)

