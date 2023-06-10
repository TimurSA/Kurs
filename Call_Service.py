import random
import time
from typing import List

from Elevator import Elevator, Call


class Call_Manager:

    def __init__(self, *, elevator1: Elevator, elevator2: Elevator):
        self.elevator1 = elevator1
        self.elevator2 = elevator2
        self.all_calls = []
        self.processed = []

    def add_call(self, calls: List[Call]):
        self.all_calls = calls

    def can_drop_by(self, earliest_call, second_earliest_call):
        if earliest_call.direction == "UP" == second_earliest_call:
            if earliest_call.from_floor < second_earliest_call.from_floor:
                return True
            else:
                return False
        if earliest_call.direction == "DOWN" == second_earliest_call:
            if earliest_call.from_floor > second_earliest_call.from_floor:
                return True
            else:
                return False

    def manage_calls_fifo(self):
        while self.all_calls:

            earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
            print("First!!!", end='')
            print(earliest_call, earliest_call.direction)
            self.all_calls.remove(earliest_call)
            second_earliest_call = None

            distance1 = abs(self.elevator1.current_floor - earliest_call.from_floor)
            distance2 = abs(self.elevator2.current_floor - earliest_call.from_floor)

            if self.all_calls:
                temp_lst = []
                if earliest_call.direction == "UP":
                    temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor > earliest_call.from_floor and x.to_floor < earliest_call.to_floor,
                            temp_lst))
                else:
                    temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor < earliest_call.from_floor and x.to_floor > earliest_call.to_floor,
                            temp_lst))
                if temp_lst:
                    second_earliest_call = min(temp_lst, key=lambda x: x.time)
                    print("Second!!!", end='')
                    print(second_earliest_call, second_earliest_call.direction)

            if distance1 <= distance2:
                self.elevator1.move_floor_fifo(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

                if not self.all_calls:
                    break

                earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
                print("First!!!", end='')
                print(earliest_call, earliest_call.direction)
                self.all_calls.remove(earliest_call)
                second_earliest_call = None
                if self.all_calls:
                    temp_lst = []
                    if earliest_call.direction == "UP":
                        temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                        if temp_lst:
                            temp_lst = list(filter(lambda
                                                       x: x.from_floor > earliest_call.from_floor and x.to_floor < earliest_call.to_floor,
                                                   temp_lst))
                    else:
                        temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                        if temp_lst:
                            temp_lst = list(filter(lambda
                                                       x: x.from_floor < earliest_call.from_floor and x.to_floor > earliest_call.to_floor,
                                                   temp_lst))
                    if temp_lst:
                        second_earliest_call = min(temp_lst, key=lambda x: x.time)
                        print("Second!!!", end='')
                        print(second_earliest_call, second_earliest_call.direction)

                self.elevator2.move_floor_fifo(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

            else:
                self.elevator2.move_floor_fifo(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

                if not self.all_calls:
                    break

                earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
                print("First!!!", end='')
                print(earliest_call, earliest_call.direction)
                self.all_calls.remove(earliest_call)
                second_earliest_call = None
                if self.all_calls:
                    temp_lst = []
                    if earliest_call.direction == "UP":
                        temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                        if temp_lst:
                            temp_lst = list(filter(lambda
                                                       x: x.from_floor > earliest_call.from_floor and x.to_floor < earliest_call.to_floor,
                                                   temp_lst))
                    else:
                        temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                        if temp_lst:
                            temp_lst = list(filter(lambda
                                                       x: x.from_floor < earliest_call.from_floor and x.to_floor > earliest_call.to_floor,
                                                   temp_lst))
                    if temp_lst:
                        second_earliest_call = min(temp_lst, key=lambda x: x.time)
                        print("Second!!!", end='')
                        print(second_earliest_call, second_earliest_call.direction)

                self.elevator1.move_floor_fifo(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

    def manage_calls_nearest(self):
        while self.all_calls:
            nearest_call: Call = min(self.all_calls, key=lambda x: abs(x.from_floor - self.elevator2.current_floor))

            nearest_call1: Call = min(self.all_calls, key=lambda x: abs(x.from_floor - self.elevator1.current_floor))
            nearest_call2: Call = min(self.all_calls, key=lambda x: abs(x.from_floor - self.elevator2.current_floor))

            distance1 = abs(self.elevator1.current_floor - nearest_call1.from_floor)
            distance2 = abs(self.elevator2.current_floor - nearest_call2.from_floor)

            if distance1 <= distance2:
                self.all_calls.remove(nearest_call1)
                temp_lst = self.elevator1.move_floor_fifo(nearest_call1, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
                self.all_calls.remove(nearest_call2)
                temp_lst = self.elevator2.move_floor_fifo(nearest_call2, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
            else:
                self.all_calls.remove(nearest_call2)
                temp_lst = self.elevator2.move_floor_fifo(nearest_call2, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
                self.all_calls.remove(nearest_call1)
                temp_lst = self.elevator1.move_floor_fifo(nearest_call1, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
