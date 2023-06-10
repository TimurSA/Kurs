"""

pip install numpy

"""

import random
from Call_Service import Call_Manager
from Calls_Generator import generate_call
from Elevator import Elevator, Call
from Passangers import generate_passengers
import time
import codecs


def generate_random_number_of_calls(number_of_calls: int):
    calls_lst = []
    for _ in range(number_of_calls):
        fr = random.randint(-5, 110)
        to = random.randint(-5, 110)
        pl = random.randint(1, Elevator.MAX_PEOPLE + 5)
        # while True:
        #     if fr != to:
        #         break
        #     fr = random.randint(1, 100)
        #     to = random.randint(1, 100)
        calls_lst.append(Call(from_floor=fr, to_floor=to, people=pl))

    return calls_lst


if __name__ == '__main__':
    lst = []
    choose = input("Выберете алгоритм:\n1. Первый вошел-первый вышел\n2. Ближайший запрос\nВпишите либо 1, либо 2.\n")

    # calls = generate_random_number_of_calls(trys)

    elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
    elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

    app = Call_Manager(elevator1=elevator1, elevator2=elevator2)

    if choose.startswith('1'):

        for minute in range(1 * 60):
            for passenger in generate_passengers():
                if passenger == 1:
                    people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                    lst.append(generate_call(people))
                    if len(lst) == 10:
                        app.add_call([generate_call(people)])
                        app.manage_calls_nearest()
                        lst = []
                else:
                    pass
    else:
        for minute in range(1 * 60):
            for passenger in generate_passengers():
                if passenger == 1:
                    people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                    lst.append(generate_call(people))
                    if len(lst) == 10:
                        app.add_call([generate_call(people)])
                        app.manage_calls_nearest()
                        lst = []
                else:
                    pass
