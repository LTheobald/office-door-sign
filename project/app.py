from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/switch", methods = ['POST'])
def switch():
    content = request.json
    if content["switch"] == "on":
        return jsonify({"switch":"on"}), 200
    elif content["switch"] == "off":
        return jsonify({"switch":"off"}), 200
    else:
        return "", 400


@app.route("/status", methods = ['POST'])
def status():
    return "ACK"


if __name__ == "__main__":
    app.run()
