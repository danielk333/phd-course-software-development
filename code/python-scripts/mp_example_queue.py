import multiprocessing as mp
import numpy as np
import time


def worker(q, r, pid):
    num = 0
    while True:
        data = q.get()
        if data is None:
            print("Stopping worker now...")
            break
        print(f"{pid=} doing task={num}")
        for ind in range(1_000):
            res = np.mean(data)
        r.put(res)
        q.task_done()
        num += 1


tasks = mp.JoinableQueue()
results = mp.Queue()

# create workers
ps = []
for i in range(6):
    p = mp.Process(target=worker, args=(tasks, results, i))
    ps.append(p)
    p.start()

task_n = 500

t0 = time.time()

# queue tasks
for i in range(task_n):
    tasks.put(np.random.randn(10_000) + i**2)

tasks.join()  # complete tasks

# get results
means = np.empty(task_n)
for i in range(task_n):
    means[i] = results.get()

t1 = time.time() - t0
print(f"EXECUTION: {t1:.4f}")

# stop workers
for i in range(len(ps)):
    tasks.put(None)
for p in ps:
    p.join()

