import cv2

retval = cv2.imread("./eeworld.png")
cv2.imshow("demo",retval)
cv2.imshow("test",retval)

key = cv2.waitKey()
if key !=-1:
    print("触发了按键")
cv2.destroyAllWindows()
