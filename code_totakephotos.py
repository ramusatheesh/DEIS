import cv2 as cv
from easytello import tello

import numpy as np
import time

my_drone = tello.Tello()

i=130
my_drone.takeoff()
#my_drone.streamon()
my_drone.send_command('streamon')
    # Creating stream capture object
cap = cv.VideoCapture('udp://@0.0.0.0:11111')
        # Runs while 'stream_state' is True
while i<150:
      
      ret, frame = cap.read()
      if frame is None:
         break
      frame=cv.resize(frame,(360,240))
      frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
      cv.imwrite("test{}.jpg".format(i),frame)

      i+=1
      if cv.waitKey(25) & 0xFF == ord('q'):
          break
i=0
cap.release()
cv.destroyAllWindows()


