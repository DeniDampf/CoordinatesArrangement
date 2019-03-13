import pygame
import CoSystem

pygame.init()


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0) 

running = True
size = [400, 300]

CoSystem.drawCoSystem(4,3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    shell = pygame.display.set_mode(size)
    shell.fill(WHITE)
    
    pygame.draw.line(shell, BLACK, [0, 0], [50,30], 5)
    pygame.draw.circle(shell, BLUE, [60, 250], 2)

    pygame.display.flip()

pygame.quit() 


