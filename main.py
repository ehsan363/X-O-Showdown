import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
table = [[0,0,0],
         [0,0,0],
         [0,0,0]]
turn = random.randint(1,2)
pygame.display.set_caption('XO Showdown')
logo = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

state = 'game'
run = True
s12 = 0
table_img = pygame.transform.scale(pygame.image.load('900x900-3x3_table.png').convert_alpha(),(900,900))
xnon_active = pygame.transform.scale(pygame.image.load('X non_active.png').convert_alpha(),(200,200))
onon_active = pygame.transform.scale(pygame.image.load('O non_active.png').convert_alpha(),(200,200))
x_active = pygame.transform.scale(pygame.image.load('X active.png').convert_alpha(),(200,200))
o_active = pygame.transform.scale(pygame.image.load('O active.png').convert_alpha(),(200,200))

def game_mode(turn):
    pass


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos

            if x >= 525 and x <= 800:
                if y >= 65 and y <=340:
                    print('1st box')
                elif y >= 355 and y <= 630:
                    print('4th box')
                elif y >= 645 and y <= 935:
                    print('7th box')
            elif x >= 815 and x <= 1090:
                if y >=

    if state == 'game':
        screen.fill((40, 40, 40))
        screen.blit(table_img, (510, 50))
        screen.blit(xnon_active, (50, 30))
        screen.blit(onon_active, (1670, 30))

        if turn == 1:
            screen.blit(x_active, (50, 30))
        elif turn == 2:
            screen.blit(o_active, (1670, 30))
        else:
            print('something went wrong with the turn')

        game_mode(turn)

    pygame.display.update()
    clock.tick(60)