# Animation: A man moving with a ball
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
ax.add_patch(Rectangle((0, 0), 100, 5, fc="green"))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    x = 5 + 0.4 * f
    man(x, 5, f * 0.3)
    add(Circle((x + 8, 7 + 6 * abs(math.sin(f * 0.2))), 2, fc="orange", ec="k"))


ani = FuncAnimation(fig, update, frames=range(200), interval=30)
plt.show()
