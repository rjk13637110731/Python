import cv2
img = cv2.imread("./eeworld.png",0)
cv2.imshow("before", img)

for i in range(10,200):
    for j in range(20,300):
        img[i,j] = 255
cv2.imshow("after", img)
key = cv2.waitKey()
cv2.destroyAllWindows()
