from typing import List
import random

from Elevator import Call, Elevator


def generate_calls(number_of_calls: int) -> List[Call]:
    calls_lst = []
    for _ in range(number_of_calls):
        fr = random.randint(1, 100)
        to = random.randint(1, 100)
        pl = random.randint(1, Elevator.MAX_PEOPLE + 5)
        # while True:
        #     if fr != to:
        #         break
        #     fr = random.randint(1, 100)
        #     to = random.randint(1, 100)
        calls_lst.append(Call(from_floor=fr, to_floor=to, people=pl))

    return calls_lst
