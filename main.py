import pygame
import CoDrawService
import CoDataService
import numpy as np

pygame.init()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0) 

running = True
size = [600, 500]
factor = 40
biasX = 20
biasY = 20

xDim = 4
yDim = 3

points = CoDataService.getPoints(xDim,yDim)

#init
CoDataService.setSouthEastNeighbours(points)
CoDataService.setRandomPredictionPoints(points,xDim,yDim)


xxx = CoDataService.findPoint(points,1,1)

for c in range(len(xxx.neighbours)):
    print('x: ' + str(xxx.neighbours[c].x) + ' y: ' + str( xxx.neighbours[c].y))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    shell = pygame.display.set_mode(size)
    shell.fill(WHITE)

    CoDrawService.drawCoordSystem(shell,xDim,yDim)
    
    for d in range(len(points)):
        CoDrawService.drawPoint(shell,points[d])

    CoDrawService.drawPointConnections(shell,CoDataService.findPoint(points,1,1))



    pygame.display.flip()

pygame.quit() 


