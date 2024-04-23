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
    initial_board =[[1, 2, 0], [4, 5, 3], [7, 8, 6]] # 0 represents the empty tile

    puzzle = EightPuzzle(initial_board)
    solver = EightPuzzleSolver(puzzle)
    # solution = solver.bfs()
    solution = solver.gbfs()

    if solution is not None:
        print("Solução encontrada:", solution)
        flash_boards(initial_board, solution , screen,pygame,background_image,WIDTH,HEIGHT,TILE_SIZE)
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
            #         elif event.key == pygame.K_w:  # Move Up
            #             puzzle.move_up()
            #         elif event.key == pygame.K_s:  # Move Down
            #             puzzle.move_down()
            #         elif event.key == pygame.K_a:  # Move Left
            #             puzzle.move_left()
            #         elif event.key == pygame.K_d:  # Move Right
            #             puzzle.move_right()

            # # Display the updated puzzle
            # screen.fill((0, 0, 0))
            # draw_board(puzzle.initial_state, pygame, screen, background_image, WIDTH, HEIGHT, TILE_SIZE)
            # pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
