import sys
import threading
from enum import IntEnum
from gpiozero import Button
from signal import pause

# UnicornHatMini will only build on a Linux box so I mock this out on other platforms
if sys.platform.startswith("linux"):
    from unicornhatmini import UnicornHATMini
    unicornhatmini = UnicornHATMini()
else:
    from unittest import mock
    unicornhatmini = mock.Mock()


# Define the enum for states
class Status(IntEnum):
    OFF = 0
    FREE = 1
    WORKING = 2
    ON_CALL = 3


current_status = Status.FREE
button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)
unicornhatmini.set_rotation(0)
unicornhatmini.set_brightness(0.1)


def switch():
    global current_status
    if current_status is Status.OFF:
        current_status = Status.FREE
    else:
        current_status = Status.OFF


def cycle():
    global current_status
    if current_status+1 is len(Status):
        current_status = Status(0)
    else:
        current_status = Status(current_status+1)


def draw():
    if current_status is Status.FREE:
        # Green
        unicornhatmini.set_all(0, 255, 0)
    elif current_status is Status.WORKING:
        # Amber
        unicornhatmini.set_all(255, 191, 0)
    elif current_status is Status.ON_CALL:
        # Red
        unicornhatmini.set_all(255, 0, 0)
    elif current_status is Status.OFF:
        unicornhatmini.clear()

    unicornhatmini.show()

def button_loop():
    try:
        button_a.when_pressed = switch
        button_b.when_pressed = switch
        button_x.when_pressed = cycle
        button_y.when_pressed = cycle
        pause()
    except KeyboardInterrupt:
        button_a.close()
        button_b.close()
        button_x.close()
        button_y.close()


x = threading.Thread(target=button_loop)
x.start()