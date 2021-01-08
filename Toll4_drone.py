import time
import math
from easytello import tello



my_drone = tello.Tello()
x1=0#initial pos(Oldage Home)
y1=0
x2=30
#Destination(Hospital)
y2=125
while(1):


      x_distance=math.sqrt((x2-x1)**2) #Get positive distance
      y_distance=math.sqrt((y2-y1)**2)


      time.sleep(1) 
      
      a=my_drone.get_attitude()
      time.sleep(1) 
      my_drone.takeoff()

      while(a[2]>5 or a[2]<0):
        my_drone.cw(5)
        time.sleep(2)
        a=my_drone.get_attitude()
        

      
      my_drone.go(x_distance,y_distance,0,10)
     
      #my_drone.down(20)
      #time.sleep(1)
      #my_drone.down(20)
      #time.sleep(1)

      

      while(a[2]>5 or a[2]<0):
        my_drone.cw(5)
        a=my_drone.get_attitude()
       

      my_drone.land()
     
      time.sleep(5)

      a=my_drone.get_attitude()
      time.sleep(1) 
      my_drone.takeoff()
      
      my_drone.go(-x_distance,-y_distance,0,10)
      print(my_drone.get_attitude())
      my_drone.down(20)
      time.sleep(1)
      my_drone.down(20)
      time.sleep(1)

      print(my_drone.get_attitude())
      
      #while(a[2]>5 or a[2]<0):
      #  my_drone.cw(5)
      #  a=my_drone.get_attitude()
      #  print("attitude",a[2])

      my_drone.land()
      print(my_drone.get_attitude())
      time.sleep(5)