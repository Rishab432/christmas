import pygame
import random

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

presentbox = pygame.image.load("C:\\Users\\AreekkR1446\\Desktop\\ICS_Classwork\\presentbox.png")
presentbox = pygame.transform.scale(presentbox, (50, 50))
santabag = pygame.image.load("C:\\Users\\AreekkR1446\\Desktop\\ICS_Classwork\\santabag.png")
santabag = pygame.transform.scale(santabag, (90, 90))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)

def moving_objs():
    global back_snow, middle_snow, front_snow, present_boxes
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
        presentx = random.randrange(0, 590)
        presenty = random.randrange(-960, 0)
        present_boxes.append([None, presentx, presenty])

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

def back_snowfall():
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

def front_snowfall():
    global front_snow
    for item in front_snow:
        if item[0] > item[3]:
            item[5] = -abs(item[5])
        elif item[0] < item[4]:
            item[5] = abs(item[5])
        item[0] += item[5]
        item[1] += item[6]
        pygame.draw.circle(screen, WHITE, item[0:2], item[2])
        if item[1] > 480:
            item[0] = random.randrange(-10, 650)
            item[1] = random.randrange(-480, 0)

""" 
The goal of the game is to catch as many falling presents as possible and for each catch you get a certain amount of points, if you reach the points needed you will win the game.
"""
def game1():
    moving_objs()
    bagx = 0
    bagy = 390
    caught = False
    value_appended = False
    while True:
        screen.fill(BLACK)
        # screen.blit(background, (0, 184))
        back_snowfall()
                
            
        for present in present_boxes:
            present[2] += 1
            present[0] = screen.blit(presentbox, (present[1], present[2]))

        bag = screen.blit(santabag, (bagx, bagy))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if bagx >= 2:
                bagx -= 2
        if keys[pygame.K_RIGHT]:
            if bagx <= 548:
                bagx += 2

        caught = False
        for present in present_boxes:
            if present[0].colliderect((bag)):
                if present[2] < bagy - 30:
                    caught = True
                    if not value_appended and present[-1] != True:
                        present.append(caught)
                        value_appended = True
                if caught and present[-1]:
                      present[1] = bagx + 20
                if present[2] > 410 and present[-1]:
                    print(present)
                    present_boxes.remove(present)
                    # points += 1
                
        front_snowfall()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    game1()
