# Circle inside another circle - Bresenham circle algorithm
import math
import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    pts = []
    x, y = 0, r
    d = 3 - 2 * r
    while x <= y:
        for dx, dy in [(x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)]:
            pts.append((xc + dx, yc + dy))
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    return pts


pts = bresenham_circle(50, 50, 40) + bresenham_circle(50, 50, 20)

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Circle inside another circle - Bresenham circle algorithm")
plt.show()
