from generator.maze_generator import MazeGenerator
from display.display import Display

if __name__ == "__main__":
    maze_generator = MazeGenerator()
    display = Display()
    maze = maze_generator.generateMaze(20, 20)
    display.display_maze(maze_generator.maze, maze_generator.width, maze_generator.height)
    