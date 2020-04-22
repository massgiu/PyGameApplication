from src.Utils import Utils
import pygame


class Player:
    # class attribute
    def __init__(self, init_x, init_y, width, height):
        # instance attribute
        self.utils = Utils()
        self.x = init_x
        self.y = init_y
        self.width = width
        self.height = height
        self.isJump = False
        self.run = True
        self.right = False
        self.left = False
        self.isWalking = False
        self.walkCount = 0
        self.jumpCount = Utils.initCount

    def draw(self, win, bullets):
        if self.walkCount + 1 >= Utils.clockTick:
            self.walkCount = 0
        # we need to select in the array walkLeft e walkRight the index
        if  (self.isWalking):
            if self.left:  # facing left
                win.blit(Utils.walkLeft[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.x, self.y))  # We integer divide walkCount by a k(Utils.clockTick / len(Utils.img_list)) to ensure each
                                                    # image is shown k times every animation
            elif self.right:  # facing right
                win.blit(Utils.walkRight[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.x, self.y))
            self.walkCount += 1
        #if it's not walking, loads first image
        else:
            if self.left: #if is turned on left
                win.blit(Utils.walkLeft[0], (self.x, self.y))  # If the character is standing still
            else: #if is turned on right
                win.blit(Utils.walkRight[0], (self.x, self.y))
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()

    def go_left(self):
        if self.x > Utils.vel - Utils.charact_width / 2:
            self.x -= Utils.vel #decrement x
            self.left = True
            self.right = False
            self.isWalking = True

    def go_right(self):
        if self.x < Utils.screen_width - Utils.charact_width:
            self.x += Utils.vel #increment x
            self.left = False
            self.right = True
            self.isWalking = True

    def is_stopped(self):
        self.walkCount = 0
        self.isWalking = False

    def stop_jump(self):
        self.isJump = True
        # self.right = False
        # self.left = False
        self.walkCount = 0

    def jump(self):
        # inizialmente la y viene decrementata: sale
        if self.jumpCount > 0:
            alfa = 1
        # dopo la y viene incrementata: scende
        else:
            alfa = -1
        self.y -= alfa * (self.jumpCount ** 2) * 0.5
        self.jumpCount -= 1
        if self.jumpCount < -Utils.initCount:
            self.isJump = False
            self.jumpCount = Utils.initCount
