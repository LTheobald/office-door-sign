from flask import Flask, jsonify, request
from .status import Status, draw

app = Flask(__name__)
switched_on = False


@app.route("/switch", methods = ['POST'])
def switch():
    content = request.json
    if content["switch"] == "on":
        switchedOn = True;
        return jsonify({"switch":"on"}), 200
    elif content["switch"] == "off":
        switchedOn = False;
        return jsonify({"switch":"off"}), 200
    else:
        return "", 400


@app.route("/status", methods=['POST'])
def status():
    content = request.json
    return set_status(content["status"])


def set_status(status):
    for name, member in Status.__members__.items():
        if (name == status) | (name.lower() == status):
            currentStatus = member
            print("Name is " + name)
            return jsonify({"status":name.lower()}), 200
    return jsonify({"status":"unknown"}), 404


currentStatus = Status.FREE
while switched_on:
    draw(currentStatus)


if __name__ == "__main__":
    app.run()
