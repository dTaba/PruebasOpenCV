import cv2 as cv
import numpy as np

img = cv.imread('./Fotos/ejemplo.jpg')
cv.imshow('Cafecito', img)

cv.waitKey(0)