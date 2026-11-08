# Star - DDA line algorithm
import math
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x, y = x1, y1
    pts = []
    for _ in range(steps + 1):
        pts.append((round(x), round(y)))
        x += xinc
        y += yinc
    return pts



def polygon(p):
    pts = []
    for i in range(len(p)):
        x1, y1 = p[i]
        x2, y2 = p[(i + 1) % len(p)]
        pts += dda(x1, y1, x2, y2)
    return pts


# 5 corners of a circle, 144 degrees apart -> joining them in order gives a star
star = [(round(50 + 40 * math.cos(math.radians(90 + 144 * i))),
         round(50 + 40 * math.sin(math.radians(90 + 144 * i)))) for i in range(5)]
pts = polygon(star)

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Star - DDA line algorithm")
plt.show()
