# Car - DDA line algorithm
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


def wheel(cx, cy, r):
    return [(round(cx + r * math.cos(math.radians(a))),
             round(cy + r * math.sin(math.radians(a)))) for a in range(0, 360, 45)]


body = [(10, 20), (90, 20), (90, 40), (70, 40), (60, 60), (30, 60), (20, 40), (10, 40)]
window1 = [(33, 42), (36, 56), (46, 56), (46, 42)]
window2 = [(50, 42), (50, 56), (58, 56), (65, 42)]
pts = polygon(body) + polygon(window1) + polygon(window2)
pts += polygon(wheel(30, 20, 8)) + polygon(wheel(70, 20, 8))

plt.plot([p[0] for p in pts], [p[1] for p in pts], "k.", markersize=3)
plt.axis("equal")
plt.title("Car - DDA line algorithm")
plt.show()
