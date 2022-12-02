import pygame
from pygame import mixer
import random

pygame.init()
pygame.font.init()
mixer.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

mixer.music.load("still sadge - a poem.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
winter_sky = pygame.image.load("winter_sky.png")
presentbox = pygame.image.load("presentbox.png")
presentbox = pygame.transform.scale(presentbox, (50, 50))
santabag = pygame.image.load("santabag.png")
santabag = pygame.transform.scale(santabag, (90, 90))
pagging = pygame.image.load("pagging.gif")
pagging = pygame.transform.scale(pagging, (100, 100))
sadge = pygame.image.load("sadge.png")
sadge = pygame.transform.scale(sadge, (100, 100))
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont(None, 70)

def moving_objs(boxes):
    global back_snow, middle_snow, front_snow, present_boxes, presents_num
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
    for i in range(boxes):
        presentx = random.randrange(0, 590)
        presenty = random.randrange(-960, 0)
        present_boxes.append([None, presentx, presenty])
    presents_num = len(present_boxes)

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
        if item[1] > 235:
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
    lvl_state = [True, False, False, False, False]
    lvl1, lvl2, lvl3, lvl4, lvl5 = 0, 1, 2, 3, 4
    moving_objs(0)
    present_fall = 1
    bagx = 0
    bagy = 390
    caught = False
    points = 0
    lvl_finish = False
    win = False
    lose = False
    lvl = 0
    while True:
        if len(present_boxes) == 0:
            lvl_finish = True
        if lvl_finish:
            if points >= presents_num*5:
                pygame.time.wait(500)
                lvl_finish = False
                points = 0
                lvl += 1
                if lvl_state[lvl1]:
                    moving_objs(20)
                    lvl_state[lvl1] = False
                    lvl_state[lvl2] = True
                elif lvl_state[lvl2]:
                    moving_objs(22)
                    lvl_state[lvl2] = False
                    lvl_state[lvl3] = True
                elif lvl_state[lvl3]:
                    moving_objs(24)
                    present_fall += 0.5
                    lvl_state[lvl3] = False
                    lvl_state[lvl4] = True
                elif lvl_state[lvl4]:
                    moving_objs(26)
                    lvl_state[lvl4] = False
                    lvl_state[lvl5] = True
                elif lvl_state[lvl5]:
                    moving_objs(30)
                    present_fall += 0.5
                    lvl_state[lvl5] = False
                else:
                    win = True
            else:
                lose = True


        screen.blit(winter_sky, (0, 0))
        points_text = FONT.render(str(points), True, WHITE)
        screen.blit(points_text, (5, 5))
        lvl_text = FONT.render(str(lvl), True, WHITE)
        lvltxt_rect = lvl_text.get_rect()
        lvltxt_rect.topright = 635, 5
        screen.blit(lvl_text, lvltxt_rect)

        back_snowfall()
            
        for present in present_boxes:
            present[2] += present_fall
            present[0] = screen.blit(presentbox, (present[1], present[2]))
        

        bag = pygame.Rect([bagx+15, bagy+3, 60, 10])
        screen.blit(santabag, (bagx, bagy))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if bagx >= 4:
                bagx -= 4
        if keys[pygame.K_RIGHT]:
            if bagx <= 546:
                bagx += 4

        caught = False
        for present in present_boxes:
            if present[0].colliderect((bag)):
                print(bagy, present[2])
                if present[2] < bagy - 45:
                    caught = True
                    if present[-1] != True:
                        present.append(True)
                if caught or present[-1] == True:
                      present[1] = bagx + 20
            if present[2] > 400 and present[-1] == True:
                present_boxes.remove(present)
                points += 10
            elif present[2] > 480:
                present_boxes.remove(present)
        
        front_snowfall()

        if win:
            screen.blit(winter_sky, (0, 0))
            win_text = FONT.render("You Win! I'm Pagging!", True, WHITE)
            screen.blit(win_text, (win_text.get_rect(center = screen.get_rect().center)))
            screen.blit(pagging, (10, 10))
        elif lose:
            screen.blit(winter_sky, (0, 0))
            win_text = FONT.render("You Lose... Sadge...", True, WHITE)
            screen.blit(win_text, (win_text.get_rect(center = screen.get_rect().center)))
            screen.blit(sadge, (10, 10))


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
