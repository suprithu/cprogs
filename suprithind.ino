#include <AFMotor.h>

AF_DCMotor motor1(1);  //motor1 is the left motor
AF_DCMotor motor2(2);  //motor2 is the right motor
int val;
char command; 

void setup() 
{       
  Serial.begin(9600);  //Set the baud rate to your Bluetooth module.
}



void loop() {
 
Serial.read();

if(val=='1')  //when the bluetooth module recieves 1 the car moves forward
{
 forward(); 
}

if(val=='2')  //when the bluetooth module recieves 2 the car moves backward
{
 backward(); 
}

if(val=='3') //when the bluetooth module recieves 3 the car moves left
{
 left(); 
}

if(val=='4')  //when the bluetooth module recieves 4 the car moves right
{
 right(); 
}

if(val=='5') //when the bluetooth module recieves 5 the car stops
{
 Stop(); 
}

}
void forward()
{
     motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void backward()
{
     motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}
void left()
{
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
}
void right()
{
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
}
void Stop()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

