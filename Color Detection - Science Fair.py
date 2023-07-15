# ---------------------------------------------------------------------------------------------------------------
# IMPORTING LIBRARIES
# ---------------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import pandas as pd
import time

# ---------------------------------------------------------------------------------------------------------------
# STARTING/CHECKING VIDEO CAPTURE
# ---------------------------------------------------------------------------------------------------------------

# Capture video feed into an object
# Syntax: cv2.VideoCapture(number to specify which camara.. usually one camara which is 0)
cam = cv2.VideoCapture(0)

# Check if camara is open
if not cam.isOpened():  
    print("Camara cannot open.. trying to turn on.")
    cam.open()
    if cam.isOpened() == True:
        print("Successful!")
    else:
        print("Unsuccessful (camara off?)")
        exit()
# ---------------------------------------------------------------------------------------------------------------
# MASKING A VIDEO CAPTURE TO DETECT COLORS
# ---------------------------------------------------------------------------------------------------------------

# Count variables
blue_count = 0
red_count = 0


# Initializes variable with current time minus six secends
# Ensures first detection will happen immediatly when code starts
time_function_done = time.time()-6


# System on (DON'T change)
sysOn = True


while sysOn:
    # Capture frame by frame
    ret, frame = cam.read()

    # if frame is read correctly --> ret == True
    if not ret:
        print("Cannot recieve frame (stream ended?). Exiting...")
        sysOn = False


    # Convert colorspace of video capture
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    # Assign lower and upper blue color variables
    # syntax: boudaries = (upper [R,B,G], lower [R,B,G])
    # Blue color values: 120 255 255
    light_blue = np.array([110,100,100])
    dark_blue = np.array([130,255,255])

    # Assign lower and upper red color variables
    # Red color values: 0 255 255
    light_red = np.array([-10, 100, 100])
    dark_red =  np.array([10, 255, 255])

    # Set color range
    # Syntax: (Accepts three parameters) cv2.inRange(input image, lower color boundray, upper color boundary)
    # Threshold HSV image to only get blue colors
    blue_mask = cv2.inRange(hsv,light_blue,dark_blue)
    red_mask = cv2.inRange(hsv,light_red,dark_red)


    # if there are any white pixels on mask, sum will be > 0
    has_blue = np.sum(blue_mask)

    has_red = np.sum(red_mask)
    

    # Checks if current time is greater then time_function_done (elapsed time)
    # time_function_done needs to be greater then the local time (time.time()) in order for statement to run
    # Runs color detection every 5 seconds
    if (time_function_done + 5) < time.time():

        # Sets variable with current time
        time_function_done = time.time()
        
        # Checks if white pixels are on mask and returns string if there is
        if has_blue > 0:
            print(f"Blue #{blue_count+1} Detected \n\n\n")
            blue_count += 1
        
        if has_red > 0:
            print(f"Red #{red_count+1} Detected\n\n\n")
            red_count += 1
            
        # else:
        #     print("No color is detected")


    # cv2.inRange() reutrns a binary mask that we'll pass into the bitwise AND operator
    # cv2.bitwise_and() creates a mask output that can be displayed afterwards
    blue_mask_output = cv2.bitwise_and(frame,frame,mask=blue_mask)
    red_mask_output = cv2.bitwise_and(frame,frame,mask=red_mask)


    # Display resulting frame
    cv2.imshow("Blue Color Detection", blue_mask_output)
    cv2.imshow("Red Color Detection", red_mask_output)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        sysOn = False


# Stops video capture
cam.release()
cv2.destroyAllWindows()

print(f"""
Video Capture has been stopped.
Blue count = {blue_count}
Red count = {red_count}
""")


