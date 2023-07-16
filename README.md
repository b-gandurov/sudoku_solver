# Sudoku Solver with Pygame Visualization

This project contains a script that solves a Sudoku puzzle and visualizes the solving process in real-time using Pygame.

## Project Overview

The main logic of the script is based on a backtracking algorithm that tries out possible solutions until it finds one that satisfies all the Sudoku rules or it has tried every possible combination.

The Pygame library is used to visualize the solving process, with the original numbers on the board displayed in black and the newly added ones in red. The board updates in real-time as the script finds the solution.

## How to Run

1. Make sure you have Python installed on your system.
2. Install Pygame if you haven't already done so. You can do this with pip:

    ```bash
    pip install pygame
    ```

3. Clone the repository to your local machine or download the script file.
4. Run the script:

    ```bash
    python sudoku_solver.py
    ```

5. Watch as the program solves the Sudoku puzzle!

## Project Structure

- `sudoku_solver.py`: This is the main script that contains the Sudoku solving algorithm and Pygame visualization logic.

## Requirements

- Python 3.5 or higher
- Pygame

## Vizualization

<img src="solve_viz.gif" alt="Sudoku Solver Visualization" width="377"/>
