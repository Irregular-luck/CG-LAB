# Animation: Sun rising over hills
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


ax.add_patch(Rectangle((0, 0), 100, 60, fc="skyblue", zorder=0))
ax.add_patch(Polygon([(0, 0), (0, 20), (25, 35), (50, 15), (75, 32), (100, 18), (100, 0)],
                     fc="green", zorder=3))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    add(Circle((50, -5 + 0.5 * f), 6, fc="yellow", zorder=1))


ani = FuncAnimation(fig, update, frames=range(100), interval=30)
plt.show()
