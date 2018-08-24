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
import cv2

camera = cv2.VideoCapture(0)

fps = 30
size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter(
    "videos/test_video1.avi",
    # cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),
    fps,
    size
    )

success, frame = camera.read()
while success and cv2.waitKey(1) == -1:
    videoWriter.write(frame)
    success, frame = camera.read()
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    cv2.imshow('video', frame)
camera.release()
cv2.destroyAllWindows()


