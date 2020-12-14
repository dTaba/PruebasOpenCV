import cv2 as cv
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale = 0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Fotos/ejemplo.jpg'))


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv a bgr', hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab a bgr', lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)