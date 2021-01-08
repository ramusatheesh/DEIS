import numpy as np
import cv2 as cv
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH) #Green Pin:6
GPIO.setup(23, GPIO.OUT,initial=GPIO.HIGH) #Red Pin:8
GPIO.setup(24, GPIO.OUT,initial=GPIO.HIGH) #Yellow Pin:9

backSub = cv.createBackgroundSubtractorMOG2()
os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'
capture = cv.VideoCapture(0)





class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, '/action', 10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
	
      msg = String()
      msg.data = 'STOP' 
      print(msg.data)
      self.publisher_.publish(msg)
rclpy.init(args=None)

minimal_publisher = MinimalPublisher()




frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (40, 3))
time.sleep(2) #Cancel initial wrong detection
print("5")
while True:

    ret, frame = capture.read()
    if frame is None:
		    
      break
		    
    fgMask = backSub.apply(frame)
		   	
		    
   
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel); 
    if(np.median(fgMask) >250):

        rclpy.spin_once(minimal_publisher)
  
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        time.sleep(10)
        frame=[]
  
minimal_publisher.destroy_node()
rclpy.shutdown()
capture.release()
#cv.destroyAllWindows()








      



