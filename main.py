import yaml
from generator.maze_generator import MazeGenerator
from display.display import Display

def load_config(path="config.yaml"):
    """Load configuration from config.yaml."""
    with open(path, "r") as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config()

    width = config.get("width", 20)
    height = config.get("height", 20)
    output_format = config.get("format", "svg")
    output_path = config.get("outputPath", "./output/")
    filename = config.get("filename", "maze")

    maze_generator = MazeGenerator()
    maze = maze_generator.generateMaze(width, height)

    display = Display()
    display.display_maze(maze, width, height, output_path, filename, output_format)