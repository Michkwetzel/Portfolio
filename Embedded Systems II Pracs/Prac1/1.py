#!/usr/bin/python3
"""
Python Practical Template
Michael Wetzel
Readjust this Docstring as follows:
Names: Michael
Student Number: WTZMIC001
Prac: 1
Date: 29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time as t
global direction

#Callback functions 
def callback1(channel):
    global direction
    direction = True
    print ("Direction up" + str(direction))
def callback2(channel):
    global direction
    direction = False
    print ("Direction down" + str(direction))

#Seting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT , initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Code to initialize `2winterrupts using the 2nd thread (for button presses)
GPIO.add_event_detect(19, GPIO.RISING, callback=callback1, bouncetime=200)
GPIO.add_event_detect(26, GPIO.RISING, callback=callback2, bouncetime=200)

def main():
#Initializing variables
    global direction
    flag = True
    i = 0
    direction = False

#While loop that runs infinite. Will respont to current binary value and call a function 
    while flag :
        if i == 0:
            i = b0(0,direction)
            print ("000\n")
            t.sleep(2)
        if i == 1:
            i = b1(1,direction)
            print ("001\n")
            t.sleep(2)
        if i == 2:
            i = b2(2,direction)
            print ("010\n")
            t.sleep(2)
        if i == 3:
            i = b3(3,direction)
            print ("011\n")
            t.sleep(2)
        if i == 4:
            i = b4(4,direction)
            print ("100\n")
            t.sleep(2)
        if i == 5:
            i = b5(5,direction)
            print ("101\n")
            t.sleep(2)
        if i == 6:
            i = b6(6,direction)
            print ("110\n")
            t.sleep(2)
        if i == 7:
            i = b7(7,direction)
            print ("111\n")
            t.sleep(2)
        if i == 8:
            i = b0(0,direction)
            print ("000\n")
            t.sleep(2)
        if i == -1:
            i = b7(7,direction)
            print ("111\n")
            t.sleep(2)

#Functions that Turns LED's on and changes the value of i according to current direction
def b0(i,direction):
    GPIO.output(4, 0)
    GPIO.output(17,0)
    GPIO.output(27,0)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b1(i,direction):
    GPIO.output(4, 1)
    GPIO.output(17,0)
    GPIO.output(27,0)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b2(i,direction):
    GPIO.output(4, 0)
    GPIO.output(17,1)
    GPIO.output(27,0)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b3(i,direction):
    GPIO.output(4, 1)
    GPIO.output(17,1)
    GPIO.output(27,0)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b4(i,direction):
    GPIO.output(4, 0)
    GPIO.output(17,0)
    GPIO.output(27,1)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b5(i,direction):
    GPIO.output(4, 1)
    GPIO.output(17,0)
    GPIO.output(27,1)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b6(i,direction):
    GPIO.output(4, 0)
    GPIO.output(17,1)
    GPIO.output(27,1)
    if direction:
        return (i+1)
    else:
        return (i-1)

def b7(i,direction):
    GPIO.output(4, 1)
    GPIO.output(17,1)
    GPIO.output(27,1)
    if direction:
        return (i+1)
    else:
        return (i-1)

if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
