import time

PROFILES = {}


def profile(func):
    def timed_func(*args, **kw):
        t0 = time.time()
        ret = func(*args, **kw)
        dt = time.time() - t0

        if func.__name__ not in PROFILES:
            PROFILES[func.__name__] = [0, 0]
        PROFILES[func.__name__][0] += 1
        PROFILES[func.__name__][1] += dt

        return ret
    return timed_func


@profile
def func():
    L = []
    for i in range(10_000):
        L.append(i)


if __name__ == "__main__":
    for lop in range(250):
        func()

    for fname, (num, ttot) in PROFILES.items():
        print(f"{fname}: called {num} times - total time {ttot:.2e} s (avg {ttot/num:.2e} s)")
