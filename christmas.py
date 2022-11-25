import pygame
import random

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

def draw_buildings(build1x, build1y):
    buildings_pos = []
    for i in range(10):
        buildings_pos.append
def game1():
    front_snow = []
    for i in range (150):
        fx = random.randrange(0, 640)
        fy = random.randrange(-480, 0)
        fz = 3
        front_snow.append([fx, fy, fz])
    middle_snow = []
    for i in range (150):
        mdx = random.randrange(0, 640)
        mdy = random.randrange(-480, 0)
        mdz = 2
        middle_snow.append([mdx, mdy, mdz])
    back_snow = []
    for i in range (150):
        bx = random.randrange(0, 640)
        by = random.randrange(-480, 0)
        bz = 1
        back_snow.append([bx, by, bz])
    presentx = 50
    presenty = 100
    while True:
        screen.fill(BLACK)
        for item in back_snow:
            item[1] += 1
            pygame.draw.circle(screen, WHITE, item[0:2], bz)
            if item[1] > 480:
                item[0] = random.randrange(0, 640)
                item[1] = random.randrange(-300, 0)
        for item in middle_snow:
            item[1] += 2
            pygame.draw.circle(screen, WHITE, item[0:2], mdz)
            if item[1] > 480:
                item[0] = random.randrange(0, 640)
                item[1] = random.randrange(-300, 0)
        # draw_buildings(build1x=10, build1y=300)
                
        presentbox = pygame.draw.rect(screen, RED, [presentx, presenty, 30, 30])
        pygame.draw.rect(screen, GREEN, [presentx+10, presenty, 10, 30])
        pygame.draw.rect(screen, GREEN, [presentx, presenty+10, 30, 10])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            presenty -= 2
        else:
            presenty += 2

        for item in front_snow:
            item[1] += 3
            pygame.draw.circle(screen, WHITE, item[0:2], fz)
            if item[1] > 480:
                item[0] = random.randrange(0, 640)
                item[1] = random.randrange(-300, 0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(30)

game1()