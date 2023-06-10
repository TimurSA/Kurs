from enum import Enum


class Elevator_Status(Enum):
    MOVING_UP = 1
    MOVING_DOWN = 2
    WAITING = 3
    STANDSTILL = 4
