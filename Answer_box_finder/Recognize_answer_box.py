import cv2
import numpy as np

# Reads the image and converts it to grayscale
img =  cv2.imread('Test_Case_1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgHeight, imgWidth = img.shape[0:2]

# Uses adaptive thresholding to turn image into a binary image
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow("threshold", threshold)
# Finds and fills contours
contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

validBoxes = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # Only look for rectangles above a certain size to avoid small errors
    if w*h > 100:
        # Get the bounding rect
        validBoxes.append((x,y,w,h))

# Was supposed to compare contours to the contents of contours. If they matched, they would be classified as a rectangle. However, never got to this
# In hindsight, this is where we should've turned to ML, and found rectangles by comparing contours to what should be the contour of a rectangle

croppedBoxes = []
if(len(validBoxes) == 0):
    # throw exception, no boxes found
    errorStatus = -1
else:
    # crop images and return section of images bounded by rectangles
    for x, y, w, h in validBoxes:
        croppedBoxes.append(img[y:y+h, x:x+w])

# return croppedBoxes
    


cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Helper functions for quick copy/paste
Shows Images:
cv2.imshow("boxes", mask)

Thresholding:
cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
'''