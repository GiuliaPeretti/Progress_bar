import pygame
from settings import *

def draw_background():
    screen.fill((240,240,240))
    draw_bars()
    draw_text()

def draw_bars():
    bar_width=SCREEN_WIDTH-100
    x1,y1,x2,y2=50, SCREEN_HEIGHT/4, bar_width, 30
    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2,y2), 2)

    x1,y1,x2,y2=50, 1.8*(SCREEN_HEIGHT/4), bar_width, 30
    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2,y2), 2)

def draw_text():
    text=font.render(str("Ore fatte: "), True, (0,0,0))
    screen.blit(text, (50, (SCREEN_HEIGHT/4)-30))

    text=font.render(str("Biglietti: "), True, (0,0,0))
    screen.blit(text, (50, 1.8*(SCREEN_HEIGHT/4)-30))

def draw_buttons():
    x1,y1,x2,y2=SCREEN_WIDTH-50-80-80-80-10-10-15-15, 3*(SCREEN_HEIGHT/5), 80, 30
    pygame.draw.rect(screen, (200,200,200), (x1,y1,x2,y2))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2,y2), 2)

    font = pygame.font.SysFont('arial', 17)
    text=font.render(str("Set goal"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_set_goal=((x1,x2),(y1,y2))


    x1,y1,x2,y2= x1+x2+10, y1, x2+15, y2
    pygame.draw.rect(screen, (200,200,200), (x1,y1,x2,y2))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2,y2), 2)

    font = pygame.font.SysFont('arial', 17)
    text=font.render(str("Add hours"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_add_hours=((x1,x2),(y1,y2))

    x1,y1,x2,y2= x1+x2+10, y1, x2, y2
    pygame.draw.rect(screen, (200,200,200), (x1,y1,x2,y2))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2,y2), 2)

    font = pygame.font.SysFont('arial', 17)
    text=font.render(str("Add ticket"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_add_tickets=((x1,x2),(y1,y2))

    return(b_set_goal,b_add_hours,b_set_goal)



pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Progress bar')
font = pygame.font.SysFont('arial', 25)



run  = True
selected_cell=(-1,-1)
draw_background()
b_set_goal,b_add_hours,b_set_goal = draw_buttons()
while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if(x>b_set_goal[0][0] and x<=b_set_goal[0][1] and y>=b_set_goal[1][0] and y<=b_set_goal[1][1]):
                print("set goal")
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()