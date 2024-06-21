import pygame
from settings import *
import ast

def draw_background(selected_bar):
    screen.fill(BACKGROUND_COLOR)
    draw_bars()
    draw_text()
    draw_textbar(selected_bar)
    display_progress()

def draw_bars():
    bar_width=SCREEN_WIDTH-100
    x1,y1,w,h=50, SCREEN_HEIGHT/4, bar_width, 30
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    x1,y1,w,h=50, 1.8*(SCREEN_HEIGHT/4), bar_width, 30
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

def draw_text():
    text=font.render(str("Ore fatte: "), True, (0,0,0))
    screen.blit(text, (50, (SCREEN_HEIGHT/4)-25))

    text=font.render(str("Biglietti: "), True, (0,0,0))
    screen.blit(text, (50, 1.8*(SCREEN_HEIGHT/4)-25))

def draw_buttons():
    x1,y1,w,h=SCREEN_WIDTH-50-95-95-10, 3*(SCREEN_HEIGHT/5), 95, 30
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    font = pygame.font.SysFont('arial', 17)
    text=font.render(str("Set goal"), True, (0,0,0))
    screen.blit(text, (x1+17, y1+5))

    b_set_goal=((x1,x1+w),(y1,y1+h))

    x1,y1,w,h=x1+w+10, 3*(SCREEN_HEIGHT/5), 95, 30
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Reset"), True, (0,0,0))
    screen.blit(text, (x1+25, y1+5))

    b_reset=((x1,x1+w),(y1,y1+h))

    x1,y1,w,h= SCREEN_WIDTH-50-95-95-10, y1+40, 95, h
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Add hours"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_add_hours=((x1,x1+w),(y1,y1+h))

    x1,y1,w,h= x1+w+10, y1, w, h
    pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    text=font.render(str("Add ticket"), True, (0,0,0))
    screen.blit(text, (x1+9, y1+5))

    b_add_ticket=((x1,x1+w),(y1,y1+h))

    return(b_set_goal,b_reset,b_add_hours,b_add_ticket)

def draw_textbar(check):

    if(check):
        color=(100,200,100)
    else:
        color=(200,200,200)
    bar_width=SCREEN_WIDTH-310
    x1,y1,w,h=50, 3*(SCREEN_HEIGHT/5), bar_width, 30
    pygame.draw.rect(screen, color, (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

    # bar_width=SCREEN_WIDTH-310
    # x1,y1,w,h=50, 3*(SCREEN_HEIGHT/5), bar_width, 30
    # pygame.draw.rect(screen, (200,200,200), (x1,y1,w,h))
    # pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)

def clear_progres():
    bar_width=(SCREEN_WIDTH-100)
    x1,y1,w,h=50, (SCREEN_HEIGHT/4), bar_width, 30
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x1,y1,w,h))

    bar_width=(SCREEN_WIDTH-100)
    x1,y1,w,h=50, 1.8*(SCREEN_HEIGHT/4), bar_width, 30
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x1,y1,w,h))
    draw_bars()

def write_in_textbar(n,selected_bar):
    draw_textbar(selected_bar)
    if(n!=0):
        font = pygame.font.SysFont('arial', 20)
        text=font.render(str(n), True, (0,0,0))
        screen.blit(text, (55, 3*(SCREEN_HEIGHT/5)+3))

def display_progress():
    clear_progres()
    color_hours=[(255,0,0),(255,100,0),(255,255,0),(150,255,0),(0,255,0),(0,255,150),(0,255,255),(0,150,255),(0,0,255),(150,0,255),(255,0,255),(255,0,150)]
    with open('data.json', 'r') as f:
        l=f.read()
    l=ast.literal_eval(l)
    current_ticket=int(l['current_ticket'])
    ticket_goal=int(l['ticket_goal'])
    hours_goal=int(l['ticket_goal'])
    hours_sessions=l['hours_sessions']

    if(ticket_goal!=0):
        bar_width=(SCREEN_WIDTH-100)*(current_ticket/ticket_goal)
        x1,y1,w,h=50, 1.8*(SCREEN_HEIGHT/4), bar_width, 30
        pygame.draw.rect(screen, (255,0,0), (x1,y1,w,h))

    if(hours_goal!=0):
        y1=SCREEN_HEIGHT/4
        for i in range(len(hours_sessions)):
            bar_width=int((SCREEN_WIDTH-100)*(int(hours_sessions[i])/hours_goal))
            pygame.draw.rect(screen, color_hours[i%len(color_hours)], (x1,y1,bar_width,h))
            x1=x1+bar_width
    draw_bars()
    #TODO: barra colorata ticket

