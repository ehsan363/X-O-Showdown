import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('XO Showdown')
clock = pygame.time.Clock()

state = 'game'
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()