from Time_Spent import measure_time
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

    @measure_time
    def manage_calls_fifo(self):
        while self.all_calls:
            earliest_call1 = None
            earliest_call2 = None

            second_earliest_call1 = None
            second_earliest_call2 = None

            if self.all_calls:
                earliest_call1: Call = min(self.all_calls,
                                           key=lambda x: x.time)
                print("First!!!" + str(earliest_call1))
            if earliest_call1:
                self.all_calls.remove(earliest_call1)

            if self.all_calls:
                earliest_call2: Call = min(self.all_calls,
                                           key=lambda x: x.time)
                print("Second!!!" + str(earliest_call2))
            if earliest_call2:
                self.all_calls.remove(earliest_call2)

            if self.all_calls:
                temp_lst = []
                if earliest_call1.direction == "UP":
                    temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor > earliest_call1.from_floor and x.to_floor < earliest_call1.to_floor,
                            temp_lst))
                else:
                    temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor < earliest_call1.from_floor and x.to_floor > earliest_call1.to_floor,
                            temp_lst))
                if temp_lst:
                    second_earliest_call1 = min(temp_lst,
                                                key=lambda x: x.time)

            if self.all_calls:
                temp_lst = []
                if earliest_call2.direction == "UP":
                    temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor > earliest_call2.from_floor and x.to_floor < earliest_call2.to_floor,
                            temp_lst))
                else:
                    temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor < earliest_call2.from_floor and x.to_floor > earliest_call2.to_floor,
                            temp_lst))
                if temp_lst:
                    second_earliest_call2 = min(temp_lst,
                                                key=lambda x: x.time)

            self.elevator1.move_floor_elevator(earliest_call1, second_earliest_call1)
            if second_earliest_call1:
                self.all_calls.remove(second_earliest_call1)

            if not self.all_calls:
                break

            self.elevator2.move_floor_elevator(earliest_call2, second_earliest_call2)
            if second_earliest_call2:
                self.all_calls.remove(second_earliest_call2)

    @measure_time
    def manage_calls_nearest(self):
        while self.all_calls:
            nearest_call1 = None
            nearest_call2 = None

            if self.all_calls:
                nearest_call1: Call = min(self.all_calls,
                                          key=lambda x: abs(x.from_floor - self.elevator1.current_floor))
                print("First!!!" + str(nearest_call1))
            if nearest_call1:
                self.all_calls.remove(nearest_call1)

            if self.all_calls:
                nearest_call2: Call = min(self.all_calls,
                                          key=lambda x: abs(x.from_floor - self.elevator2.current_floor))
                print("Second!!!" + str(nearest_call2))
            if nearest_call2:
                self.all_calls.remove(nearest_call2)

            second_nearest_call1 = None
            second_nearest_call2 = None

            if self.all_calls:
                temp_lst = []
                if nearest_call1.direction == "UP":
                    temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor > nearest_call1.from_floor and x.to_floor < nearest_call1.to_floor,
                            temp_lst))
                else:
                    temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor < nearest_call1.from_floor and x.to_floor > nearest_call1.to_floor,
                            temp_lst))
                if temp_lst:
                    second_nearest_call1 = min(temp_lst, key=lambda x: abs(x.from_floor - self.elevator1.current_floor))

            if self.all_calls:
                temp_lst = []
                if nearest_call2.direction == "UP":
                    temp_lst = list(filter(lambda x: x.direction == "UP", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor > nearest_call2.from_floor and x.to_floor < nearest_call2.to_floor,
                            temp_lst))
                else:
                    temp_lst = list(filter(lambda x: x.direction == "DOWN", self.all_calls))
                    if temp_lst:
                        temp_lst = list(filter(
                            lambda x: x.from_floor < nearest_call2.from_floor and x.to_floor > nearest_call2.to_floor,
                            temp_lst))
                if temp_lst:
                    second_nearest_call2 = min(temp_lst, key=lambda x: abs(x.from_floor - self.elevator2.current_floor))

            self.elevator1.move_floor_elevator(nearest_call1, second_nearest_call1)
            if second_nearest_call1:
                self.all_calls.remove(second_nearest_call1)

            if not self.all_calls:
                break

            self.elevator2.move_floor_elevator(nearest_call2, second_nearest_call2)
            if second_nearest_call2:
                self.all_calls.remove(second_nearest_call2)
