import numpy as np
import cv2 as cv

cap = cv.VideoCapture('jahy.mp4')

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('out.avi', fourcc, 60, (1280, 720))

while True:
    ret, frame = cap.read()

    if not ret:
        print('Cannot read frame')
        break

    frame = cv.flip(frame, 90)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)

    cv.imshow('Jahy', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()