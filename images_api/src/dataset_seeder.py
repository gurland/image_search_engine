import os.path
import urllib.request
import csv
import requests

from pathlib import Path


UPLOAD_IMAGE_URL = "https://d32bdp38hd.execute-api.eu-central-1.amazonaws.com/images"
ADD_IMAGE_TO_INDEX_URL = "http://localhost/api/images"


def upload_image(path: Path) -> str:
    with open(path, "rb") as f:
        response = requests.post(UPLOAD_IMAGE_URL, data=f)
        return response.json().get("url")


def add_image_to_index(image_url: str, metadata: str):
    requests.post(ADD_IMAGE_TO_INDEX_URL, json={
        "url": image_url,
        "metadata": metadata
    })

    print(f"Added image to index: {metadata}")


if not os.path.isfile("train_attribution.csv"):
    print("train_attribution.csv not found. Downloading...")
    urllib.request.urlretrieve("https://s3.amazonaws.com/google-landmark/metadata/train_attribution.csv", "train_attribution.csv")


train_index = {}
with open("train_attribution.csv", "r", encoding="utf-8") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        train_index[row[0]] = f"Author: {row[2]} | {row[4].replace('File:', '').rstrip('.jpg').rstrip('.JPG')}"


for path in Path('0').rglob('*.jpg'):
    file_hash = path.name.rstrip(".jpg")
    image_url = upload_image(path)
    add_image_to_index(image_url, train_index[file_hash])


print("Done!")
