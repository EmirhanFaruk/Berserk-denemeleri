
# Modification date: Thu Nov 18 21:54:02 2021

# Production date: Sun Sep  3 15:43:23 2023

import pygame



#self note: dont put function into function containing win.blit or its not gonna work well
# initialize the pygame
pygame.init()

# create the screen(width, height)
win = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load("background.png")

# self.keys
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


        self.keys = pygame.key.get_pressed()



    #walk right
    def walkRight(self, x, right, left, attackingHitbox, hitbox, walkCount, direction):
        self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction = x, right, left, attackingHitbox, hitbox, walkCount, direction
        self.x += self.vel
        self.right = True
        self.left = False
        self.attackingHitbox = (self.x + 23, self.y + 5, 45, 60)
        self.hitbox = (self.x + 25, self.y, 14, 63)
        try:
            win.blit(walkRight[self.walkCount//2], (self.x,self.y))
            trydone = 1
        except:
            self.walkCount = 0
            win.blit(walkRight[self.walkCount//2], (self.x,self.y))
            trydone = 2
        finally:
            self.walkCount +=1
            self.direction = "right"
            if trydone == 1:
                return self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction, trydone
            else:
                return self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction, trydone
    
    #walk left
    def walkLeft(self, x, right, left, attackingHitbox, hitbox, walkCount, direction):
        self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction = x, right, left, attackingHitbox, hitbox, walkCount, direction
        self.x -= self.vel
        self.left = True
        self.right = False
        self.attackingHitbox = (self.x - 4, self.y + 5, 45, 60)
        self.hitbox = (self.x + 25, self.y, 14, 63)
        try:
            win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
            trydone = 1
        except:
            self.walkCount = 0
            win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
            trydone = 2
        finally:
            self.walkCount += 1
            self.direction = "left"
            if trydone == 1:
                return self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction, trydone
            else:
                return self.x, self.right, self.left, self.attackingHitbox, self.hitbox, self.walkCount, self.direction, trydone
    
    """
    #Jumping
    def jump_ready(self):
        if self.keys[pygame.K_UP]:
            self.isJump = True
            self.right = False
            self.left = False
            self.walkCount = 0
    
    def jump_notready(self):
          if self.jumpCount >= -7:
              neg = 1
              if self.jumpCount < 0:
                  neg = -1
              self.y -= (self.jumpCount ** 2) * 0.5 * neg
              self.jumpCount -= 1
          else:
              self.isJump = False
              self.jumpCount = 7


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
    """
    #stand
    def stand(self, right, left, walkCount, direction, attackingHitbox, hitbox):
        self.right, self.left, self.walkCount, self.direction, self.attackingHitbox, self.hitbox = right, left, walkCount, direction, attackingHitbox, hitbox
        self.right = False
        self.left = False
        self.walkCount = 0
        if self.direction == "right":
            self.attackingHitbox = (self.x + 23, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)
            
        if self.direction == "left":
            self.attackingHitbox = (self.x - 4, self.y + 5, 45, 60)
            self.hitbox = (self.x + 25, self.y, 14, 63)
                
        return self.right, self.left, self.walkCount, self.direction, self.attackingHitbox, self.hitbox
    
    #draw all on the screen
    def draw(self, win):
        #draw hitbox and attacking hitbox(smh didnt accept the function i created so i did this)
        pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.attackingHitbox, 2)
        



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

    
    keys = pygame.key.get_pressed()
    log = man.x, man.y
    
    print(log)
    
    if keys[pygame.K_SPACE]:
        if not man.attacking:
            man.attacking = True
            if man.direction == "left":
                if man.attackCount < 12:
                    win.blit(attackLeft[man.attackCount//3], (man.x,man.y))
                    man.attackCount += 1
                else:
                    man.attacking = False
                    man.attackCount = 0
            else:
                if man.attackCount < 12:
                    win.blit(attackRight[man.attackCount//3], (man.x,man.y))
                    man.attackCount += 1
                else:
                    man.attacking = False
                    man.attackCount = 0

    if keys[pygame.K_RIGHT] and man.x < 1200:
        man.x, man.right, man.left, man.attackingHitbox, man.hitbox, man.walkCount, man.direction, trydone = man.walkRight(man.x, man.right, man.left, man.attackingHitbox, man.hitbox, man.walkCount, man.direction)
        win.blit(walkRight[man.walkCount//2], (man.x, man.y))
    elif keys[pygame.K_LEFT] and man.x > 110:#90
        man.x, man.right, man.left, man.attackingHitbox, man.hitbox, man.walkCount, man.direction, trydone = man.walkLeft(man.x, man.right, man.left, man.attackingHitbox, man.hitbox, man.walkCount, man.direction)
        win.blit(walkLeft[man.walkCount//2], (man.x, man.y))

    else:
        man.right, man.left, man.walkCount, man.direction, man.attackingHitbox, man.hitbox = man.stand(man.right, man.left, man.walkCount, man.direction, man.attackingHitbox, man.hitbox)
        if man.direction == "right":
            win.blit(charr, (man.x, man.y))
        else:
            win.blit(charl, (man.x, man.y))

    if keys[pygame.K_UP]:
        if not man.isJump:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    if man.isJump:
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
