from flask import Flask, jsonify, request
from project.status import Status, draw
from multiprocessing import Process, Value

app = Flask(__name__)
switched_on = True
current_status = Status.FREE


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
            print("Setting new state to " + name)
            current_status = member
            return jsonify({"status":name.lower()}), 200
    return jsonify({"status":"unknown"}), 404


def display_loop():
    while switched_on:
        print(current_status)
        #draw(current_status)
        time.sleep(0.05)


if __name__ == "__main__":
    display_on = Value('b', True)
    p = Process(target=display_loop, args=(display_on,))
    p.start()
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
    p.join()