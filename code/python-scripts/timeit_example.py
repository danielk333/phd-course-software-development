def list_comp():
    L = [i for i in range(1000)]


def loop():
    L = []
    for i in range(1000):
        L.append(i)


if __name__ == "__main__":
    import timeit

    num = 10_000
    lc_dt = timeit.timeit(list_comp, number=num) / num
    lo_dt = timeit.timeit(loop, number=num) / num

    print(f"avg list comp time: {lc_dt} s")
    print(f"avg loop time     : {lo_dt} s")
    print(f"list comp speedup: {lo_dt/lc_dt} times")
