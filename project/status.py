import time
import sys
from enum import auto, Enum


# UnicornHatMini will only build on a Linux box so I mock this out on other platforms
if sys.platform.startswith("linux"):
    from unicornhatmini import UnicornHATMini
    unicornhatmini = UnicornHATMini()
else:
    from unittest import mock
    unicornhatmini = mock.Mock()


# Define the enum for states
class Status(Enum):
    FREE = auto()
    WORKING = auto()
    ON_CALL = auto()


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
