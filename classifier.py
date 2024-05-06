import cv2 as cv
import os
import pandas as pd
import numpy as np

def main():
    for _, dirs, _ in os.walk("trainset"):
        for dir in dirs:
            tiles = []  # Move the tiles list outside of the innermost loop
            for _, _, files in os.walk(f"trainset/{dir}"):
                for file in files:
                    tile = cv.imread(f"trainset/{dir}/{file}")
                    tile = np.ravel(tile)
                    tiles.append(dir)
                    tiles.append(tile)
            train = pd.DataFrame(tiles)
            print(train)
    train.to_csv("train.csv", index=False)
            
    
                    

if __name__ == "__main__":
    main()