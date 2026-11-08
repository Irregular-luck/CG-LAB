# Animation: Moving car with a traffic light
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
ax.add_patch(Rectangle((60, 5), 2, 28, fc="k"))   # pole
ax.plot([50, 50], [0, 5], "w-")                   # stop line
state = {"x": -20}


def update(f):
    for a in moving:
        a.remove()
    moving.clear()
    p = f % 180
    color = "green" if p < 70 else "yellow" if p < 90 else "red"

    # the car stops just before the stop line (x = 50) when the light is red
    if not (color == "red" and 45 <= state["x"] + 20 < 50):
        state["x"] += 0.8
    if state["x"] > 100:
        state["x"] = -20

    car(state["x"], 5, "blue")
    add(Rectangle((57, 33), 8, 18, fc="k"))                                   # light box
    add(Circle((61, 47), 2, fc="red" if color == "red" else "gray"))
    add(Circle((61, 42), 2, fc="yellow" if color == "yellow" else "gray"))
    add(Circle((61, 37), 2, fc="lime" if color == "green" else "gray"))


ani = FuncAnimation(fig, update, frames=range(1000), interval=30)
plt.show()
