import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

cv.imshow('Display', img)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

while True:
    if cv.waitKey(1) == ord('q'):
        break