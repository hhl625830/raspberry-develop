# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project_Name :  raspberryPi-devellop
   File Name：     savaVideo.py
   Description :
   Author :       HuHongLin
   date：          2018/8/22
-------------------------------------------------
   Change Activity:
                   2018/8/22 15:17:
-------------------------------------------------
"""
import time

import RPi.GPIO as GPIO
import cv2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
fcounter = 0
facefind = 0
t_start = time.time()
fps = 0
face_detector = cv2.CascadeClassifier('../Cascades/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0


def draw_frame(img, faces, gray):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

def my_callback(channel):
    print("button pressed!")
    global count
    count += 1
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


        cv2.imwrite("dataSet/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
        print("----------------------------save OK!----------------------")
    time.sleep(0.01)
    pass


GPIO.add_event_detect(35, GPIO.RISING, callback=my_callback)
while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, 1) # flip video image vertically
    global fps
    global count
    if fcounter == 3:
        fcounter = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        if str(len(faces)) != 0:
            facefind = 1
            facess = faces
        else:
            facefind = 0

            draw_frame(img, faces, gray)
    else:
        if facefind == 1 and str(len(facess)) != 0:
            draw_frame(img, faces, gray)

    fcounter += 1
    fps = fps + 1
    sfps = fps / (time.time() - t_start)
    cv2.putText(img, "FPS : " + str(int(sfps)), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('video', img)

    try:
        print("I'm working...")

        pass
    except KeyboardInterrupt:
        break
        pass
    pass

    k = cv2.waitKey(1000 // 12) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()


