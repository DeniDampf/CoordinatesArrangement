import pygame
import Services.CoDrawService as CoDrawService
import Services.CoDataService as CoDataService
import Services.TrainingService as TrainingService

import numpy as np

pygame.init()

# TODO: Move to helper class
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0) 

running = True
size = [1400, 1000]


xDim = 40    
yDim = 30

points = CoDataService.getPoints(xDim,yDim)

#init
CoDataService.setSouthEastNeighbours(points)


trainingModel = TrainingService.TrainingService(points,xDim,yDim)
trainingModel.predictCoordsModel()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #SPACE pressed
            if event.key == 32:
                print('Thanks for pressing SPACE')
                trainingModel.trainCoordsModel()
                trainingModel.predictCoordsModel()
   
    shell = pygame.display.set_mode(size)
    shell.fill(WHITE)

    CoDrawService.drawCoordSystem(shell,xDim,yDim)
     
    for d in range(len(points)):
        CoDrawService.drawPoint(shell,points[d])

    for point in points:        
        CoDrawService.drawPointConnections(shell,point)

    pygame.display.flip()

pygame.quit() 


