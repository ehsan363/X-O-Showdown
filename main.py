import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
table = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
turn = random.randint(1, 2)
pygame.display.set_caption('XO Showdown')
logo = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

state = 'game'
run = True
s12 = 0
table_img = pygame.transform.scale(pygame.image.load('900x900-3x3_table.png').convert_alpha(), (900, 900))
xnon_active = pygame.transform.scale(pygame.image.load('X non_active.png').convert_alpha(), (200, 200))
onon_active = pygame.transform.scale(pygame.image.load('O non_active.png').convert_alpha(), (200, 200))
x_active = pygame.transform.scale(pygame.image.load('X active.png').convert_alpha(), (200, 200))
o_active = pygame.transform.scale(pygame.image.load('O active.png').convert_alpha(), (200, 200))

board_state = [0] * 9
print(board_state)
def game_mode(turn, box):
    
    if board_state[box - 1] == 0:
        board_state[box - 1] = turn

        return 2 if turn == 1 else 1
    return turn


def draw_pieces():

    positions = [
        (555, 95),
        (845, 95),
        (1135, 95),
        (555, 385),
        (845, 385),
        (1135, 385),
        (555, 675),
        (845, 675),
        (1135, 675)
    ]

    for i, piece in enumerate(board_state):
        if piece == 1:
            screen.blit(x_active, positions[i])
        elif piece == 2:
            screen.blit(o_active, positions[i])


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if x >= 525 and x <= 800:
                if y >= 65 and y <= 340:
                    turn = game_mode(turn, 1)
                elif y >= 355 and y <= 630:
                    turn = game_mode(turn, 4)
                elif y >= 645 and y <= 935:
                    turn = game_mode(turn, 7)

            elif x >= 815 and x <= 1090:
                if y >= 65 and y <= 340:
                    turn = game_mode(turn, 2)
                elif y >= 355 and y <= 630:
                    turn = game_mode(turn, 5)
                elif y >= 645 and y <= 935:
                    turn = game_mode(turn, 8)

            elif x >= 1105 and x <= 1395:
                if y >= 65 and y <= 340:
                    turn = game_mode(turn, 3)
                elif y >= 355 and y <= 630:
                    turn = game_mode(turn, 6)
                elif y >= 645 and y <= 935:
                    turn = game_mode(turn, 9)

    if state == 'game':
        screen.fill((40, 40, 40))
        screen.blit(table_img, (510, 50))
        screen.blit(xnon_active, (50, 30))
        screen.blit(onon_active, (1670, 30))

        draw_pieces()

        if turn == 1:
            screen.blit(x_active, (50, 30))
        elif turn == 2:
            screen.blit(o_active, (1670, 30))
        else:
            print('something went wrong with the turn')

    pygame.display.update()
    clock.tick(60)