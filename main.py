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

    # calls = generate_random_number_of_calls(100)

    elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
    elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

    app = Call_Manager(elevator1=elevator1, elevator2=elevator2)
    # app.add_call(calls)
    # app.manage_calls_nearest()
    # app.elevator1.print_statistics()
    # app.elevator2.print_statistics()

    rand_size = 1

    k = 0

    if choose.startswith('1'):
        for minute in range(1 * 60):
            for passenger in generate_passengers():
                if passenger == 1:
                    k += 1
                    people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                    lst.append(generate_call(people))
                    if len(lst) == rand_size:
                        app.add_call(lst)
                        app.manage_calls_fifo()
                        rand_size = random.randint(1, 15)
                        lst = []
                else:
                    pass
        app.elevator1.print_statistics()
        app.elevator2.print_statistics()
    else:
        for minute in range(1 * 60):
            for passenger in generate_passengers():
                if passenger == 1:
                    k += 1
                    people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                    lst.append(generate_call(people))
                    if len(lst) == rand_size:
                        app.add_call(lst)
                        app.manage_calls_nearest()
                        rand_size = random.randint(1, 15)
                        lst = []
                else:
                    pass
        app.elevator1.print_statistics()
        app.elevator2.print_statistics()

    print(k)