from cfg import PG_DB, PG_HOST, PG_PASSWORD, PG_USER
from playhouse.postgres_ext import *

db = PostgresqlDatabase(PG_DB, user=PG_USER, host=PG_HOST, password=PG_PASSWORD)


class BaseModel(Model):
    class Meta:
        database = db


class IndexedImage(BaseModel):
    url = CharField(unique=True)
    qdrant_id = CharField(unique=True)
    metadata = TextField()
    fts_search_index = TSVectorField()

    def to_dict(self):
        return {
            "url": self.url,
            "qdrant_id": self.qdrant_id,
            "metadata": self.metadata,
        }
