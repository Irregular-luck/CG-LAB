# Star - Bresenham line algorithm
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



def polygon(p):
    pts = []
    for i in range(len(p)):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % len(p)]
        pts += bresenham(x1, y1, x2, y2)
    return pts


# 5 corners of a circle, 144 degrees apart -> joining them in order gives a star
star = [(round(50 + 40 * math.cos(math.radians(90 + 144 * i))),
         round(50 + 40 * math.sin(math.radians(90 + 144 * i)))) for i in range(5)]
pts = polygon(star)

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Star - Bresenham line algorithm")
plt.show()
