# Animation: A fruit falls from the tree
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
ax.add_patch(Rectangle((0, 0), 100, 5, fc="green"))
ax.add_patch(Rectangle((45, 5), 6, 25, fc="saddlebrown"))   # trunk
ax.add_patch(Circle((48, 38), 14, fc="green"))              # leaves


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    y = max(7.5, 32 - 0.03 * max(0, f - 20) ** 2)
    add(Circle((55, y), 2.5, fc="red"))


ani = FuncAnimation(fig, update, frames=range(100), interval=30)
plt.show()
