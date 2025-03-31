import numpy as np
import numpy.ctypeslib as npct
import pathlib
import ctypes as c

FLAGS_W = "aligned, c_contiguous, writeable"
FLAGS_RO = "aligned, c_contiguous"
vec_type_ro = npct.ndpointer(np.float64, ndim=1, flags=FLAGS_RO)
mat_type_rw = npct.ndpointer(np.float64, ndim=2, flags=FLAGS_RO)

HERE = pathlib.Path(__file__).parent
lib = c.CDLL(HERE / "logistic.so")

lib.logistic.restype = c.c_double
lib.logistic.argtypes = [
    c.c_double,
    c.c_double,
]

lib.logistic_sweep.restype = None
lib.logistic_sweep.argtypes = [
    c.c_uint32,
    c.c_uint32,
    vec_type_ro,
    vec_type_ro,
    mat_type_rw,
]

lib.test.restype = c.c_int
lib.test.argtypes = []

if __name__ == "__main__":
    print(lib.logistic(0.5, 0.8))
    lib.test()

    n = 10
    r = np.array([1, 2, 3], dtype=np.float64)
    x0 = np.ones_like(r) * 0.5
    res = np.empty((r.size, n), dtype=np.float64)
    lib.logistic_sweep(n, r.size, r, x0, res)
    print(res)
