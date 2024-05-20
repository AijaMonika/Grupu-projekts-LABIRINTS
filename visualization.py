import matplotlib.pyplot as plt
import numpy as np

#Code for visualization
def visualize (path, maze_data):

    # Map characters to colors
    color_map = {
        'X': 'black',  # Wall
        'S': 'red',    # Start
        'G': 'red'     # Goal
    }
    path_color = '#d7ffb0' # Color for the path
    default_color = 'white'  # Default color for numbers

    # Extract the maze size
    rows = len(maze_data)
    cols = max(len(line) for line in maze_data)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(cols/4, rows/3.2))  # Reduced figure size for a tighter maze
    ax.set_xlim(-0.5, cols-0.5)
    ax.set_ylim(-0.5, rows-0.5)
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which='minor', color='k', linestyle='-', linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Plot each cell
    for y, line in enumerate(maze_data):
        for x, char in enumerate(line):
            if (y, x) in path and char not in ['S', 'G']:
                bg_color = path_color
            else:
                bg_color = color_map.get(char, default_color)
            text_color = 'black' if char in color_map else 'black'
            ax.text(x, rows - 1 - y, char, color=text_color, ha='center', va='center', fontsize=8, fontweight='bold', backgroundcolor=bg_color)

    plt.gca().invert_yaxis()  # Invert the y-axis to match the layout in the data
    plt.axis('off')  # Turn off the axis
    plt.show()