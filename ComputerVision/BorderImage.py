import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

blue = [255, 255, 0]

img1 = cv.imread('unnamed.jpg')

replicate = cv.copyMakeBorder()