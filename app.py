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
    return await render_template('index.html', detected_faces = json.dumps(["dflhdhfd", "kdkbvds", "kdscdb"]))


@app.route('/detectFace', methods=["POST"])
async def detectFace():
    isthisFile = request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    await isthisFile.save(str(Path(__file__).resolve().parent) + "/uploads/" + isthisFile.filename)
    detected_faces = FaceRecognition().detect_face()
    return jsonify(detected_faces)

app.run(host=socket.gethostname(), port=80, debug=True)
