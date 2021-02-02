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

#Seting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT , initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i = 0
   
#Call back functions for if buttons are pressed. These set the direction of the press
def buttonup(self):
    global i
    i = i + 1
    displayi(i)

def buttondown(self):
    global i
    i = i - 1
    displayi(i)
    
#to avoid code redundancy here is the function to identify which binary value must be displayed
def displayi(n):
    global i
    if n == 0:
        b0()
    if n == 1:
        b1()
    if n == 2:
        b2()
    if n == 3:
        b3()
    if n == 4:
        b4()
    if n == 5:
        b5()
    if n == 6:
        b6()
    if n == 7:
        b7()
    if n == 8:
        i = 0
        b0()
    if n == -1:
        i = 7
        b7()

#There functions are called from displayi() function and they set the outputs of the GPIO Pins
def b0():
    GPIO.output(4, 0)
    GPIO.output(17,0)
    GPIO.output(27,0)

def b1():
    GPIO.output(4, 1)
    GPIO.output(17,0)
    GPIO.output(27,0)

def b2():
    GPIO.output(4, 0)
    GPIO.output(17,1)
    GPIO.output(27,0)

def b3():
    GPIO.output(4, 1)
    GPIO.output(17,1)
    GPIO.output(27,0)

def b4():
    GPIO.output(4, 0)
    GPIO.output(17,0)
    GPIO.output(27,1)

def b5():
    GPIO.output(4, 1)
    GPIO.output(17,0)
    GPIO.output(27,1)

def b6():
    GPIO.output(4, 0)
    GPIO.output(17,1)
    GPIO.output(27,1)

def b7():
    GPIO.output(4, 1)
    GPIO.output(17,1)
    GPIO.output(27,1)

#Indefinite loop
def main ():
    while True : pass;

#Code to initialize interrupts using the 2nd thread (for button presses)
GPIO.add_event_detect(19, GPIO.RISING, callback=buttonup, bouncetime=200)
GPIO.add_event_detect(26, GPIO.RISING, callback=buttondown, bouncetime=200)

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
