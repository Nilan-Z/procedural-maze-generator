class Cell:
    def __init__(self, x: int, y: int):
        '''Initialize a Cell instance.'''
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]
        self.visited = False
