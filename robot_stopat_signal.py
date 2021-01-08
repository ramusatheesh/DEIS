import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
import serial
import numpy as np

ser=serial.Serial("/dev/ttyUSB0",baudrate=115200)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
p=[]
n=[]
l=0
r=0
xi=0
yi=0
x=0
y=0
k=0
i=0

l=76
r=80
r=str(r)
l=str(l)
ser.write(l.encode()+b"/n"+r.encode())
rclpy.init(args=None)



class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__("minimal_subscriber")
		self.subscription=self.create_subscription(String,"traffic",self.listener_callback,0)
		self.subscription
		
		

		
	def listener_callback(self,msg):
		global i
		command=msg.data
		print(command)
		
		if(command=="STOP" and i==0):
				i+=1
				l=0
				r=0
				r=str(r)
				l=str(l)
				ser.write(l.encode()+b"/n"+r.encode())
				
				time.sleep(5)
				l=76
				r=80
				r=str(r)
				l=str(l)
				ser.write(l.encode()+b"/n"+r.encode())
				time.sleep(10)
				l=0
				r=0
				r=str(r)
				l=str(l)
				ser.write(l.encode()+b"/n"+r.encode())
				

		
				

			
minimal_subscriber=MinimalSubscriber()
i=0
rclpy.spin(minimal_subscriber)


	




		
		

		
			
		
		
		
	










	






			




		
		

		
			

	
	
	

		
