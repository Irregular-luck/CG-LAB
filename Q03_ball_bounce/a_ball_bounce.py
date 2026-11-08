# Animation: Ball bouncing on the ground
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


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    t = (f % 50) / 50
    x = 10 + 0.4 * f
    y = 8 + 140 * t * (1 - t)
    add(Circle((x, y), 3, fc="red"))


ani = FuncAnimation(fig, update, frames=range(200), interval=30)
plt.show()
