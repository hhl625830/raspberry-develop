import time

import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
# smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
fcounter = 0
facefind = 0
t_start = time.time()
fps = 0


def draw_frame(img, faces, gray):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # eyes = eyeCascade.detectMultiScale(
        #     roi_gray,1.3,5,0,(5, 5)
        # )
        #
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        #
        # smile = smileCascade.detectMultiScale(
        #     roi_gray,
        #     scaleFactor=1.3,
        #     minNeighbors=5,
        #     minSize=(25, 25),
        # )
        #
        # for (xx, yy, ww, hh) in smile:
        #     cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)


while True:
    ret, img = cap.read()
    # img = cv2.flip(img, -1)
    global fps
    if fcounter == 3:
        fcounter = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.3,5)

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

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
