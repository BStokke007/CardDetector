# CardDetector

## General Informasion

On how we will do the project it make parts of the code individually
and combine the codes in to one code.

### Testing

To test the individual part of the whole there should be a reference to 
the output so that reason can do the rest.

## Problems

### Problem nr.1

There is a problem when it comes to mare than one card, when creating a window for each of the card in totall in the test.
One is a blank card (the back side of a joker) and the other ten of clubs, the left window was the ten and the right was the blank.
When removing the cards the window stay as the card was read last(lats frame detected) as they should , but when I take the ten of clubs back in frame the right window (blank window)
changes to the ten of clubs, what is left on the screen is two windows of teh same card (the ten of clubs). This dossn't only happen to the one mentioned, but can happen to anny card.


#### test

There may change later so problem doesn't happen)

### Probelm nr.2


## How to make the code?

### Step 1

Make the camera work through a python code by using OpenCV.

The camera that shall be in use on Step 1 is the camera on the PC,
but the camera that is going to be used futher is curently unknown. 
It maybe be a USB camera, PiRaspberry or something else.
In the worst case it is going to be the one on the PC.

### Step 2:

Make a program that sees if there are any cards on the table or as the program sees it rectangles. 

This is going to be done by using OpenCV.
This can be done by bluring, graying and shresholding combined 
so that the pixels that are left are only in black and white.


### Step 3:

After the code sees the card it shall store the image and compare it 
with the other stored reference images of the other cards. 

To compare the reference image and the card on the table. 

The reference images are just images of the numbers and suts in the corner of the card in black and white!

### Step 4:



### Step 5:

A Camera shall be placed on the edge of the table so that the UR5 is on.
The Camera that i shall use in the main camera on my PC to see the cards on the table.
The Camera should see the table witch is where the playing cards are going to be placed on.

### Set 6:




