import numpy as np
import matplotlib.pyplot as plt


Ns = 2 ** np.arange(4, 12, 2)
n = np.arange(1, 1000)


def T_binom_tree(N, n):
    return N / n + 2 * np.log2(n)


fig, ax = plt.subplots()

for N in Ns:
    ax.loglog(n, T_binom_tree(N, n), label=f"Problem size N={N}")

ax.plot(Ns / 4, T_binom_tree(Ns, Ns / 4), "or", label="Cores = N/4")
ax.set_xlabel("Parallelization number")
ax.set_ylabel("Execution time [arb. units]")
ax.legend()

fig.savefig("./static/media/example_binom_tree.png", dpi=200)
plt.show()
