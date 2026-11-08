# Ladder - Bresenham line algorithm
import math
import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    pts = []
    while True:
        pts.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return pts


pts = bresenham(30, 10, 30, 90) + bresenham(60, 10, 60, 90)   # two rails
for y in range(20, 90, 15):                                    # rungs
    pts += bresenham(30, y, 60, y)

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Ladder - Bresenham line algorithm")
plt.show()
