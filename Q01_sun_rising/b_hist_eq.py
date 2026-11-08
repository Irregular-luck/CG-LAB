# Histogram equalisation
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

# input.jpg = any image kept in the same folder as this file
img = np.array(Image.open(Path(__file__).with_name("input.jpg")).convert("L"))

hist = np.bincount(img.ravel(), minlength=256)       # histogram
cdf = hist.cumsum()                                  # cumulative sum
cdf = (cdf - cdf.min()) / (cdf.max() - cdf.min()) * 255
out = cdf[img]                                       # map every pixel through the cdf

plt.figure(figsize=(10, 7))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.title("Original")
plt.subplot(2, 2, 2)
plt.imshow(out, cmap="gray", vmin=0, vmax=255)
plt.title("Equalised")
plt.subplot(2, 2, 3)
plt.hist(img.ravel(), 256, (0, 256))
plt.title("Original histogram")
plt.subplot(2, 2, 4)
plt.hist(out.ravel(), 256, (0, 256))
plt.title("Equalised histogram")
plt.tight_layout()
plt.show()
