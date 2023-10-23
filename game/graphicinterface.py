import pygame
import sys
import random
from board import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
BOARD_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Define Scrabble tile values
tile_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10,
}

# Define multipliers for each square (2x, 3x letter, 2x, 3x word)
square_multipliers = [
    [3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 3],
    [1, 2, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [3, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 2, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 2, 1],
    [3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 3],
]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrabble")

# Function to draw the game board with multipliers
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            multiplier = square_multipliers[row][col]
            pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
            if multiplier == 2:
                pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 8)
            elif multiplier == 3:
                pygame.draw.circle(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 12)
            elif multiplier == 2 * 2:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 4, row * TILE_SIZE + TILE_SIZE // 4, TILE_SIZE // 2, TILE_SIZE // 2))
            elif multiplier == 3 * 3:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE + TILE_SIZE // 6, row * TILE_SIZE + TILE_SIZE // 6, 2 * TILE_SIZE // 3, 2 * TILE_SIZE // 3))

# Function to draw tiles and their values
def draw_tiles(tiles):
    for tile in tiles:
        x, y, letter = tile
        pygame.draw.rect(screen, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
        text_surface = FONT.render(letter, True, BLACK)
        screen.blit(text_surface, (x + TILE_SIZE // 3, y + TILE_SIZE // 3))

        if letter in tile_values:
            value_surface = FONT.render(str(tile_values[letter]), True, BLACK)
            screen.blit(value_surface, (x + TILE_SIZE - 2 * TILE_SIZE // 3, y + TILE_SIZE - TILE_SIZE // 2))

# Main game loop
running = True
tiles_on_board = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board
    screen.fill(BLACK)
    draw_board()
    draw_tiles(tiles_on_board)

    # Update the display
    pygame