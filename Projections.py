import numpy as np
import Printer
from tkinter import *
from Bresenham import Bresenham

def getMatrix(side, fatia):

    if side == 'front':  #frontal  (x/y)
        return np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0], 
                        [0, 0, 0, 1]])

    elif side == 'side': #lateral (y/z)
        return  np.array([[0, 1, 0, 0], 
                        [0, 0, 0, 1], 
                        [0, 0, 0, 1]])

    elif side == 'ground': #planta (x/z)
        return np.array([[1, 0, 0, 0],
                        [0, 0, 0, 1], 
                        [0, 0, 0, 1]])
    else:
        print("There's no such side.")
        return None

def Parallel(polygon, side, fatia=0):
    polygon = np.array(polygon).transpose()
    matrix = getMatrix(side, fatia).transpose()
    polygon = matrix.dot(polygon)

    if side == 'front': #[[],[]] a[1:]
        return np.delete(polygon,2,0)

    elif side == 'side':
        return np.delete(polygon,0,0)

    elif side == 'ground':
        return np.delete(polygon,1,0)

strange_cube = [[0,0,2],[2,0,2],[2,1,2],[0,1,2],[0,0,0],[2,0,0],[2,2,0],[0,2,0]]
project = Parallel(strange_cube, 'front')
points = Bresenham.Poliline(project)
flat_list = [item for sublist in points for item in sublist]
print(flat_list)
Bresenham.Draw(flat_list)
Printer.CriarTemplate()
mainloop()
