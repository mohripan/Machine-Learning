import numpy as np
import cv2 as cv

img = cv.imread('unnamed.jpg')

b, g, r = cv.split(img)
img = cv.merge((r,r, r))

while True:
    cv.imshow('Display Windows', img)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
    