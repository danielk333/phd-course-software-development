import time
import numpy as np


def iter_fun(zn, C):
    return zn**2 + C


def iter_n_loop(z0, C, max_num, limit):
    z = z0 * np.ones(C.shape, dtype=C.dtype)

    mat_shape = z.shape
    mat_size = z.size

    # we only iterate until the limit is passed, then it is considered divergant
    # use the "iters" as a indication of this
    iters = np.zeros((mat_size,), dtype=np.int32)

    # flatten for only one loop
    z.shape = (mat_size,)
    C.shape = (mat_size,)

    for it in range(mat_size):
        for ind in range(max_num):
            z[it] = iter_fun(z[it], C[it])

            if z[it] * np.conj(z[it]) > limit**2:
                iters[it] = ind
                break

    # all iterations that survived without passing limit went trough the entire loop
    iters[iters == 0] = max_num

    # change shape back to original
    z.shape = mat_shape
    C.shape = mat_shape
    iters.shape = mat_shape
    return z, iters


def iter_n_vec(z0, C, max_num, limit):
    z = z0 * np.ones(C.shape, dtype=C.dtype)

    # we only iterate until the limit is passed, then it is considered divergant
    # use the "iters" as a indication of this
    iters = np.zeros(C.shape, dtype=np.int32)
    for ind in range(max_num):
        z[iters == 0] = iter_fun(z[iters == 0], C[iters == 0])

        # if the norm of z passes the limit, stop iteration by setting the value to the iteration integer
        z_norm = z * np.conj(z)
        z_norm_check = np.logical_and(z_norm > limit**2, iters == 0)
        iters[z_norm_check] = ind

    # all iterations that survived so far went trough the entire loop
    iters[iters == 0] = max_num
    return z, iters


def mandelbrot_set(C_mat, max_num, limit, iter_fun):
    z0 = 0.0 + 0.0j
    Z, iters = iter_fun(z0, C_mat, max_num=max_num, limit=limit)
    Z_norm = np.real(np.sqrt(Z * np.conj(Z)))
    return Z_norm, iters


if __name__ == "__main__":
    n_base = 300

    xmin, xmax, xn = -0.45, -0.42, n_base
    ymin, ymax, yn = -0.59, -0.55, n_base
    xv = np.linspace(xmin, xmax, xn, dtype=np.float32)
    yv = np.linspace(ymin, ymax, yn, dtype=np.float32)
    X, Y = np.meshgrid(xv, yv)

    max_num = 120
    limit = 4.0

    t0 = time.time()
    Z_norm, iters = mandelbrot_set(
        C_mat=X + Y * 1.0j, max_num=max_num, limit=limit, iter_fun=iter_n_loop
    )
    dtl = time.time() - t0
    print(f"loop execution time {dtl} sec")

    t0 = time.time()
    Z_norm, iters = mandelbrot_set(
        C_mat=X + Y * 1.0j, max_num=max_num, limit=limit, iter_fun=iter_n_vec
    )
    dtv = time.time() - t0
    print(f"vectorized execution time {dtv} sec")
    print(f"speedup {dtl/dtv}")
