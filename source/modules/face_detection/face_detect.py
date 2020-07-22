from os.path import abspath
import numpy as np
import cv2


def has_face(img):
    img_array = np.array(bytearray(img), dtype=np.uint8)
    img_gray = cv2.cvtColor(cv2.imdecode(img_array, -1), cv2.COLOR_BGR2GRAY)
    haar_cascade_face = cv2.CascadeClassifier(
        abspath('modules/face_detection/haarcascade_frontalface_default.xml'))
    faces_rects = haar_cascade_face.detectMultiScale(img_gray,
                                                     scaleFactor=1.2,
                                                     minNeighbors=5)
    return True if len(faces_rects) else False
