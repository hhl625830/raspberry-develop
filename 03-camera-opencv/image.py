# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO
import cv2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
count = 0
cap = cv2.VideoCapture(0)
# cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
def my_callback(channel):
        print("button pressed!")
        global count
        count += 1
        cv2.imwrite("images/test_img_" + str(count) + ".jpg", frame)
        print("----------------------------save OK!----------------------")
        time.sleep(0.01)
        pass

GPIO.add_event_detect(35, GPIO.RISING, callback=my_callback)
while True:
    
    # get a frame
    ret, frame = cap.read()
    #print("frame.shape: {}".format(frame.shape))
   
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    try:
        print("I'm working...")
        
        pass
    except KeyboardInterrupt:
        break
        pass
    pass


GPIO.cleanup()

cap.release()
cv2.destroyAllWindows()