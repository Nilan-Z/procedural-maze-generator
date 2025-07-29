from PIL import Image, ImageDraw

class Display:
    def __init__(self, cell_size=10):
        self.cell_size = cell_size

    def display_maze(self, maze, width, height, output_path='maze.png'):
        """
        Dessine le labyrinthe et l'enregistre en image PNG.

        Parameters:
            maze (list): Liste plate de cellules avec des murs.
            width (int): Nombre de colonnes.
            height (int): Nombre de lignes.
            output_path (str): Chemin de sauvegarde de l'image.
        """
        img_width = width * self.cell_size
        img_height = height * self.cell_size

        image = Image.new('RGB', (img_width, img_height), 'white')
        draw = ImageDraw.Draw(image)

        for y in range(height):
            for x in range(width):
                cell = maze[y * width + x]
                x0 = x * self.cell_size
                y0 = y * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # Murs : top, right, bottom, left
                if cell.walls[0]:
                    draw.line([(x0, y0), (x1, y0)], fill='black')
                if cell.walls[1]:
                    draw.line([(x1, y0), (x1, y1)], fill='black')
                if cell.walls[2]:
                    draw.line([(x0, y1), (x1, y1)], fill='black')
                if cell.walls[3]:
                    draw.line([(x0, y0), (x0, y1)], fill='black')

        image.save(output_path)
        print(f"✅ Maze image saved to: {output_path}")
