from models.puzzle_model import EightPuzzle
from services.EightPuzzleSolver import *
from services.Helpers import *


# Main game loop
def main():
    # Define the initial puzzle board
    initial_board = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]  # 0 represents the empty tile

    puzzle = EightPuzzle(initial_board)

    print("Initial State:")
    puzzle.print_state(puzzle.initial_state)

    print("\nBFS Solution:")
    bfs_solution = bfs(puzzle)
    if not bfs_solution:
        print("No solution found.")

    # print("\nDFS Solution:")
    # dfs_solution = dfs(puzzle)
    # if not dfs_solution:
    #     print("No solution found.")

    print("\nGreedy Search Solution:")
    greedy_solution = greedy_search(puzzle, "MHD")
    if not greedy_solution:
        print("No solution found.")

    print("\nGreedy Search Solution:")
    greedy_solution = greedy_search(puzzle, "HD")
    if not greedy_solution:
        print("No solution found.")


if __name__ == "__main__":
    main()
