import cv2 as cv

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Fotos/xd.jpg'))

cv.imshow('Yo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Yo pero gris', gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Yo blureado', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Edgy diego', canny)

dilated = cv.dilate(canny , (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

resized = cv.resize(img,(200, 200), interpolation = cv.INTER_CUBIC)
cv.imshow('DIEGO CHIQUITO', resized)

crop = img[50:200, 200:400]
cv.imshow('Cropea3', crop)

cv.waitKey(0)