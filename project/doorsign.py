import sys
from enum import IntEnum
from gpiozero import Button


class DoorSign:

    # Define the enum for states
    class Status(IntEnum):
        OFF = 0
        FREE = 1
        WORKING = 2
        ON_CALL = 3

    def __init__(self):
        # UnicornHatMini will only build on a Linux box so I mock this out on other platforms
        if sys.platform.startswith("linux"):
            from unicornhatmini import UnicornHATMini
            self.unicornhatmini = UnicornHATMini()
        else:
            from unittest import mock
            self.unicornhatmini = mock.Mock()

        self.current_status = self.Status.FREE
        self.button_a = Button(5)
        self.button_b = Button(6)
        self.button_x = Button(16)
        self.button_y = Button(24)
        self.unicornhatmini.set_rotation(0)
        self.unicornhatmini.set_brightness(0.1)

    def switch(self):
        if self.current_status is self.Status.OFF:
            self.current_status = self.Status.FREE
        else:
            self.current_status = self.Status.OFF

    def cycle(self):
        if self.current_status+1 is len(self.Status):
            self.current_status = self.Status(0)
        else:
            self.current_status = self.Status(self.current_status+1)

    def set(self, status):
        for name, member in self.Status.__members__.items():
            if (name == status) | (name.lower() == status):
                print("Setting new state to " + name)
                self.current_status = member
                return True
        return False

    def draw(self):
        if self.current_status is self.Status.FREE:
            # Green
            self.unicornhatmini.set_all(0, 255, 0)
        elif self.current_status is self.Status.WORKING:
            # Amber
            self.unicornhatmini.set_all(255, 191, 0)
        elif self.current_status is self.Status.ON_CALL:
            # Red
            self.unicornhatmini.set_all(255, 0, 0)
        elif self.current_status is self.Status.OFF:
            self.unicornhatmini.clear()

        self.unicornhatmini.show()