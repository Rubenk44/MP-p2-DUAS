

class Board():
    def __init__(self, tiles = [[]]):
        self.tiles = tiles
        self.blobs = []
        """
        Tiles (for a single board) will look like this:
        tiles = [
            [tile1, tile2, tile3, tile4, tile5],
            [tile6, tile7, tile8, tile9, tile10],
            [tile11, tile12, tile13, tile14, tile15],
            [tile16, tile17, tile18, tile19, tile20],
            [tile21, tile22, tile23, tile24, tile25]            
        ]
        """
    
    def _adjacent(self, x, y):
        """
        gets adjacent tiles (diagonals not included)
        """
        adjacent = []
        if x+1 < len(self.tiles):
            adjacent.append(self.tiles[x+1][y])
        if x-1 >= 0:
            adjacent.append(self.tiles[x-1][y])
        if y+1 < len(self.tiles[x]):
            adjacent.append(self.tiles[x][y+1])
        if y-1 >= 0:
            adjacent.append(self.tiles[x][y-1])
        return adjacent
    
    def blob(self):
        pass
    
def main():
    tiles = [
        [("Plains", 0), ("Plains", 0), ("Plains", 0), ("Plains", 0), ("Forest", 0)],
        [("Ocean", 0), ("Forest", 0), ("Swamp", 1), ("Plains", 2), ("Ocean", 1)],
        [("Forest", 0), ("Forest", 0), ("Home", 0), ("Ocean", 0), ("Ocean", 0)],
        [("Forest", 0), ("Forest", 1), ("Forest", 1), ("Plains", 2), ("Plains", 1)],
        [("Forest", 0), ("Plains", 0), ("Plains", 0), ("Plains", 1), ("Desert", 0)]
    ]

    # print(tiles)
    board = Board(tiles=tiles)
    adjacent = board._adjacent(2,2)
    print(adjacent)

if __name__ == "__main__":
    main()