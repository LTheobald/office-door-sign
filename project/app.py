import time
import threading
from flask import Flask, jsonify, request
from project.doorsign import DoorSign


app = Flask(__name__)
doorSign = DoorSign()


@app.route("/")
def root():
    return jsonify({"running":True}), 200


@app.route("/switch")
def switch():
    doorSign.switch
    return "OK", 200


@app.route("/status", methods=['POST'])
def status():
    content = request.json
    if DoorSign.set(content["status"]):
        return jsonify({"status": content["status"]}), 200
    return jsonify({"status": "UNKNOWN: " + content["status"]}), 404


def display_loop():
    while True:
        DoorSign.draw
        time.sleep(0.05)


x = threading.Thread(target=display_loop)
x.start()
if __name__ == "__main__":
    app.run(debug=True)

