# FIRST ATTEMPT, the 'Brute force' check of all paths, no bueno for checking all of the mazes, as it takes ~30 seconds for the 11x11
def find_paths(current_cell, maze_content, maze_size, path_contents=None, visited=None):
    if path_contents is None:
        path_contents = []
    if visited is None:
        visited = []

    # Add the current cell to visited
    visited.append(current_cell)

    # Base condition: if current cell is the goal
    if maze_content[current_cell] == 'G':
        return [list(path_contents) + [current_cell]] # Return a list containing its path, ensure it's a copy

    # Add the current cell to the path content if it's not the start
    if maze_content[current_cell] != 'S':
        path_contents.append(current_cell)

    paths = [] # This will accumulate all valid paths
    around = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for cells_around in around:
        new_cell = (current_cell[0] + cells_around[0], current_cell[1] + cells_around[1])

        # Check for boundaries and if the cell is not visited
        if 0 <= new_cell[0] < maze_size and 0 <= new_cell[1] < maze_size:
            if new_cell not in visited and maze_content.get(new_cell, 'X') != 'X':
                # Recursively find paths from the new cell
                new_paths = find_paths(new_cell, maze_content, maze_size, list(path_contents), list(visited))
                if new_paths:
                    paths.extend(new_paths)  # Extend the main paths list with new paths found

    return paths  # Return all accumulated paths


# Finds the smallest value path in a given path list
def find_path_with_smallest_sum(paths, maze_content):
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
def optimized_find_paths(start_position, maze_content, maze_size):
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

