#coding=utf-8
#中文乱码处理

import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

# img = cv2.imread("bd_icon.png")


def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


# img = cv2ImgAddText(img, "北斗启航", 50, 320, (51, 51, 51), 48)
#
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()