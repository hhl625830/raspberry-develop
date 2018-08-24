# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project_Name :  raspberryPi-develop  
   File Name：     poolFaceDetection.py
   Description :
   Author :       HuHongLin
   date：          2018/8/23
-------------------------------------------------
   Change Activity:
                   2018/8/23 11:43:
-------------------------------------------------
"""

import multiprocessing as mp
import cv2
import os
import time

t_start = time.time()
fps = 0


# 人脸检测函数
def get_faces(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier(
        "Cascades/haarcascade_frontalface_default.xml"
    )
    faces = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3)

    return faces, img, gray


# 画框函数，
def draw_frame(faces, img, gray):

    global fps


    if len(faces):
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸

    # 计算FPS
    fps = fps + 1
    sfps = fps / (time.time() - t_start)
    cv2.putText(img, "FPS : " + str(int(sfps)), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Image", img)


if __name__ == '__main__':

    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    pool = mp.Pool(processes=4)

    read, img = camera.read()
    pr1 = pool.apply_async(get_faces, [img])
    read, img = camera.read()
    pr2 = pool.apply_async(get_faces, [img])
    read, img = camera.read()
    pr3 = pool.apply_async(get_faces, [img])
    read, img = camera.read()
    pr4 = pool.apply_async(get_faces, [img])

    fcount = 1

    while (True):
        read, img = camera.read()

        if fcount == 1:
            pr1 = pool.apply_async(get_faces, [img])
            faces, img, gray = pr2.get()
            draw_frame(faces, img, gray)

        elif fcount == 2:
            pr2 = pool.apply_async(get_faces, [img])
            faces, img, gray = pr3.get()
            draw_frame(faces, img, gray)

        elif fcount == 3:
            pr3 = pool.apply_async(get_faces, [img])
            faces, img, gray = pr4.get()
            draw_frame(faces, img, gray)

        elif fcount == 4:
            pr4 = pool.apply_async(get_faces, [img])
            faces, img, gray = pr1.get()
            draw_frame(faces, img, gray)
            fcount = 0

        fcount += 1

        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break
    # 按q退出
    cv2.destroyAllWindows()