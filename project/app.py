import time
import atexit
from flask import Flask, jsonify, request
from multiprocessing import Process
from project.doorsign import DoorSign


def create_app():
    app = Flask(__name__)
    running = True
    doorSign = DoorSign()

    def interrupt():
        print("Terminating")
        p.terminate()

    def display_loop():
        while running:
            doorSign.draw
            time.sleep(0.05)

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
        if doorSign.set(content["status"]):
            return jsonify({"status": content["status"]}), 200
        return jsonify({"status": "UNKNOWN: " + content["status"]}), 404

    p = Process(target=display_loop)
    p.start()
    atexit.register(interrupt(p))
    return app


app = create_app()