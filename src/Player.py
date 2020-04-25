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
        self.jumpCount = Utils.init_count
        self.bullets = []
        self.shootLoop = 0
        self.score = 50
        self.hitbox = (self.x + 15, self.y + 10, 30, 55)

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
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, -   1) #-1 no lines, 0 fill, 1 thin line
        # bullets
        if self.shootLoop < Utils.numMaxBullet // 2:
            self.shootLoop += 1
        else:
            self.shootLoop = 0
        for bullet in self.bullets:
            bullet.draw(win)
        # enemy display score
        font = pygame.font.SysFont("comicsans", 30, False)  # True means bold
        text = font.render("Score: " + str(self.score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        # update hitbox
        self.hitbox = (self.x + 15, self.y + 10, 30, 55)
        # player display score
        # font1 = pygame.font.SysFont('comicsans', 100)
        # text = font1.render('-5', 1, (255, 0, 0))
        # win.blit(text, (250 - (text.get_width() / 2), 200))
        win.blit(text, (Utils.screen_width - 120, 10))
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
        if self.jumpCount < -Utils.init_count:
            self.isJump = False
            self.jumpCount = Utils.init_count

    def fire_bullets(self, enemy):
        if self.shootLoop == 0:
            facing = -1 if self.left else 1
            if len(self.bullets) < Utils.numMaxBullet:  # it fires until numMax bullets
                # create a bullet starting at the middle of the character and put in bullets vector
                self.bullets.append(Projectile(round(self.x + self.width / 2), round(self.y + self.height / 2), 6,
                                               (255, 0, 0), facing))

    def move_bullets(self):
        for bullet in self.bullets:
            if Utils.screen_width > bullet.x > 0:
                bullet.x += bullet.vel
            else:  # remove bullets out of screen
                self.bullets.pop(self.bullets.index(bullet))
            # Check collision with enemy
            if (bullet.y - bullet.radius < self.enemy.hitbox[1] + self.enemy.hitbox[3]) and \
                    (bullet.y + bullet.radius > self.enemy.hitbox[1]):  # Checks x coords
                if (bullet.x + bullet.radius > self.enemy.hitbox[0]) and (
                        bullet.x - bullet.radius < self.enemy.hitbox[0] + self.enemy.hitbox[2]):  # Checks y coords
                    self.score += 1
                    self.enemy.hit()
                    self.bullets.pop(self.bullets.index(bullet))  # removes bullet from bullet list

    #This metodh decrements score if goblin hits player
    def check_hit(self,enemy):
        if enemy.visible and self.hitbox[1] < self.hitbox[1] + enemy.hitbox[3] and self.hitbox[1] + self.hitbox[3] > enemy.hitbox[1]:
            if self.hitbox[0] + self.hitbox[2] > enemy.hitbox[0] and self.hitbox[0] < enemy.hitbox[0] + \
                    enemy.hitbox[2]:
                self.hit()

    def hit(self):
        self.score -= 25
        if self.score>0:
            # reset the player position
            self.x = 0
            self.y = Utils.init_pos_y
            self.isJump = False
            self.jumpCount = Utils.init_count
            self.walkCount = 0
            pygame.display.update()
            # i = 0
            # while i < 200:
            #     pygame.time.delay(10)
            #     i += 1
            #     #This code gives opportunity to exit during pause
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             i = 301
            #             pygame.quit()

            # After we are hit we are going to display a message to the screen for
            # a certain period of time
        else:
            pygame.display.update()
