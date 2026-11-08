# Animation: Earth moving around the Sun
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


ax.add_patch(Rectangle((0, 0), 100, 60, fc="black", zorder=0))
ax.add_patch(Circle((50, 30), 25, fill=False, ec="white", ls="--"))   # orbit
ax.add_patch(Circle((50, 30), 6, fc="yellow"))                        # sun


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    a = math.radians(f)
    add(Circle((50 + 25 * math.cos(a), 30 + 25 * math.sin(a)), 2.5, fc="dodgerblue"))


ani = FuncAnimation(fig, update, frames=range(360), interval=30)
plt.show()
