import time
from flask import Flask, jsonify, request
from flask_script import Manager, Server
from multiprocessing import Process
from project.doorsign import DoorSign


app = Flask(__name__)
running = True
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
    print("Started loop")
    while running:
        print("In loop")
        DoorSign.draw
        time.sleep(0.05)
    pass


class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        global p
        p = Process(target=display_loop)
        p.start()
        return Server.__call__(self, app, *args, **kwargs)


manager = Manager(app)
manager.add_command('runserver', CustomServer())

if __name__ == "__main__":
    manager.run()