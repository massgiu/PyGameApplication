import pygame
from src.Utils import Utils
from src.Player import Player

pygame.init()

win = pygame.display.set_mode((Utils.screen_width, Utils.screen_height))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # create an object to help track time
player = Player(Utils.init_pos_x,Utils.init_pos_y,Utils.screen_width,Utils.screen_height);

while player.run:
    clock.tick(Utils.clockTick)  # se diminuisce, va più lento (indica il numero di frame per sec)
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.run = False

    keys = pygame.key.get_pressed()
    #Left
    if keys[pygame.K_LEFT] and player.init_x > Utils.vel - Utils.charact_width/2:
        player.goLeft()
    #Right
    elif keys[pygame.K_RIGHT] and player.init_x < Utils.screen_width - Utils.charact_width:
        player.goRight()
    else:
        player.isStopped()
    #Not jumping: Up and Down and jump
    if not (player.isJump):
        if keys[pygame.K_UP] and player.init_y > Utils.vel- Utils.charact_height/2:
            player.init_y -= Utils.vel
        if keys[pygame.K_DOWN] and player.init_y < Utils.screen_height - Utils.charact_height:
            player.init_y += Utils.vel
        if keys[pygame.K_SPACE]:
            player.stopJump()
    else:
        player.jump()
    player.reDrawGameWin(win)
pygame.quit()