import warnings
warnings.filterwarnings("ignore")
import cv2 as cv
import os
from board import Board
from joblib import load

from TM import Template_matching

def get_tiles(image):
    # creates an empty array to store the tiles
    tiles = []
    # iterates over the image in 5 by 5 blocks
    for i in range(5):
        for j in range(5):
            # appends the tile to the array by slicing the image into 100x100 blocks (tiles)
            tiles.append(image[100*i:100*(i+1), 100*j:100*(j+1)])
    # returns the array of tiles for the game
    return tiles

# defined ground truth of scores for the games
scores = {"1.jpg":"36","2.jpg":"43","3.jpg":"52","4.jpg":"42","5.jpg":"36","6.jpg":"43",
          "7.jpg":"52","8.jpg":"42","9.jpg":"36","10.jpg":"38","11.jpg":"49","12.jpg":"22",
          "13.jpg":"45","14.jpg":"38","15.jpg":"49","16.jpg":"22","17.jpg":"40","18.jpg":"60",
          "19.jpg":"36","20.jpg":"53","21.jpg":"40","22.jpg":"60","23.jpg":"36","24.jpg":"53",
          "25.jpg":"44","26.jpg":"48","27.jpg":"67","28.jpg":"65","29.jpg":"44","30.jpg":"48",
          "31.jpg":"67","32.jpg":"65","33.jpg":"21","34.jpg":"36","35.jpg":"46","36.jpg":"51",
          "37.jpg":"21","38.jpg":"36","39.jpg":"46","40.jpg":"51","41.jpg":"33","42.jpg":"43",
          "43.jpg":"66","44.jpg":"33","45.jpg":"38","46.jpg":"43","47.jpg":"66","48.jpg":"42",
          "49.jpg":"26","50.jpg":"34","51.jpg":"37","52.jpg":"42","53.jpg":"26","54.jpg":"34",
          "55.jpg":"37","56.jpg":"44","57.jpg":"64","58.jpg":"34","59.jpg":"38","60.jpg":"44",
          "61.jpg":"64","62.jpg":"34","63.jpg":"38","64.jpg":"64","65.jpg":"80","66.jpg":"124",
          "67.jpg":"99","68.jpg":"66","69.jpg":"124","70.jpg":"90","71.jpg":"66","72.jpg":"80",
          "73.jpg":"124","74.jpg":"99","75.jpg":"","76.jpg":"","77.jpg":"","78.jpg":"",
          "79.jpg":"","80.jpg":"","81.jpg":"","82.jpg":"","83.jpg":"","84.jpg":"",
          "85.jpg":"","86.jpg":"","87.jpg":"","88.jpg":"","89.jpg":"","90.jpg":"",
          "91.jpg":"","92.jpg":"","93.jpg":""}

def main():
    # loads the model (RFC)
    model = load("model.joblib")
    # iterates over the files in the directory
    for _, _, files in os.walk(r"King Domino dataset\Cropped and perspective corrected boards"):
        # iterates over each file in the directory
        for file in files:
            # checks if the file is above 59, as the first 59 images are the training set
            if int(file.split(".")[0]) > 59:
                # checks file index
                print(file)
                # loads the full game
                game = cv.imread(f"King Domino dataset/Cropped and perspective corrected boards/{file}")
                # gets the tiles of the game
                tiles = get_tiles(game)
                # creates a board object for handling the game
                board = Board()
                # iterates over the tiles with num for board position
                for num, tile in enumerate(tiles):
                    # template matches the tile to get the crowns
                    crowns = Template_matching(os.listdir(r"Templates"), tile)
                    # resizes the tile to 25x25 and flattens it to match training format
                    tile = cv.resize(tile, (25, 25))
                    tile = tile.flatten()
                    # predicts the terrain of the tile
                    terrain = model.predict([tile])[0]
                    # calculates the x and y position of the tile. the % operation is used to get the x position (vertical) 
                    # and the // operation is used to get the y position (horizontal)
                    x = num % 5
                    y = num // 5
                    # adds the tile to the board object
                    board.add_tile((terrain, crowns), x, y)
                # prints the calculated score and the actual score
                print("Calculated score: " + str(board.get_score()))
                print("Actual score: " + scores[file])
            # if the file is below 59, it is a training image
            else:
                # therefore, it is skipped
                continue
            
if __name__ == "__main__":
    main()