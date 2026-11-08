# Circle inside a circle - Midpoint circle algorithm
import math
import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    pts = []
    x, y = 0, r
    p = 1 - r
    while x <= y:
        for dx, dy in [(x, y), (y, x), (-x, y), (-y, x), (x, -y), (y, -x), (-x, -y), (-y, -x)]:
            pts.append((xc + dx, yc + dy))
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
    return pts


pts = midpoint_circle(50, 50, 40) + midpoint_circle(50, 50, 20)

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Circle inside a circle - Midpoint circle algorithm")
plt.show()
