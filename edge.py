import cv2


img_test = cv2.imread('King Domino dataset\\Cropped and perspective corrected boards\\6.jpg')
#Blur image. Det gør allegedly edge detection bedre
img_blur = cv2.GaussianBlur(img_test,(3,3), SigmaX=0, SigmaY=0)

cv2.imshow("Original", img_blur)
cv2.waitKey(0)

def edgeDetection(image):
    pass