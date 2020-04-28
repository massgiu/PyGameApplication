import pygame
from src.Utils import Utils
from src.Player import Player
from src.Enemy import Enemy

pygame.init()

win = pygame.display.set_mode((Utils.screen_width, Utils.screen_height))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # create an object to help track time
player = Player(Utils.init_pos_x, Utils.init_pos_y, Utils.charact_width, Utils.charact_height)
enemy = Enemy(Utils.enemy_init_pos_x, Utils.enemy_init_pos_y, Utils.enemy_width, Utils.enemy_height, Utils.screen_width - 150)


while player.run:
    clock.tick(Utils.clockTick)  # if descreases, goes faster (frame rate for sec)
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.run = False

    keys = pygame.key.get_pressed()

    player.check_hit(enemy)

    # fires bullets
    if keys[pygame.K_SPACE]:
        player.fire_bullets(enemy)
    # Left
    if keys[pygame.K_LEFT]:
        player.go_left()
    # Right
    elif keys[pygame.K_RIGHT]:
        player.go_right()
    else:
        player.is_stopped()
    # Up and Down and jump
    if not (player.isJump):
        if keys[pygame.K_UP]:
            player.start_jumping()
    # Player jumping
    else:
        player.jump()
    # Load background image at (0,0)
    win.blit(Utils.bg_image, (0, 0))
    enemy.draw(win)
    player.draw(win)
pygame.quit()
