import cv2

retval = cv2.imread("./eeworld.png")
cv2.imshow("demo",retval)
s = cv2.imwrite("./demo.png",retval)
