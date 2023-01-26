from flask import Flask, request, send_from_directory
from flask_cors import CORS
from db import add_image_to_index, search_image
from feature_extraction import extract_features

app = Flask(__name__)
CORS(app)


@app.route("/api")
def heartbeat():
    return {"message": "Api is running"}


@app.route('/api/images', methods=["POST"])
def post_image_to_index():
    payload = request.get_json()
    image_url = payload.get("url")

    if not image_url:
        return {"message": "No url provided"}, 400

    try:
        features = extract_features(image_url)
        add_image_to_index(features, image_url, payload.get("metadata", ""))
        return {"message": "successs"}
    except Exception as e:
        return {"message": str(e)}, 400


@app.route('/api/images/search', methods=["POST"])
def search_simmilar_images():
    payload = request.get_json()

    image_url = payload.get("url")
    metadata = payload.get("metadata")

    try:
        features = None
        if image_url:
            features = extract_features(image_url)

        return search_image(features, metadata)
    except Exception as e:
        return {"message": str(e)}, 400


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
