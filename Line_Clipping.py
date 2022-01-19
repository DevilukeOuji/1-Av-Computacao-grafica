from contextlib import nullcontext
import Bresenham
import Printer
from tkinter import *


INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

x_max = 74 #pick those as args
y_max = 74
x_min = -74
y_min = -74

def computeCode(x,y):
    code = INSIDE
  
    if (x < x_min): code |= LEFT #left
    elif x > x_max: code |= RIGHT#right

    if y < y_min: code |= BOTTOM #below
    elif y > y_max: code |= TOP #above

    return code


# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x2, y2) to P2 = (x2, y2)
def cohenSutherlandClip( x1,  y1,
                          x2,  y2):

    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
  
    #Initialize line as outside the rectangular window
    accepted = False
  
    while True:
        #both inside
        if code1 == 0 and code2 == 0:  
            accepted = True
            break
        
        #both outside
        elif (code1 & code2): break
        
        else: #Some segment of line lies within the rectangle
            code_out = None
            x,y = None, None
  
            #At least one endpo is outside the
            #rectangle, pick it.
            if code1 != 0: code_out = code1
            else: code_out = code2
  
            #Find using formulas y = y1 + slope * (x - x1), x = x1 + (1  / slope) * (y - y1)

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
            
             #Now ersection po x, y is found
             #We replace po outside rectangle
             #by ersection po
            if code_out == code1: 
                x1, y1 = x, y
                code1 = computeCode(x1, y1)
            else:
                x2, y2 = x, y
                code2 = computeCode(x2, y2)

    if accepted:
        print(f"Line accepted from {x1}, {y1} to {x2}, {y2}")
        points = Bresenham.Bresenham.Bresenham([x1,y1], [x2,y2])
        Bresenham.Bresenham.Draw(points)
    else: print('Line rejected')

cohenSutherlandClip(5,5, 84, 78);

Printer.CriarTemplate()
mainloop()