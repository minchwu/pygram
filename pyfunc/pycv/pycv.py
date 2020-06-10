# -*- coding: utf-8 -*-
# author: Minch Wu
"""pycv.

opencv 二次封装及接口实现
"""

import cv2 as cv

image = cv.imread("./picture/0003.jpg")
cv.imshow('Image', image)
print(image.shape)
cv.waitKey()
