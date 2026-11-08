# Animation: Boy rolling a ball down the hill
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


def man(x, y, step):
    s = 2 * math.sin(step)
    add(Circle((x, y + 14), 2, fc="w", ec="k", lw=2))   # head
    line([x, x], [y + 6, y + 12])                       # body
    line([x, x + s], [y + 6, y])                        # legs
    line([x, x - s], [y + 6, y])
    line([x, x - s], [y + 11, y + 8])                   # arms
    line([x, x + s], [y + 11, y + 8])


ax.add_patch(Rectangle((0, 0), 100, 60, fc="skyblue", zorder=0))
ax.add_patch(Polygon([(0, 0), (0, 40), (100, 5), (100, 0)], fc="green"))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    x = 5 + 0.45 * f
    man(x, 40 - 0.35 * x, f * 0.3)
    bx = x + 8
    by = 40 - 0.35 * bx + 2.7
    add(Circle((bx, by), 2.5, fc="orange", ec="k"))
    a = -f * 0.4
    line([bx, bx + 2.5 * math.cos(a)], [by, by + 2.5 * math.sin(a)])   # shows the rolling


ani = FuncAnimation(fig, update, frames=range(170), interval=30)
plt.show()
