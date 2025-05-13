#!/usr/bin/env python
from mpi4py import MPI

comm = MPI.COMM_WORLD
name = MPI.Get_processor_name()
print(f"hello! name: {name}, my rank is {comm.rank}")
