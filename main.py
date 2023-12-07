import pygame as pg
from pygame.locals import *
import os
import sys
import math
import random
from player import player
from sprites import wall, spike
from settings import *

pg.init()

clock = pg.time.Clock()

def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score
               
    return last



def endScreen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []
                   
    run = True
    while run:
        pg.time.delay(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                run = False
                runner.falling = False
                runner.sliding = False
                runner.jumping = False

        win.blit(bg, (0,0))
        largeFont = pg.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
        currentScore = largeFont.render('Score: '+ str(score),1,(255,255,255))
        win.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        win.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pg.display.update()
    score = 0


def redrawWindow():
    largeFont = pg.font.SysFont('comicsans', 30)
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
    runner.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)

    win.blit(text, (700, 10))
    pg.display.update()


pg.time.set_timer(USEREVENT+1, 500)
pg.time.set_timer(USEREVENT+2, 3000)
speed = 30

score = 0

run = True
runner = player(200, 313, 64, 64)

obstacles = []
pause = 0
fallSpeed = 0

while run:
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()
        
    score = speed//10 - 3

    for obstacle in obstacles:
        if obstacle.collide(runner.hitbox):
            runner.falling = True
            
            if pause == 0:
                pause = 1
                fallSpeed = speed
        if obstacle.x < -64:
            obstacles.pop(obstacles.index(obstacle))
        else:
            obstacle.x -= 1.4
    
    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width() 
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
            
        if event.type == USEREVENT+1:
            speed += 1
            
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0:
                obstacles.append(wall(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(spike(810, 0, 48, 310))
                
    if runner.falling == False:
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            if not(runner.jumping):
                runner.jumping = True

        if keys[pg.K_DOWN]:
            if not(runner.sliding):
                runner.sliding = True

    clock.tick(speed)
    redrawWindow()