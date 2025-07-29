from generator.cell import Cell

class Display:
    def __init__(self):
        pass

    def display_maze(self, maze, width, height):
        """
        Displays the maze structure as ASCII art in the console.
        """
        header = (" " + "_") * width 
        print(header)
        for y in range(height):
            row = ""
            for x in range(width):
                cell = maze[y * width + x]
                row += "|" if cell.walls[3] else " "
                row += "_" if cell.walls[2] else " "

            last_cell = maze[y * width + width - 1]
            row += "|" if last_cell.walls[1] else " "
            print(row)