

#include <RedBot.h>
RedBotMotors motors;
int leftPower;  // variable for setting the drive power
int rightPower;
int data;  // variable for holding incoming data from PC to Arduino
int i,j;






RedBotSensor IRSensor1 = RedBotSensor(A3); // initialize a sensor object on A3
RedBotSensor IRSensor2 = RedBotSensor(A6); // initialize a sensor object on A6
RedBotSensor IRSensor3 = RedBotSensor(A7); // initialize a sensor object on A7





int buttonState = 0;    
const int trigPin = 9;
const int echoPin = 10;
const int buttonPin = 3;  


const int red = A0;
const int green = 10;
const int blue = 3;  


// defines variables
long duration;
int distance;

void setup()
{
 pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(buttonPin, INPUT);

pinMode(red, OUTPUT); 
Serial.begin(9600); // Starts the serial communication

}

void loop()
{
buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance
distance= duration;//*0.034/2;

Serial.println(distance);



  

if(distance>500){
  Serial.print("Running");
  if(IRSensor3.read()>100 & IRSensor2.read()<100)//left
{
   motors.leftMotor(0);
    motors.rightMotor(0);
    delay(1000); 
  motors.leftMotor(-80);
    motors.rightMotor(0);
    while(IRSensor3.read()>100);
    
  }
    if(IRSensor2.read()>100)//right
{
     motors.leftMotor(0);
    motors.rightMotor(0);
    delay(1000); 
  motors.leftMotor(0);
    motors.rightMotor(-80);
    while(IRSensor2.read()>100 & IRSensor3.read()<100);
    
  }
//  if(IRSensor2.read()>100 & IRSensor3.read()>100)//str
//{
//  motors.leftMotor(-50);
//    motors.rightMotor(-50);
//    while(IRSensor2.read()>100 & IRSensor3.read()>100);
//    
//  }
else
{
  
  motors.leftMotor(-50);
    motors.rightMotor(-40);
   
  }
}
else
{
  
  motors.leftMotor(0);
    motors.rightMotor(0);
} 

buttonState = digitalRead(buttonPin);
  } 
  //Emergency Vehicle
  
  else {

digitalWrite(red, HIGH);
    if(Serial.available()>0)
  {
    i=Serial.parseInt();
   j=Serial.parseInt();
   Serial.print(i);
   Serial.print(j);
  }
     motors.leftMotor(-i);
    motors.rightMotor(-j);
  buttonState = digitalRead(buttonPin);
    
  }
  digitalWrite(red, LOW);

}
