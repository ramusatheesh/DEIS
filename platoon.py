import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time
import keyboard
import warnings
import serial
ser=serial.Serial("/dev/ttyUSB0",baudrate=115200)
warnings.filterwarnings("ignore")


order=0 #to save # of nth vehicle,index
platoonsd=0 #Master =0
leftspeed=80
rightspeed=100
pid=0
vid=7 #From Spiral
q=0
class MinimalSubscriber(Node):
	global pid,vid
	number=[]
	def __init__(self):
		super().__init__("minimal_subscriber")
		self.subscription=self.create_subscription(String,"/action",self.listener_callback,10)
		self.subscription


	def listener_callback(self,msg):
	        
		p=[]
		global pid,vid,order
		command=msg.data
		p=command.split(";")
		if(command=='test'):
			
			pid=vid
			
		if(p[0]=='m'):
			print("Speed to arduino serial Left {} Right {}".format(p[1],p[2]))
			ser.write(p[1].encode()+b"/n"+p[2].encode())
		if(command=='s'):#Change Master
			print("Changing Master")
			pid=vid
		minimal_publisher= MinimalPublisher()
		
		rclpy.spin_once(minimal_publisher)
		#super().__init__('minimal_publisher')
		#minimal_publisher.publisher_ = self.create_publisher(String, "master", 10)
		#msg.data ="slave"
		#minimal_publisher.publisher_.publish(msg)
		        
			


	
class MinimalPublisher(Node):
    global leftspeed,rightspeed,pid,vid,q	
   
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, "/action", 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
      global q,pid
      if(keyboard.is_pressed("q")):
       q=1
      msg = String()
      if(pid==vid):
       msg.data ="m"+";"+str(leftspeed)+";"+str(rightspeed) 
       self.publisher_.publish(msg)
      if(pid==vid and q==1):#change Master
       msg.data ="s"
       self.publisher_.publish(msg)
       l=80
       r=0
       r=str(r)
       l=str(l)
       ser.write(l.encode()+b"/n"+r.encode())
       time.sleep(2.5)
       l=62
       r=80
       r=str(r)
       l=str(l)
       ser.write(l.encode()+b"/n"+r.encode())
       time.sleep(2.5)
       l=0
       r=0
       r=str(r)
       l=str(l)
       ser.write(l.encode()+b"/n"+r.encode())
       time.sleep(25)
      	
     
    
      	 
      

def main(args=None):
	global platoonsd
	rclpy.init(args=args)

	minimal_subscriber=MinimalSubscriber()
	
	rclpy.spin(minimal_subscriber)
	#rclpy.spin(minimal_publisher)
	#minimal_publisher.destroy_node()
	#rclpy.shutdown()
	    



if __name__=="__main__":
	main()
