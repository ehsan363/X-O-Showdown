import pygame
import random

from dulwich.porcelain import remove

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
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
winner_disp = pygame.transform.scale(pygame.image.load('winner_disp.png'), (1920,1080))

board_state = [0] * 9

Xorder = []
Oorder = []
winner = None


def winner_display(winner):
    screen.blit(winner_disp, (0,0))
    print(winner, 'WON!!!!!')
    if winner == 1:
        screen.blit(x_active, (938, 100))
    elif winner == 2:
        screen.blit(o_active, (938, 100))


def game_mode(turn, box):
    box_to_clear = None
    winner = None
    if board_state[box - 1] == 0:
        board_state[box - 1] = turn
        if turn == 1:
            Xorder.append(box)
            if len(Xorder) == 4:
                box_to_clear = Xorder[0]
                del Xorder[0]

        elif turn == 2:
            Oorder.append(box)
            if len(Oorder) == 4:
                box_to_clear = Oorder[0]
                del Oorder[0]

        if board_state[0] != 0:
            if board_state[0] == board_state[1]  == board_state[2]:
               winner = board_state[0]
            elif board_state[0] == board_state[3] == board_state[6]:
                winner = board_state[0]
            elif board_state[0] == board_state[4] == board_state[8]:
                winner = board_state[0]

        if board_state[4] != 0:
            if board_state[4] == board_state[3] == board_state[5]:
                winner = board_state[4]
            elif board_state[1] == board_state[4] == board_state[7]:
                winner = board_state[4]
            elif board_state[6] == board_state[4] == board_state[2]:
                winner = board_state[4]

        if board_state[8] != 0:
            if board_state[8] == board_state[7] == board_state[6]:
                winner = board_state[8]
            elif board_state[8] == board_state[5] == board_state[2]:
                winner = board_state[8]

        return 2 if turn == 1 else 1, box_to_clear, winner
    return turn, box_to_clear, winner


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
                    turn, box_to_clear, winner = game_mode(turn, 1)
                elif y >= 355 and y <= 630:
                    turn, box_to_clear, winner = game_mode(turn, 4)
                elif y >= 645 and y <= 935:
                    turn, box_to_clear, winner = game_mode(turn, 7)

            elif x >= 815 and x <= 1090:
                if y >= 65 and y <= 340:
                    turn, box_to_clear, winner = game_mode(turn, 2)
                elif y >= 355 and y <= 630:
                    turn, box_to_clear, winner = game_mode(turn, 5)
                elif y >= 645 and y <= 935:
                    turn, box_to_clear, winner = game_mode(turn, 8)

            elif x >= 1105 and x <= 1395:
                if y >= 65 and y <= 340:
                    turn, box_to_clear, winner = game_mode(turn, 3)
                elif y >= 355 and y <= 630:
                    turn, box_to_clear, winner = game_mode(turn, 6)
                elif y >= 645 and y <= 935:
                    turn, box_to_clear, winner = game_mode(turn, 9)

            if box_to_clear != None:
                for i in range(len(board_state)):
                    if i == box_to_clear-1:
                        board_state[i] = 0

        if event.type == pygame.MOUSEBUTTONDOWN and winner != None:
            board_state = [0] * 9

    if state == 'game':
        screen.fill((40, 40, 40))
        screen.blit(table_img, (510, 50))

        draw_pieces()
        if winner != None:
            winner_display(winner)

        if turn == 1:
            screen.blit(x_active, (50, 30))
            screen.blit(onon_active, (1670, 30))

        elif turn == 2:
            screen.blit(o_active, (1670, 30))
            screen.blit(xnon_active, (50, 30))

        else:
            print('something went wrong with the turn')

    pygame.display.update()
    clock.tick(60)