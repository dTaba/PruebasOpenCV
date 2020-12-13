import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('./Fotos/xd.jpg'))

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translate = translate(img, -50, 50)
cv.imshow('Translated', translate)

def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow('Rotada', rotated)

resized = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resize', resized)

flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

crop = img[200:300, 300:400]
cv.imshow('Crop', crop)

cv.waitKey(0)