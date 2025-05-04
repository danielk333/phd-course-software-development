import logging
import threading
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger("my_logger")


def worker(ident, num):
    for i in range(num):
        time.sleep(0.05)
        logger.info(f"{ident}: {i}")


threads = []
for ind in range(2):
    threads.append(
        threading.Thread(
            target=worker,
            args=(
                f"worker {ind}",
                (ind + 1) * 10,
            ),
        )
    )

for th in threads:
    th.start()

for th in threads:
    th.join()
