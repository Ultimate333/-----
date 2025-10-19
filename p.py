import pygame, random
pygame.init()
screen = pygame.display.set_mode((400, 400))
snake = [[100, 100]]; food = [300, 300]; dirs = [0, 20]
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP: dirs = [0, -20]
            if e.key == pygame.K_DOWN: dirs = [0, 20]
            if e.key == pygame.K_LEFT: dirs = [-20, 0]
            if e.key == pygame.K_RIGHT: dirs = [20, 0]
    new_head = [snake[0][0] + dirs[0], snake[0][1] + dirs[1]]
    snake.insert(0, new_head)
    if snake[0] == food:
        food = [random.randrange(0, 400, 20), random.randrange(0, 400, 20)]
    else: snake.pop()
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))
    for segment in snake: pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
    pygame.display.flip(); clock.tick(10)