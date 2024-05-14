import matplotlib.pyplot as plt
import numpy as np

#Code for visualization
def visualize(path, maze_data):
    color_map = {'X': 'black', 'S': 'red', 'G': 'red'}
    path_color = '#d7ffb0'
    default_color = 'white'

    rows = len(maze_data)
    cols = max(len(line) for line in maze_data)

    fig, ax = plt.subplots(figsize=(cols/4, rows/3.2))
    ax.set_xlim(-0.5, cols-0.5)
    ax.set_ylim(-0.5, rows-0.5)
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which='minor', color='k', linestyle='-', linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for y, line in enumerate(maze_data):
        for x, char in enumerate(line):
            bg_color = path_color if (y, x) in path else color_map.get(char, default_color)
            text_color = 'black' if char in color_map else 'black'
            ax.text(x, rows - 1 - y, char, color=text_color, ha='center', va='center', fontsize=8, fontweight='bold', backgroundcolor=bg_color)

    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()
