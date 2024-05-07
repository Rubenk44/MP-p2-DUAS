import numpy as np
import pandas as pd
import os
import cv2 as cv
from Main import get_tiles

def train():
    df = pd.DataFrame(columns=["tile", "terrain"])
    # iterate over the images for each terrain type folder in 'trainset' and append the flattened tile and terrain type to the dataframe
    for terrain in os.listdir("trainset"):
        for file in os.listdir(f"trainset/{terrain}"):
            image = cv.imread(f"trainset/{terrain}/{file}")
            image = cv.resize(image, (100, 100))
            tile = []
            for i in range(len(image.flatten())):
                tile.append(image.flatten()[i])
            image = pd.Series(data=(tile, terrain), index=["tile", "terrain"])
            df = df._append(image, ignore_index=True)
    # save the dataframe to a csv file
    df.to_csv("trainset.csv", index=False)

if __name__ == "__main__":
    train()