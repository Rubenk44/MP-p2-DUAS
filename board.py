

class Board():
    def __init__(self, tiles = [[]]):
        self.tiles = tiles
        self.blobs = []
    
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
    
    def _get_blob(self):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                for i in range(len(self.blobs)):
                    if self.tiles[x][y] not in self.blobs[i]:
                        blob = []
                        blob.append(self.tiles[x][y])
                        terrain = self.tiles[x][y][0]
                        for adj in self._adjacent(x, y):
                            if adj[0] == terrain:
                                blob.append(adj)
                        self.blobs.append(blob)
        return self.blobs
    
    def get_score(self):
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
    blobs = board._get_blob()
    print(blobs)


if __name__ == "__main__":
    main()