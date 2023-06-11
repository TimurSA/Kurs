import numpy as np
import random
from Calls_Generator import generate_call
from Elevator import Elevator


def generate_passengers():
    peak_hours = [8, 14, 20]
    p_current = 0

    for minute in range(24 * 60):
        hour = minute // 60
        if hour in peak_hours:
            p_current = 0.5
        else:
            p_current = 0.2
        yield np.random.binomial(1, p_current)
