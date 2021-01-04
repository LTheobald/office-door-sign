from unicornhatmini import UnicornHATMini
from flask import Flask, jsonify
from markupsafe import escape
from project.status import Status

app = Flask(__name__)

# Setup or UnicornHatMini
unicornhatmini = UnicornHATMini()
unicornhatmini.set_rotation(0)
unicornhatmini.set_brightness(0.1)

# Default status on startup
current_status = Status.FREE


def set_status(status):
    """Set the current status to one matching the passed in string if appropriate"""
    global current_status
    for name, member in Status.__members__.items():
        if (name == status) | (name.lower() == status):
            print("Changing current status from", current_status, "to", member)
            current_status = member
            draw()
            return True
    return False


def draw():
    """Updates the UnicornHatMini to reflect current status"""
    unicornhatmini.set_all(current_status.r, current_status.g, current_status.b)
    unicornhatmini.show()


@app.route("/")
def root():
    """A simple message to prove the API is up and accepting requests"""
    return jsonify({"running":True}), 200


@app.route("/switch")
def switchOnOff():
    """An easy switch to turn the display on or off"""
    global current_status
    if current_status is Status.OFF:
        current_status = Status.FREE
    else:
        current_status = Status.OFF
    draw()
    return "OK", 200


@app.route("/status/<status>")
def status(status):
    """Change the status to the supplied string"""
    safeStatus = escape(status)
    if set_status(safeStatus):
        return jsonify({"status": safeStatus}), 200
    return jsonify({"status": "UNKNOWN: " + safeStatus}), 404


# LET'S DO THIS!
draw()