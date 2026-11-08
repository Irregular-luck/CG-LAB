import matplotlib.pyplot as plt

def line(x0, y0, x1, y1):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    xs=[]
    ys=[]
    while True:

        xs.append(x0)
        ys.append(y0)
        
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    plt.plot(xs, ys, color="black")

# body
line(0, 2, 20, 2)     # bottom
line(0, 2, 0, 6)      # front
line(0, 6, 6, 6)      # hood
line(6, 6, 9, 10)     # windshield
line(9, 10, 15, 10)   # roof
line(15, 10, 18, 6)   # rear window
line(18, 6, 20, 6)    # trunk
line(20, 6, 20, 2)    # back

# wheels (squares)
line(3, 0, 7, 0)
line(3, 0, 3, 2)
line(7, 0, 7, 2)

line(13, 0, 17, 0)
line(13, 0, 13, 2)
line(17, 0, 17, 2)

plt.axis("equal")
plt.show()