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

    def manage_calls_fifo(self):
        while self.all_calls:
            earliest_call: Call = min(self.all_calls, key=lambda x: x.time)
            self.all_calls.remove(earliest_call)

            distance1 = abs(self.elevator1.current_floor - earliest_call.from_floor)
            distance2 = abs(self.elevator2.current_floor - earliest_call.from_floor)

            if distance1 <= distance2:
                temp_lst = self.elevator1.move_floor_fifo(earliest_call, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
                temp_lst = self.elevator2.move_floor_fifo(earliest_call, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
            else:
                temp_lst = self.elevator2.move_floor_fifo(earliest_call, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)
                temp_lst = self.elevator1.move_floor_fifo(earliest_call, self.all_calls)
                for i in temp_lst:
                    self.all_calls.remove(i)

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
