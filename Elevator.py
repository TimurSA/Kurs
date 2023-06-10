import time
from datetime import datetime, timedelta
from typing import List
import codecs


class Call:

    def __init__(self, *, from_floor: int, to_floor: int, people: int):
        self.from_floor = from_floor
        self.to_floor = to_floor
        self.direction = "DOWN" if self.from_floor - self.to_floor > 0 else "UP"
        self.people = people
        self.time = datetime.now()

    def __str__(self):
        return f'from {self.from_floor} to {self.to_floor}'


class Elevator:
    number_of_el = 1

    MAX_FLOOR = 100
    MIN_FLOOR = 1
    MAX_PEOPLE = 10

    TIME_WAIT = 5
    TIME_PER_FLOOR = 5

    def __init__(self, *, current_floor: int = 1):
        if current_floor > Elevator.MAX_FLOOR:
            self.current_floor = Elevator.MAX_FLOOR
        elif current_floor < 1:
            self.current_floor = 1
        else:
            self.current_floor = current_floor
        self.all_time_waited = 0
        self.all_time_moved = 0
        self.people_in_el = 0
        self.all_people_left = 0
        self.id = Elevator.number_of_el
        Elevator.number_of_el += 1

        self.log = []  # список логов

        # Функция добавления вызова (можно передавать много аргументов)

    def write_log(self, s: List[str]):
        with codecs.open("log.txt", "a", "utf-8") as file:
            for i in s:
                full_str = f'{self.id} ' + i + '\n'
                file.write(f'{full_str}')

    def read_log(self, s: str):
        with open("log.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)

    def move_floor(self, from_floor, to_floor):
        self.all_time_moved += abs(from_floor - to_floor) * Elevator.TIME_PER_FLOOR
        self.current_floor = to_floor

    def move_floor_elevator(self, call1, call2):
        earliest_call = call1
        second_earliest_call = call2

        # Проверка входных данных
        if earliest_call.people > Elevator.MAX_PEOPLE:
            self.log.append("Перегрузка лифта! Слишком много человек...")
            self.write_log(self.log)
            self.log = []
            return
        if earliest_call.from_floor > Elevator.MAX_FLOOR or earliest_call.from_floor < Elevator.MIN_FLOOR:
            self.log.append("Лифт вызывается с не существующего этажа...")
            self.write_log(self.log)
            self.log = []
            return
        if earliest_call.to_floor > Elevator.MAX_FLOOR or earliest_call.to_floor < Elevator.MIN_FLOOR:
            self.log.append("Лифт не может отправиться на несуществующий этаж...")
            self.write_log(self.log)
            self.log = []
            return
        if earliest_call.from_floor == earliest_call.to_floor:
            self.log.append("Нельзя поехать на этаж, на котором вы находитесь...")
            self.write_log(self.log)
            self.log = []
            return

        self.people_in_el += earliest_call.people

        if abs(self.current_floor - earliest_call.from_floor) == 0:
            self.log.append(f'Receiving call from the same floor... Floor ={self.current_floor}')
        else:
            self.log.append(f'Moving from {self.current_floor} to {earliest_call.from_floor}')
            self.move_floor(self.current_floor, earliest_call.from_floor)
            self.all_time_waited += Elevator.TIME_WAIT

        if second_earliest_call:
            if second_earliest_call.people + earliest_call.people <= Elevator.MAX_PEOPLE:
                self.people_in_el += second_earliest_call.people
            else:
                temp = Elevator.MAX_FLOOR - self.people_in_el
                self.people_in_el = Elevator.MAX_PEOPLE
                self.all_people_left += second_earliest_call.people - temp

            if earliest_call.direction == "UP":

                if earliest_call.from_floor < second_earliest_call.from_floor and earliest_call.to_floor == second_earliest_call.to_floor:
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.from_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.from_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.to_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.to_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.people_in_el -= self.people_in_el
                    self.write_log(self.log)
                    self.log = []
                    return

                if earliest_call.from_floor < second_earliest_call.from_floor and earliest_call.to_floor > second_earliest_call.to_floor:
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.from_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.from_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.to_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.to_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.people_in_el -= second_earliest_call.people

            else:
                if earliest_call.from_floor > second_earliest_call.from_floor and earliest_call.to_floor == second_earliest_call.to_floor:
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.from_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.from_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.to_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.to_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.people_in_el -= self.people_in_el
                    self.write_log(self.log)
                    self.log = []
                    return

                if earliest_call.from_floor > second_earliest_call.from_floor and earliest_call.to_floor < second_earliest_call.to_floor:
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.from_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.from_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.log.append(f'Moving from {self.current_floor} to {second_earliest_call.to_floor}')
                    self.move_floor(self.current_floor, second_earliest_call.to_floor)
                    self.all_time_waited += Elevator.TIME_WAIT
                    self.people_in_el -= second_earliest_call.people

        #####################################################

        self.log.append(f'Moving from {self.current_floor} to {earliest_call.to_floor}')
        self.move_floor(self.current_floor, earliest_call.to_floor)
        self.all_time_waited += Elevator.TIME_WAIT
        self.people_in_el -= earliest_call.people
        self.write_log(self.log)
        self.log = []

    def print_statistics(self):
        print(
            f'Time spent moving: {self.all_time_moved};\nTime spent waiting: {self.all_time_waited};\nRatio: {self.all_time_moved / self.all_time_waited}\nPeople left due to lack of space: {self.all_people_left}')


if __name__ == "__main__":
    pass
