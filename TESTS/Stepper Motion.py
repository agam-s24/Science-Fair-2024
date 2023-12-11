#!/usr/bin/python3

# OBJECTIVE: biild a program that will sense motion and turn on and move motors simontainously (mutiple)
# Must use BCD formatting because of driver board of motor

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO. Try to run sudo to run your script")
import time


# GPIO NUMBER = 16 --> BCM = 23
sensor = 23


# Motor wiring --> BCM
in1 = 17 # GPIO: 11
in2 = 18 # GPIO: 12
in3 = 27 # GPIO: 13
in4 = 22 # GPIO: 15
# change buzzer to motor --> sensor will sense moveoment or certain thing and move motor s

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°

direction = False # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
# sequence is in an anti-clockwise motion
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]



# Intilzating mode
GPIO.setmode(GPIO.BCM)

# setting up inputs/outputs
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(in1,GPIO.OUT) 
GPIO.setup(in2,GPIO.OUT) 
GPIO.setup(in3,GPIO.OUT) 
GPIO.setup(in4,GPIO.OUT) 



GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
print("IR Sensor Ready.....")
print(" ")

# able to include other sets of motor pins 
# this set makes up one motor
motor_pins_set_1= [in1,in2,in3,in4]
motor_step_counter = 0 

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()

try: 
    while True:
        if GPIO.input(sensor):
            for i in range(step_count):

                # Motor pin set 1 here (replicate for in statement for other motor pin sets)
                for pin in range(0, len(motor_pins_set_1)):
                    GPIO.output( motor_pins_set_1[pin], step_sequence[motor_step_counter][pin] )
                    print("Object Detected")

                    while GPIO.input(sensor):
                        time.sleep(0.2)
                if direction==True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                elif direction==False:
                    motor_step_counter = (motor_step_counter + 1) % 8
                else: # defensive programming
                    print( "uh oh... direction should *always* be either True or False" )
                    cleanup()
                    exit( 1 )
                time.sleep( step_sleep )
        else:
          # mot sure if this works
          GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    exit(1)

cleanup()
exit(0)