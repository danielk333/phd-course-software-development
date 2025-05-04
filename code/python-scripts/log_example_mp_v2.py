import logging
import pathlib
import multiprocessing
import time
import random
import tempfile


def worker(ident, dirname):
    logger = logging.getLogger(ident)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(dirname / f"{ident}.log")
    logger.addHandler(handler)
    for i in range(10):
        time.sleep(random.random() * 0.1)
        logger.info(f"{ident}: {i}")


with tempfile.TemporaryDirectory() as tmpdirname:
    processes = []
    dirname = pathlib.Path(tmpdirname)
    for i in range(5):
        p = multiprocessing.Process(
            target=worker, args=(f"Worker-{i}", dirname)
        )
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    for logfile in dirname.glob("*.log"):
        print(f"reading {logfile}")
        print(logfile.read_text())
