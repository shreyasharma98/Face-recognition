import cv2
import numpy as np


face_id = int(input())
count = 0

haar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while(True):
    ret ,frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame', frame)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break


cap.release()
cv2.destroyAllWindows()
