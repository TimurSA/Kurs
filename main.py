"""

pip install numpy

"""
import random
from Call_Service import Call_Manager
from Calls_Generator import generate_call
from Elevator import Elevator
import numpy as np
from tkinter import *
import codecs


def start_program():
    result_label = Label(root, text="Результат: ")
    req_label = Label(root, text="")

    result_label.pack()
    req_label.pack()

    Elevator.MAX_FLOOR = int(max_floor_entry.get().strip())
    time_duration = int(time_duration_entry.get().strip())
    peak_hours = list(map(int, peak_hours_entry.get().split()))
    peak_hours = list(filter(lambda x: 0 < x <= 24, peak_hours))
    p_in_peak = float(p_in_peak_entry.get().strip())
    p_not_in_peak = float(p_not_in_peak_entry.get().strip())
    choose_alg = str(choose_alg_label_entry.get().strip())

    elevator1 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))
    elevator2 = Elevator(current_floor=random.randint(1, Elevator.MAX_FLOOR))

    app = Call_Manager(elevator1=elevator1, elevator2=elevator2)

    all_people = 0
    req = 0
    p_current = 0
    rand_size = 1
    lst = []
    full_calls = []
    if choose_alg.strip() == '1':
        print('\nUsing FIFO Algorithm...')
        for minute in range(time_duration * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = p_in_peak
            else:
                p_current = p_not_in_peak

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                req += 1
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                all_people += people
                lst.append(generate_call(people))
                with codecs.open("log_req.txt", "a", "utf-8") as file:
                    file.write(f'{lst[-1]}\n')
                if minute == (time_duration * 60) - 1 and lst:
                    app.add_call(lst)
                    app.manage_calls_fifo()
                    rand_size = random.randint(1, 15)
                    lst = []
                    break
                if len(lst) == rand_size:
                    app.add_call(lst)
                    app.manage_calls_fifo()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass
    elif choose_alg.strip() == '2':
        print('\nUsing Nearest-pick Algorithm...')
        for minute in range(time_duration * 60):
            hour = minute // 60
            if hour in peak_hours:
                p_current = p_in_peak
            else:
                p_current = p_not_in_peak

            passenger = np.random.binomial(1, p_current)
            if passenger == 1:
                req += 1
                people = random.randint(1, Elevator.MAX_PEOPLE + 5)
                all_people += people
                lst.append(generate_call(people))
                with codecs.open("log_req.txt", "a", "utf-8") as file:
                    file.write(f'{lst[-1]}\n')
                if minute == (time_duration * 60) - 1 and lst:
                    app.add_call(lst)
                    app.manage_calls_nearest()
                    rand_size = random.randint(1, 15)
                    lst = []
                    break
                if len(lst) == rand_size:
                    app.add_call(lst)
                    app.manage_calls_nearest()
                    rand_size = random.randint(1, 15)
                    lst = []
            else:
                pass

    else:
        print('Неверный ввод выбора алгоритма')
    print(f'People appeared:: {all_people}')

    result_label.config(
        text="Результат: " +
             f"\nElevator 1 statistics:\n" + app.elevator1.return_statistics() + f"\nElevator 2 statistics:\n" + app.elevator2.return_statistics()
             + "\nPeople appeared:" + str(all_people) + "\nNumber of calls: " + str(req))

    # temp_txt = '\n'.join(list(map(str, (full_calls))))
    #
    # req_label.config(text=temp_txt)


if __name__ == '__main__':
    # Создание окна
    root = Tk()

    # Добавление компонентов
    max_floor_label = Label(root, text="Введите количество этажей в здании:")
    max_floor_label.pack()
    max_floor_entry = Entry(root)
    max_floor_entry.pack()

    time_duration_label = Label(root, text="Введите время работы лифтов (от 1 до 24 часов):")
    time_duration_label.pack()
    time_duration_entry = Entry(root)
    time_duration_entry.pack()

    peak_hours_label = Label(root, text="Введите часы пик через пробел:")
    peak_hours_label.pack()
    peak_hours_entry = Entry(root)
    peak_hours_entry.pack()

    p_in_peak_label = Label(root, text="Введите значение p_current в час пик:")
    p_in_peak_label.pack()
    p_in_peak_entry = Entry(root)
    p_in_peak_entry.pack()

    p_not_in_peak_label = Label(root, text="Введите значение p_current не в час пик:")
    p_not_in_peak_label.pack()
    p_not_in_peak_entry = Entry(root)
    p_not_in_peak_entry.pack()

    choose_alg_label = Label(root,
                             text="Выберете алгоритм:\n1. Первый вошел-первый вышел\n2. Ближайший запрос\nВпишите либо 1, либо 2.\n")

    choose_alg_label.pack()
    choose_alg_label_entry = Entry(root)
    choose_alg_label_entry.pack()

    start_button = Button(root, text="Запустить программу", command=start_program)
    start_button.pack()

    # Запуск цикла обработки событий
    root.mainloop()
