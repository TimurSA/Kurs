"""

pip install numpy

"""
import random
from Call_Service import Call_Manager
from Calls_Generator import generate_call
from Elevator import Elevator
import numpy as np


def service():
    # peak_hours = [8, 14, 20]
    Elevator.MAX_FLOOR = int(input("Введите сколько этадей в здании: "))
    time_duration = int(input("Введите время работы ливтов (от 1 до 24 часов): "))
    peak_hours = list(map(int, input(
        "Введите через пробел часы пик (Если выходит за рамки 24 часов, часы пик не учитываются: ").split()))
    peak_hours = list(filter(lambda x: 0 < x <= 24, peak_hours))
    p_in_peak = float(input("Введите значение p_current в час пик: "))
    p_not_in_peak = float(input("Введите значение p_current не в час пик: "))

    elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
    elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

    app = Call_Manager(elevator1=elevator1, elevator2=elevator2)

    choose_alg = input(
        "Выберете алгоритм:\n1. Первый вошел-первый вышел\n2. Ближайший запрос\nВпишите либо 1, либо 2.\n")

    all_people = 0
    p_current = 0
    rand_size = 5
    lst = []
    if choose_alg.startswith('1'):
        for minute in range(time_duration * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = p_in_peak
            else:
                p_current = p_not_in_peak

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                start = minute
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                all_people += people
                lst.append(generate_call(people))
                print(lst[-1])
                if minute == (time_duration * 60) - 1 and lst:
                    app.add_call(lst)
                    app.manage_calls_fifo()
                    rand_size = random.randint(1, 15)
                    lst = []
                    break
                if len(lst) == rand_size:
                    stop = minute
                    app.add_call(lst)
                    app.manage_calls_fifo()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass
        print(app.elevator1.return_statistics())
        print(app.elevator2.return_statistics())
    else:
        for minute in range(time_duration * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = p_in_peak
            else:
                p_current = p_not_in_peak

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                start = minute
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                all_people += people
                lst.append(generate_call(people))
                print(lst[-1])
                if minute == (time_duration * 60) - 1 and lst:
                    app.add_call(lst)
                    app.manage_calls_nearest()
                    rand_size = random.randint(1, 15)
                    lst = []
                    break
                if len(lst) == rand_size:
                    stop = minute
                    app.add_call(lst)
                    app.manage_calls_nearest()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass
        print(app.elevator1.return_statistics())
        print(app.elevator2.return_statistics())

    print(all_people)


if __name__=='__main__':
    service()

