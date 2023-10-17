import cv2

retval = cv2.imread(r"C:\Users\FullMoon\Pictures\eeworld.png")
cv2.imshow("demo", retval)
key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow("PressA", retval)
elif key == ord('B'):
    cv2.imshow("PressB", retval)
