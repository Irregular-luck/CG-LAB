# Animation: Coconut falling from the coconut tree
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
ax.add_patch(Rectangle((0, 0), 100, 4, fc="khaki"))
ax.add_patch(Polygon([(45, 4), (51, 4), (54, 40), (49, 40)], fc="saddlebrown"))   # trunk
for leaf in ([(51, 42), (32, 50), (38, 41)], [(51, 42), (70, 50), (64, 41)],
             [(51, 42), (34, 34), (42, 40)], [(51, 42), (68, 34), (60, 40)],
             [(51, 42), (47, 54), (55, 54)]):
    ax.add_patch(Polygon(leaf, fc="green"))                                       # leaves
ax.add_patch(Circle((48, 38), 2, fc="saddlebrown", ec="k"))                       # coconut


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    y = max(6, 38 - 0.03 * max(0, f - 20) ** 2)
    add(Circle((55, y), 2, fc="saddlebrown", ec="k"))


ani = FuncAnimation(fig, update, frames=range(100), interval=30)
plt.show()
