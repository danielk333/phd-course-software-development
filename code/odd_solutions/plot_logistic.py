import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from load_logistic import lib

np.random.seed(23874)

n = 100
samps = 50
r = np.linspace(2, 3.6, num=1000, dtype=np.float64)

res_arrs = [
    np.empty((r.size, n), dtype=np.float64)
    for ind in range(samps)
]
for ind, arr in enumerate(res_arrs):
    lib.logistic_sweep(
        n,
        r.size,
        r,
        np.random.rand(len(r)),
        arr,
    )

fig, ax = plt.subplots(figsize=(16, 9))
scs = [
    ax.scatter(r, res_arrs[ind][:, 0], c="k", s=1)
    for ind in range(samps)
]

ax.set_xlim([2.9, 3.6])
ax.set_ylim([0, 1])

def animate(ind):
    for si, sc in enumerate(scs):
        sc.set_offsets(np.stack([r, res_arrs[si][:, ind]]).T)
    return scs

ani = animation.FuncAnimation(
    fig,
    animate,
    repeat=True,
    frames=n,
    interval=50,
)
plt.show()
