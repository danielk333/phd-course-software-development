import time
import numpy as np
import matplotlib.pyplot as plt


def iter_fun(zn, C):
    return zn**2 + C


def iter_n(z0, C, max_num, limit):
    assert z0.shape == C.shape, "Initial value and constant shapes do not match"

    mat_shape = z0.shape
    mat_size = z0.size

    # init the result matrix
    z = z0.copy()

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


def mandelbrot_set(C_mat, max_num, limit):
    z0 = np.zeros(C_mat.shape, dtype=np.complex64)
    Z, iters = iter_n(z0, C_mat, max_num=max_num, limit=limit)
    Z_norm = np.real(np.sqrt(Z * np.conj(Z)))
    return Z_norm, iters


if __name__ == "__main__":
    zoom_n = 2
    n_base = 300

    if zoom_n == 1:
        xmin, xmax, xn = -0.5, -0.4, n_base
        ymin, ymax, yn = -0.62, -0.56, n_base
    elif zoom_n == 2:
        xmin, xmax, xn = -0.45, -0.42, n_base
        ymin, ymax, yn = -0.59, -0.55, n_base
    else:
        xmin, xmax, xn = -2.25, 0.75, n_base
        ymin, ymax, yn = -1.25, 1.25, n_base

    xv = np.linspace(xmin, xmax, xn, dtype=np.float32)
    yv = np.linspace(ymin, ymax, yn, dtype=np.float32)

    X, Y = np.meshgrid(xv, yv)

    max_num = 120
    limit = 4.0

    t0 = time.time()
    Z_norm, iters = mandelbrot_set(C_mat=X + Y * 1.0j, max_num=max_num, limit=limit)
    dt = time.time() - t0
    print(f"execution time {dt} sec")

    width = 8.0
    height = 6.0 * yn / xn
    fig = plt.figure(figsize=(width, height))
    ax = fig.add_subplot(111, aspect=1)

    im = ax.imshow(
        iters, cmap=plt.cm.jet, interpolation="nearest", extent=[xmin, xmax, ymin, ymax]
    )
    ax.set(
        xlabel="real$(C)$",
        ylabel="imag$(C)$",
        title="Mandelbrot set, limit: {}, max iterations: {}".format(limit, max_num),
    )

    cbar = plt.colorbar(im)
    cbar.ax.set_ylabel("Iterations until diverged", rotation=270)

    plt.show()
