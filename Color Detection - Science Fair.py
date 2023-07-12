 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Written by Agamveer Singh Sansoe
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import cv2
import os
import numpy as np


# Capture video feed into an object
cam = cv2.VideoCapture(0)

# Display current frame of feed


# Importing Images Function

# We need to filter through a folder directory to find all available images and store them into a list
def load_images_from_folder(folder_path):
    images = []
   
    for filename in os.listdir(folder_path):    

        # syntax: os.path.join(folder path, another path if needed, filename) --> needed to join a folder path and the filename 
        # example: print(os.path.join("/Users/agam/Desktop", "transcript.txt"))
        img = cv2.imread(os.path.join(folder_path,filename))


        # OpenCV2 can detect JPEGs, PNGs, and TIFFs automatically, or else will return a None
        # Detect if this img is a JPEG, PNG, or TIFF       
        if img is not None:
            # Store image into list
            images.append(img)  
        else:

            # Alert that the file is invalid
            print(f"{filename} is in a invalid format!")
            continue


