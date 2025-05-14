import ctypes

import numpy as np
import numpy.ctypeslib as npct

lib = ctypes.cdll.LoadLibrary("./main.so")
# Define the data types we need
ro_f8_vec = npct.ndpointer(np.float64, ndim=1, flags="aligned, contiguous")
rw_f8_vec = npct.ndpointer(np.float64, ndim=1, flags="aligned, contiguous, writeable")

# Define the C-interface
lib.twice.restype = None
lib.twice.argtypes = [
    ro_f8_vec,
    rw_f8_vec,
    ctypes.c_int,
]


def twice(values):
    result = np.empty_like(values)
    length = ctypes.c_int(len(values))

    lib.twice(values, result, length)

    return result


if __name__ == "__main__":
    x = np.arange(num, dtype=np.float64)

    y = foo(x)

    print(f"INPUT : {x}")
    print(f"OUTPUT: {y}")

    print("\nRUNNING COMPLEX-FOO")
    x = (np.arange(num) + 1j * np.arange(num)[::-1]).astype(np.complex64)

    y = foo(x)

    print(f"INPUT : {x}")
    print(f"OUTPUT: {y}")
