from PIL import Image, ImageDraw
import os

class Display:
    """
    A class responsible for rendering a maze and exporting it as a PNG image.

    Each maze cell is represented as a square of fixed pixel size, with visible walls
    drawn based on the structure of the maze.

    Attributes:
        cell_size (int): Size (in pixels) of one maze cell. Default is 10.
    """

    def __init__(self, cell_size: int = 10):
        """
        Initialize the Display instance.

        Args:
            cell_size (int): Pixel size of a single maze cell. Default is 10.
        """
        self.cell_size = cell_size

    def display_maze(self, maze, width: int, height: int, output_path: str = './output/', filename: str = 'maze', output_format: str = 'png'):
        """
        Render the maze and save it to a file in the specified format.

        Args:
            maze (list): Flat list of cell objects, each with a `walls` attribute
                         representing [top, right, bottom, left] walls.
            width (int): Number of columns in the maze.
            height (int): Number of rows in the maze.
            output_path (str): Path where the image will be saved. Default is './output/maze.png'.
            output_format (str): Format of the output file ('png' or 'svg'). Default is 'png'.
        """
    
        full_path = os.path.join(output_path, f"{filename}.{output_format.lower()}")
        os.makedirs(output_path, exist_ok=True)  # Assure que le dossier existe

        if output_format.lower() == 'png':
            self.display_maze_png(maze, width, height, full_path)
        elif output_format.lower() == 'svg':
            self.display_maze_svg(maze, width, height, full_path)
        else:
            raise ValueError(f"Unsupported format: {output_format}. Use 'png' or 'svg'.")

        

    def display_maze_png(self, maze, width: int, height: int, output_path: str = './output/maze.png'):
        """
        Render the maze as an image and save it to a file.

        Args:
            maze (list): Flat list of cell objects, each with a `walls` attribute
                         representing [top, right, bottom, left] walls.
            width (int): Number of columns in the maze.
            height (int): Number of rows in the maze.
            output_path (str): Path where the image will be saved. Default is './output/maze.png'.
        """
        img_width = width * self.cell_size
        img_height = height * self.cell_size

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        image = Image.new('RGB', (img_width, img_height), 'white')
        draw = ImageDraw.Draw(image)

        for y in range(height):
            for x in range(width):
                cell = maze[y * width + x]
                x0 = x * self.cell_size
                y0 = y * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # Draw walls: [top, right, bottom, left]
                if cell.walls[0]:
                    draw.line([(x0, y0), (x1, y0)], fill='black')      # top
                if cell.walls[1]:
                    draw.line([(x1, y0), (x1, y1)], fill='black')      # right
                if cell.walls[2]:
                    draw.line([(x0, y1), (x1, y1)], fill='black')      # bottom
                if cell.walls[3]:
                    draw.line([(x0, y0), (x0, y1)], fill='black')      # left

        image.save(output_path)

    def display_maze_svg(self, maze, width: int, height: int, output_path: str = './output/maze.svg'):
        """
        Render the maze as an SVG file with a white background and clean, continuous borders.

        Args:
            maze (list): Flat list of cell objects, each with a `walls` attribute
                        representing [top, right, bottom, left] walls.
            width (int): Number of columns in the maze.
            height (int): Number of rows in the maze.
            output_path (str): Path where the SVG will be saved.
        """
        cell = self.cell_size
        svg_lines = []

        svg_width = width * cell
        svg_height = height * cell

        svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">')

        svg_lines.append(f'<rect width="{svg_width}" height="{svg_height}" fill="white" />')

        svg_lines.append('<g stroke="black" stroke-width="1">')

        for y in range(height):
            for x in range(width):
                index = y * width + x
                cell_obj = maze[index]
                x0 = x * cell
                y0 = y * cell
                x1 = x0 + cell
                y1 = y0 + cell

                if cell_obj.walls[0]:  # Top
                    svg_lines.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" />')
                if cell_obj.walls[1]:  # Right
                    svg_lines.append(f'<line x1="{x1}" y1="{y0}" x2="{x1}" y2="{y1}" />')
                if cell_obj.walls[2]:  # Bottom
                    svg_lines.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" />')
                if cell_obj.walls[3]:  # Left
                    svg_lines.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" />')

        svg_lines.append('</g>')
        svg_lines.append('</svg>')

        with open(output_path, 'w') as f:
            f.write('\n'.join(svg_lines))
