import numpy as np
from numpy.linalg import norm
import pickle
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
import requests
import PIL
from io import BytesIO
from time import sleep
from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid

URL = "http://olidawiki.s3-website.eu-central-1.amazonaws.com/c676eba0-78ee-42f4-a48c-758cdb77a5f8.jpg"

MODEL = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3), pooling='avg')


def extract_features(img_url):
    r = requests.get(img_url)
    img = PIL.Image.open(BytesIO(r.content)).resize((224, 224)).convert("RGB")

    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = MODEL.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    return normalized_features

features = extract_features("http://olidawiki.s3-website.eu-central-1.amazonaws.com/3295f28c-b5c7-4437-b6c0-79efc55f5c44.jpg", model)

print(features)

BASE_API_URL = os.getenv("BASE_API_URL", "http://images_api:80/api")
QDRANT_HOST = os.getenv("QDRANT_HOST", "http://images_api:80/api")

client = QdrantClient(host=QDRANT_HOST, port=6333)


try:
    client.get_collection(collection_name="images_collection")
except Exception as e:
    client.recreate_collection(
        collection_name="images_collection",
        vectors_config=models.VectorParams(size=2048, distance=models.Distance.COSINE),
    )


def add_image_to_index(image_url):
    features = extract_features(image_url)

    try:
        point_id = image_url.split("/")[-1].split(".jpg")[0]
    except:
        point_id = str(uuid.uuid4())

    client.upsert(
        collection_name="images_collection",
        points=[
            models.PointStruct(
                id=point_id,
                vector=features.tolist(),
            ),
        ]
    )


if __name__ == '__main__':
    while True:
        requests.get()
        sleep(1)