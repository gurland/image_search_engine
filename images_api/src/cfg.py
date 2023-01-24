import os

PG_USER = os.getenv("PG_USER", "postgres")
PG_PASSWORD = os.getenv("PG_PASSWORD", "example")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_DB = os.getenv("PG_DB", "postgres")

QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "images_collection")
