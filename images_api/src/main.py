from flask import Flask, request, send_from_directory
from models import IndexedImage
from image_index import add_image_to_index

app = Flask(__name__)


@app.route("/api")
def heartbeat():
    return {"message": "Api is running"}


@app.route('/api/images/<string:qdrant_id>')
def get_image_by_qdrant_id(qdrant_id):
    try:
        return IndexedImage.get(qdrant_id=qdrant_id).to_dict()
    except Exception as e:
        return {"message": str(e)}, 400


@app.route('/api/images', methods=["POST"])
def post_image_to_index():
    payload = request.get_json()
    image_url = payload.get("url")
    if not image_url:
        return {"message": "No url provided"}, 400

    try:
        added_image = add_image_to_index(image_url, payload.get("metadata", ""))
        return added_image.to_dict()
    except Exception as e:
        return {"message": str(e)}, 400


@app.route('/api/images/search', methods=["POST"])
def search_simmilar_images():
    image_url = request.get_json().get("url")
    if not image_url:
        return {"message": "No url provided"}, 400

    try:
        added_image = add_image_to_index(image_url, payload.get("metadata", ""))
        return added_image.to_dict()
    except Exception as e:
        return {"message": str(e)}, 400


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
