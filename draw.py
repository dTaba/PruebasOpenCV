import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# blank[200:300, 200:300] = 0,0,255
# cv.imshow('Red', blank)

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = -1)
# cv.imshow('Blank',  blank)

cv.circle(blank, (250, 250), 40, (0, 0 ,255), thickness = -1)
# cv.imshow('Circle', blank)

cv.line(blank, (0, 0), (250, 250), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

cv.putText(blank, 'MI PAIS', (320, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness= 2)
cv.imshow('Text', blank)

cv.waitKey(0)