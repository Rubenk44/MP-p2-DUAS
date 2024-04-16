

class board():
    def __init__(self, tiles = {}):
        self.tiles = tiles

        """
        Tiles (for a single board) will look like this:
        tiles = {
            "[x1,y1]": "([tile terrain], bool(crown))", 
            "[x2,y1]": "([tile terrain], bool(crown))", 
            "[x3,y1]": "([tile terrain], bool(crown))", 
            "[x4,y1]": "([tile terrain], bool(crown))", 
            "[x5,y1]": "([tile terrain], bool(crown)",
            ...
            "[x1,y5]": "([tile terrain], bool(crown))",
            "[x2,y5]": "([tile terrain], bool(crown))",
            "[x3,y5]": "([tile terrain], bool(crown))",
            "[x4,y5]": "([tile terrain], bool(crown))",
            "[x5,y5]": "([tile terrain], bool(crown))"
        }
        """
    
    def cal_score(self):
        """
        for every blob, the number of crowns is multiplied by the number of tiles in the blob
        """
        score = 0

        return score

    def __adjacent__(self, x, y):
        """
        gets adjacent tiles (diagonals not included)
        """
        return []