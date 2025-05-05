import io
import cProfile
import pstats
import numpy as np

pr = cProfile.Profile()
pr.enable()

L = [i for i in range(1000)]
L = []
for i in range(1_000):
    L.append(i)
for i in range(10_000):
    x = np.eye(3) @ np.ones((3,))

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
ps.print_stats(20)
print("PROFILING: \n" + s.getvalue())
