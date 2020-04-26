import pygame

class Utils:
    #Class attributes (static)
    init_pos_x = 100
    init_pos_y = 570# 410
    enemy_init_pos_x = init_pos_x+100
    enemy_init_pos_y = init_pos_y
    screen_width = 990 #500
    screen_height = 675 #480
    charact_width = 40
    charact_height = 60
    enemy_width = 64
    enemy_height = 64
    init_count = 10
    vel = 5
    enemyVel = 3
    numMaxBullet = 5
    enemy_health = 10
    img_list = [x for x in range(15) if x > 0]
    img_list_enemy = [x for x in range(11) if x > 0]
    walkRight = [pygame.image.load('../media/R' + str(x) + '.png') for x in img_list]
    walkRight = [pygame.transform.scale(x, (60, 70)) for x in walkRight]
    walkLeft = [pygame.image.load('../media/L' + str(x) + '.png') for x in img_list]
    walkLeft = [pygame.transform.scale(x, (60, 70)) for x in walkLeft]
    walkRightE = [pygame.image.load('../media/R' + str(x) + 'E.png') for x in img_list_enemy]
    walkLeftE = [pygame.image.load('../media/L' + str(x) + 'E.png') for x in img_list_enemy]
    clockTick = int(len(img_list)) * 3  # higher is factor, higher is speed animation
    clockTickEnemy = int(len(img_list_enemy)) * 3  # higher is factor, higher is speed animation
    bg_image = pygame.image.load('../media/bg1.jpg')
    char = pygame.image.load('../media/standing.png')
    font_size = 30
