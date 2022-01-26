import Bresenham
import Printer as Printer
from tkinter import *

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

x_max = 50
y_max = 50
x_min = -50
y_min = -50

def computeCode(x,y):
    code = INSIDE
  
    if (x < x_min): code |= LEFT
    elif x > x_max: code |= RIGHT

    if y < y_min: code |= BOTTOM 
    elif y > y_max: code |= TOP 

    return code

def LineClipping(point1, point2):
    x1,y1 = point1[0], point1[1]
    x2,y2 = point2[0], point2[0]

    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
  
    accepted = False
  
    while True:

        if code1 == 0 and code2 == 0:  
            accepted = True
            break
        elif (code1 & code2): break
        else: 
            code_out = None
            x,y = None, None
  
            if code1 != 0: code_out = code1
            else: code_out = code2

            if code_out & TOP: #po is above the clip rectangle
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            
            elif code_out & BOTTOM: #po is below the rectangle
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            
            elif code_out & RIGHT: #po is to the right of rectangle
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            
            elif code_out & LEFT: #po is to the left of rectangle
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1: 
                x1, y1 = x, y
                code1 = computeCode(x1, y1)
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2)

    if accepted:
        print(f"Line accepted from {x1}, {y1} to {x2}, {y2}")
        points = Bresenham.Bresenham([x1,y1], [x2,y2])
        Bresenham.Draw(points)
    else: print('Line rejected')
