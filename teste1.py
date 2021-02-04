import cv2
import numpy as np

img = cv2.imread('garrafas.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)

number = 0

for cnt in contours:
    #cv2.putText(img, "{}".format(cnt + 1), (int(10) - 45, int(20)+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    cv2.drawContours(img,[cnt],0,(0,0,255),1)
    number += 1

cv2.putText(img, "{}".format(number), (10, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
print(number)

cv2.imwrite("gasTeste2.jpg", img)