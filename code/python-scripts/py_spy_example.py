from threading import Event, Thread
import numpy as np
import signal


def worker(exit_event: Event):
    while not exit_event.is_set():
        x = np.eye(3) @ np.ones((3,))
        x += 3


ev = Event()
th = Thread(target=worker, args=(ev,))
th.start()

try:
    signal.pause()
except KeyboardInterrupt:
    ev.set()
    th.join()
