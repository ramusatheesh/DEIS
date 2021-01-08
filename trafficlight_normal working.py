import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH) #Green Pin:6
GPIO.setup(23, GPIO.OUT,initial=GPIO.HIGH) #Red Pin:8
GPIO.setup(24, GPIO.OUT,initial=GPIO.HIGH) #Yellow Pin:9


while(1):
					#Green

	
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(18, GPIO.LOW)
	time.sleep(40)
					#Yellow
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	time.sleep(3)
					#Red
	
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(23, GPIO.LOW)
	time.sleep(40)
					#Yellow
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	time.sleep(3)
			
	

