 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Written by Agamveer Sansoe
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import cv2
import os
import numpy as np
import pandas as pd



# ---------------------------------------------------------------------------------------------------------------
# RUNNING A VIDEO CAPTURE
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



while True:
    # Capture frame by frame
    ret, frame = cam.read()

    # if frame is read correctly --> ret == True
    if not ret:
        print("Cannot recieve frame (stream ended?). Exiting...")
        break


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

    # Checks if white pixels are on mask and returns string if there is
    if has_blue > 0:
        print("Blue Detected\n\n\n")
    if has_red > 0:
        print("Red Detected\n\n\n")

    # cv2.inRange() reutrns a binary mask that we'll pass into the bitwise AND operator
    blue_mask_output = cv2.bitwise_and(frame,frame,mask=blue_mask)
    red_mask_output = cv2.bitwise_and(frame,frame,mask=red_mask)


    # Display resulting frame
    cv2.imshow("Blue Color Detection", blue_mask_output)
    cv2.imshow("Red Color Detection", red_mask_output)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break


# Stops video capture
cam.release()
cv2.destroyAllWindows()


# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------


# # Reading CSV file and giving names to each column
# index = ["color","color_name","hex","R","G","B"]
# csv_file = pd.read_csv("colors.csv", names=index, header=None)
# print(csv_file)

# while True:
    
#     # Capture the current frame
#     frame  = cam.read()

#     # Display current frame
#     cv2.imshow("frame", frame)

# # Importing Images Function

# # We need to filter through a folder directory to find all available images and store them into a list
# def load_images_from_folder(folder_path):
#     images = []
   
#     for filename in os.listdir(folder_path):    

#         # syntax: os.path.join(folder path, another path if needed, filename) --> needed to join a folder path and the filename 
#         # example: print(os.path.join("/Users/agam/Desktop", "transcript.txt"))
#         img = cv2.imread(os.path.join(folder_path,filename))


#         # OpenCV2 can detect JPEGs, PNGs, and TIFFs automatically, or else will return a None
#         # Detect if this img is a JPEG, PNG, or TIFF       
#         if img is not None:
#             # Store image into list
#             images.append(img)  
#         else:

#             # Alert that the file is invalid
#             print(f"{filename} is in a invalid format!")
#             continue


