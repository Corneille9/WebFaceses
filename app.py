import json
import os.path
import socket
from pathlib import Path

from quart import Quart, render_template, Request, abort, jsonify
from quart.flask_patch.globals import request

from FaceRecognition import FaceRecognition

app = Quart(__name__)


@app.route("/")
async def index():
    print()
    return await render_template('index.html', detected_faces=json.dumps(["dflhdhfd", "kdkbvds", "kdscdb"]))


@app.route('/detectFace', methods=["POST"])
async def detectFace():
    image_name = request.get_json()
    print("image_name", image_name)
    detected_faces = FaceRecognition().detect_face(file="uploads/" + image_name.get("data"))
    return jsonify(detected_faces)


@app.route('/upload', methods=["POST"])
async def upload():
    isthisFile = request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    await isthisFile.save(str(Path(__file__).resolve().parent) + "/uploads/" + isthisFile.filename)
    return jsonify({"result": "HTTP/200 ok"})


if __name__ == "__main__":
    app.run(host=socket.gethostname(), port=80, debug=True)
