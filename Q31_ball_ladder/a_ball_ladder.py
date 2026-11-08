# Animation: Ball bouncing down the rungs of a ladder
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Rectangle, Polygon, Ellipse

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.set_aspect("equal")
ax.axis("off")

moving = []  # everything that moves is re-drawn in every frame


def add(p):
    moving.append(ax.add_patch(p))


def line(x, y, c="k", w=2):
    moving.extend(ax.plot(x, y, c=c, lw=w))


ax.plot([40, 40], [5, 55], "k", lw=3)       # rails
ax.plot([60, 60], [5, 55], "k", lw=3)
for y in range(10, 51, 10):                 # rungs
    ax.plot([40, 60], [y, y], "k", lw=3)


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    k = f // 25                  # rung the ball is leaving
    t = (f % 25) / 25
    y0 = 50 - 10 * k
    y = (y0 + 3) * (1 - t) + (y0 - 10 + 3) * t + 24 * t * (1 - t)
    add(Circle((50, y), 3, fc="red"))


ani = FuncAnimation(fig, update, frames=range(100), interval=30)
plt.show()
