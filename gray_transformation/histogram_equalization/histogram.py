import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("Fig0310(b)(washed_out_pollen_image).tif",0)
#img = cv2.imread("Fig0316(1)(top_left).tif",0)
#img = cv2.imread("Fig0316(4)(bottom_left).tif",0)
img = cv2.imread("Fig0316(3)(third_from_top).tif",0)

# cv2.calcHist(images, channels, mask, histSize, ranges[,hist[,accumulate]])

#hist = cv2.calcHist([img], [0], None, [256], [0,256])
#hist, bins = np.histogram(img.ravel(), 256, [0,256])

plt.hist(img.ravel(), 256, [0,256])
plt.show()

#cv2.imshow("image", img)
#cv2.waitKey(0)