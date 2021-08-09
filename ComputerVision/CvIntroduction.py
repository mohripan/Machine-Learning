import cv2 as cv
import sys

img = cv.imread('unnamed.jpg')

if img is None:
    sys.exit('Could not read the image')

cv.imshow('Display Window', img)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite('unnamed.png', img)