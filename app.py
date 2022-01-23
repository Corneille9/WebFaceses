import socket

from quart import Quart, render_template, Request, abort, jsonify

from FaceRecognition import FaceRecognition

app = Quart(__name__)


@app.route("/")
async def index():
    return await render_template('index.html')


@app.route('/detectFace', methods=["POST"])
async def detectFace():
    detected_faces = FaceRecognition().detect_face()
    return jsonify(detected_faces)

app.run(host=socket.gethostname(), port=80, debug=True)
