# Function to draw the board
def draw_board(board,pygame,screen,background_image,WIDTH,HEIGHT,TILE_SIZE):
    for row in range(3):
        for col in range(3):
            if board[row][col] != 0:
                image_x = (board[row][col] - 1) % 3 * (WIDTH // 3)
                image_y = (board[row][col] - 1) // 3 * (HEIGHT // 3)
                tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                image_rect = pygame.Rect(image_x, image_y, WIDTH // 3, HEIGHT // 3)
                screen.blit(background_image, tile_rect, image_rect)
                pygame.draw.rect(screen, (255, 255, 255), tile_rect, 2)



# Flash initial board followed by goal board
def flash_boards(initial_state, goal_state,screen,pygame,background_image ,WIDTH,HEIGHT,TILE_SIZE):
    screen.fill((0, 0, 0))
    draw_board(initial_state,pygame,screen,background_image,WIDTH,HEIGHT,TILE_SIZE)
    pygame.display.flip()
    pygame.time.wait(1000)  # Adjust the delay as needed
    screen.fill((0, 0, 0))
    draw_board(goal_state,pygame,screen,background_image,WIDTH,HEIGHT,TILE_SIZE)
    pygame.display.flip()
    pygame.time.wait(1000)  # Adjust the delay as needed
