import numpy as np

import pygame


factor = 100
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


def drawPoint(display,point):
    pygame.draw.circle(display, RED, [int(point.xPrediction*factor + biasX),int(point.yPrediction*factor + biasY)], 3)

def drawPointConnections(display,point):
      

    for neighbour in point.neighbours: 
        pointCoords = coordToInt([point.xPrediction,point.yPrediction])
        neighbourCoords = coordToInt([neighbour.xPrediction,neighbour.yPrediction])
        pygame.draw.line(display, BLACK,pointCoords,neighbourCoords, 1)
        
def coordToInt(coord):   
    return [int(coord[0]*factor + biasX),int(coord[1]*factor + biasY)]



    

     
