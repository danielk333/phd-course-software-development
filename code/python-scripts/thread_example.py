from threading import Thread


def worker(index):
    print(f"Worker doing {index}")


th = []
for ind in range(6):
    t = Thread(target=worker, args=(ind,))
    th.append(t)
    t.start()

for t in th:
    t.join()
