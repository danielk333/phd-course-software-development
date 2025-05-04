import logging
import logging.handlers
import multiprocessing
import time
import random


def worker(log_queue, ident):
    logger = logging.getLogger(ident)
    logger.setLevel(logging.DEBUG)

    handler = logging.handlers.QueueHandler(log_queue)
    logger.addHandler(handler)
    for i in range(10):
        time.sleep(random.random() * 0.1)
        logger.info(f"{ident}: {i}")


log_queue: multiprocessing.Queue = multiprocessing.Queue(-1)

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

queue_handler = logging.handlers.QueueListener(log_queue, handler)
queue_handler.start()


processes = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(log_queue, f"Worker-{i}"))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
