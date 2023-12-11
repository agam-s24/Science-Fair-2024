import RPi.GPIO as GPIO
import time

# Define GPIO pins for Step, Dir, and Enable
STEP_PIN = 11
DIR_PIN = 12
ENABLE_PIN = 22  # Optional, connect to the Enable pin on the A4988 if used

# Set up GPIO mode and configure pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable the stepper motor (if Enable pin is used)
GPIO.output(ENABLE_PIN, GPIO.LOW)

# Set the direction (CW or CCW)
GPIO.output(DIR_PIN, GPIO.HIGH)  # Set to GPIO.HIGH for clockwise rotation, GPIO.LOW for counterclockwise

# Function to move the stepper motor
def move_stepper(steps, delay):
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

# Set the number of steps and delay between steps
num_steps = 200  # Adjust based on your motor's specifications
delay = 0.001    # Adjust based on your motor's specifications

# Move the stepper motor
try:
    move_stepper(num_steps, delay)

except KeyboardInterrupt:
    print("Program terminated by user")

finally:
    # Disable the stepper motor and clean up GPIO
    GPIO.output(ENABLE_PIN, GPIO.HIGH)
    GPIO.cleanup()