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
                    tile = np.ravel(tile, order='C')
                    tiles.append(tile)
            dir = pd.DataFrame(tiles)
            print(dir)
            
    
                    

if __name__ == "__main__":
    main()