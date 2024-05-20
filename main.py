from maze import load_maze, read_maze_from_file
from pathfinding import find_paths, optimized_find_paths, find_path_with_smallest_sum
from visualization import visualize
import timeit

def get_user_choice():
    while True:
        choice = input("Solve maze 1, 2, or 3?: ")
        if choice in ['4', '1', '2', '3']:
            return int(choice)
        print("Invalid input. Please enter 1, 2, or 3.")

def run_brute_force(start_position, maze_content, maze_size):
    paths = find_paths(start_position, maze_content, maze_size)
    shortest_route, min_sum = find_path_with_smallest_sum(paths, maze_content)
    print(f"Brute force path: {shortest_route} with sum: {min_sum}")
    return shortest_route

def run_optimized(start_position, maze_content, maze_size):
    path, cost = optimized_find_paths(start_position, maze_content, maze_size)
    print(f"Optimal path: {path} with cost: {cost}")
    return path

def main():
    default_maze = None
    maze_number = default_maze if default_maze is not None else get_user_choice()
    maze_files = {4: 'maze_4x4.txt', 1: 'maze_11x11.txt', 2: 'maze_31x31.txt', 3: 'maze_101x101.txt'}
    maze_file_path = maze_files.get(maze_number, 'maze_4x4.txt')
    maze_content, start_position, goal_position, maze_size = load_maze(maze_file_path)

    algo_choice = input("Choose algorithm - 'brute' for Brute Force, 'optimized' for Optimized: ").strip().lower()

    if algo_choice == 'brute':
        timer = timeit.Timer(lambda: run_brute_force(start_position, maze_content, maze_size))
    elif algo_choice == 'optimized':
        timer = timeit.Timer(lambda: run_optimized(start_position, maze_content, maze_size))
    
    execution_time = timer.timeit(number=1)
    print(f"Execution time: {execution_time:.20f} seconds")

    if algo_choice == 'brute':
        shortest_route = run_brute_force(start_position, maze_content, maze_size)
        edited_path = [cell for cell in shortest_route if cell != 'S' and cell != 'G']
    else:
        path = run_optimized(start_position, maze_content, maze_size)
        edited_path = [coordinates for coordinates, label in path]
    
    maze_data = read_maze_from_file(maze_file_path)
    visualize(edited_path, maze_data)

if __name__ == "__main__":
    main()
