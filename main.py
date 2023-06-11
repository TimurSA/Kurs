"""

pip install numpy

"""
import datetime
import random
from Call_Service import Call_Manager
from Calls_Generator import generate_call
from Elevator import Elevator, Call
from Passangers import generate_passengers
import time
import numpy as np
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

    elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
    elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

    app = Call_Manager(elevator1=elevator1, elevator2=elevator2)

    rand_size = 1
    peak_hours = [8, 14, 20]
    p_current = 0

    k = 0

    if choose.startswith('1'):
        for minute in range(24 * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = 0.5
            else:
                p_current = 0.2

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                start = minute
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                k += people
                lst.append(generate_call(people))
                if len(lst) == 10:
                    stop = minute
                    app.add_call(lst)
                    app.manage_calls_fifo()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass
        app.elevator1.print_statistics()
        app.elevator2.print_statistics()
    else:
        for minute in range(24 * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = 0.5
            else:
                p_current = 0.2

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                start = minute
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                k += people
                lst.append(generate_call(people))
                if len(lst) == 10:
                    stop = minute
                    app.add_call(lst)
                    app.manage_calls_nearest()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass
        app.elevator1.print_statistics()
        app.elevator2.print_statistics()

    print(k)
