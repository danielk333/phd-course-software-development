from multiprocessing import Process


def worker(index):
    print(f"Worker doing {index}")


ps = []
for ind in range(6):
    p = Process(target=worker, args=(ind,))
    ps.append(p)
    p.start()

for p in ps:
    p.join()
