import ctypes

import numpy as np
import numpy.typing as npt
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


def twice(values: npt.NDArray[np.float64]):
    result = np.empty_like(values)
    length = ctypes.c_int(len(values))

    lib.twice(values, result, length)

    return result


if __name__ == "__main__":
    x = np.arange(10, dtype=np.float64)

    print("running c-twice")
    y = twice(x)

    print(f"INPUT : {x}")
    print(f"OUTPUT: {y}")
