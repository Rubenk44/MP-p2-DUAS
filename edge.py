import cv2


img_test = cv2.imread('King Domino dataset\\Cropped and perspective corrected boards\\6.jpg')
img_hsv = cv2.cvtColor(img_test, cv2.COLOR_BGR2HSV)

#Blur image. Det gør allegedly edge detection bedre
img_blur = cv2.GaussianBlur(img_hsv,(3,3), sigmaX=0, sigmaY=0)

_,_,v = cv2.split(img_hsv)

#Edging sobels
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
cv2.imshow("Blur", img_blur)
cv2.waitKey(0)
"""
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
 
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
 
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
"""

# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)

def edgeDetection(image):
    pass