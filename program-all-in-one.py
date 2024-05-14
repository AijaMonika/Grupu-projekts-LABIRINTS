# GRUPA: Aija Monika Vainiņa; Aleksis Java
import matplotlib.pyplot as plt
import numpy as np
import time


# FIRST ATTEMPT, the 'Brute force' check of all paths, no bueno for checking all of the mazes, as it takes ~30 seconds for the 11x11
def find_paths(current_cell, path_contents=None, visited=None):
    if path_contents is None:
        path_contents = []
    if visited is None:
        visited = []

    # Add the current cell to visited
    visited.append(current_cell)

    # Base condition: if current cell is the goal
    if maze_content[current_cell] == 'G':
        return [list(path_contents) + [current_cell]]  # Return a list containing its path, ensure it's a copy


    # Add the current cell to the path content if it's not the start
    if maze_content[current_cell] != 'S':
        path_contents.append(current_cell)

    paths = []  # This will accumulate all valid paths
    around = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for cells_around in around:
        new_cell = (current_cell[0] + cells_around[0], current_cell[1] + cells_around[1])

        # Check for boundaries and if the cell is not visited
        if 0 <= new_cell[0] < maze_size and 0 <= new_cell[1] < maze_size:
            if new_cell not in visited:
                if maze_content.get(new_cell, 'X') != 'X':
                    # Recursively find paths from the new cell
                    new_paths = find_paths(new_cell, list(path_contents), list(visited))
                    if new_paths:
                        paths.extend(new_paths)  # Extend the main paths list with new paths found

    return paths  # Return all accumulated paths

# Finds the smallest value path in a given path list
def find_path_with_smallest_sum(paths):
    # Initialize the minimum sum to a very high value for initial comparison
    min_sum = float('inf')
    smallest_path = None

    # Iterate through each path in the list of paths
    for path in paths:
        # Calculate the 'cost' of the current path by adding the cell values
        current_sum = sum(int(maze_content[cell]) if maze_content[cell].isdigit() else 0 for cell in path)

        # Check if the current sum is smaller than the found minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
            smallest_path = path

    return smallest_path, min_sum





# SECOND 'Optimized' attempt
def optimized_find_paths(start_position):
    queue = [(0, start_position, [])]  # Start with the start position at zero cost
    visited = set()  # Track visited cells

    while queue:
        queue.sort(key=lambda x: x[0])  # Sort queue to get the lowest cost entry
        current_cost, current_cell, path = queue.pop(0)

        # If the goal is reached, return the path and cost
        if maze_content[current_cell] == 'G':
            return path + [(current_cell, 'G')], current_cost

        # Avoid revisiting cells
        if current_cell in visited:
            continue
        visited.add(current_cell)

        around = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for cells_around in around:
            new_cell = (current_cell[0] + cells_around[0], current_cell[1] + cells_around[1])
            if 0 <= new_cell[0] < maze_size and 0 <= new_cell[1] < maze_size:
                if new_cell not in visited and maze_content.get(new_cell, 'X') != 'X':
                    # Special handling for 'G' and 'S' where no cost should be added
                    if maze_content[new_cell] == 'G':
                        new_cost = current_cost
                    elif maze_content[new_cell] == 'S':
                        new_cost = current_cost
                    else:
                        new_cost = current_cost + int(maze_content[new_cell])

                    queue.append((new_cost, new_cell, path + [(current_cell, maze_content[current_cell])]))

    return None, float('inf')  # Return None if no path is found



# Loads the maze from a file, converts it to a (row,col) key : content value dictionary
def load_maze(file_path):
    maze = {}
    with open(file_path, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                maze[(row, col)] = char
                if char == 'S':
                    global start_position
                    start_position = (row, col)
                if char == 'G':
                    global goal_position
                    goal_position = (row, col)                   
    return maze

def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Prompt the user to choose a maze until a valid input is given
def get_user_choice():
    while True:
        choice = input("Solve maze 1, 2, or 3?: ")
        if choice in ['4', '1', '2', '3']:
            return int(choice)
        print("Invalid input. Please enter 1, 2, or 3.")

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

def main():
    default_maze = None # Default maze number. Set to None to prompt which one to use

    # Determine which maze to solve: default or user input
    if default_maze is not None:
        maze_number = default_maze
    else:
        maze_number = get_user_choice()

    # Mapping of maze numbers to their corresponding file names (program is on same level as the files)
    maze_files = {
        4: 'maze_4x4.txt',
        1: 'maze_11x11.txt',
        2: 'maze_31x31.txt',
        3: 'maze_101x101.txt'
    }

    global maze_size
    maze_size = {4: 4, 1: 11, 2: 31, 3: 101}.get(maze_number, 4)
    
    # Fetch the correct file path based on the chosen maze number
    maze_file_path = maze_files.get(maze_number, 'maze_4x4.txt')

    # Load the maze content from the file
    global maze_content
    maze_content = load_maze(maze_file_path)

    # Output to check if the start and goal positions are correctly identified
    print(f"Start Position: {start_position}, Goal Position: {goal_position}, size: {maze_size}")

    # Ask user to choose algorithm
    algo_choice = input("Choose algorithm - 'brute' for Brute Force, 'optimized' for Optimized: ").strip().lower()

    if algo_choice == 'brute':
        start_time = time.time()
        paths = find_paths(start_position)
        shortest_route, min_sum = find_path_with_smallest_sum(paths)
        end_time = time.time()
        print(f"Brute force path: {shortest_route} with sum: {min_sum}")
    elif algo_choice == 'optimized':
        start_time = time.time()
        path, cost = optimized_find_paths(start_position)
        end_time = time.time()
        print(f"Optimal path: {path} with cost: {cost}")

    # Calculate and print the execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

    # Visualization
    if algo_choice == 'brute':
        edited_path = [cell for cell in shortest_route if cell != 'S' and cell != 'G']
    else:
        edited_path = [coordinates for coordinates, label in path]
    maze_data = read_maze_from_file(maze_file_path)
    visualize(edited_path, maze_data)

# initialization
if __name__ == "__main__":
    main()