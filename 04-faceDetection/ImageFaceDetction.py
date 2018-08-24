import cv2

filepath =  "images/hwasmart.jpg"
img = cv2.imread(filepath)

# gray

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap = cv2.CascadeClassifier(
        "Cascades/haarcascade_frontalface_default.xml"
    )

# draw a ractangle on the picture
#x = y = 10 # coordinate
#w = 100 # size of the rectangle
color = (0, 0, 255) # draw color
#cv2.rectangle(img, (x, y), (x+w, y+w), color,1) # draw rectangle
faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 10), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 10), min(w // 8, h // 8),
                   color)

        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)


# show image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()