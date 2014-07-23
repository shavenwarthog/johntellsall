import numpy as np

import sys; sys.path.append('/usr/lib/pyshared/python2.7')

import cv2
from cv2 import *

im = cv2.imread('rubik.png')
im = cv2.bilateralFilter(im,9,75,75)
im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)   # HSV image


# hue 20-30 = color yellow 

# HSV color code lower and upper bounds
COLOR_MIN = np.array([0, 100, 100], np.uint8)
COLOR_MAX = np.array([255, 255, 255], np.uint8)

frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)     # Thresholding image
# cv2.imshow('threshed', frame_threshed)

contours,hierarchy = cv2.findContours(
    frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE,
)
cv2.drawContours(im, contours, -1, (0,0,255), 3)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    print x,y,'\t',w,h
    cv2.rectangle(im, (x,y), (x+w,y+h), (120,255,120), 2)
cv2.imshow('contours', im)
cv2.waitKey()
sys.exit(0)


# imgray = frame_threshed
# ret,thresh = cv2.threshold(frame_threshed,127,255,0)
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print type(contours)
# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     print x,y
#     cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow("Show",im)
# # cv2.imwrite("extracted.jpg", im)
# cv2.waitKey()
# # cv2.destroyAllWindows()
