import cv2 as cv
import numpy as np

def Template_matching(Template, image, threshold):
    threshold = threshold
    # Reading Template and the board image
    template = cv.imread(Template, 0)
    # Saving the width and height
    w, h = template.shape[::-1]
    image_rgb = cv.imread(image)
    # Converting to grayscale
    image_gray = cv.cvtColor(image_rgb, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(image_gray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    print("Found", len(loc[0]), "matches")
    for pt in zip(*loc[::-1]):
        cv.rectangle(image_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    # Show the final image with the matched area.
    cv.imshow('Detected', image_rgb)
    return image_rgb
    
def main():
    result_image = Template_matching("crownblur.png", r"/Users/rubenkronborg/Desktop/Universitet/2. Semester/DUAS/MP-p2-DUAS/King Domino dataset/Cropped and perspective corrected boards/1.jpg",0.5)
    cv.imshow('Detected', result_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
