def load_maze(file_path):
    maze = {}
    start_position = None
    goal_position = None
    with open(file_path, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                maze[(row, col)] = char
                if char == 'S':
                    start_position = (row, col)
                if char == 'G':
                    goal_position = (row, col)
    # Correctly calculate the maze size by finding the max row and col values
    if maze:
        max_row = max(row for row, col in maze.keys())
        max_col = max(col for row, col in maze.keys())
        maze_size = max(max_row, max_col) + 1  # Assuming the maze is square and 0-indexed
    else:
        maze_size = 0  # No maze loaded

    return maze, start_position, goal_position, maze_size
  


def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
