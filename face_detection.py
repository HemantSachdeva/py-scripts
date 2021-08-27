#!/usr/bin/env python3

try:
    import cv2
    import numpy as np
except ImportError:
    raise ImportError('OpenCV is not installed')

face_cascade = cv2.CascadeClassifier('video/haarcascade_frontalface_default.xml')

number = 0
cam = cv2.VideoCapture('video/people.mp4')
while True:
    try:
        _, img = cam.read()
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage)
        print(faces)

        if len(faces) == 0:
            print('No faces found')
        else:
            print(f"Found {len(faces)} faces")
            number = faces.shape[0]
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

            cv2.rectangle(img, ((0, img.shape[0] - 25)),
                        (270, img.shape[0]), (255, 255, 255), -1)
            cv2.putText(img, f"Number of faces detected: " + str(
                faces.shape[0]), (0, img.shape[0] - 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 0))
            cv2.imshow('Image with faces', img)
            cv2.imshow('Gray image', grayImage)
            cv2.waitKey(1)

    except KeyboardInterrupt():
        cv2.destroyAllWindows()
