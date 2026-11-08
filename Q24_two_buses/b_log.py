# Logarithmic transformation: s = c * log(1 + r)
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

# input.jpg = any image kept in the same folder as this file
img = np.array(Image.open(Path(__file__).with_name("input.jpg")).convert("L"))

c = 255 / np.log(1 + img.max())
out = c * np.log(1 + img.astype(float))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(out, cmap="gray", vmin=0, vmax=255)
plt.title("Logarithmic transformation")
plt.show()
