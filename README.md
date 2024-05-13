# Grupu-projekts-LABIRINTS
A group project for finding a path in a maze. Made by Aleksis Java and Aija Monika Vainiņa.

## PROMPTS (@ChatGPT4) & BRAINING (Short Recaps)
**SOLUTION for each maze:**
- **99**
- **1076**
- **1763**

## Inputs:
- **Three `.txt` files** containing mazes defined as follows:

![image](https://github.com/AijaMonika/Grupu-projekts-LABIRINTS/assets/72495103/737fbb6c-2640-4656-ad0a-4c65db29b054)

- `X` represents walls, which are non-traversable.
- `G` represents the endpoint or goal.
- `S` represents the starting point.
- The numbers represent the values of coins on a traversable path.

## Outputs:
- **Visual Representation**: A graphical display of the path from S to G which highlights the path taken.
- **Textual Representation**: A description of the path from S to G detailing the movements step-by-step.
- **Total Coins Gathered**: The sum of all coin values collected on the path from S to G with the minimum amount of coins gathered.


## Workflow of generating the code provided in this repository:

1. **Initial Setup**
   - Get a quick program that can read the mazes. Users can specify which maze to load, or it defaults to the first one for easier future development.
   - **Prompt**: Write a Python script to select and load a maze from text files with a default option and input validation, including explanatory comments.

2. **Development of Maze Structure**
   - Gave kudos and proceeded to request a program setup suitable for the pathfinder algorithm (geared towards matrix utilization).
   - **Prompt**: A MazeCell object is sensible as it stores the type of each cell in the maze.

3. **Brute Force Graph Algorithm**
   - Attempt to gather all paths from S to any endpoint (G or dead end) and print paths in ascending order.
   - The task criteria were fed into the prompt.
   - **Outcome**: Did not end well; started to implement by hand:
     - Introduction of "global" variables.
     - Began crafting a recursive method by hand to check the surroundings of the start and save paths that are not walls or out of borders.

4. **Refinement**
   - Re-wrote a lot of the ChatGPT code to make it logical and understandable.

5. **Recursive Method Development**
   - Expanded the base to support valid recursion in `find_paths`, considering criteria (flag for visited cells and eliminate dead-end paths as they are irrelevant).
   - **Prompt**: Implement a valid recursion in find_paths given criteria.

6. **Path Finding Flaw**
   - The initial `find_paths` function returned the first valid path but did not consider all other paths.

7. **Path Evaluation**
   - **Prompt**: Add a calculation function for counting each path's value.

8. **Brute Force Method Completion**
   - First method (`find_paths` that is 'brute force') created.
   - **Observation**: Extremely inefficient for a 5x5 maze, finding 140 ways to solve it, but all were valid paths from S to G.
   - Inefficiency noted as it reviewed all possible paths, though each cell can only be visited once.
   - Key point: Algorithm made many possibilities due to the ability to make diagonal jumps, revisiting corner paths, and registering them as valid.

9. **Conclusion: Optimization is Key**
   - Quick thought - check each valid cell, not path, and register the shortest path to a valid cell (BigBrain approach).

10. **Optimized Algorithm Generation**
    - **Prompt**: Generate an optimized algorithm that doesn’t use imports, is based on the previously made `find_paths`, using the idea of checking the best path to a cell with an example of a diagonal skip.
    - Involved a lot of code copy-pasting, describing examples, combating errors until arriving at a solution.
    - When all errors were fixed and a valid algorithm was generated, it was simply copied and pasted.
    - Left as is because the principle of "if it works, don't touch it" is key in any development.

11. **Redefine Code Structure for Better Readability**
    - Divided the code into multiple files to enhance manageability and maintainability.
    - Added comments explaining the working principles of the algorithm to clarify functionality and improve code readability.
    - Added a function for visualizing the maze, providing a more intuitive understanding of how the algorithm navigates through the maze.

12. **Upload to GitHub**
