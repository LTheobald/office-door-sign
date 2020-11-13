from flask import Flask, jsonify, request
from project.status import Status, draw

app = Flask(__name__)
switched_on = True
current_status = Status.FREE
while switched_on:
    draw(current_status)


@app.route("/")
def root():
    return jsonify({"running":"ok"}), 200


@app.route("/switch", methods = ['POST'])
def switch():
    content = request.json
    if content["switch"] == "on":
        switched_on = True;
        return jsonify({"switch":"on"}), 200
    elif content["switch"] == "off":
        switched_on = False;
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
            current_status = member
            print("Name is " + name)
            return jsonify({"status":name.lower()}), 200
    return jsonify({"status":"unknown"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0")
