import py_calc
import compiled_py_calc
import cy_calc
import time
import random


def test_func(func):
    random.seed(3245)
    vec = [float(x) for x in range(500)]
    mat = [[random.random() for row in range(500)] for col in range(500)]
    repeat = 50

    t0 = time.process_time()
    func(vec, mat, repeat)
    dt = time.process_time() - t0

    return dt


py_dt = test_func(py_calc.calc)
cpy_dt = test_func(compiled_py_calc.calc)
cy_dt = test_func(cy_calc.calc)

print(f"  python: {py_dt:.2e} s (speedup: {py_dt/py_dt:.2f})")
print(f"compiled: {cpy_dt:.2e} s (speedup: {py_dt/cpy_dt:.2f})")
print(f"  cython: {cy_dt:.2e} s (speedup: {py_dt/cy_dt:.2f})")
