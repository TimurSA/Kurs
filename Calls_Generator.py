from typing import List
import random

from Elevator import Call, Elevator


def generate_call(people):
    fr = random.randint(1, Elevator.MAX_PEOPLE)
    to = random.randint(1, Elevator.MAX_PEOPLE)
    pl = people

    return Call(from_floor=fr, to_floor=to, people=pl)
