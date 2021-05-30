# Import libraries

import numpy as np
import cv2
import time 

cap = cv2.VideoCapture(0) #video capture object and in bracket write webcame number
time.sleep(2) #2 or 3 seconds time for cam to setup
backgound = 0

# capturing the background
for i in range(30):
    ret , backgorund= cap.read() #30 iterations to capture the background

#till the capture object is runing this while loop will be runing
while (cap.isOpened()):
    ret , img = cap.read() #capturing the image to perform operation on it
   
   #to stop this code
    if not ret:
        break
    #converting from bgr to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #color space of the image when it is captured

    lower_red = np.array([0,120,70]) #hsv values , lower red means 0-10 as the colors get very light after that in 0-30
    upper_red = np.array([10,255,255])

    mask1 = cv2.inRange(hsv , lower_red , upper_red) #separating the cloak part

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([10,255,255])

    mask2 = cv2.inRange(hsv , lower_red , upper_red)

    mask1= mask1 + mask2

    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_OPEN, np.ones((3,3),np.uint8) , iterations=2) #noise reduction
    mask1 = cv2.morphologyEx(mask1 , cv2.MORPH_DILATE, np.ones((3,3),np.uint8) , iterations=1) #smoothning image
    
    mask2 = cv2.bitwise_not(mask1) #everything except the cloak
    res1 = cv2.bitwise_and(backgorund , background , mask=mask1) #segmentation of color
    res2 = cv2.bitwise_and(img , img , mask=mask2) #used to substitute the cloak part
    final_output = cv2.addWeighted(res1,1,res2,1,0) #liniear add two images
    cv2.imshow("yaya",final_output)
    k = cv2.waitKey(10)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()




     



