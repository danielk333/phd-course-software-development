import numpy as np

np.random.seed(1)
size = 10_000
data = np.random.randn(size, 2)
with open("data.csv", "w") as fh:
    fh.write(
        ",".join([f"{x}" for x in data.flatten()])
    )
