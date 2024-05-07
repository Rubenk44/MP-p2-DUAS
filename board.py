class Board():
    def __init__(self, tiles = [[]]):
        self.tiles = tiles
        self.blobs = []
    
    def _adjacent(self, x, y):
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

    def _get_blob(self):
        blobs = []
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                pass

    
    def get_score(self):
        """
        Returns the score of the king domino board
        """
        blobs = self._get_blob()
        score = 0
        for blob in blobs:
            score += len(blob)
        return score
    
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
    print(board._get_blob())
    # board.get_score()



if __name__ == "__main__":
    main()