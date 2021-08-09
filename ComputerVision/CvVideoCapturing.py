import numpy as np
import cv2 as cv

cap = cv.VideoCapture('jahy.mp4')

while True:
    ret, frame = cap.read()

    if not ret:
        print('Cant receive frame')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('Jahy Sama', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()