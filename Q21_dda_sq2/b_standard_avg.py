# Standard average (mean) filter
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

k = np.ones((3, 3)) / 9
out = convolve(img, k)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(out, cmap="gray", vmin=0, vmax=255)
plt.title("Standard average filter")
plt.show()
