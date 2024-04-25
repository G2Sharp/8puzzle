from models.puzzle_model import EightPuzzle
from services.EightPuzzleSolver import EightPuzzleSolver
from services.Helpers import *


# Main game loop
def main():
    # Define the initial puzzle board
    # initial_board = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]  # 0 represents the empty tile
    initial_board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # 0 represents the empty tile

    puzzle = EightPuzzle(initial_board)
    solver = EightPuzzleSolver(puzzle)
    solver.bfs()
    solver.dfs()
    solver.gbfs("MDH")


if __name__ == "__main__":
    main()
