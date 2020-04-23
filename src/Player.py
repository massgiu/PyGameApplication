from src.Utils import Utils
from src.Projectile import Projectile
from src.AbstractCharacter import AbstractCharacter
import pygame


class Player(AbstractCharacter):
    # class attribute
    def __init__(self, init_x, init_y, width, height):
        super().__init__(init_x, init_y, width, height)
        self.vel = Utils.vel
        self.isJump = False
        self.run = True
        self.right = False
        self.left = False
        self.isWalking = False
        self.jumpCount = Utils.initCount
        self.bullets = []
        self.shootLoop = 0

    def draw(self, win):
        # move bullets at every cycle scan
        self.move_bullets()
        if self.walkCount + 1 >= Utils.clockTick:
            self.walkCount = 0
        # we need to select in the array walkLeft e walkRight, the index
        if self.isWalking:
            if self.left:  # facing left
                win.blit(Utils.walkLeft[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.x,
                          self.y))  # We integer divide walkCount by a k(Utils.clockTick / len(Utils.img_list)) to ensure each
                # image is shown k times every animation
            elif self.right:  # facing right
                win.blit(Utils.walkRight[self.walkCount // int(Utils.clockTick / len(Utils.img_list))],
                         (self.x, self.y))
            self.walkCount += 1
        # if it's not walking, loads first image
        else:
            if self.left:  # if is turned on left
                win.blit(Utils.walkLeft[0], (self.x, self.y))  # If the character is standing still
            else:  # if is turned on right
                win.blit(Utils.walkRight[0], (self.x, self.y))
        # hitbox
        self.hitbox = (self.x + 15, self.y + 10, 30, 55)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
        # bullets
        if self.shootLoop < Utils.numMaxBullet:
            self.shootLoop+=1
        else:
            self.shootLoop=0
        for bullet in self.bullets:
            bullet.draw(win)
        pygame.display.update()

    def go_left(self):
        if self.x > self.vel - self.width / 2:
            self.x -= self.vel  # decrement x
            self.left = True
            self.right = False
            self.isWalking = True

    def go_right(self):
        if self.x < Utils.screen_width - self.width:
            self.x += self.vel  # increment x
            self.left = False
            self.right = True
            self.isWalking = True

    def is_stopped(self):
        self.walkCount = 0
        self.isWalking = False

    def start_jumping(self):
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

    def fire_bullets(self, enemy):
        self.enemy = enemy
        if self.shootLoop == 0:
            facing = -1 if self.left else 1
            if len(self.bullets) < Utils.numMaxBullet:  # it fires until numMAx bullets
                # create a bullet starting at the middle of the character and put in bullets vector
                self.bullets.append(
                    Projectile(round(self.x + self.width / 2), round(self.y + self.height / 2), 6, (255, 0, 0),
                               facing))

    def move_bullets(self):
        for bullet in self.bullets:
            if bullet.x < Utils.screen_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:  # remove bullets out of screen
                self.bullets.pop(self.bullets.index(bullet))
            #Check collision with enemu
            if (bullet.y - bullet.radius < self.enemy.hitbox[1] + self.enemy.hitbox[3]) and \
                    (bullet.y + bullet.radius > self.enemy.hitbox[1]):  # Checks x coords
                if (bullet.x + bullet.radius > self.enemy.hitbox[0]) and (bullet.x - bullet.radius < self.enemy.hitbox[0] + \
                        self.enemy.hitbox[2]):  # Checks y coords
                    self.enemy.hit()
                    self.bullets.pop(self.bullets.index(bullet))  # removes bullet from bullet list
