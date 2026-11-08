# Animation: Two buses moving in opposite directions
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


def bus(x, y, c):
    add(Rectangle((x, y + 2.5), 30, 10, fc=c, ec="k"))
    for i in range(4):
        add(Rectangle((x + 2 + 7 * i, y + 8), 5, 3, fc="w"))   # windows
    add(Circle((x + 7, y + 2.5), 2.5, fc="k"))
    add(Circle((x + 23, y + 2.5), 2.5, fc="k"))


ax.add_patch(Rectangle((0, 0), 100, 30, fc="gray"))
ax.plot([0, 100], [14.5, 14.5], "w--")


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    bus(-30 + 0.9 * f, 1, "orange")      # left to right
    bus(100 - 0.9 * f, 15, "green")      # right to left


ani = FuncAnimation(fig, update, frames=range(150), interval=30)
plt.show()
