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
class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__("minimal_subscriber")
		self.subscription=self.create_subscription(String,"/robotPositions",self.listener_callback,10)
		self.subscription
		


	def listener_callback(self,msg):
		global l,x,y,xi,yi
		global r,k
		
		command=msg.data
		#print(command)
		p=command.split(" ")
	

			

		
		for i in range(0,len(p)):
			#print(p[i])
			if(p[i]=="7"):
				n=p[i-3].split(";")
				x=n[1]
				y=p[i-2]

				
		
				
				
		xi=int(float(x)) #changing string to float x corrdinate
		yi=int(float(y)) #changing string to float y corrdinate 

		print("x=",xi)
		print("y=",yi)
				
		
		
		if(xi<490 and xi>380 and yi<100 and yi>30): #22 483
			
					print('arrived at oldhome')
					l=62
					r=70
					r=str(r)
					l=str(l)
					ser.write(l.encode()+b"/n"+r.encode())
					k=0
	

		if(xi<800 and xi>400 and yi<970 and yi>870):
					if(k==0):
						print('Intersection')
						k=1
					
				
						l=80 #9
						r=0
						l=str(l)
						r=str(r)
						ser.write(l.encode()+b"/n"+r.encode())
						time.sleep(2.5)
						l=62 
						r=70
						
						l=str(l)
						r=str(r)
						ser.write(l.encode()+b"/n"+r.encode())
						
						#time.sleep(2)
					
		
		if(xi<800 and xi>700 and yi<1200 and yi>700):	# HOSPITAL LOCATION
					print('arrived at hospital')							
					l=0
					r=0
					r=str(r)
					l=str(l)
					ser.write(l.encode()+b"/n"+r.encode())
					
		

	
		#l=str(l)
		#r=str(r)

		#ser.write(l.encode())
		#ser.write(b"/n")
		#ser.write(r.encode())



		
		

		
			
		
		
		
	
def main(args=None):
	rclpy.init(args=args)
	minimal_subscriber=MinimalSubscriber()

	rclpy.spin(minimal_subscriber)


if __name__=="__main__":
	main()
