from enum import Enum

class Status(Enum):
    """ Enum representing my status to reflect on the door sign. """

    OFF = (0, 0, 0)           # Black / Off
    FREE = (0, 255, 0)        # Green
    WORKING = (0, 255, 255)   # Yellow
    ON_CALL = (255, 0, 0)     # Red

    @property
    def color(self):
        return self.value