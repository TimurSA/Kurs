import random
from Call_Service import Call_Manager
from Calls_Generator import generate_calls
from Elevator import Elevator, Call

trys = int(input("Сколько зарпосов: "))

calls = []

while True:
    if isinstance(trys, int):
        break
    print('Некорректный ввод')
    trys = int(input("Сколько запросов: "))

calls = generate_calls(trys)

elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

app = Call_Manager(elevator1=elevator1, elevator2=elevator2)

app.add_call(calls)
app.manage_calls_fifo()

app.add_call(calls)
app.manage_calls_nearest()
# choose = input("Выберете алгоримт:\n1. Первый вошел-первый вышел\n2. Ближайший запрос\nВпишите либо 1, либо 2.\n")
# if choose.startswith('1'):
#     app.manage_calls_fifo()
# else:
#     app.manage_calls_nearest()
