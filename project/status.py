import enum


class Status(enum.Enum):
    """A enum to keep track of the colours used on the display & their
    meanings """

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    FREE = 0, 255, 0
    WORKING = 255, 191, 0
    ON_CALL = 255, 0, 0
    OFF = 0, 0, 0
