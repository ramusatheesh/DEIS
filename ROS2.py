import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
import serial

ser=serial.Serial("/dev/ttyUSB0")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
p=[]
n=[]
class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__("minimal_subscriber")
		self.subscription=self.create_subscription(String,"/action",self.listener_callback,10)
		self.subscription


	def listener_callback(self,msg):
		command=msg.data
		p=command.split(",")
		n=p[5].split(";")
		#l=str(n[0]+"\n "+n[1])
		l=str(n[0])
		r=str(n[1])
		
		
		
		#ser.write(b"1")
		ser.write(l.encode())
		ser.write(b"/n")
		ser.write(r.encode())

def main(args=None):
	rclpy.init(args=args)
	minimal_subscriber=MinimalSubscriber()

	rclpy.spin(minimal_subscriber)


if __name__=="__main__":
	main()
