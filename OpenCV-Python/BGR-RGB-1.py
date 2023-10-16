import cv2
from matplotlib import pyplot as plt
import numpy as np

img_opencv = cv2.imread(r"C:\Users\FullMoon\Pictures\eeworld.png")
B = img_opencv[:, :, 0]
G = img_opencv[:, :, 1]
R = img_opencv[:, :, 2]

img_matplotlib = img_opencv[:, :, ::-1]

plt.subplot(121)
plt.imshow(img_opencv)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()
