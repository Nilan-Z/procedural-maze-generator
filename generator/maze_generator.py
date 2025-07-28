from generator.cell import Cell
import random

class MazeGenerator():
    def __init__(self):
        """Initializes the MazeGenerator with an empty list of visited cells and dimensions."""
        self.visited_cells = []
        self.width = 0
        self.height = 0
        self.maze = []

    def generateMaze(self, width, height):
        """Generates a maze of given width and height."""
        self.width = width
        self.height = height
        self.maze = [Cell(x, y) for y in range(height) for x in range(width)]
        self.visited_cells = []  # Reset visited cells
        self.initialize_maze()
        return self.maze

    def initialize_maze(self):
        """Starts the maze generation from a random cell."""
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

        self.display_maze()

    def propagate(self, cell):
        """Propagates through the maze from the given cell, removing walls."""
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
        """Returns a list of neighboring cells that have not been visited."""
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
        """Finds a visited cell that still has unvisited neighbors."""
        for cell in reversed(self.visited_cells):  # Try most recent first
            if self.get_not_visited_neighbors(cell):
                return cell
        return None

    def display_maze(self):
        """Displays the maze in a simple text format."""
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                cell = self.maze[y * self.width + x]
                row += "|" if cell.walls[3] else " "
                row += "_" if cell.walls[2] else " "

            last_cell = self.maze[y * self.width + self.width - 1]
            row += "|" if last_cell.walls[1] else " "
            print(row)
