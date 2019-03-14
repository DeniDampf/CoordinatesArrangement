import pygame
import CoSystem
import numpy as np

pygame.init()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0) 

running = True
size = [400, 300]
factor = 40
biasX = 20
biasY = 20
coords = CoSystem.drawCoSystem(9,6)

print(coords)

if len(coords.shape) != 3:
    #TODO: throw exception
    print('something went wrong!!')
    coords = []
else:
    xDim = coords.shape[0]
    yDim = coords.shape[1]

print(coords.shape)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    shell = pygame.display.set_mode(size)
    shell.fill(WHITE)
    
    #pygame.draw.line(shell, BLACK, [0, 0], [50,30], 5)
    pygame.draw.circle(shell, BLUE, [60, 250], 2)

    for x in range(xDim):
        for y in range(yDim):            
            pygame.draw.circle(shell, BLUE, [x*factor + biasX, y*factor + biasY], 2)


    pygame.display.flip()

pygame.quit() 


