#!/usr/bin/env python
import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

t0_all = time.time()
print(f"rank-{comm.rank}/{comm.size} starting")

if comm.rank == 0:
    items = [np.random.random(1000) + x for x in range(10000)]
else:
    items = None

items = comm.bcast(items, root=0)
t0 = time.time()

for ind in range(comm.rank, len(items), comm.size):
    items[ind] = items[ind] - np.mean(items[ind])

dt = time.time() - t0

if comm.rank == 0:
    for rank in range(1, comm.size):
        for ind in range(rank, len(items), comm.size):
            items[ind] = comm.recv(source=rank, tag=ind)
else:
    for ind in range(comm.rank, len(items), comm.size):
        comm.send(items[ind], dest=0, tag=ind)

if comm.rank == 0:
    su = 0
    for dat in items:
        su += np.mean(dat)

dt_all = time.time() - t0_all
print(f"rank-{comm.rank}/{comm.size}: work time {dt} s (total {dt_all} s)")
