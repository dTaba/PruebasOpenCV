import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Fotos/ejemplo.jpg'))

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

cv.imshow("Bordes", canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

countours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)} contours encontrados')

cv.drawContours(blank, countours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)