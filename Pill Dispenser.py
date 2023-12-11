import RPi.GPIO as GPIO
import time
import sys
import os



# what buttons will be put in the pill dispenser
# Make every button a function --> when button is pressed, function is called
# everything happens in a while loop (while [sysRunning is true], check for signal of this button [if signal is found, execute function])





# When this program starts, system is already running
sysRunning = True

# Button assignment
buttonPin = 17

# SETTING UP 

# set up GPIO button
def setup():
    # set mode
    GPIO.setmode(GPIO.BCM)

    #set up pins
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonSignal():
    inputState = GPIO.input(buttonPin)
    if inputState == GPIO.LOW:
        return True
    elif inputState == GPIO.HIGH:
        return False
    else:
        print("unable to detect input on " + buttonPin)
        return None

# FUNCTIONS (BUTTONS)

def poweroff():
    print("powering off.. ") # PLACEHOLDER ACTION. Replace with actual powering off code
    sys.exit() # stop program
    

# Initlizae GPIO


while sysRunning:
    if buttonSignal() == True:
        poweroff()

    # avoid high CPU 
    time.sleep(0.1)
    