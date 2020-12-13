import cv2 as cv

# Funciones #

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Solo sirve para webcam
    capture.set(3, width)
    capture.set(4, height)

# # Leyendo imagenes #

# img = cv.imread('./Fotos/Cara.jpg')
# img_resized = rescaleFrame(img)
# cv.imshow('Cara', img_resized)

# cv.waitKey(0)

# Leyendo videos #

# capture = cv.VideoCapture(0)
   
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video', frame_resized)
    
#     if cv.waitKey(20) & 0xFF==ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()