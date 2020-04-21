import pygame

class Utils:
    #Class attributes (static)
    init_pos_x = 200
    init_pos_y = 410
    screen_width = 500
    screen_height = 480
    charact_width = 40
    charact_height = 60
    initCount = 10
    vel = 5
    numMaxBullet = 5
    img_list = [x for x in range(10) if x > 0]
    walkRight = [pygame.image.load('../media/R' + str(x) + '.png') for x in img_list]
    walkLeft = [pygame.image.load('../media/L' + str(x) + '.png') for x in img_list]
    clockTick = int(len(img_list)) * 3  # higher is factor, higher is speed animation
    bg_image = pygame.image.load('../media/bg.jpg')
    char = pygame.image.load('../media/standing.png')
