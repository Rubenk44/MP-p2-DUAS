import cv2 as cv
import numpy as np
import os

def Template_matching(Template_folder, img_bgr, threshold=0.749, iou_threshold=0.2):
    crownbox = []

    for file_name in Template_folder:
        template_path = os.path.join(r"Templates", file_name)
        template = cv.imread(template_path)

        for rotation in range(4):
            template = np.rot90(template, rotation)
            h, w, _ = template.shape
            res = cv.matchTemplate(img_bgr, template, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= threshold)
            
        
            for pts in zip(*loc[::-1]):
                unions = []
                newbox = [pts[0], pts[1], pts[0] + w, pts[1] + h]

                if crownbox == []: 
                    crownbox.append(newbox)
                    cv.rectangle(img_bgr, pts, (pts[0] + w, pts[1] + h), (0,255,255), 2)
                    print(template_path)
                    print(newbox)

                for box in crownbox: 
                    xA = max(box[0], newbox[0])
                    yA = max(box[1], newbox[1])
                    xB = min(box[2], newbox[2])
                    yB = min(box[3], newbox[3])

                    # compute the area of intersection rectangle
                    interArea = (xB - xA) * (yB - yA)

                    # compute the area of both the prediction and ground-truth
                    # rectangles
                    boxAArea = (box[2] - box[0]) * (box[3] - box[1])
                    boxBArea = (newbox[2] - newbox[0]) * (newbox[3] - newbox[1])

                    # compute the intersection over union by taking the intersection
                    # area and dividing it by the sum of prediction + ground-truth
                    # areas - the interesection area
                    iou = interArea / float(boxAArea + boxBArea - interArea)
                    unions.append(iou)
                
                if all(iou < iou_threshold for iou in unions):
                    crownbox.append(newbox)
                    cv.rectangle(img_bgr, pts, (pts[0] + w, pts[1] + h), (0,255,255), 2)
                    print(template_path)
                    print(newbox)
    # print(crownbox)
    return (crownbox, len(crownbox))
               
                
                

def main():
    img_rgb = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/6.jpg")
    threshold = 0.749
    template_folder = os.listdir(r"Templates") 
    iou_threshold = 0.2
    result_image = Template_matching(template_folder, img_rgb, threshold, iou_threshold)
    cv.imshow('Detected', img_rgb)
    print(result_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()