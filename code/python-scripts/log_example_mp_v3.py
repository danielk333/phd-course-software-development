import logging
import multiprocessing
import time
import random

def worker(ident):
    logger = multiprocessing.get_logger()
    for i in range(10):
        time.sleep(random.random() * 0.1)
        logger.info(f"{ident}: {i}")


logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)

processes = []
for i in range(5):
    p = multiprocessing.Process(
        target=worker, args=(f"Worker-{i}", )
    )
    processes.append(p)
    p.start()
for p in processes:
    p.join()
