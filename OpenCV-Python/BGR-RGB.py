import cv2
from matplotlib import pyplot as plt


img_opencv = cv2.imread(r"C:\Users\FullMoon\Pictures\eeworld.png")
b, g, r = cv2.split(img_opencv)
img_matplotlib = cv2.merge([r, g, b])
plt.subplot(121)
plt.imshow(img_opencv)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()
