import pygame, os

# Initialise the pygame
pygame.init()

#### LOAD VISUAL GAME ASSETS ####

# Set title and icon
pygame.display.set_caption("SNAKE")
icon = pygame.image.load('assets/snake.png')
pygame.display.set_icon(icon)

# Define key logos
SNAKE_HEAD = pygame.image.load(os.path.join('assets','snake_head.png'))
SNAKE_HEAD_TURN = pygame.image.load(os.path.join('assets','snake_head_turn.png'))
SNAKE_BODY = pygame.image.load(os.path.join('assets','snake_straight.png'))
SNAKE_BODY_TURN = pygame.image.load(os.path.join('assets','snake_body_turn.png'))
SNAKE_TAIL = pygame.image.load(os.path.join('assets','snake_tail.png'))
FOOD_IMAGE = pygame.image.load(os.path.join('assets','food.png'))
WALL_IMAGE = pygame.image.load(os.path.join('assets','wall.png'))

# Define snake logos variations
SNAKE_HEAD_UP = SNAKE_HEAD
SNAKE_HEAD_LEFT = pygame.transform.rotate(SNAKE_HEAD,90)
SNAKE_HEAD_DOWN = pygame.transform.rotate(SNAKE_HEAD,180)
SNAKE_HEAD_RIGHT = pygame.transform.rotate(SNAKE_HEAD,270)

# Going up, turning right / left
SNAKE_HEAD_TURN_WD = SNAKE_HEAD_TURN
SNAKE_HEAD_TURN_WA = pygame.transform.flip(SNAKE_HEAD_TURN_WD, True, False)
# Going left, turning up / down
SNAKE_HEAD_TURN_AW = pygame.transform.rotate(SNAKE_HEAD_TURN,90)
SNAKE_HEAD_TURN_AS = pygame.transform.flip(SNAKE_HEAD_TURN_AW, False, True)
# Going down, turning left / right
SNAKE_HEAD_TURN_SA = pygame.transform.rotate(SNAKE_HEAD_TURN,180)
SNAKE_HEAD_TURN_SD = pygame.transform.flip(SNAKE_HEAD_TURN_SA, True, False)
# Going right, turning down / up
SNAKE_HEAD_TURN_DS = pygame.transform.rotate(SNAKE_HEAD_TURN,270)
SNAKE_HEAD_TURN_DW = pygame.transform.flip(SNAKE_HEAD_TURN_DS, False, True)

SNAKE_BODY_UP = SNAKE_BODY
SNAKE_BODY_LEFT = pygame.transform.rotate(SNAKE_BODY,90)
SNAKE_BODY_DOWN = pygame.transform.rotate(SNAKE_BODY,180)
SNAKE_BODY_RIGHT = pygame.transform.rotate(SNAKE_BODY,270)

# Going up, turning right / left
SNAKE_BODY_TURN_WD = SNAKE_BODY_TURN
SNAKE_BODY_TURN_WA = pygame.transform.flip(SNAKE_BODY_TURN_WD, True, False)
# Going left, turning up / down
SNAKE_BODY_TURN_AW = pygame.transform.rotate(SNAKE_BODY_TURN,90)
SNAKE_BODY_TURN_AS = pygame.transform.flip(SNAKE_BODY_TURN_AW, False, True)
# Going down, turning left / right
SNAKE_BODY_TURN_SA = pygame.transform.rotate(SNAKE_BODY_TURN,180)
SNAKE_BODY_TURN_SD = pygame.transform.flip(SNAKE_BODY_TURN_SA, True, False)
# Going right, turning down / up
SNAKE_BODY_TURN_DS = pygame.transform.rotate(SNAKE_BODY_TURN,270)
SNAKE_BODY_TURN_DW = pygame.transform.flip(SNAKE_BODY_TURN_DS, False, True)

SNAKE_TAIL_UP = SNAKE_TAIL
SNAKE_TAIL_LEFT = pygame.transform.rotate(SNAKE_TAIL,90)
SNAKE_TAIL_DOWN = pygame.transform.rotate(SNAKE_TAIL,180)
SNAKE_TAIL_RIGHT = pygame.transform.rotate(SNAKE_TAIL,270)

# Define font 
fontName = 'press-start-2p.regular.ttf'
fontSize = 50
FONT_BIG = pygame.font.Font(os.path.join('assets',fontName), int(fontSize))
FONT_MEDIUM = pygame.font.Font(os.path.join('assets',fontName), int(fontSize / 2))
FONT_SMALL = pygame.font.Font(os.path.join('assets',fontName), int(fontSize / 4))
