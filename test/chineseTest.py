# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project_Name :  raspberryPi-develop  
   File Name：     chineseTest.py
   Description :
   Author :       HuHongLin
   date：          2018/8/23
-------------------------------------------------
   Change Activity:
                   2018/8/23 15:36:
-------------------------------------------------
"""

import cv2
import sys
import os.path

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import chineseText as text

img = cv2.imread("bd_icon.png")
img = text.cv2ImgAddText(img, "北斗启航", 50, 320, (51, 51, 51), 48)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
