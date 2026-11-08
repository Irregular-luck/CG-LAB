# Sobel filter
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

# input.jpg = any image kept in the same folder as this file
img = np.array(Image.open(Path(__file__).with_name("input.jpg")).convert("L"))


def convolve(image, k):
    h, w = image.shape
    p = np.pad(image.astype(float), 1, mode="edge")
    out = np.zeros((h, w))
    for i in range(k.shape[0]):
        for j in range(k.shape[1]):
            out += k[i, j] * p[i:i + h, j:j + w]
    return out

gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
mag = np.sqrt(convolve(img, gx) ** 2 + convolve(img, gy) ** 2)
out = mag / mag.max() * 255

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(out, cmap="gray", vmin=0, vmax=255)
plt.title("Sobel filter")
plt.show()
