from src.Utils import Utils
import pygame


class Player:
    # class attribute
    def __init__(self, init_x, init_y, width, height):
        # instance attribute
        self.utils = Utils()
        self.init_x = init_x
        self.init_y = init_y
        self.width = width
        self.height = height
        self.isJump = False
        self.run = True
        self.right = False
        self.left = False
        self.isWalking = False
        self.walkCount = 0
        self.jumpCount = Utils.initCount

    def reDrawGameWin(self, win):
        win.blit(self.utils.bg_image, (0, 0))  # This will draw our background image at (0,0)
        if self.walkCount + 1 >= Utils.clockTick:
            self.walkCount = 0
        # we need to select in the array walkLeft e walkRight the index
        if  (self.isWalking):
            if self.left:  # facing left
                win.blit(self.utils.walkLeft[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.init_x, self.init_y))  # We integer divide walkCount by a k(Utils.clockTick / len(Utils.img_list)) to ensure each
                                                    # image is shown k times every animation
            elif self.right:  # facing right
                win.blit(self.utils.walkRight[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.init_x, self.init_y))
            self.walkCount += 1
        #if it's not walking, loads first image
        else:
            if self.right: #if is turned on right
                win.blit(self.utils.walkRight[0], (self.init_x, self.init_y))  # If the character is standing still
            else: #if is turned on left
                win.blit(self.utils.walkLeft[0], (self.init_x, self.init_y))
        # pygame.draw.rect(win, (255, 0, 0), (init_x, init_y, charact_width, charact_height))
        pygame.display.update()

    def goLeft(self):
        self.init_x -= Utils.vel #decrement x
        self.left = True
        self.right = False
        self.isWalking = True

    def goRight(self):
        self.init_x += Utils.vel #increment x
        self.left = False
        self.right = True
        self.isWalking = True

    def isStopped(self):
        self.walkCount = 0
        self.isWalking = False

    def stopJump(self):
        self.isJump = True
        self.right = False
        self.left = False
        self.walkCount = 0

    def jump(self):
        # inizialmente la y viene decrementata: sale
        if self.jumpCount > 0:
            alfa = 1
        # dopo la y viene incrementata: scende
        else:
            alfa = -1
        self.init_y -= alfa * (self.jumpCount ** 2) * 0.5
        self.jumpCount -= 1
        if self.jumpCount < -Utils.initCount:
            self.isJump = False
            self.jumpCount = Utils.initCount
