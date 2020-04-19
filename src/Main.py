import pygame
from src.Utils import Utils
from src.Player import Player

pygame.init()
utils = Utils()

win = pygame.display.set_mode((utils.screen_width, utils.screen_height))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # create an object to help track time
player = Player(utils.init_pos_x,utils.init_pos_y,utils.screen_width,utils.screen_height);

while utils.run:
    clock.tick(utils.clockTick)  # se diminuisce, va più lento (indica il numero di frame per sec)
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            utils.run = False

    keys = pygame.key.get_pressed()
    #Left
    if keys[pygame.K_LEFT] and player.init_x > utils.vel:
        player.goLeft()
    #Right
    elif keys[pygame.K_RIGHT] and player.init_x < utils.screen_width - utils.charact_width:
        player.goRight()
    else:
        player.isStopped()
    #Not jumping: Up and Down and jump
    if not (player.isJump):
        if keys[pygame.K_UP] and player.init_y > utils.vel:
            player.init_y -= utils.vel
        if keys[pygame.K_DOWN] and player.init_y < utils.screen_height - utils.charact_height:
            player.init_y += utils.vel
        if keys[pygame.K_SPACE]:
            player.stopJump()
    else:
        player.jump()
    player.reDrawGameWin(win)
pygame.quit()