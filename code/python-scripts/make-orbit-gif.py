"""Make a nice gif of a few orbits

pip requirements: numpy matplotlib pyorb
Also requires pillow for saving

"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyorb

plt.style.use("dark_background")
HERE = Path(__file__).parent

# For reproducibility
np.random.seed(8237487)
num = 100

orbs = pyorb.Orbit(
    M0=pyorb.M_sol,
    num=num,
    a=(1 + np.random.randn(num)*0.2) * pyorb.AU,
    e=np.random.rand(num) * 0.1,
    i=np.random.randn(num) * 40.0,
    omega=np.random.randn(num) * 360.0,
    Omega=np.random.randn(num) * 360.0,
    anom=np.random.randn(num) * 360.0,
    degrees=True,
)

days = 3600 * 24
time_step = 1.0 * days
trail = np.linspace(0, -20 * days, 20, dtype=np.float64)
times = np.arange(60) * time_step

# container for fast calculation
orb_trail = pyorb.Orbit(
    M0=pyorb.M_sol,
    num=len(trail),
    direct_update=False,
    auto_update=False,
    degrees=True,
)


def orb_trail_position(orb):
    orb_trail._kep[:, :] = orb._kep[:, 0][:, None]
    orb_trail.mean_anomaly += orb_trail.mean_motion * trail
    orb_trail.calculate_cartesian()
    r = orb_trail.cartesian[:3, :]
    return r


fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection="3d")
lines = []
dots = []

# Init lines to draw
for orb in orbs:
    r = orb_trail_position(orb)

    (ln,) = ax.plot(
        r[0, :], r[1, :], r[2, :],
        ls="-", c="#68b4ff", alpha=0.5,
    )
    (dot,) = ax.plot(
        r[0, 0], r[1, 0], r[2, 0],
        ls="none", marker=".", c="#00ff2f", alpha=0.5,
    )
    lines.append(ln)
    dots.append(dot)

# insert some rulers
theta = np.linspace(0, np.pi * 2, 200)
for au_dist in [1, 2, 3, 5]:
    ax.plot(
        au_dist * pyorb.AU * np.cos(theta),
        au_dist * pyorb.AU * np.sin(theta),
        ls="-",
        alpha=0.4,
        c="#ffffff",
    )

ax.grid(False)
ax.axis("off")
ax.view_init(14, -6)

box_size = 1
ax.set_xlim([-box_size * pyorb.AU, box_size * pyorb.AU])
ax.set_ylim([-box_size * pyorb.AU, box_size * pyorb.AU])
ax.set_zlim([-box_size * pyorb.AU, box_size * pyorb.AU])


def animate(ind):
    for line, dot, orb in zip(lines, dots, orbs):
        orb.propagate(times[ind])
        r = orb_trail_position(orb)

        line.set_xdata(r[0, :])
        line.set_ydata(r[1, :])
        line.set_3d_properties(r[2, :])

        dot.set_xdata([r[0, 0]])
        dot.set_ydata([r[1, 0]])
        dot.set_3d_properties([r[2, 0]])
    return lines + dots


ani = animation.FuncAnimation(
    fig,
    animate,
    repeat=True,
    frames=len(times),
    interval=50,
)

writer = animation.PillowWriter(
    fps=15,
    metadata=dict(artist="Daniel Kastinen"),
    bitrate=1800,
)
ani.save(HERE.parents[1] / "static" / "media" / "orbits.gif", writer=writer)
