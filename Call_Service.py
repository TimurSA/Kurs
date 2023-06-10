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

            earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
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


            if distance1 <= distance2:
                self.elevator1.move_floor_elevator(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

                if not self.all_calls:
                    break

                earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
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

                self.elevator2.move_floor_elevator(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

            else:
                self.elevator2.move_floor_elevator(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

                if not self.all_calls:
                    break

                earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
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

                self.elevator1.move_floor_elevator(earliest_call, second_earliest_call)
                if second_earliest_call:
                    self.all_calls.remove(second_earliest_call)

    @measure_time
    def manage_calls_nearest(self):
        while self.all_calls:
            nearest_call1 = None
            nearest_call2 = None

            if self.all_calls:
                nearest_call1: Call = min(self.all_calls,
                                          key=lambda x: abs(x.from_floor - self.elevator1.current_floor))
            if nearest_call1:
                self.all_calls.remove(nearest_call1)

            if self.all_calls:
                nearest_call2: Call = min(self.all_calls,
                                          key=lambda x: abs(x.from_floor - self.elevator2.current_floor))
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
                    second_nearest_call1 = min(temp_lst, key=lambda x: x.time)

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
                    second_nearest_call2 = min(temp_lst, key=lambda x: x.time)

            self.elevator1.move_floor_elevator(nearest_call1, second_nearest_call1)
            if second_nearest_call1:
                self.all_calls.remove(second_nearest_call1)

            if not self.all_calls:
                break

            self.elevator2.move_floor_elevator(nearest_call2, second_nearest_call2)
            if second_nearest_call2:
                self.all_calls.remove(second_nearest_call2)
