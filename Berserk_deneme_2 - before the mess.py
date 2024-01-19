
# Modification date: Thu Nov 18 20:33:10 2021

# Production date: Sun Sep  3 15:43:23 2023

import pygame

# initialize the pygame
pygame.init()

# create the screen(width, height)
win = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load("background.png")

# Keys
keys = pygame.key.get_pressed()

# Title and icon
pygame.display.set_caption("Berserk")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


# Walking
walkRight = [pygame.image.load('R2d2.png'), pygame.image.load('R3d2.png'), pygame.image.load('R4d2.png'), pygame.image.load('R5d2.png'), pygame.image.load('R8d2.png'), pygame.image.load('R9d2.png'), pygame.image.load('R10d2.png'), pygame.image.load('R11d2.png')]
walkLeft = [pygame.image.load('L2d.png'), pygame.image.load('L3d.png'), pygame.image.load('L4d.png'), pygame.image.load('L5d.png'), pygame.image.load('L8d.png'), pygame.image.load('L9d.png'), pygame.image.load('L10d.png'), pygame.image.load('L11d.png')]
attackRight = [pygame.image.load('RA1d.png'), pygame.image.load('R3d2.png'), pygame.image.load('R4d2.png'), pygame.image.load('R5d2.png')]
attackLeft = [pygame.image.load('L2d.png'), pygame.image.load('L3d.png'), pygame.image.load('L4d.png'), pygame.image.load('L5d.png')]
background = pygame.image.load('background.png')
emap = 0
eemap = 0
charr = pygame.image.load('playerd.png')
charl = pygame.image.load('playerleftd.png')
#gigip = pygame.image.load('gigi.png')



class player(object):
    def __init__(self, x, y, width, height, direction):
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
        self.direction = "right"
        self.attacking = False
        self.attackCount = 0
        self.attackingHitbox = (self.x + 20, self.y + 5, 50, 60)
        self.hitbox = (self.x + 25, self.y, 14, 63)

    #walk right
    def walkRight(self):
        if keys[pygame.K_RIGHT] and self.x < 1200:
            self.x += self.vel
            self.right = True
            self.left = False
            self.attackingHitbox = (self.x + 23, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)
        try:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
        except:
            self.walkCount = 0
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
        finally:
            self.walkCount +=1
            self.direction = "right"
    
    #walk left
    def walkLeft(self):
        if keys[pygame.K_LEFT] and self.x > 110:#90
            self.x -= self.vel
            self.left = True
            self.right = False
            self.attackingHitbox = (self.x - 4, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)
        try:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
        except:
            self.walkCount = 0
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
        finally:
            self.walkCount += 1
            self.direction = "left"

    #stand
    def stand(self):
        self.right = False
        self.left = False
        self.walkCount = 0
        if self.direction == "right":
            self.attackingHitbox = (self.x + 23, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)
        if self.direction == "left":
            self.attackingHitbox = (self.x - 4, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)

        if self.direction == "right":
                win.blit(charr, (self.x,self.y))
        if self.direction == "left":
                win.blit(charl, (self.x,self.y))
    
    #attack left
    def attackLeft(self):
        if self.attackCount < 12:
            win.blit(attackLeft[self.attackCount//3], (self.x,self.y))
            self.attackCount += 1
        else:
            self.attacking = False
            self.attackCount = 0
    
    #attack right
    def attackRight(self):
        if self.attackCount < 12:
            win.blit(attackRight[self.attackCount//3], (self.x,self.y))
            self.attackCount += 1
        else:
            self.attacking = False
            self.attackCount = 0
    
    #draw hitbox and attacking hitbox
    def drawHitboxes(self):
        pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.attackingHitbox, 2)
    

    #draw all on the screen
    def draw(self, win):
        if not self.attacking:
            if self.left:
                walkLeft(self)
            elif self.right:
                walkRight(self)
            else:
                stand(self)
        else:
            if self.left:
                attackLeft(self)
            elif self.right:
                attackRight(self)
        drawHitboxes(self)



def redrawGameWindow():
    win.blit(background, (0,0))
    man.draw(win)
    pygame.display.update()

man = player(162, 600, 64, 64, "right")
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    print(man.attackCount)
    
    if keys[pygame.K_SPACE]:
        if not man.attacking:
            man.attacking = True

            
        
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

    redrawGameWindow()


    pygame.display.update()
