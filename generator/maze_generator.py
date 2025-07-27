from generator.cell import Cell
import random
class MazeGenerator():
    def __init__(self):
        pass

    def generateMaze(self, width, height):
        """Generates a maze of given width and height.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.

        Returns:
            list[Cell]: A flat list of Cell objects representing the maze.
        """
        self.width = width
        self.height = height
        self.maze = [Cell(x, y) for y in range(height) for x in range(width)]
        self.initialize_maze()
        return self.maze
    
    def initialize_maze(self):
        initial_cell = random.choice(self.maze)
        initial_cell.visited = True
        self.display_maze()
        self.propagate(initial_cell)
    
    def propagate(self, cell):
        not_visited_neighbors = self.get_not_visited_neighbors(cell)
        ''' Future logic to handle propagation
        if not not_visited_neighbors:
            pass #Add logic to handle when there are no unvisited neighbors
        random_not_visited_neighbors = random.choice(not_visited_neighbors) 
        if random_not_visited_neighbors.x == cell.x - self.width:
            cell.wall[1] = False  # Remove wall to the top
        '''

            
    
    def get_not_visited_neighbors(self, cell):
        """Returns a list of neighboring cells that have not been visited.

        Args:
            cell (Cell): The current cell.

        Returns:
            list[Cell]: A list of neighboring cells that have not been visited.
        """
        neighbors = []

        # Helper to get cell by coordinates, returns None if out of bounds
        def get_cell(x, y):
            if 0 <= x < self.width and 0 <= y < self.height:
                return self.maze[y * self.width + x]
            return None

        # Check left neighbor
        left = get_cell(cell.x - 1, cell.y)
        if left and not left.visited:
            neighbors.append(left)

        # Check right neighbor
        right = get_cell(cell.x + 1, cell.y)
        if right and not right.visited:
            neighbors.append(right)

        # Check top neighbor
        top = get_cell(cell.x, cell.y - 1)
        if top and not top.visited:
            neighbors.append(top)

        # Check bottom neighbor
        bottom = get_cell(cell.x, cell.y + 1)
        if bottom and not bottom.visited:
            neighbors.append(bottom)

        return neighbors
    
    def display_maze(self):
        """Displays the maze in a simple text format."""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                cell = self.maze[y * self.width + x]
                row += " " if not cell.walls[0] else "#"
            print(row)
        print()
    