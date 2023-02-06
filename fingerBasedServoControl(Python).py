# Servo Motion Based on Hand Tracking
# EGN 4060, Spring 2022
# Final Project
# Brendon Hales, Lizzy Mikulas, Roger Breit

# Imports for OpenCV, time, and serial communication to the Arduino
import cv2, time
from serial import Serial

# Import for hand detection
from cvzone.HandTrackingModule import HandDetector

# Initialize Arduino Communication
ArduinoSerial = Serial('com4', 9600, timeout=0.1)
time.sleep(1)

# Determines movement angle based on the number of fingers held up on one hands
def oneHandIdentification(oneHandType, oneHandFingers):
    handIdentifier = oneHandType
    fingerIdentifier = oneHandFingers
    movementAngle = 0
    # One finger up on one hand
    if fingerIdentifier == [1, 0, 0, 0, 0]:
        movementAngle = 10
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 1, 0, 0, 0]:
        movementAngle = 10
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 1, 0, 0]:
        movementAngle = 10
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 0, 1, 0]:
        movementAngle = 10
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 0, 0, 1]:
        movementAngle = 10
        moveXArduino(handIdentifier, movementAngle)
    # Two fingers up on one hand
    elif fingerIdentifier == [1, 1, 0, 0, 0]:
        movementAngle = 20
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 1, 1, 0, 0]:
        movementAngle = 20
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 1, 1, 0]:
        movementAngle = 20
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 0, 1, 1]:
        movementAngle = 20
        moveXArduino(handIdentifier, movementAngle)
    # Three fingers up on one hand
    elif fingerIdentifier == [1, 1, 1, 0, 0]:
        movementAngle = 30
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 1, 1, 1, 0]:
        movementAngle = 30
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 0, 1, 1, 1]:
        movementAngle = 30
        moveXArduino(handIdentifier, movementAngle)
    # Four fingers up on one hand
    elif fingerIdentifier == [1, 1, 1, 1, 0]:
        movementAngle = 40
        moveXArduino(handIdentifier, movementAngle)
    elif fingerIdentifier == [0, 1, 1, 1, 1]:
        movementAngle = 40
        moveXArduino(handIdentifier, movementAngle)
    # Five fingers up on one hand
    elif fingerIdentifier == [1, 1, 1, 1, 1]:
        movementAngle = 50
        moveXArduino(handIdentifier, movementAngle)

# Determines movement angle based on the number of fingers held up on two hands
def twoHandIdentification(twoHandType1, twoHandFingers1, twoHandType2, twoHandFingers2):
    hand1Identifier = twoHandType1
    finger1Identifier = twoHandFingers1
    hand2Identifier = twoHandType2
    finger2Identifier = twoHandFingers2
    yMovementAngle = 0
    # One finger up on both hands (same finger)
    if finger1Identifier == [1, 0, 0, 0, 0] and finger2Identifier == [1, 0, 0, 0, 0]:
        yMovementAngle = 5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 1, 0, 0, 0] and finger2Identifier == [0, 1, 0, 0, 0]:
        yMovementAngle = 5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 1, 0, 0] and finger2Identifier == [0, 0, 1, 0, 0]:
        yMovementAngle = 5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 0, 1, 0] and finger2Identifier == [0, 0, 0, 1, 0]:
        yMovementAngle = 5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 0, 0, 1] and finger2Identifier == [0, 0, 0, 0, 1]:
        yMovementAngle = 5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    # Two fingers up on both hands (same fingers)
    elif finger1Identifier == [1, 1, 0, 0, 0] and finger2Identifier == [1, 1, 0, 0, 0]:
        yMovementAngle = 10
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 1, 1, 0, 0] and finger2Identifier == [0, 1, 1, 0, 0]:
        yMovementAngle = 10
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 1, 1, 0] and finger2Identifier == [0, 0, 1, 1, 0]:
        yMovementAngle = 10
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 0, 1, 1] and finger2Identifier == [0, 0, 0, 1, 1]:
        yMovementAngle = 10
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    # Three fingers up on both hands (same fingers)
    elif finger1Identifier == [1, 1, 1, 0, 0] and finger2Identifier == [1, 1, 1, 0, 0]:
        yMovementAngle = 15
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 1, 1, 1, 0] and finger2Identifier == [0, 1, 1, 1, 0]:
        yMovementAngle = 15
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 0, 1, 1, 1] and finger2Identifier == [0, 0, 1, 1, 1]:
        yMovementAngle = 15
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    # Four fingers up on both hands (same fingers)
    elif finger1Identifier == [1, 1, 1, 1, 0] and finger2Identifier == [1, 1, 1, 1, 0]:
        yMovementAngle = 20
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    elif finger1Identifier == [0, 1, 1, 1, 1] and finger2Identifier == [0, 1, 1, 1, 1]:
        yMovementAngle = 20
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    # Five fingers up on both hands (same fingers)
    elif finger1Identifier == [1, 1, 1, 1, 1] and finger2Identifier == [1, 1, 1, 1, 1]:
        yMovementAngle = 25
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)
    # No fingers up on both hands
    elif finger1Identifier == [0, 0, 0, 0, 0] and finger2Identifier == [0, 0, 0, 0, 0]:
        yMovementAngle = -5
        moveYArduino(hand1Identifier, hand2Identifier, yMovementAngle)

