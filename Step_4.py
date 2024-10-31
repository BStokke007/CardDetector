"""
This code is going to compare a list* of reference images 
and the card image that are in view of the camera in use.
All paths to an image is a relativ paths 
and not an absolute path because there are some absolute paths that are not accepted or can't be read.

Made by B.Stokke, on 31.10.2024 
"""

from skimage.metrics import structural_similarity as ssim # Library to compare two images
import cv2 as cv


# best_score is set to be the Worst score possible so that the first comparison is the best so far and can be better or stay the same.
best_score = float(0)

# The paths to the reference images for the suit of the card that are compared
suit_path = [r"OpevCV_prat\Card_Imgs\Hearts.jpg", r"OpevCV_prat\Card_Imgs\Spades.jpg", r"OpevCV_prat\Card_Imgs\Diamonds.jpg", r"OpevCV_prat\Card_Imgs\Clubs.jpg"]

# A random* image of the suits that are on the card
image = r"OpevCV_prat\Card_Imgs\Spades.jpg"

# Load the image in no colors (only in gray)
img1 = cv.imread(image, cv.IMREAD_GRAYSCALE)

# For loop that compares the image to all the reference images 
for i in range(len(suit_path)):
    # Compute SSIM between the two images 
    img2 = cv.imread(suit_path[i], cv.IMREAD_GRAYSCALE)

    # Stop the comparasion 
    if img1.shape != img2.shape: 
        wrong_img = suit_path[i]
        break

    score, diff = ssim(img1, img2, full=True) # compare the two images 

    # set best_score to the highest score 
    if score > best_score:
        best_score = score 

# Trun the Score to a  
best_score_in_procent = int(best_score * 100)


if best_score == 0: # Check if the score has changed
    print("Image {imgage} is not the same dimension as {wrong_img}")
    
elif best_score < 0.4: # Check if there's a desent Score 
    print("There is no good match, SSIM Score is:", best_score_in_procent) 

else: # if there's nothing wrong output the score
    print(f"SSIM Score: {best_score_in_procent}%")
