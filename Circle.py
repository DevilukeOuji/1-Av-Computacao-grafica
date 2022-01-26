from tkinter import *
from Paint import PaintPixel

def DrawCircle(x, y, center):
    PaintPixel( x + center[0],  y + center[1],)
    PaintPixel( y + center[0],  x + center[1],)
    PaintPixel( y + center[0], -x + center[1],)
    PaintPixel( x + center[0], -y + center[1],)
    PaintPixel(-x + center[0], -y + center[1],)
    PaintPixel(-y + center[0], -x + center[1],)
    PaintPixel(-y + center[0],  x + center[1],)
    PaintPixel(-x + center[0],  y + center[1],)

def Draw(center, radius):
    points = []
    x, y = 0, round(radius)
    err = 3 - 2 * radius

    points.append([x,y])
    
    DrawCircle(x, y, center)
    
    while y >= x: 
        x += 1
        if err > 0:
            y -=1
            err = err + 4 * (x - y) + 10
        else:
            err = err + 4 * x + 6
        points.append([x,y])
        DrawCircle(x, y, center)
    
    return points