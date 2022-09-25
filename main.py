import pygame, copy, sys, os
import config, assets, fn

# Initialise the pygame
pygame.init()


# Executes game control flow
def main():
    # Generates game menu. If menu is closed, returns False
    if not fn.gameMenu():
        pygame.quit()
        return

    # Generates level selection menu. If menu is closed, returns False
    if not fn.levelMenu():
        pygame.quit()
        return

    # Define walls and populate it with wall rects
    walls = []
    if not fn.generateWalls(walls):
        pygame.quit()
        return

    # Define snake and its starting position
    snake = []
    if not fn.generateSnake(snake,config.SNAKE_LENGTH):
        pygame.quit()
        return

    # Generates initial food
    food = pygame.Rect(0, 0, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
    if not fn.generateFood(food,snake,walls):
        pygame.quit()
        return

    # Game loop variables
    run = True
    clock = pygame.time.Clock()
    frame = 1

    # Game loop
    while run:
        clock.tick(config.FPS)
        if frame > config.FPS:
            frame = 1

        # Check if game is being closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        fn.drawWindow(snake, food, walls)

        # Records next snake movement direction
        keysPressed = pygame.key.get_pressed()
        fn.movementDirection(keysPressed)

        # Setting fast forward
        if keysPressed[pygame.K_SPACE] and config.GAME_SPEED == config.START_GAME_SPEED:
            config.GAME_SPEED = int(config.START_GAME_SPEED / 2)
        elif not keysPressed[pygame.K_SPACE]:
            config.GAME_SPEED = config.START_GAME_SPEED

        # Executes the gameplay based on the set speed or fast forward when holding space
        if frame % config.GAME_SPEED == 0:
            # Copy the tail rect
            tail = copy.copy(snake[config.SNAKE_LENGTH - 1])
            # Move player ahead
            fn.movePlayer(snake)
            # If food is eaten, add the tail to the snake
            if fn.eatFood(food,walls,snake):
                snake.append(tail)
                config.SNAKE_LENGTH += 1
            # Snake dies if hits the wall
            snake_head = snake[0]
            if fn.wallCollision(snake_head,walls) or fn.snakeCollision(snake_head,snake):
                fn.finishScreen()
                break

        frame += 1
    pygame.quit()


if __name__ == "__main__":
    main()