import pygame
from pygame.locals import *
import os
import sys
import math
import spritesheet
from settings import *

pygame.init()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()
FPS = 120
frames = FPS/12

class player(object):
    run = [win.blit(run1, (0, 0)), win.blit(run2, (72, 0)), win.blit(run3, (150, 0)), win.blit(run4, (250, 0)), win.blit(run5, (250, 0)), win.blit(run6, (250, 0)), win.blit(run7, (250, 0)), win.blit(run8, (250, 0))]
    jump = [SpriteStripAnim('images/Soldier_1/Idle.png', (0,0,24,24), 8, 1, True, frames)]
    # slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width  
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1
            
        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1


def redrawWindow():
    win.blit(bg, (bgX, 0))  
    win.blit(bg, (bgX2, 0))
    runner.draw(win) # NEW
    pygame.display.update() 

# Call this from the game loop!

pygame.time.set_timer(USEREVENT+1, 500) # Sets the timer for 0.5 seconds
# This should go above the game loop
runner = player(200, 313, 64, 64)
# This should go above our game loop

run = True
speed = 30  # NEW
n = 0
run[n].iter()
image = run[n].next()

while run:
    redrawWindow() 
    bgX -= 1.4  
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:  
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()
    
        if event.type == USEREVENT+1: # Checks if timer goes off
            speed += 1 # Increases speed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]: # If user hits space or up arrow key
        if not(runner.jumping):  # If we are not already jumping
            runner.jumping = True

    if keys[pygame.K_DOWN]:  # If user hits down arrow key
        if not(runner.sliding):  # If we are not already sliding
            runner.sliding = True

    clock.tick(speed)  # NEW

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()