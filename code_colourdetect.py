import cv2 as cv
from easytello import tello
from tkinter import *

import numpy as np
import time
time.sleep(3)
my_drone = tello.Tello()


my_drone.takeoff()

#my_drone.streamon()
my_drone.send_command('streamon')
    # Creating stream capture object
cap = cv.VideoCapture('udp://@0.0.0.0:11111')
        # Runs while 'stream_state' is True
while True:
      
      ret, frame = cap.read()
      if frame is None:
         break
      frame=cv.resize(frame,(360,240))
      blur = cv.GaussianBlur(frame,(5,5),0)
      #cv.imshow("original",frame)
      #cv.imshow("blurred",blur)
      hsv_frame=cv.cvtColor(blur,cv.COLOR_BGR2HSV)
      low_red = np.array([0, 70, 50])
      high_red = np.array([10, 255, 255])
      mask1 = cv.inRange(hsv_frame, low_red, high_red)
      mask2=cv.inRange(hsv_frame,np.array([170, 70, 50]),np.array([180, 255, 255]))

      mask = mask1 | mask2;
      mask3 = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3,3),np.uint8))

      mask3 = cv.morphologyEx(mask3, cv.MORPH_DILATE, np.ones((3,3),np.uint8))

 

      contours, hierarchy = cv.findContours(mask3, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
      op=cv.drawContours (frame, contours, -1, (0,255,0), 3)
      cv.imshow('Frame', frame)
      cv.imshow('Mask',mask)
      for contour in contours:
         area = cv.contourArea(contour)
      if (area>100):
         time.sleep(3)
         print("AMBULANCE is DETECTED")
  
         window = Tk()

         window.title("Welcome to LikeGeeks app")

         lbl = Label(window, text="AMBULANCE DETECTED", font=("Arial Bold", 80),fg="red")

         lbl.grid(column=0, row=0)

         window.mainloop()
         break
    

                 
      #mask2 = cv.bitwise_not(mask1)
      #res1 = cv.bitwise_and(frame,frame,mask=mask2)

      
      
      
      #
      
      if cv.waitKey(25) & 0xFF == ord('q'):
          break
cap.release()
cv.destroyAllWindows()


