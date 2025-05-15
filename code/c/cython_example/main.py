import py_calc
import compiled_py_calc
import cy_calc
import timeit

samples = 100
vec = list(range(2000))
mat = [[int(col == row) for row in range(2000)] for col in range(100)]

py_dt = timeit.timeit(lambda: py_calc.calc(vec, mat), number=samples) / samples
cpy_dt = timeit.timeit(lambda: compiled_py_calc.calc(vec, mat), number=samples) / samples
cy_dt = timeit.timeit(lambda: cy_calc.calc(vec, mat), number=samples) / samples

print(f"  python: {py_dt} s")
print(f"compiled: {cpy_dt} s")
print(f"  cython: {cy_dt} s")
