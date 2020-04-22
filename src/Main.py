import pygame
from src.Utils import Utils
from src.Player import Player
from src.Enemy import Enemy
from src.Projectile import Projectile

pygame.init()

win = pygame.display.set_mode((Utils.screen_width, Utils.screen_height))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # create an object to help track time
player = Player(Utils.init_pos_x,Utils.init_pos_y,Utils.charact_width,Utils.charact_height)
goblin = Enemy(Utils.enemy_init_pos_x, Utils.enemy_init_pos_y, Utils.enemy_width, Utils.enemy_height, 300)
bullets = []

while player.run:
    clock.tick(Utils.clockTick)  # se diminuisce, va più lento (indica il numero di frame per sec)
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.run = False

    keys = pygame.key.get_pressed()

    #fires bullets
    if keys[pygame.K_SPACE]:
        facing = -1 if player.left else 1
        if len(bullets) < Utils.numMaxBullet: #it fires until numMAx bullets
            # create a bullet starting at the middle of the character and put in bullets vector
            bullets.append(Projectile(round(player.x+player.width/2), round(player.y+player.height/2), 6, (255, 0, 0), facing))
    # move bullets
    for bullet in bullets:
        if bullet.x < Utils.screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:  # remove bullets out of screen
            bullets.pop(bullets.index(bullet))
    #Left
    if keys[pygame.K_LEFT]:
        player.go_left()
    #Right
    elif keys[pygame.K_RIGHT]:
        player.go_right()
    else:
        player.is_stopped()
    #Not jumping: Up and Down and jump
    if not (player.isJump):
        # if keys[pygame.K_UP] and player.y > Utils.vel- Utils.charact_height/2:
        #     player.y -= Utils.vel
        # if keys[pygame.K_DOWN] and player.y < Utils.screen_height - Utils.charact_height:
        #     player.y += Utils.vel
        if keys[pygame.K_UP]:
            player.stop_jump()
    #Player jumping
    else:
        player.jump()
    # Load background image at (0,0)
    win.blit(Utils.bg_image, (0, 0))
    goblin.draw(win)
    player.draw(win, bullets)
pygame.quit()