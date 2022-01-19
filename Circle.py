import Printer
from tkinter import *
class Circle: 

    def DrawCircle(self, x, y, center):
        Printer.DesenharPixel( x + center[0],  y + center[1],)
        Printer.DesenharPixel( y + center[0],  x + center[1],)
        Printer.DesenharPixel( y + center[0], -x + center[1],)
        Printer.DesenharPixel( x + center[0], -y + center[1],)
        Printer.DesenharPixel(-x + center[0], -y + center[1],)
        Printer.DesenharPixel(-y + center[0], -x + center[1],)
        Printer.DesenharPixel(-y + center[0],  x + center[1],)
        Printer.DesenharPixel(-x + center[0],  y + center[1],)

    def Draw(self, center, radius):
        points = []
        x, y = 0, round(radius)
        err = 3 - 2 * radius

        points.append([x,y])
        
        self.DrawCircle(x, y, center)
        
        while y >= x: 
            x += 1
            if err > 0:
                y -=1
                err = err + 4 * (x - y) + 10
            else:
                err = err + 4 * x + 6
            points.append([x,y])
            self.DrawCircle(x, y, center)
        
        return points
        
c = Circle()

c.Draw([25,13], 27.65)