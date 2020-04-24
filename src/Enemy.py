from src.AbstractCharacter import AbstractCharacter
from src.Utils import Utils
import pygame


class Enemy(AbstractCharacter):

    def __init__(self, x, y, width, height, end):
        super().__init__(x, y, width, height)
        self.path = [x, end]  # This will define where our enemy starts and finishes its walking.
        self.vel = Utils.enemyVel
        self.health = Utils.enemy_health
        self.visible = True
        self.hitbox = (self.x + 15, self.y + 2, 30, 58)

    # This method manages images during enemy's movement
    def draw(self, win):
        self.move()
        if self.visible:  # NEW
            if self.walkCount + 1 >= Utils.clockTickEnemy:  # Since we have 11 images for each animtion our upper bound is 33.
                # We will show each image for 3 frames. 3 x 11 = 33.
                self.walkCount = 0

            if self.vel > 0:  # If we are moving to the right we will display our walkRight images
                win.blit(Utils.walkRightE[self.walkCount // int(Utils.clockTickEnemy / len(Utils.img_list_enemy))],
                         (self.x, self.y))
                self.walkCount += 1
            else:  # Otherwise we will display the walkLeft images
                win.blit(Utils.walkLeftE[self.walkCount // int(Utils.clockTickEnemy / len(Utils.img_list_enemy))],
                         (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, -1)
            # hitbox showing enemy weakness color Red
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #width = 50
            # hitbox showing enemy health color green: for every hit red increases of 10 pixels
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - 5*(10-self.health), 10))


    def move(self):
        if self.vel > 0:  # If we are moving right
            if self.x < self.path[1] + self.vel:  # If we have not reached the furthest right point on our path.
                self.x += self.vel
            else:
                self.__change_direction()  # Change direction and move back the other way

        else:  # If we are moving left
            if self.x > self.path[0] - self.vel:  # If we have not reached the furthest left point on our path
                self.x += self.vel  # increment x
            else:
                self.__change_direction()  # Change direction
        # update hitbox
        self.hitbox = (self.x + 15, self.y + 2, 30, 58)

    # Private method
    def __change_direction(self):
        self.vel = self.vel * -1
        self.x += self.vel
        self.walkCount = 0

    def hit(self):
        if self.health>0:
            self.health -=1
        else:
            self.visible = False
