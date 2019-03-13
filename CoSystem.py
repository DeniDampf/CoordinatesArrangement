import numpy as np

def drawCoSystem(x,y):
    coords = np.zeros((x,y,2))
    print(coords.shape)

    for xx in range(x):
        for yy in range(y):
            print(str(xx) + '/' + str (yy))
            coords[xx,yy] = [xx,yy]
           

    print(coords)