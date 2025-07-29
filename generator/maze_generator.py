from generator.cell import Cell
import random

class MazeGenerator:
    """
    A class for generating a 2D maze using randomized propagation.

    Attributes:
        visited_cells (list): List of cells that have been visited.
        width (int): Width of the maze.
        height (int): Height of the maze.
        maze (list[Cell]): A flat list of Cell objects representing the maze.
    """

    def __init__(self):
        """
        Initializes an empty maze with default dimensions and empty visited cells list.
        """
        self.visited_cells = []
        self.width = 0
        self.height = 0
        self.maze = []

    def generateMaze(self, width, height):
        """
        Generates a maze with the given width and height.

        Args:
            width (int): Number of cells in the horizontal direction.
            height (int): Number of cells in the vertical direction.

        Returns:
            list[Cell]: A flat list of Cell objects forming the complete maze.
        """
        self.width = width
        self.height = height
        self.maze = [Cell(x, y) for y in range(height) for x in range(width)]
        self.visited_cells = []  # Reset visited cells
        self.initialize_maze()
        self.add_entrance_exit()
        return self.maze

    def initialize_maze(self):
        """
        Initializes the maze by selecting a random starting cell, 
        then uses randomized propagation and backtracking to generate the maze.
        """
        initial_cell = random.choice(self.maze)
        initial_cell.visited = True
        self.visited_cells.append(initial_cell)

        current_cell = initial_cell
        while len(self.visited_cells) < len(self.maze):
            new_cell = self.propagate(current_cell)
            if new_cell is not None:
                current_cell = new_cell
            else:
                # Backtrack to a previous visited cell with unvisited neighbors
                backtracked = self.find_backtrack_cell()
                if backtracked:
                    current_cell = backtracked
                else:
                    break  # Should not happen unless maze is complete


    def propagate(self, cell):
        """
        Chooses a random unvisited neighbor, removes the wall between it and the current cell, 
        and marks it as visited.

        Args:
            cell (Cell): The current cell from which to propagate.

        Returns:
            Cell | None: The newly visited neighbor, or None if no unvisited neighbors exist.
        """
        not_visited_neighbors = self.get_not_visited_neighbors(cell)
        if not not_visited_neighbors:
            return None  # No unvisited neighbors, need to backtrack

        random_neighbor = random.choice(not_visited_neighbors)
        random_neighbor.visited = True
        self.visited_cells.append(random_neighbor)

        dx = random_neighbor.x - cell.x
        dy = random_neighbor.y - cell.y

        # Remove walls between current cell and neighbor
        if dx == -1:
            cell.walls[3] = False
            random_neighbor.walls[1] = False
        elif dx == 1:
            cell.walls[1] = False
            random_neighbor.walls[3] = False
        elif dy == -1:
            cell.walls[0] = False
            random_neighbor.walls[2] = False
        elif dy == 1:
            cell.walls[2] = False
            random_neighbor.walls[0] = False

        return random_neighbor

    def get_not_visited_neighbors(self, cell):
        """
        Finds neighboring cells that have not yet been visited.

        Args:
            cell (Cell): The current cell to check from.

        Returns:
            list[Cell]: List of unvisited neighboring Cell objects.
        """
        neighbors = []

        def get_cell(x, y):
            if 0 <= x < self.width and 0 <= y < self.height:
                return self.maze[y * self.width + x]
            return None

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            neighbor = get_cell(cell.x + dx, cell.y + dy)
            if neighbor and not neighbor.visited:
                neighbors.append(neighbor)

        return neighbors

    def find_backtrack_cell(self):
        """
        Searches for a previously visited cell that still has unvisited neighbors.

        Returns:
            Cell | None: A cell to backtrack to, or None if none exist.
        """
        for cell in reversed(self.visited_cells):  # Try most recent first
            if self.get_not_visited_neighbors(cell):
                return cell
        return None
    
    def add_entrance_exit(self):
        """
        Adds an entrance and exit to the maze by modifying the walls of the first and last cells.
        """

        border_cells = [cell for cell in self.maze 
                    if cell.y == 0 or cell.y == self.height - 1 or
                       cell.x == 0 or cell.x == self.width - 1]
        
        self.maze_entrance = random.choice(border_cells)
        border_cells.remove(self.maze_entrance)
        self.maze_exit = random.choice(border_cells)

        if self.maze_entrance.y == 0:
            self.maze_entrance.walls[0] = False  
        elif self.maze_entrance.y == self.height - 1:
            self.maze_entrance.walls[2] = False  
        elif self.maze_entrance.x == 0:
            self.maze_entrance.walls[3] = False  
        elif self.maze_entrance.x == self.width - 1:
            self.maze_entrance.walls[1] = False  

        if self.maze_exit.y == 0:
            self.maze_exit.walls[0] = False
        elif self.maze_exit.y == self.height - 1:
            self.maze_exit.walls[2] = False
        elif self.maze_exit.x == 0:
            self.maze_exit.walls[3] = False
        elif self.maze_exit.x == self.width - 1:
            self.maze_exit.walls[1] = False

