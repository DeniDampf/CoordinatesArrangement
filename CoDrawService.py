import numpy as np

import pygame


factor = 40
biasX = 20
biasY = 20

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0) 

def drawCoordSystem(display,xDim,yDim):

    for x in range(xDim):
        for y in range(yDim):
            pygame.draw.circle(display, BLUE, [x*factor + biasX, y*factor + biasY], 2)
     
