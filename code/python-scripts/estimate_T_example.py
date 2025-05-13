import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt


def estimate_parallel_fraction(N, execution_times):
    return scs.linregress(N, execution_times)


def model(N, n):
    return (3600 + 45 * N / n) * (1 + np.random.randn(*N.shape) * 0.01)


if __name__ == "__main__":
    np.random.seed(1)

    particles = np.arange(100, 1_000, 100)
    T_tot = model(particles, 1)
    res = estimate_parallel_fraction(particles, T_tot)
    print(res)

    fig, ax = plt.subplots()
    ax.plot(particles, T_tot / 3600, "bo", label="data")
    ax.plot(
        particles,
        (res.intercept + res.slope * particles) / 3600,
        "g--",
        label=f"fit: T_b = {int(res.intercept):d} sec, T_p = {int(res.slope):d} sec",
    )
    ax.set_xlabel("Test particles N")
    ax.set_ylabel("Execution time [hours]")
    ax.legend()
    fig.savefig("./static/media/example_T_estimate.png", dpi=200)
    plt.show()

    particles = np.arange(100_000, 1_000_000, 200_000)
    cores = np.arange(1, 2_000, 10)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for p in particles:
        T_tot = res.intercept + res.slope * p / cores
        T_1 = res.intercept + res.slope * p
        S = T_1 / T_tot
        axes[0].loglog(cores, T_tot / 3600, label=f"N = {p:_}")
        axes[1].plot(cores, S)

    axes[0].loglog(cores, 10_000 / cores, ls="--", label="Max 10 000 core hours")
    axes[0].legend()
    axes[0].set_xlabel("Cores used")
    axes[0].set_ylabel("Execution time [hours]")
    axes[1].set_xlabel("Cores used")
    axes[1].set_ylabel("Speedup")

    fig.savefig("./static/media/example_hpc_estimate.png", dpi=200)
    plt.show()


