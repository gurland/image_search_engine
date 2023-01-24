from qdrant_client import QdrantClient
from qdrant_client.http import models

from cfg import QDRANT_HOST, QDRANT_COLLECTION


qdrant_client = QdrantClient(host=QDRANT_HOST, port=6333)


def setup_qdrant(client):
    try:
        client.get_collection(collection_name=QDRANT_COLLECTION)
    except Exception as e:
        client.recreate_collection(
            collection_name=QDRANT_COLLECTION,
            vectors_config=models.VectorParams(size=2048, distance=models.Distance.COSINE),
        )

    client.create_payload_index(
        collection_name=QDRANT_COLLECTION,
        field_name="metadata",
        field_schema=models.TextIndexParams(
            type="text",
            tokenizer=models.TokenizerType.WORD,
            min_token_len=2,
            max_token_len=15,
            lowercase=True,
        )
    )

