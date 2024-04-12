import pygame
import sys
from models.puzzle_model import EightPuzzle
from services.EightPuzzleSolver import EightPuzzleSolver
from services.Helpers import *
# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
TILE_SIZE = WIDTH // 3

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8 Puzzle')

# Load the background image
background_image = pygame.image.load('./public/turtle.jpg')  # Adjust the filename as per your image

# Main game loop
def main():
    # Define the initial puzzle board
    initial_board = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8] ] # 0 represents the empty tile

    puzzle = EightPuzzle(initial_board)
    solver = EightPuzzleSolver(puzzle)
    solution = solver.bfs()

    if solution is not None:
        flash_boards(initial_board, solution , screen,pygame,background_image,WIDTH,HEIGHT,TILE_SIZE)
        print("Solução encontrada:", solution)
    else:
        screen.fill((0, 0, 0))
        draw_board(initial_board,pygame,screen,background_image,WIDTH,HEIGHT,TILE_SIZE)
        pygame.display.flip()

        print("Não foi possível encontrar uma solução para o puzzle.")

    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
