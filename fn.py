import pygame, random, sys, os, copy
import config, assets
from maps import map01, map02, map03

# Generates the snake at the fixed location on the grid
def generateSnake(snake,snake_length):
    for i in range(snake_length):
        snake.append(pygame.Rect(config.GRID_BLOCK_SIZE * 9, config.GRID_BLOCK_SIZE * (3 - i), config.IMAGE_WIDTH, config.IMAGE_HEIGHT))
    return True

# Generates walls based on the selected game level
def generateWalls(walls):
    # Generates wall rects and appends to walls
    if config.GAME_LEVEL == 1:
        for block in map01:
            wall = pygame.Rect(block[0] * config.GRID_BLOCK_SIZE, block[1] * config.GRID_BLOCK_SIZE, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
            walls.append(wall)
    elif config.GAME_LEVEL == 2:
        for block in map02:
            wall = pygame.Rect(block[0] * config.GRID_BLOCK_SIZE, block[1] * config.GRID_BLOCK_SIZE, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
            walls.append(wall)
    elif config.GAME_LEVEL == 3:
        for block in map03:
            wall = pygame.Rect(block[0] * config.GRID_BLOCK_SIZE, block[1] * config.GRID_BLOCK_SIZE, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
            walls.append(wall)
    else:
        return False
    return True

# This function renders game difficulty menu and sets the speed based on user input
def gameMenu():
    config.SCREEN.fill(config.BACKGROUND_COLOR)
    bigText = assets.FONT_MEDIUM.render("Welcome to SNAKE", 1, (255,255,255))
    smallText = assets.FONT_SMALL.render("Press key 1 (MIN) to 5 (MAX) to select speed!", 1, (255,255,255))
    config.SCREEN.blit(bigText, (config.WIDTH/2 - bigText.get_width() /
                         2, config.HEIGHT/2 - bigText.get_height()/2))
    config.SCREEN.blit(smallText, (config.WIDTH/2 - smallText.get_width() /
                         2, config.HEIGHT/2 - smallText.get_height()/2 + smallText.get_height() + 100))
    pygame.display.update()
    menuOn = True
    while menuOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    config.GAME_SPEED = 30
                if event.key == pygame.K_2:
                    config.GAME_SPEED = 24
                if event.key == pygame.K_3:
                    config.GAME_SPEED = 18
                if event.key == pygame.K_4:
                    config.GAME_SPEED = 12
                if event.key == pygame.K_5:
                    config.GAME_SPEED = 6
                if config.GAME_SPEED != 0:
                    config.START_GAME_SPEED = config.GAME_SPEED
                    return True

# This function renders game map menu and sets the map based on user input
def levelMenu():
    config.SCREEN.fill(config.BACKGROUND_COLOR)
    bigText = assets.FONT_MEDIUM.render("Select your map", 1, (255,255,255))
    smallText = assets.FONT_SMALL.render("Press key 1 to 3 to select map!", 1, (255,255,255))
    config.SCREEN.blit(bigText, (config.WIDTH/2 - bigText.get_width() /
                         2, config.HEIGHT/2 - bigText.get_height()/2))
    config.SCREEN.blit(smallText, (config.WIDTH/2 - smallText.get_width() /
                         2, config.HEIGHT/2 - smallText.get_height()/2 + smallText.get_height() + 100))
    pygame.display.update()
    menuOn = True
    while menuOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    config.GAME_LEVEL = 1
                if event.key == pygame.K_2:
                    config.GAME_LEVEL = 2
                if event.key == pygame.K_3:
                    config.GAME_LEVEL = 3
                if config.GAME_LEVEL != 0:
                    return True

# Renders the game window with walls, snake and food
def drawWindow(snake, food, walls):
    config.SCREEN.fill(config.BACKGROUND_COLOR)
    # Renders walls
    for wall in walls:
        config.SCREEN.blit(assets.WALL_IMAGE, (wall.x, wall.y))

    # Renders snake
    for i in range(config.SNAKE_LENGTH):
        # Head
        if i == 0:
            if config.ACTUAL_DIRECTION == 'UP' and config.TARGET_DIRECTION == 'UP':
                snakeHeadImg = assets.SNAKE_HEAD_UP
            if config.ACTUAL_DIRECTION == 'UP' and config.TARGET_DIRECTION == 'LEFT':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_WA
            if config.ACTUAL_DIRECTION == 'UP' and config.TARGET_DIRECTION == 'RIGHT':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_WD
            if config.ACTUAL_DIRECTION == 'LEFT' and config.TARGET_DIRECTION == 'LEFT':
                snakeHeadImg = assets.SNAKE_HEAD_LEFT
            if config.ACTUAL_DIRECTION == 'LEFT' and config.TARGET_DIRECTION == 'DOWN':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_AS
            if config.ACTUAL_DIRECTION == 'LEFT' and config.TARGET_DIRECTION == 'UP':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_AW
            if config.ACTUAL_DIRECTION == 'DOWN' and config.TARGET_DIRECTION == 'DOWN':
                snakeHeadImg = assets.SNAKE_HEAD_DOWN
            if config.ACTUAL_DIRECTION == 'DOWN' and config.TARGET_DIRECTION == 'RIGHT':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_SD
            if config.ACTUAL_DIRECTION == 'DOWN' and config.TARGET_DIRECTION == 'LEFT':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_SA
            if config.ACTUAL_DIRECTION == 'RIGHT' and config.TARGET_DIRECTION == 'RIGHT':
                snakeHeadImg = assets.SNAKE_HEAD_RIGHT
            if config.ACTUAL_DIRECTION == 'RIGHT' and config.TARGET_DIRECTION == 'UP':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_DW 
            if config.ACTUAL_DIRECTION == 'RIGHT' and config.TARGET_DIRECTION == 'DOWN':
                snakeHeadImg = assets.SNAKE_HEAD_TURN_DS                          
            config.SCREEN.blit(snakeHeadImg, (snake[i].x, snake[i].y))
        # Tail
        elif i == config.SNAKE_LENGTH - 1:
            if snake[i].y < snake[i - 1].y:
                snakeTailImg = assets.SNAKE_TAIL_DOWN
            if snake[i].x > snake[i - 1].x:
                snakeTailImg = assets.SNAKE_TAIL_LEFT
            if snake[i].y > snake[i - 1].y:
                snakeTailImg = assets.SNAKE_TAIL_UP
            if snake[i].x < snake[i - 1].x:
                snakeTailImg = assets.SNAKE_TAIL_RIGHT
            config.SCREEN.blit(snakeTailImg, (snake[i].x, snake[i].y))
        # Body
        else:
            # Moving straight up
            if (snake[i].x == snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y > snake[i - 1].y):
                snakeBodyImg = assets.SNAKE_BODY_UP
            # Moving up right
            if (snake[i].x < snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y == snake[i - 1].y and snake[i].y < snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_WD
            # Moving up left
            if (snake[i].x > snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y == snake[i - 1].y and snake[i].y < snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_WA
            # Moving straight right
            if (snake[i].x < snake[i - 1].x and snake[i].y == snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_RIGHT
            # Moving right up
            if (snake[i].x == snake[i - 1].x and snake[i].x > snake[i + 1].x and snake[i].y > snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_DW
            # Moving right down
            if (snake[i].x == snake[i - 1].x and snake[i].x > snake[i + 1].x and snake[i].y < snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_DS
            # Moving straight down
            if (snake[i].x == snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y < snake[i - 1].y):
                snakeBodyImg = assets.SNAKE_BODY_DOWN
            # Moving down left
            if (snake[i].x > snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y == snake[i - 1].y and snake[i].y > snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_SA
            # Moving down right
            if (snake[i].x < snake[i - 1].x and snake[i].x == snake[i + 1].x and snake[i].y == snake[i - 1].y and snake[i].y > snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_SD
            # Moving straight left
            if (snake[i].x > snake[i - 1].x and snake[i].y == snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_LEFT
            # Moving left up
            if (snake[i].x == snake[i - 1].x and snake[i].x < snake[i + 1].x and snake[i].y > snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_AW
            # Moving left down
            if (snake[i].x == snake[i - 1].x and snake[i].x < snake[i + 1].x and snake[i].y < snake[i - 1].y and snake[i].y == snake[i + 1].y):
                snakeBodyImg = assets.SNAKE_BODY_TURN_AS
            config.SCREEN.blit(snakeBodyImg, (snake[i].x, snake[i].y))
    # Renders food
    config.SCREEN.blit(assets.FOOD_IMAGE, (food.x, food.y))
    pygame.display.update()

# Adjusts target direction based on user input
def movementDirection(keysPressed):
    if keysPressed[pygame.K_w] and config.ACTUAL_DIRECTION != 'DOWN': # UP
        config.TARGET_DIRECTION = 'UP'
    if keysPressed[pygame.K_a] and config.ACTUAL_DIRECTION != 'RIGHT': # LEFT
        config.TARGET_DIRECTION = 'LEFT'
    if keysPressed[pygame.K_s] and config.ACTUAL_DIRECTION != 'UP': # DOWN
        config.TARGET_DIRECTION = 'DOWN'
    if keysPressed[pygame.K_d] and config.ACTUAL_DIRECTION != 'LEFT': # RIGHT
        config.TARGET_DIRECTION = 'RIGHT'

# Moves player in the target direction
def movePlayer(snake):
    # Position is recalculated for each snake block
    for i in range(config.SNAKE_LENGTH - 1,-1,-1):
        # Snake head moves according to the movement direction
        if i == 0:
            if config.TARGET_DIRECTION == 'UP':
                if snake[i].y == config.Y_MIN:
                    snake[i].y = config.Y_MAX * config.GRID_BLOCK_SIZE
                else:
                    snake[i].y -= config.GRID_BLOCK_SIZE
            if config.TARGET_DIRECTION == 'LEFT':
                if snake[i].x == config.X_MIN:
                    snake[i].x = config.X_MAX * config.GRID_BLOCK_SIZE
                else:
                    snake[i].x -= config.GRID_BLOCK_SIZE
            if config.TARGET_DIRECTION == 'DOWN':
                if snake[i].y == config.Y_MAX * config.GRID_BLOCK_SIZE:
                    snake[i].y = config.Y_MIN
                else:
                    snake[i].y += config.GRID_BLOCK_SIZE
            if config.TARGET_DIRECTION == 'RIGHT':
                if snake[i].x == config.X_MAX * config.GRID_BLOCK_SIZE:
                    snake[i].x = config.X_MIN
                else:
                    snake[i].x += config.GRID_BLOCK_SIZE
        else:
        # Rest of snake body parts inherits position from the previous body part
            snake[i].x = snake[i - 1].x
            snake[i].y = snake[i - 1].y

    # Actual direction is updated
    config.ACTUAL_DIRECTION = config.TARGET_DIRECTION

# Detects if food was eaten and spawns new food
def eatFood(food,walls,snake):
    if snake[0].colliderect(food):
        # Add points
        config.POINTS += 1
        return generateFood(food,walls,snake)
    else:
        return False

# Spawns food at a new location
def generateFood(food,walls,snake):
        # Spawn food at a new location
        food.x = random.randint(config.X_MIN,config.X_MAX) * config.GRID_BLOCK_SIZE
        food.y = random.randint(config.Y_MIN,config.Y_MAX) * config.GRID_BLOCK_SIZE
        # Check if the food hits the wall or snake, and if yes, then generates the food until it does not
        while pygame.Rect.collidelist(food,walls) != -1 or pygame.Rect.collidelist(food,snake) != -1:
            food.x = random.randint(config.X_MIN,config.X_MAX) * config.GRID_BLOCK_SIZE
            food.y = random.randint(config.Y_MIN,config.Y_MAX) * config.GRID_BLOCK_SIZE
        return True

# Detects if player has hit the wall
def wallCollision(player,WALLS):
    if pygame.Rect.collidelist(player,WALLS) != -1:
        return True
    else:
        return False

# Detects if player has hit itself
def snakeCollision(player,SNAKE):
    for i in range(config.SNAKE_LENGTH):
        if i != 0:
            if pygame.Rect.colliderect(player,SNAKE[i]):
                return True
    return False
        

# Renders finish screen after game ends
def finishScreen():
    gameOver = assets.FONT_BIG.render("Game over!", 1, (255,255,255))
    pressToContinue = assets.FONT_SMALL.render("Press enter to leave...", 1, (255,255,255))
    config.SCREEN.blit(gameOver, (config.WIDTH/2 - gameOver.get_width() /
                         2, config.HEIGHT/2 - gameOver.get_height()/2))
    config.SCREEN.blit(pressToContinue, (config.WIDTH/2 - pressToContinue.get_width() /
                         2, config.HEIGHT/2 - pressToContinue.get_height()/2 + gameOver.get_height()))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_RETURN]:
            return
