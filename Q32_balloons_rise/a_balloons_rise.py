# Animation: Balloons rising from the bottom to the top
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
balloons = [(10, "red", 0.3), (30, "blue", 0.5), (50, "green", 0.4),
            (70, "orange", 0.6), (90, "purple", 0.35)]


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    for i, (x, c, speed) in enumerate(balloons):
        y = (f * speed) % 80 - 10
        wobble = 2 * math.sin(f / 10 + i)
        line([x + wobble, x + wobble], [y - 5, y - 15], c="gray", w=1)   # string
        add(Ellipse((x + wobble, y), 8, 10, fc=c, ec="k"))


ani = FuncAnimation(fig, update, frames=range(200), interval=30)
plt.show()
