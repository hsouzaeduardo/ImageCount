import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

filename = 'gasTeste.jpg'

image = cv2.imread("gas1.jpg")

image_blur = cv2.medianBlur(image,31)

image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)

cv2.imwrite(filename, image_blur_gray) 

kernel = np.ones((3,3),np.uint8)

thresh = cv2.adaptiveThreshold(image_blur_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 3)

opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, last_image =  cv2.threshold(dist_transform, 0.3*dist_transform.max(),255,0)
last_image = np.uint8(last_image)

cnts = cv2.findContours(last_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

def display(img,count,cmap="gray"):
    
    f_image = cv2.imread("gas1.jpg")
    f, axs = plt.subplots(1,2,figsize=(12,5))
    axs[0].imshow(f_image,cmap="gray")
    axs[1].imshow(img,cmap="gray")
    print(count)
    axs[1].set_title("Total Bujões = {}".format(count))
    
def showDisplay(cnts):
    
    for (i, c) in enumerate(cnts):
        ((x, y), _) = cv2.minEnclosingCircle(c)
        
        cv2.putText(image, "{}".format(i + 1), (int(x) - 45, int(y)+20),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
        
       #cv2.drawContours(image, [c], -1, (66,72,79), 2)

        #cv2.imwrite(filename, image) 

    cv2.imshow("source", image)
        
    cv2.waitKey(0)

   

display(image,len(cnts))

showDisplay(cnts)
