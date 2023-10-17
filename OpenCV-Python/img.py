import cv2
import numpy as np

img = np.zeros((800, 800), dtype=np.uint8)
print("img=\n", img)
cv2.imshow("one", img)
print("读取像素点img[0,3] = ", img[0, 3])
img[0, 3] = 255
print("修改后img=\n", img)
print("读取像素点img[0,3] = ", img[0, 3])
cv2.imshow("two", img)
key = cv2.waitKey()
cv2.destroyAllWindows()
