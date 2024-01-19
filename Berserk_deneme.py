
# Modification date: Sat Jan 29 12:43:34 2022

# Production date: Sun Sep  3 15:43:23 2023

import pygame

# initialize the pygame
pygame.init()

# create the screen(width, height)
win = pygame.display.set_mode((1280, 720))

# Background
background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.png")

# Title and icon
pygame.display.set_caption("Berserk")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


# Walking
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3d1.png'), pygame.image.load('R4d1.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7d1.png'), pygame.image.load('R8d1.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3d1.png'), pygame.image.load('L4d1.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7d1.png'), pygame.image.load('L8d1.png')]
attackRight = [pygame.image.load('RA1.png'), pygame.image.load('RA1d1.png'), pygame.image.load('RA2d1.png'), pygame.image.load('RA2d2.png')]
attackLeft = [pygame.image.load('LA1.png'), pygame.image.load('LA1d1.png'), pygame.image.load('LA2d1.png'), pygame.image.load('LA2d2.png')]
jumpAttackRight = [pygame.image.load('RAJ1.png'), pygame.image.load('RAJ2.png'), pygame.image.load('RAJ3.png'), pygame.image.load('RAJ4d2.png'), pygame.image.load('RAJ4.png'), pygame.image.load('RAJ4.png')]
jumpAttackLeft = [pygame.image.load('LAJ1.png'), pygame.image.load('LAJ2.png'), pygame.image.load('LAJ3.png'), pygame.image.load('LAJ4d2.png'), pygame.image.load('LAJ4.png'), pygame.image.load('LAJ4.png')]
charr = pygame.image.load('playerd.png')
charl = pygame.image.load('playerleftd.png')
enemyr = pygame.image.load('enemyR.png')
enemyl = pygame.image.load('enemyL.png')
ewr = [pygame.image.load('enemyRd2.png'), pygame.image.load('enemyR1.png'), pygame.image.load('enemyRd2.png'), pygame.image.load('enemyR2.png')]
ewl = [pygame.image.load('enemyL.png'), pygame.image.load('enemyL1.png'), pygame.image.load('enemyL.png'), pygame.image.load('enemyL2.png')]
ear = [pygame.image.load('enemyRd2.png'), pygame.image.load('enemyRd2.png'), pygame.image.load('enemyRd2.png'), pygame.image.load('enemyRd2.png')]
eal = [pygame.image.load('enemyL.png'), pygame.image.load('enemyL.png'), pygame.image.load('enemyL.png'), pygame.image.load('enemyL.png')]



