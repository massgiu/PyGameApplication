from src.Utils import Utils
import pygame

class Player:
    def __init__(self,init_x,init_y,width,height):
        self.utils = Utils()
        self.init_x = init_x
        self.init_y = init_y
        self.width = width
        self.height = height
        self.isJump = False
        self.right = False
        self.left = False
        self.walkCount = 0
        self.jumpCount = self.utils.initCount

    def reDrawGameWin(self,win):
        win.blit(self.utils.bg_image, (0, 0))  # This will draw our background image at (0,0)
        if self.walkCount + 1 >= self.utils.clockTick:
            self.walkCount = 0
        # we need to select in the array walkLeft e walkRight the index
        if self.left:  # facing left
            win.blit(self.utils.walkLeft[self.walkCount // int(self.utils.clockTick / len(self.utils.img_list))],
                     (self.init_x, self.init_y))  # We integer divide walkCount by 3 to ensure each
            self.walkCount += 1  # image is shown 3 times every animation
        elif self.right:  # facing right
            win.blit(self.utils.walkRight[self.walkCount // int(self.utils.clockTick / len(self.utils.img_list))], (self.init_x, self.init_y))
            self.walkCount += 1
        else:
            win.blit(Utils.char, (self.init_x, self.init_y))  # If the character is standing still
        # pygame.draw.rect(win, (255, 0, 0), (init_x, init_y, charact_width, charact_height))
        pygame.display.update()

    def goLeft(self):
        self.init_x -= self.utils.vel
        self.left = True
        self.right = False

    def goRight(self):
        self.init_x += self.utils.vel
        self.left = False
        self.right = True

    def isStopped(self):
        self.left = False
        self.right = False
        self.walkCount = 0

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
        if self.jumpCount < -self.utils.initCount:
            self.isJump = False
            self.jumpCount = self.utils.initCount