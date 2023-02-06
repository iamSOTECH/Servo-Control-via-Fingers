/*
  Servo Motion Based on Hand Tracking
  EGN 4060, Spring 2022
  Final Project
  Brendon Hales, Lizzy Mikulas, Roger Breit
*/
#include <Servo.h>

// Servos
Servo xServo;
Servo yServo;

// Global variables
int xPos = 0; // Variable for the x servo position
int yPos = 90;  // Variable for the y servo position
String dataFromPython;  // Variable to hold data transmitted from Python

void servoMove(String data)
{
  // Horizontal
  // Left
  // Moves the x servo left by 10 degrees until the limit of 180 degrees is reached
  if (data == "Left 10")
  {
    if ((xPos + 10) <= 180)
    {
      xPos = xPos + 10;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(180);
      delay(15);
    }
  }
  // Moves the x servo left by 20 degrees until the limit of 180 degrees is reached
  else if (data == "Left 20")
  {
    if ((xPos + 20) <= 180)
    {
      xPos = xPos + 20;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(180);
      delay(15);
    }
  }
  // Moves the x servo left by 30 degrees until the limit of 180 degrees is reached
  else if (data == "Left 30")
  {
    if ((xPos + 30) <= 180)
    {
      xPos = xPos + 30;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(180);
      delay(15);
    }
  }
  // Moves the x servo left by 40 degrees until the limit of 180 degrees is reached
  else if (data == "Left 40")
  {
    if ((xPos + 40) <= 180)
    {
      xPos = xPos + 40;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(180);
      delay(15);
    }
  }
  // Moves the x servo left by 50 degrees until the limit of 180 degrees is reached
  else if (data == "Left 50")
  {
    if ((xPos + 50) <= 180)
    {
      xPos = xPos + 50;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(180);
      delay(15);
    }
  }
  // Right
  // Moves the x servo right by 10 degrees until the limit of 180 degrees is reached
  else if (data == "Right 10")
  {
    if ((xPos - 10) >= 0)
    {
      xPos = xPos - 10;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(0);
      delay(15);
    }
  }
  // Moves the x servo right by 20 degrees until the limit of 180 degrees is reached
  else if (data == "Right 20")
  {
    if ((xPos - 20) >= 0)
    {
      xPos = xPos - 20;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(0);
      delay(15);
    }
  }
  // Moves the x servo right by 30 degrees until the limit of 180 degrees is reached
  else if (data == "Right 30")
  {
    if ((xPos - 30) >= 0)
    {
      xPos = xPos - 30;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(0);
      delay(15);
    }
  }
  // Moves the x servo right by 40 degrees until the limit of 180 degrees is reached
  else if (data == "Right 40")
  {
    if ((xPos - 40) >= 0)
    {
      xPos = xPos - 40;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(0);
      delay(15);
    }
  }
  // Moves the x servo right by 50 degrees until the limit of 180 degrees is reached
  else if (data == "Right 50")
  {
    if ((xPos - 50) >= 0)
    {
      xPos = xPos - 50;
      xServo.write(xPos);
      delay(15);
    }
    else
    {
      xServo.write(0);
      delay(15);
    }
  }
  // Vertical
  // Up
  // Moves the y servo up by 5 degrees until the limit of 180 degrees is reached
  else if (data == "Right Left 5" || data == "Left Right 5")
  {
    if ((yPos + 5) <= 180)
    {
      yPos = yPos + 5;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(180);
      delay(15);
    }
  }
  // Moves the y servo up by 10 degrees until the limit of 180 degrees is reached
  else if (data == "Right Left 10" || data == "Left Right 10")
  {
    if ((yPos + 10) <= 180)
    {
      yPos = yPos + 10;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(180);
      delay(15);
    }
  }
  // Moves the y servo up by 15 degrees until the limit of 180 degrees is reached
  else if (data == "Right Left 15" || data == "Left Right 15")
  {
    if ((yPos + 15) <= 180)
    {
      yPos = yPos + 15;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(180);
      delay(15);
    }
  }
  // Moves the y servo up by 20 degrees until the limit of 180 degrees is reached
  else if (data == "Right Left 20" || data == "Left Right 20")
  {
    if ((yPos + 20) <= 180)
    {
      yPos = yPos + 20;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(180);
      delay(15);
    }
  }
  // Moves the y servo up by 25 degrees until the limit of 180 degrees is reached
  else if (data == "Right Left 25" || data == "Left Right 25")
  {
    if ((yPos + 25) <= 180)
    {
      yPos = yPos + 25;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(180);
      delay(15);
    }
  }
  // Down
  // Moves the y servo down by 5 degrees until the limit of 90 degrees is reached
  else if (data == "Right Left -5" || data == "Left Right -5")
  {
    if ((yPos - 5) >= 90)
    {
      yPos = yPos - 5;
      yServo.write(yPos);
      delay(15);
    }
    else
    {
      yServo.write(90);
      delay(15);
    }
  }
  else
  {
    xServo.write(xPos);
    yServo.write(yPos);
    delay(15);
  }
}

void setup()
{
  xServo.attach(9); // Attaches the X servo on pin 9
  yServo.attach(10);  // Sttaches the y servo on pin 10
  Serial.begin(9600); // Initializes serial communication with baud rate of 9600
  xServo.write(0);  // Initializes X Direction Servo at 0 degrees
  yServo.write(90); // Initializes Y DIrection Servo at 90 degrees
}

void loop()
{
  while (Serial.available())    //whatever the data that is coming in serially and assigning the value to the variable “data”
  {
    dataFromPython = Serial.readStringUntil('\n');  // Reads incoming data from Python until a new line character is reached
    // Serial.write("Successful data transmission \n"); // Testing
    servoMove(dataFromPython);  // Calls servoMove funciton
  }
}
