class Board():
    def __init__(self, tiles=[[]]):
        self.tiles = [
            [("None", 0), ("None", 0), ("None", 0), ("None", 0), ("None", 0)],
            [("None", 0), ("None", 0), ("None", 0), ("None", 0), ("None", 0)],
            [("None", 0), ("None", 0), ("None", 0), ("None", 0), ("None", 0)],
            [("None", 0), ("None", 0), ("None", 0), ("None", 0), ("None", 0)],
            [("None", 0), ("None", 0), ("None", 0), ("None", 0), ("None", 0)]
        ]
        self.blobs = []

    def add_tile(self, tile, x, y):
        """
        Adds a tile to the board at the specified position. The tile is a tuple (terrain, crowns)
        """
        # sets the tile (terrain, crowns) at the specified position
        self.tiles[x][y] = tile

    def _adjacent(self, x, y):
        """
        Returns a list of adjacent tiles
        """
        # initializes the adjacent list
        adjacent = []
        # checks if the tile is within the board
        if x + 1 < len(self.tiles):
            # appends the tile to the adjacent list if it is within the board
            adjacent.append((x + 1, y))
        # repeats the process for the other directions
        if x - 1 >= 0:
            adjacent.append((x - 1, y))
        if y + 1 < len(self.tiles[x]):
            adjacent.append((x, y + 1))
        if y - 1 >= 0:
            adjacent.append((x, y - 1))
        return adjacent

    def _get_area(self, x, y, visited):
        """
        Returns the area of the connected tiles starting from the specified position
        """
        # checks if the tile has been visited
        if (x, y) in visited:
            # returns an empty list and 0 if the tile has been visited
            return [], 0
        # sets the terrain and crowns of the tile at the specified position
        terrain, crowns = self.tiles[x][y]
        # returns an empty list and 0 if the terrain is "None"
        if terrain == "None":
            return [], 0
        # marks the tile as visited
        visited.add((x, y))
        # initializes the area and crowns of the connected tiles
        area = [(x, y)]
        # sets the area crowns to the crowns of the tile
        area_crowns = crowns
        # iterates over the adjacent tiles
        for nx, ny in self._adjacent(x, y):
            # checks if the adjacent tile has the same terrain
            if self.tiles[nx][ny][0] == terrain:
                # gets the area and crowns of the adjacent tile
                sub_area, sub_crowns = self._get_area(nx, ny, visited)
                area.extend(sub_area)
                area_crowns += sub_crowns
        return area, area_crowns

    def get_score(self):
        """
        Returns the score of the board
        """
        # sets initial score to 0
        score = 0
        # initializes visited set. Set is used because duplicate tiles are not allowed
        visited = set()
        # iterates over the tiles
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                # 
                area, area_crowns = self._get_area(x, y, visited)
                if area:
                    terrain, _ = self.tiles[x][y]
                    score += len(area) * area_crowns
                    visited.update(area)
        return score

def main():
    tiles = [
        [("Plains", 0), ("Plains", 0), ("Plains", 0), ("Plains", 0), ("Forest", 0)],
        [("Ocean", 0), ("Forest", 0), ("Swamp", 1), ("Plains", 2), ("Ocean", 1)],
        [("Forest", 0), ("Forest", 0), ("Home", 0), ("Ocean", 0), ("Ocean", 0)],
        [("Forest", 0), ("Forest", 1), ("Forest", 1), ("Plains", 2), ("Plains", 1)],
        [("Forest", 0), ("Plains", 0), ("Plains", 0), ("Plains", 1), ("Desert", 0)]
    ]

    board = Board(tiles=tiles)
    print(board.get_score())

if __name__ == "__main__":
    main()