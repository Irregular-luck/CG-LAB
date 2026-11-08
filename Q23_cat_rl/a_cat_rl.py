# Animation: A cat moves from right to left
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


def cat(x, y, d, step):
    s = 1.5 * math.sin(step)
    hx, hy = x + 7 * d, y + 9
    add(Ellipse((x, y + 6), 14, 7, fc="orange"))                 # body
    add(Circle((hx, hy), 3.5, fc="orange"))                      # head
    add(Polygon([(hx - 3, hy + 2), (hx - 2.5, hy + 6), (hx - 0.5, hy + 3)], fc="orange"))
    add(Polygon([(hx + 0.5, hy + 3), (hx + 2.5, hy + 6), (hx + 3, hy + 2)], fc="orange"))
    add(Circle((hx - 1.2, hy + 0.5), 0.5, fc="k"))               # eyes
    add(Circle((hx + 1.2, hy + 0.5), 0.5, fc="k"))
    line([x - 7 * d, x - 11 * d], [y + 7, y + 14], c="orange", w=3)   # tail
    line([x - 4, x - 4 + s], [y + 3, y], c="orange", w=3)             # legs
    line([x + 4, x + 4 - s], [y + 3, y], c="orange", w=3)


ax.add_patch(Rectangle((0, 0), 100, 60, fc="skyblue", zorder=0))
ax.add_patch(Rectangle((0, 0), 100, 3, fc="green"))


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    cat(100 - 0.5 * f, 3, -1, f * 0.3)


ani = FuncAnimation(fig, update, frames=range(220), interval=30)
plt.show()
