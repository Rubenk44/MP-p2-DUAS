import cv2 as cv
import numpy as np
import os

def Template_matching(Template_folder, image, threshold):
    img_rgb = cv.imread(image)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    for file_name in Template_folder:
        template_path = os.path.join(r"/Users/rubenkronborg/Desktop/Templates", file_name)
        template = cv.imread(template_path, cv.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]

        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

    return img_rgb


def main():
    template_folder = os.listdir(r"/Users/rubenkronborg/Desktop/Templates") 
    result_image = Template_matching(template_folder, r"King Domino dataset/Cropped and perspective corrected boards/25.jpg", 0.7)
    cv.imshow('Detected', result_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
