import time
import atexit
from flask import Flask, jsonify, request
from multiprocessing import Process
from project.doorsign import DoorSign
from markupsafe import escape

doorSign = DoorSign()
running = True

def create_app():
    app = Flask(__name__)

    def interrupt():
        print("Terminating")
        p.terminate()

    def display_loop(doorSign):
        while running:
            doorSign.draw()
            time.sleep(0.05)

    @app.route("/")
    def root():
        return jsonify({"running":True}), 200

    @app.route("/switch")
    def switch():
        global doorSign
        doorSign.switch
        return "OK", 200

    @app.route("/status/<status>")
    def status(status):
        global doorSign

        safeStatus = escape(status)
        if doorSign.set(safeStatus):
            return jsonify({"status": safeStatus}), 200
        return jsonify({"status": "UNKNOWN: " + safeStatus}), 404

    p = Process(target=display_loop, args={doorSign})
    p.start()
    atexit.register(interrupt)
    return app


app = create_app()