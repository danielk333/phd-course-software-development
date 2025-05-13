from multiprocessing import Pool


def f(x):
    return x * x


with Pool(5) as p:
    par_computed_map = p.map(f, range(100))
    print(par_computed_map)