# Sends data to move the x servo to the Arduino
def moveXArduino(handIdentifier, movementAngle):
    string = handIdentifier + ' ' + str(movementAngle) + '\n'
    #print("Python", string) # Testing
    ArduinoSerial.write(bytes(string, 'utf-8'))
    #print(ArduinoSerial.read_until('\n'))   # Testing
    time.sleep(.015)

# Sends data to move the y servo to the Arduino
def moveYArduino(hand1Identifier, hand2Identifier, movementAngle):
    string = hand1Identifier + ' ' + hand2Identifier + ' ' + str(movementAngle) + '\n'
    #print("Python", string) # Testing
    ArduinoSerial.write(bytes(string, 'utf-8'))
    #print(ArduinoSerial.read_until('\n'))   # Testing 
    time.sleep(.015)

# Start of main function
# Initiate webcam video capture
webcam = cv2.VideoCapture(0)

# Hand Detection
handDetect = HandDetector(detectionCon=0.8, maxHands=2)

while webcam.isOpened():
    ret, frame = webcam.read()
    foundHands, bbox = handDetect.findHands(frame)

    if foundHands:   # If hands are found in the frame
        if len(foundHands) == 1: # If only one hand is found in the frame
            # 1 hand
            oneHand = foundHands[0]
            oneHandType = oneHand["type"]  # Left or Right

            # Determine number of fingers up on hand
            # Outputs array where the thumb is the most left location, and pinky is the furthest right
            # Example: Thumb ring finger up [1, 0, 0, 1, 0]
            oneHandFingers = handDetect.fingersUp(oneHand)
            #print(handType1, fingers1)  # Testing
            oneHandIdentification(oneHandType, oneHandFingers)
        elif len(foundHands) == 2:   # If 2 hands are found in the frame  
            # 2 hands
            hand1 = foundHands[0]
            hand2 = foundHands[1]
            handType1 = hand1["type"]   # Left or Right
            handType2 = hand2["type"]   # Left or Right
            # Determine number of fingers up on each hand
            # Outputs array where the thumb is the most left location, and pinky is the furthest right
            # Example: Thumb ring finger up [1, 0, 0, 1, 0]
            fingers1 = handDetect.fingersUp(hand1)
            fingers2 = handDetect.fingersUp(hand2)
            #print(handType1, fingers1, handType2, fingers2) # Testing
            twoHandIdentification(handType1, fingers1, handType2, fingers2)
    
    cv2.imshow('Press "ESC" to quit', frame)    # Output webcam feed
    # press 'ESC' to Quit
    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
