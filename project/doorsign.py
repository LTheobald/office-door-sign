import sys
from enum import IntEnum
from unicornhatmini import UnicornHATMini


class DoorSign:
    # Define the enum for states
    class Status(IntEnum):
        OFF = 0
        FREE = 1
        WORKING = 2
        ON_CALL = 3

    def __init__(self):
        self.current_status = self.Status.FREE
        self.unicornhatmini = UnicornHATMini()
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
                self.current_status = member
                print("Set: " + self.current_status.name)
            return True
        return False

    def get(self):
        return self.current_status.name

    def draw(self):
        print("Draw: " + self.current_status.name)
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
