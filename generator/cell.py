class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False
