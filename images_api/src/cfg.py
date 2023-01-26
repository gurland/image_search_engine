import os

QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant")
QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME", "images_collection")
