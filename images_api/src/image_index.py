import uuid
from io import BytesIO
from time import sleep

import numpy as np
import PIL
import requests
from numpy.linalg import norm

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image


URL = "http://olidawiki.s3-website.eu-central-1.amazonaws.com/c676eba0-78ee-42f4-a48c-758cdb77a5f8.jpg"

MODEL = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3), pooling='avg')


def extract_features(img_url: str) -> list:
    r = requests.get(img_url)
    img = PIL.Image.open(BytesIO(r.content)).resize((224, 224)).convert("RGB")

    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = MODEL.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)

    return normalized_features.tolist()
