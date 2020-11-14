import time
import threading
from flask import Flask, jsonify, request
from project.status import Status, draw


app = Flask(__name__)
current_status = Status.FREE


@app.route("/")
def root():
    return jsonify({"running":"ok"}), 200


@app.route("/switch", methods = ['POST'])
def switch():
    global current_status

    content = request.json
    if content["switch"] == "on":
        print('Switching on')
        current_status = Status.FREE
        return jsonify({"switch":"on"}), 200
    elif content["switch"] == "off":
        print('Switching off')
        current_status = Status.OFF
        return jsonify({"switch":"off"}), 200
    else:
        return "", 400


@app.route("/status", methods=['POST'])
def status():
    content = request.json
    return set_status(content["status"])


def set_status(status):
    global current_status

    for name, member in Status.__members__.items():
        if (name == status) | (name.lower() == status):
            print("Setting new state to " + name)
            current_status = member
            return jsonify({"status":name.lower()}), 200
    return jsonify({"status":"unknown"}), 404


def display_loop():
    global current_status

    while True:
        draw(current_status)
        time.sleep(0.05)


x = threading.Thread(target=display_loop)
x.start()
if __name__ == "__main__":
    app.run(debug=True)
