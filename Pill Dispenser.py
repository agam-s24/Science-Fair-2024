import RPi.GPIO as GPIO
import time
import sys
import os



# what buttons will be put in the pill dispenser
# Make every button a function --> when button is pressed, function is called
# everything happens in a while loop (while [sysRunning is true], check for signal of this button [if signal is found, execute function])

# Code a “start “ button to start dispensing process. Turn stepper motor and slow speed (in a certain direction) to slowly drop the dispenser. If motion sensor detects something, turn stepper motor fast at opposite direction (to make the dispenser go up) with certain calculated delay. Variable “x” repeat process. (Variable x determined by input)



# When this program starts, system is already running
sysRunning = True

# Button assignment
poweroff_button_Pin = 17

# SETTING UP 

# set up GPIO button
def setup():
    # set mode
    GPIO.setmode(GPIO.BCM)

    #set up pins
    GPIO.setup(poweroff_button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def poweroff_button_signal():
    inputState = GPIO.input(poweroff_button_Pin)
    if inputState == GPIO.LOW:
        return True
    elif inputState == GPIO.HIGH:
        return False
    else:
        print("unable to detect input on " + poweroff_button_Pin)
        return None

# FUNCTIONS (BUTTONS)

def poweroff():
    print("powering off.. ") # PLACEHOLDER ACTION. Replace with actual powering off code
    sys.exit() # stop program
    
def start():    
    pass

# Initlizae GPIO


while sysRunning:
    if poweroff_button_Pin() == True:
        poweroff()

    # avoid high CPU 
    time.sleep(0.1)
    