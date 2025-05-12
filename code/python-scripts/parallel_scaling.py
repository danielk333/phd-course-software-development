import time
import argparse
import subprocess
import numpy as np
import scipy.optimize as scio
import matplotlib.pyplot as plt


def speedup_amdahls(num, fraction_parallel):
    return 1 / (1 - fraction_parallel + fraction_parallel / num)


def speedup_gustafson(num, fraction_parallel):
    return 1 + (num - 1) * fraction_parallel


def _opt_fun(p, nums, s):
    return np.sum((s - speedup_amdahls(nums, p)) ** 2)


def estimate_parallel_fraction(execution_times, nums, base_execution_time):
    return scio.minimize_scalar(
        fun=_opt_fun,
        args=(nums, base_execution_time / execution_times),
        bounds=[0, 1],
    )


def test():
    def model(num, frac):
        return 1 - frac + frac / num

    np.random.seed(1)

    nums = np.arange(1, 20)
    t_total = 1.0
    p = 0.9
    t = model(nums, p) + np.random.randn(*nums.shape) * 0.01
    t[0] = 1
    t *= t_total
    popt = estimate_parallel_fraction(t, nums, t_total)
    print(popt)

    p_est = popt.x

    fig, ax = plt.subplots()
    ax.plot(nums, t, "b-", label="data")
    ax.plot(
        nums,
        model(nums, p_est),
        "g--",
        label=f"fit: p={p_est:.3e}",
    )
    ax.set_xlabel("Parallelization number")
    ax.set_ylabel("Execution time")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("nums", type=int)

    args = parser.parse_args()

    nums = np.arange(1, args.nums)
    t = np.zeros_like(nums)
    for ind, num in enumerate(nums):
        t0 = time.time()
        subprocess.run(args.command.format(num=num))
        t[ind] = time.time() - t0
    popt = estimate_parallel_fraction(t, nums, t[0])
    print(popt)
    p_est = popt.x

    fig, ax = plt.subplots()
    ax.plot(nums, t, "b-", label="data")
    ax.plot(
        nums,
        t[0] / speedup_amdahls(nums, p_est),
        "g--",
        label=f"fit: p={p_est:.3e}",
    )
    ax.set_xlabel("Parallelization number")
    ax.set_ylabel("Execution time")
    plt.show()
