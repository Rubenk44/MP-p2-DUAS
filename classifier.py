import cv2 as cv
import os
import pandas as pd
import numpy as np

def flatten(img):
    # Flatten the image
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (100, 100))
    img = img.flatten()
    return img

def main():
    for _, dirs, _ in os.walk("trainset"):
        for dir in dirs:
            print(dir)
            tiles = []  # Move the tiles list outside of the innermost loop
            for _, _, files in os.walk(f"trainset/{dir}"):
                for file in files:
                    tile = cv.imread(f"trainset/{dir}/{file}")
                    print(tile)
                    tile = flatten(tile)
                    tiles.append(tile)
            # for each dir create a dataframe
            df = pd.DataFrame(tiles)
            df.to_csv(f"{dir}.csv", index=False)
    # train.to_csv("train.csv", index=False)

if __name__ == "__main__":
    main()