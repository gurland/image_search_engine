from typing import List, Optional
import uuid
import re

from qdrant_client import QdrantClient
from qdrant_client.http import models

from cfg import QDRANT_HOST, QDRANT_COLLECTION_NAME

qdrant_client = QdrantClient(host=QDRANT_HOST, port=6333)


def setup_qdrant():
    try:
        qdrant_client.get_collection(collection_name=QDRANT_COLLECTION_NAME)
    except Exception as e:
        qdrant_client.recreate_collection(
            collection_name=QDRANT_COLLECTION_NAME,
            vectors_config=models.VectorParams(size=2048, distance=models.Distance.COSINE),
        )

    qdrant_client.create_payload_index(
        collection_name=QDRANT_COLLECTION_NAME,
        field_name="metadata",
        field_schema=models.TextIndexParams(
            type="text",
            tokenizer=models.TokenizerType.WORD,
            min_token_len=2,
            max_token_len=15,
            lowercase=True,
        )
    )


def search_image(image_features_vector: Optional[List[float]], metadata: str):
    if image_features_vector is not None:
        result, _ = qdrant_client.search(
            collection_name=QDRANT_COLLECTION_NAME,
            limit=20,
            query_vector=image_features_vector
        )
    else:
        # FTS search
        result, _ = qdrant_client.scroll(
            collection_name=QDRANT_COLLECTION_NAME,
            limit=20,
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="metadata",
                        match=models.MatchText(text=metadata),
                    )
                ]
            )
        )

    return [record.json() for record in result]


def add_image_to_index(features: List[float], image_url: str, metadata: str):
    try:
        point_id = re.search(r"(.*)/(.*)(\.)", image_url)[2]
        uuid.UUID(point_id, version=4)
    except Exception as e:
        point_id = str(uuid.uuid4())

    qdrant_client.upsert(
        collection_name=QDRANT_COLLECTION_NAME,
        points=[
            models.PointStruct(
                id=point_id,
                vector=features,
                payload={
                    "metadata": metadata,
                    "image_url": image_url
                }
            ),
        ]
    )
