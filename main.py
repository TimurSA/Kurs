import random
import time
from Call_Service import Call_Manager

from Elevator import Elevator, Call

trys = int(input("Сколько зарпосов: "))


calls = []

while True:
    if isinstance(trys, int):
        break
    print('Некорректный ввод')
    trys = int(input("Сколько зарпосов: "))

for _ in range(trys):
    while True:
        from_floor = random.randint(1, 100)
        to_floor = random.randint(1, 100)
        people = random.randint(1, 10)
        if from_floor != to_floor:
            break
    temp_call = Call(from_floor=from_floor, to_floor=to_floor, people=people)
    # time.sleep(0.10)
    calls.append(temp_call)

elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

for call in calls:
    print(call)

app = Call_Manager(elevator1=elevator1, elevator2=elevator2)
app.add_call(calls)

choose = input("Выберете алгоримт:\n1. Первый вошел-первый вышел\n2. Ближайший запрос\nВпишите либо 1, либо 2")
if choose.startswith('1'):
    app.manage_calls_fifo()
else:
    print(elevator1.add_call_nearest(calls))


