import pygame

# Initialize Pygame
pygame.init()

# Define dimension of window
width = 800
high = 800

# Window
window = pygame.display.set_mode((width, high))
pygame.display.set_caption("Board of scrabble")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw window
def draw_window():
    # Draw background
    window.fill(BLACK)
    
    # Draw boxes
    for row in range(15):
        for column in range(15):
            pygame.draw.rect(ventana, BLANCO, (column * 50, row * 50, 50, 50), 1)

    # Update the screen
    pygame.display.update()

# Loop of the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_window()

# Quit the game
pygame.quit()