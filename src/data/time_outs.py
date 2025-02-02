from enum import Enum


class TimeOut(Enum):
    VERY_SHORT = 1
    SHORT = 3
    MEDIUM = 10
    LONG = 30
    VERY_LONG = 60