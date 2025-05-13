import time
from threading import Thread
from multiprocessing import Pool

iter_num = 60000000


def counter(num):
    while num > 0:
        num -= 1


t1 = Thread(target=counter, args=(iter_num // 2,))
t2 = Thread(target=counter, args=(iter_num // 2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print("threading exec time -", end - start)


start = time.time()
counter(iter_num)
end = time.time()

print("linear exec time -", end - start)

pool = Pool(2)

start = time.time()

r1 = pool.apply_async(counter, [iter_num // 2])
r2 = pool.apply_async(counter, [iter_num // 2])
pool.close()
pool.join()

end = time.time()

print("multiprocessing exec time -", end - start)