def set_ticket_goal(n):
    if(n>0):
        with open('data.json', 'r') as f:
            l=f.read()
        l=ast.literal_eval(l)
        l['ticket_goal']=n
        l=str(l)
        l=l.replace("'",'"')
        with open('data.json', 'w') as f:
            f.write(l)
        print("goal setted at"+str(n))

def add_ticket(n):
    if(n>=0):
        with open('data.json', 'r') as f:
            l=f.read()
        l=ast.literal_eval(l)
        if(l['current_ticket']+n>=l['ticket_goal']):
            l['current_ticket']=l['ticket_goal']
        else:
            l['current_ticket']=l['current_ticket']+n
        l=str(l)
        l=l.replace("'",'"')
        with open('data.json', 'w') as f:
            f.write(l)
        print("added ticket "+str(n))

def add_hours(n):
    if(n>0):
        with open('data.json', 'r') as f:
            l=f.read()
        l=ast.literal_eval(l)
        print("l: ")
        print(l)
        print(l['hours_sessions'])
        #sommare tutti gli elementi dell'array e controllare che non sia maggiore del goal
        #se si append la differenza o 0
        somma=sum(l['hours_sessions'])
        if(somma+n>=l['ticket_goal']):
            dif=l['ticket_goal']-somma
            if(dif!=0):
                l['hours_sessions'].append(dif)
        else:
            l['hours_sessions'].append(n)
        print(l)
        l=str(l)
        l=l.replace("'",'"')
        with open('data.json', 'w') as f:
            f.write(l)
        print("added ticket "+str(n))

def reset():
    with open('data.json', 'r') as f:
        l=f.read()
    l=ast.literal_eval(l)
    l['current_ticket']=0
    l['ticket_goal']=0
    l['hours_goal']=0
    l['hours_sessions']=[]
    l=str(l)
    l=l.replace("'",'"')
    with open('data.json', 'w') as f:
        f.write(l)

def select_text_bar(check):
    if(check):
        color=(100,200,100)
    else:
        color=(200,200,200)
    bar_width=SCREEN_WIDTH-310
    x1,y1,w,h=50, 3*(SCREEN_HEIGHT/5), bar_width, 30
    pygame.draw.rect(screen, color, (x1,y1,w,h))
    pygame.draw.rect(screen, (0,0,0), (x1,y1,w,h), 2)
    global number
    write_in_textbar(number)

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Progress bar')
font = pygame.font.SysFont('arial', 20)
run  = True
selected_cell=(-1,-1)
selected_bar=False
draw_background(selected_bar)
b_set_goal, b_reset, b_add_hours, b_add_ticket = draw_buttons()
text_bar_area=((50, 50+SCREEN_WIDTH-310),(3*(SCREEN_HEIGHT/5),3*(SCREEN_HEIGHT/5)+30))
number=0

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if(x>b_set_goal[0][0] and x<=b_set_goal[0][1] and y>=b_set_goal[1][0] and y<=b_set_goal[1][1]):
                print("set goal")
                set_ticket_goal(number)
                display_progress()
            elif(x>b_add_hours[0][0] and x<=b_add_hours[0][1] and y>=b_add_hours[1][0] and y<=b_add_hours[1][1]):
                print("add hours")
                add_hours(number)
                display_progress()
            elif(x>b_add_ticket[0][0] and x<=b_add_ticket[0][1] and y>=b_add_ticket[1][0] and y<=b_add_ticket[1][1]):
                print("add ticket")
                add_ticket(number)
                display_progress()
            elif(x>b_reset[0][0] and x<=b_reset[0][1] and y>=b_reset[1][0] and y<=b_reset[1][1]):
                print("reset")
                reset()
                display_progress()
            elif(x>text_bar_area[0][0] and x<=text_bar_area[0][1] and y>=text_bar_area[1][0] and y<=text_bar_area[1][1]):
                print("select text")
                selected_bar=True
                write_in_textbar(number,selected_bar)
            else:
                selected_bar=False
                write_in_textbar(number,selected_bar)
        if (event.type == pygame.KEYDOWN):
            if(selected_bar):
                if (event.key==pygame.K_BACKSPACE):
                    number=number//10
                    print(number)
                    write_in_textbar(number,selected_bar)
                else:
                    for i in range(len(INPUTS)):
                        if (event.key==INPUTS[i]):
                            number=number*10+i
                            print(number)
                            write_in_textbar(number,selected_bar)
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()