class player(object):
    def __init__(self, x, y, width, height, direction, health, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkSoundCheck = True
        self.isJump = False
        self.jumpCount = 7
        self.direction = direction
        self.health = health
        self.attacking = False
        self.damaging = False
        self.damaged = False
        self.damage = damage
        self.attackCount = 0
        self.wasJump = False
        self.attackingHitbox = (self.x + 20, self.y + 5, 50, 60)
        self.hitbox = (self.x + 25, self.y, 14, 63)


    def attack(self, enemy):
        if not self.damaged and self.damaging and enemy.x > self.attackingHitbox[0] or enemy.x + enemy.width < self.attackingHitbox[0] + self.attackingHitbox[2] and enemy.y > self.attackingHitbox[1] or enemy.y + enemy.height < self.attackingHitbox[1] + self.attackingHitbox[3]:
            if not enemy.damaging:
                enemy.heath -= self.damage
                self.damaged= True
            else:
                print("CLANG!(from the player)")


    def draw(self, win):
        if not self.isJump and self.wasJump:
            self.attacking = False
            self.wasJump = False
            self.damaging = False
            self.isJump = False
            self.attackCount = 0
        if not self.attacking:
            if self.left:
                try:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                except:
                    self.walkCount = 0
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.direction = "left"
            elif self.right:
                try:
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                except:
                    self.walkCount = 0
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.direction = "right"
            else:
                if self.direction == "right":
                    win.blit(charr, (self.x,self.y))
                if self.direction == "left":
                    win.blit(charl, (self.x,self.y))
        else:
            if not self.isJump and not self.wasJump:
                if self.direction == "left":
                    if self.attackCount < 12:
                        win.blit(attackLeft[self.attackCount//3], (self.x,self.y))
                        self.attackCount += 1
                    else:
                        self.attacking = False
                        self.attackCount = 0
                    if self.attackCount < 7:
                        self.damaging = False
                    else:
                        self.damaging = True
                elif self.direction == "right":
                    if self.attackCount < 12:
                        win.blit(attackRight[self.attackCount//3], (self.x,self.y))
                        self.attackCount += 1
                    else:
                        self.attacking = False
                        self.attackCount = 0
                    if self.attackCount < 7:
                        self.damaging = False
                    else:
                        self.damaging = True
            else:
                self.wasJump = True
                if self.direction == "left":
                    if self.attackCount < 18:
                        win.blit(jumpAttackLeft[self.attackCount//3], (self.x,self.y))
                        self.attackCount += 1
                    else:
                        self.attackCount = 0
                        self.attacking = False
                        self.wasJump = False
                    if self.attackCount < 9:
                        self.damaging = False
                    else:
                        self.damaging = True
                elif self.direction == "right":
                    if self.attackCount < 18:
                        win.blit(jumpAttackRight[self.attackCount//3], (self.x,self.y))
                        self.attackCount += 1
                    else:
                        self.attackCount = 0
                        self.attacking = False
                        self.wasJump = False
                    if self.attackCount < 9:
                        self.damaging = False
                    else:
                        self.damaging = True

        """
        if self.damaging and self.isJump:
            #print("Jump attack")
            pygame.draw.rect(win, (255, 0, 100), self.attackingHitbox, 2)
            
        elif self.damaging:
            #print("Normal attack")
            pygame.draw.rect(win, (255, 0, 0), self.attackingHitbox, 2)
        pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
        """

class enemy:
    def __init__(self, x, y, width, height, direction, health, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkSoundCheck = True
        self.direction = direction
        self.health = health
        self.attacking = False
        self.willAttack = False
        self.damaging = False
        self.damaged = False
        self.damage = damage
        self.attackCount = 0
        self.attackingHitbox = (man.x - 4, man.y + 5, 45, 60)#(self.x - 32, self.y + 15, 64, 113)
        self.hitbox = (self.x + self.width // 4, self.y + 30, self.width//2, self.height - 30)
    


    def attack(self, enemy):
        if not self.damaged and self.damaging and enemy.x > self.attackingHitbox[0] or enemy.x + enemy.width < self.attackingHitbox[0] + self.attackingHitbox[2] and enemy.y > self.attackingHitbox[1] or enemy.y + enemy.height < self.attackingHitbox[1] + self.attackingHitbox[3]:
            if not enemy.damaging:
                enemy.heath -= self.damage
                self.damaged = True
            else:
                print("CLANG!(from the enemy)")


    def turn_to_player(self, player):
        if not self.attacking:
            if player.x < self.x + (self.width//2) - 15:
                self.direction = "left"
            else:
                self.direction = "right"
    
    def detect_player(self, player):#attack range: 64px
        if player.x > self.x - 48 and player.x < self.x + self.width - 8:
            self.attacking = True
            self.willAttack = True
        elif self.willAttack:
            self.attacking = True
        else:
            self.attacking = False
    
    def draw(self, win):
        self.attacking = bool(self.willAttack)
        if not self.attacking:
            if self.left:
                try:
                    win.blit(ewl[self.walkCount//4], (self.x,self.y))
                except:
                    self.walkCount = 0
                    win.blit(ewl[self.walkCount//4], (self.x,self.y))
                self.walkCount += 1
                self.direction = "left"
            elif self.right:
                try:
                    win.blit(ewr[self.walkCount//4], (self.x,self.y))
                except:
                    self.walkCount = 0
                    win.blit(ewr[self.walkCount//4], (self.x,self.y))
                self.walkCount +=1
                self.direction = "right"
            else:
                if self.direction == "right":
                    win.blit(enemyr, (self.x,self.y))
                if self.direction == "left":
                    win.blit(enemyl, (self.x,self.y))
        else:
            if self.direction == "left":
                if self.attackCount < 28:
                    win.blit(eal[self.attackCount//7], (self.x,self.y))
                    self.attackCount += 1
                else:
                    self.attacking = False
                    self.attackCount = 0
                    self.willAttack = False
                if self.attackCount < 15:
                    self.damaging = False
                else:
                    self.damaging = True
            elif self.direction == "right":
                if self.attackCount < 28:
                    win.blit(ear[self.attackCount//7], (self.x,self.y))
                    self.attackCount += 1
                else:
                    self.attacking = False
                    self.attackCount = 0
                    self.willAttack = False
                if self.attackCount < 15:
                    self.damaging = False
                else:
                    self.damaging = True
        """
        if self.damaging:
            #print("Normal attack")
            pygame.draw.rect(win, (255, 0, 0), self.attackingHitbox, 2)
        pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
        return
        """
    








            
background_counter = 0
def redrawGameWindow(counter):
    if counter < 10:
        win.blit(background1, (0,0))
    elif counter < 20:
        win.blit(background2, (0,0))
    elif counter < 31:
        win.blit(background3, (0,0))
    enemyy.draw(win)
    man.draw(win)
    pygame.display.update()
    counter += 1
    if counter > 30:
        counter = 0
    return counter

man = player(162, 600, 64, 64, "right", 99999999999, 1)
enemyy = enemy(800, 536, 128, 128, "left", 99999999999, 1)
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    #print(man.attacking, man.wasJump, man.isJump, man.attackCount)
    #print(man.isJump)
    
    if keys[pygame.K_SPACE]:
        if not man.attacking:
            man.attacking = True
    
    if (man.attacking and man.isJump) or not man.attacking:
        if keys[pygame.K_LEFT] and man.x > 110:#90
            man.x -= man.vel
            man.left = True
            man.right = False
            man.attackingHitbox = (man.x - 4, man.y + 5, 45, 60)
            man.hitbox = (man.x + 25, man.y, 14, 63)
        elif keys[pygame.K_RIGHT] and man.x < 1200:
            man.x += man.vel
            man.right = True
            man.left = False
            man.attackingHitbox = (man.x + 23, man.y + 5, 45, 60)
            man.hitbox = (man.x + 25, man.y, 14, 63)
        else:
            man.right = False
            man.left = False
            man.walkCount = 0
            if man.direction == "right":
                man.attackingHitbox = (man.x + 23, man.y + 5, 45, 60)
                man.hitbox = (man.x + 25, man.y, 14, 63)
            if man.direction == "left":
                man.attackingHitbox = (man.x - 4, man.y + 5, 45, 60)
                man.hitbox = (man.x + 25, man.y, 14, 63)
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0            
    else:
        if man.jumpCount >= -7:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 7
    
    enemyy.turn_to_player(man)
    enemyy.detect_player(man)
    if enemyy.direction == "left" and not enemyy.attacking:
        enemyy.x -= enemyy.vel
        enemyy.left = True
        enemyy.right = False
        enemyy.attackingHitbox = (enemyy.x - 32, enemyy.y + 15, 110, 113)#(enemyy.x - 4, enemyy.y + 5, 45, 60)
        enemyy.hitbox = (enemyy.x + enemyy.width // 4, enemyy.y + 30, enemyy.width//2, enemyy.height - 30)#(enemyy.x + 25, enemyy.y, 14, 63)
    elif enemyy.direction == "right" and not enemyy.attacking:
        enemyy.x += enemyy.vel
        enemyy.left = False
        enemyy.right = True
        enemyy.attackingHitbox = (enemyy.x + 64, enemyy.y + 15, 96, 113)#(enemyy.x + 23, enemyy.y + 5, 45, 60)
        enemyy.hitbox = (enemyy.x + enemyy.width // 4, enemyy.y + 30, enemyy.width//2, enemyy.height - 30)#(enemyy.x + 25, enemyy.y, 14, 63)
    else:
        enemyy.right = False
        enemyy.left = False
        enemyy.walkCount = 0
        if enemyy.direction == "right":
            enemyy.attackingHitbox = (enemyy.x + 64, enemyy.y + 15, 96, 113)#(enemyy.x + 23, enemyy.y + 5, 45, 60)
            enemyy.hitbox = (enemyy.x + enemyy.width // 4, enemyy.y + 30, enemyy.width//2, enemyy.height - 30)#(enemyy.x + 25, enemyy.y, 14, 63)
        if enemyy.direction == "left":
            enemyy.attackingHitbox = (enemyy.x - 32, enemyy.y + 15, 110, 113)#(enemyy.x - 4, enemyy.y + 5, 45, 60)
            enemyy.hitbox = (enemyy.x + enemyy.width // 4, enemyy.y + 30, enemyy.width//2, enemyy.height - 30)#(enemyy.x + 25, enemyy.y, 14, 63)




    background_counter = redrawGameWindow(background_counter)


    pygame.display.update()
