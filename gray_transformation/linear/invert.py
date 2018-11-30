import cv2

img = 255-cv2.imread("Fig0304(a)(breast_digital_Xray).tif",0)

cv2.imshow("image", img)
cv2.waitKey(0)