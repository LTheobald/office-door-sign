import time
from enum import auto, Enum
from unicornhatmini import UnicornHATMini

# Define the enum for states
class Status(Enum):
    FREE = auto()
    WORKING = auto()
    ON_CALL = auto()

unicornhatmini = UnicornHATMini()
unicornhatmini.set_rotation(0)
unicornhatmini.set_brightness(0.1)

def draw(status):
    if status == Status.FREE:
        unicornhatmini.set_all(0, 255, 0)
    elif status == Status.WORKING:
        unicornhatmini.set_all(255, 0, 0)
    elif status == Status.ON_CALL:
        unicornhatmini.set_all(0, 255, 255)

    unicornhatmini.show()
    time.sleep(0.05)