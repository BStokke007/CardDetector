"""
This code is going to resize an image so that it can be campared later.
There is a image witch has the correct dimensions and can be compared visually

To resize to the correct size you must add the width and the height separately 
All the refference images must be the same size and dimensions.

Made by Vincent on 24.10.2024
"""

import cv2 as cv

# A random* image that are going to be resized
img2 = cv.imread("OpevCV_prat\Card_Imgs\Clubs.jpg")
cv.imshow("Visuel Check", img2)

# Get images from the directory "Photos/tanjiro.jpg", and define it as img
img = cv.imread(r"OpevCV_prat\Photos\cat.jpg")
cv.imshow('Orginal image', img) # put the picture in a window named "Tanjiro"

#Function to rescale the frame of the window
def rescaleFrame(image, scale=0.75): 
    width = int(image.shape[1]*0 + 70) # When frame.shape is 1 we refer to the width
    height = int(image.shape[0]*0 + 125) # When frame.shape is 0 we refer to the height

    dimensions = (width,height) # Define it as dimensions

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img) # The new image is now called resized_image
cv.imshow("image", resized_image) # show the resized image
cv.waitKey(0) # wait for a key to be pressed 
