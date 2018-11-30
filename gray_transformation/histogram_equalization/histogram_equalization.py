import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Fig0310(b)(washed_out_pollen_image).tif",0)

# equalizeHist(src, dst)
cv2.equalizeHist(img, img);

plt.hist(img.ravel(), 256, [0,256])
plt.show()

cv2.imshow("image", img)
cv2.waitKey(0)