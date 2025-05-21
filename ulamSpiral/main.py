import pygame as pg
import sys
import math
import numpy

WIDTH =  1280
HEIGHT = 720
TITLE = "Spiralle"


pg.init()
pg.font.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((0,0,0))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

class Draw():
    def __init__(self):
        self.font = pg.font.SysFont('Comic Sans MS', 10)
        self.step = 1
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.stepSize = 15
        self.numSteps = 1
        self.state = 0
        
    def isPrime(self, value):
        self.i = 2
        if (value == 1): return False
        for self.i in range(2, value):
            if self.i <= math.sqrt(value):
                if (value % self.i == 0):
                    return False
        return True

    def spawn(self):
        self.step_display = self.font.render(str(self.step), False, (0, 250, 0))
        # screen.blit(self.step_display, (self.x ,self.y))
        if self.isPrime(self.step):
            screen.blit(self.step_display, (self.x ,self.y))

        match self.state:
            case 0:
                self.x += self.stepSize
            case 1:
                self.y -= self.stepSize
            case 2:
                self.x -= self.stepSize
            case 3:
                self.y += self.stepSize

        if (self.step % self.numSteps == 0):
            self.state = (self.state + 1) % 4
            
            if (self.state % 2 == 0):
                self.numSteps += 1
        
        if (self.y == HEIGHT):
            self.stepSize = 0

        self.step += 1 

draw = Draw()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
    draw.spawn()
    # draw.isPrime(7)
    pg.display.flip()
    clock.tick(120)
    
pg.quit()