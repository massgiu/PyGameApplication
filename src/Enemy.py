from src.AbstractCharacter import AbstractCharacter
from src.Utils import Utils


class Enemy(AbstractCharacter):

    def __init__(self, x, y, width, height, end):
        super().__init__(x, y, width, height)
        self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        self.vel = Utils.enemyVel

    # This method manages images during enemy's movement
    def draw(self, win):
        self.move()
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

    # Private method
    def __change_direction(self):
        self.vel = self.vel * -1
        self.x += self.vel
        self.walkCount = 0
