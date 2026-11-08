# Animation: Ball rolling down an inclined plane
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
ax.add_patch(Rectangle((0, 0), 100, 10, fc="green"))
ax.add_patch(Polygon([(10, 10), (90, 10), (10, 50)], fc="tan", ec="k"))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    t = (f / 150) ** 2                   # speeds up as it rolls down
    px = 10 + 80 * t                     # point on the slope
    py = 50 - 40 * t
    cx = px + 3 * 0.447                  # ball centre = slope point + radius along the normal
    cy = py + 3 * 0.894
    add(Circle((cx, cy), 3, fc="red", ec="k"))
    a = -t * 89.4 / 3                    # rolling angle = distance / radius
    line([cx, cx + 3 * math.cos(a)], [cy, cy + 3 * math.sin(a)])


ani = FuncAnimation(fig, update, frames=range(150), interval=30)
plt.show()
