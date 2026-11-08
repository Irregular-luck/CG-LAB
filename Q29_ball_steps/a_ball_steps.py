# Animation: Ball bouncing down the steps
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
for i in range(5):
    ax.add_patch(Rectangle((20 * i, 0), 20, 45 - 9 * i, fc="saddlebrown", ec="k"))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    k = f // 25                  # which step the ball is leaving
    t = (f % 25) / 25
    top = 45 - 9 * k
    y = (top + 3) * (1 - t) + (top - 9 + 3) * t + 40 * t * (1 - t)
    x = 10 + 20 * (k + t)
    add(Circle((x, y), 3, fc="red"))


ani = FuncAnimation(fig, update, frames=range(100), interval=30)
plt.show()
