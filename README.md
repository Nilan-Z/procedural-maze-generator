# procedural-maze-generator

A simple maze generator in Python, supports customizable dimensions and outputs


## Installation

Clone the repository:

```bash
git clone https://github.com/Nilan-Z/procedural-maze-generator.git
cd procedural-maze-generator
```

Install dependencies:

```python
pip install -r requirements.txt
```
## How to config

Maze generation parameters are defined in the config.yaml file, located at the root of the project.

```yaml
width: 25             # Maze width in cells
height: 25            # Maze height in cells
format: svg           # Output format: 'svg' or 'png'
outputPath: ./output/ # Directory where the maze image will be saved
filename: maze        # Name of the output file (without extension)
```

## How to run

After configuring `config.yaml`, run the generator with:

```bash
python generate_maze.py
```

The maze will be saved to the output directory you specified.


## Example

Here’s a sample generated maze (SVG format):

![Maze example](output/example-maze.svg)

You can adjust the dimensions and format in `config.yaml` to generate different types of mazes.


