from typing import List
import random

from Elevator import Call, Elevator


def generate_call(people):
    fr = random.randint(-5, 110)
    to = random.randint(-5, 110)
    pl = people

    return Call(from_floor=fr, to_floor=to, people=pl)
