import time
import atexit
from flask import Flask, jsonify, request
from flask_script import Manager, Server
from multiprocessing import Process
from project.doorsign import DoorSign


running = True
doorSign = DoorSign()

def create_app():
    app = Flask(__name__)

    def interrupt(p):
        print("Terminating")
        p.terminate()

    def display_loop():
        print("Started loop")
        while running:
            print("In loop")
            DoorSign.draw
            time.sleep(0.05)

    p = Process(target=display_loop)
    p.start()
    atexit.register(interrupt(p))
    return app


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


app = create_app()