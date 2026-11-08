# Power-law transformation: s = c * r^gamma
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

# input.jpg = any image kept in the same folder as this file
img = np.array(Image.open(Path(__file__).with_name("input.jpg")).convert("L"))

c = 255
gamma = 0.5
out = c * (img / 255.0) ** gamma

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(out, cmap="gray", vmin=0, vmax=255)
plt.title("Power-law transformation (gamma = 0.5)")
plt.show()
