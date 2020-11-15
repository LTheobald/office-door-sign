import time
import atexit
from flask import Flask, jsonify, request
from multiprocessing import Process, Manager
from project.doorsign import DoorSign
from markupsafe import escape


def create_app():
    app = Flask(__name__)
    doorSign = DoorSign()
    running = True

    manager = Manager()
    lproxy = manager.list()
    lproxy.append(doorSign)

    def interrupt():
        print("Terminating")
        p.terminate()

    def display_loop(listProxy):
        doorSign = listProxy[0]
        while running:
            doorSign.draw()
            time.sleep(0.05)

    @app.route("/")
    def root():
        return jsonify({"running":True}), 200

    @app.route("/switch")
    def switch():
        doorSign.switch
        return "OK", 200

    @app.route("/status/<status>")
    def status(status):
        safeStatus = escape(status)
        if doorSign.set(safeStatus):
            return jsonify({"status": safeStatus}), 200
        return jsonify({"status": "UNKNOWN: " + safeStatus}), 404

    p = Process(target=display_loop, args=(lproxy,))
    p.start()
    atexit.register(interrupt)
    return app


app = create_app()