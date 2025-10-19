import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
p1 = [10, 160]; p2 = [580, 160]; ball = [300, 200]; speed = [4, 4]
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: p1[1] -= 5
    if keys[pygame.K_s]: p1[1] += 5
    p2[1] = ball[1] - 40  # ИИ следует за мячом
    ball[0] += speed[0]; ball[1] += speed[1]
    if ball[1] <= 0 or ball[1] >= 380: speed[1] *= -1
    if (ball[0] <= 30 and p1[1] <= ball[1] <= p1[1] + 80) or (ball[0] >= 570 and p2[1] <= ball[1] <= p2[1] + 80): speed[0] *= -1
    pygame.draw.rect(screen, (255, 255, 255), (*p1, 20, 80))
    pygame.draw.rect(screen, (255, 255, 255), (*p2, 20, 80))
    pygame.draw.circle(screen, (255, 255, 255), ball, 10)
    pygame.display.flip(); clock.tick(60)