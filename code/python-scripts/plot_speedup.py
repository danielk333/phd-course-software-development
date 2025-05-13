import numpy as np
import matplotlib.pyplot as plt


nums = np.arange(1, 1000)
T1 = 1.3
T2 = 123.9


def T(n):
    return T1 + T2 / n


def break_fraction(fraction):
    return T2 / (T1 * (fraction - 1) + fraction * T2)


break_n = int(break_fraction(0.1))

fig, ax = plt.subplots()
ax.loglog(nums, T(nums), "b-", label="parallelized code")
ax.axvline(break_n, c="r", label=f"90% execution time reduction: n={break_n}")
ax.set_xlabel("Parallelization number")
ax.set_ylabel("Execution time [sec]")
ax.legend()

fig.savefig("example_exec_time.png", dpi=200)
plt.show()
