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
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)

def snowspeed(x, z):
    if z == 1:
        movex = round(random.uniform(0.2, 0.5), 1)
        movey = round(random.uniform(0.7, 1.3), 1)
        right_limit = x + 4
        left_limit = x - 4
    elif z == 2:
        movex = round(random.uniform(0.5, 0.8), 1)
        movey = round(random.uniform(1.3, 1.9), 1)
        right_limit = x + 7
        left_limit = x - 7
    else:
        movex = round(random.uniform(0.8, 1.1), 1)
        movey = round(random.uniform(1.9, 2.5), 1)
        right_limit = x + 10
        left_limit = x - 10
    return right_limit, left_limit, movex, movey

def snowfall():
    global back_snow, middle_snow
    for item in back_snow:
        if item[0] > item[3]:
            item[5] = -abs(item[5])
        elif item[0] < item[4]:
            item[5] = abs(item[5])
        item[0] += item[5]
        item[1] += item[6]
        pygame.draw.circle(screen, (105, 105, 105), item[0:2], item[2])
        if item[1] > 480:
            item[0] = random.randrange(-10, 650)
            item[1] = random.randrange(-480, 0)
    for item in middle_snow:
        if item[0] > item[3]:
            item[5] = -abs(item[5])
        elif item[0] < item[4]:
            item[5] = abs(item[5])
        item[0] += item[5]
        item[1] += item[6]
        pygame.draw.circle(screen, (170, 170, 170), item[0:2], item[2])
        if item[1] > 480:
            item[0] = random.randrange(-10, 650)
            item[1] = random.randrange(-480, 0)



""" 
The goal of the game is to catch as many falling presents as possible and for each catch you get a certain amount of points, if you reach the points needed you will win the game.
"""
def game1():
    global back_snow, middle_snow
    back_snow = []
    for i in range (150):
        bx = random.randrange(-10, 650)
        brlimit = bx + 4
        bllimit = bx - 4
        by = random.randrange(-480, 0)
        bz = 1
        brlimit, bllimit = snowspeed(bx, bz)[ :2]
        b_mvx, b_mvy = snowspeed(bx, bz)[2: ]
        back_snow.append([bx, by, bz, brlimit, bllimit, b_mvx, b_mvy])
    middle_snow = []
    for i in range (150):
        mdx = random.randrange(-10, 650)
        mdrlimit = mdx + 7
        mdllimit = mdx - 7
        mdy = random.randrange(-480, 0)
        mdz = 2
        mdrlimit, mdllimit = snowspeed(mdx, mdz)[ :2]
        md_mvx, md_mvy = snowspeed(mdx, mdz)[2: ]
        middle_snow.append([mdx, mdy, mdz, mdrlimit, mdllimit, md_mvx, md_mvy])
    front_snow = []
    for i in range (150):
        fx = random.randrange(-10, 650)
        frlimit = fx + 10
        fllimit = fx - 10
        fy = random.randrange(-480, 0)
        fz = 3
        frlimit, fllimit = snowspeed(fx, fz)[ :2]
        f_mvx, f_mvy = snowspeed(fx, fz)[2:]
        front_snow.append([fx, fy, fz, frlimit, fllimit, f_mvx, f_mvy])
    present_boxes = []
    for i in range(20):
        presentx = random.randrange(0, 610)
        presenty = random.randrange(-480, 0)
        presentbox = pygame.draw.rect(screen, RED, [presentx, presenty, 30, 30])
        present_boxes.append([presentbox, presentx, presenty])
    click = False
    grab = False
    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill(BLACK)
        snowfall()
                
        for present in present_boxes:
            present[2] += 1
            present[0] = pygame.draw.rect(screen, RED, [present[1], present[2], 30, 30])
            pygame.draw.rect(screen, GREEN, [present[1]+10, present[2], 10, 30])
            pygame.draw.rect(screen, GREEN, [present[1], present[2]+10, 30, 10])
            if present[0].collidepoint((mx, my)) and click:
                grab = True
            if grab:
                present[0] = pygame.draw.rect(screen, RED, [mx, my, 30, 30])
                pygame.draw.rect(screen, GREEN, [present[1]+10, present[2], 10, 30])
                pygame.draw.rect(screen, GREEN, [present[1], present[2]+10, 30, 10])
        # for present in present_boxes:
        #     if grab:
        #         present[1: ] = mx, my

        # presentbox = pygame.draw.rect(screen, RED, [presentx, presenty, 30, 30])
        

        for item in front_snow:
            if item[0] > item[3]:
                item[5] = -abs(item[5])
            elif item[0] < item[4]:
                item[5] = abs(item[5])
            item[0] += item[5]
            item[1] += item[6]
            pygame.draw.circle(screen, WHITE, item[0:2], fz)
            if item[1] > 480:
                item[0] = random.randrange(-10, 650)
                item[1] = random.randrange(-480, 0)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                print(True)
            if event.type == pygame.MOUSEBUTTONUP:
                grab = False
                print(False)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    game1()
