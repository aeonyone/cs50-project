import pygame

# Define game grid
GRID_BLOCK_SIZE = 32
GRID_X_BLOCKS = 20
GRID_Y_BLOCKS = 20
X_MIN, X_MAX =  0, GRID_X_BLOCKS - 1
Y_MIN, Y_MAX =  0, GRID_Y_BLOCKS - 1
IMAGE_WIDTH, IMAGE_HEIGHT = GRID_BLOCK_SIZE, GRID_BLOCK_SIZE

# Create the screen
WIDTH, HEIGHT = GRID_BLOCK_SIZE * GRID_X_BLOCKS, GRID_BLOCK_SIZE * GRID_Y_BLOCKS
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set default background color
BACKGROUND_COLOR = (29, 82, 16)

# Define blank or default game variables
FPS = 60
START_GAME_SPEED = 0
GAME_SPEED = 0 # Less is more, allowed values: 1,2,3,4,5,6,10,12,15,20,30,60
GAME_LEVEL = 0
TARGET_DIRECTION = 'DOWN'
ACTUAL_DIRECTION = 'DOWN'
SNAKE_LENGTH = 3
POINTS = 0 