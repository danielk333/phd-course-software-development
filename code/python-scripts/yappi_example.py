import yappi
import numpy as np


def func():
    for ind in range(1_000_000):
        x = ind % 69
    del x


yappi.set_clock_type("cpu")
yappi.start()

for index in range(10):
    y = np.eye(4) * 49.0
    func()

yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
