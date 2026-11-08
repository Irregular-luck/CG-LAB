# Animation: A car moving along a straight road
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


def car(x, y, c):
    add(Rectangle((x, y + 2.5), 20, 5, fc=c, ec="k"))       # body
    add(Rectangle((x + 5, y + 7.5), 10, 4, fc=c, ec="k"))   # roof
    add(Circle((x + 5, y + 2.5), 2.5, fc="k"))              # wheels
    add(Circle((x + 15, y + 2.5), 2.5, fc="k"))


ax.add_patch(Rectangle((0, 0), 100, 60, fc="skyblue", zorder=0))
ax.add_patch(Rectangle((0, 0), 100, 5, fc="gray"))
ax.plot([0, 100], [2.5, 2.5], "w--")


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    car(-20 + 0.9 * f, 5, "red")


ani = FuncAnimation(fig, update, frames=range(130), interval=30)
plt.show()
