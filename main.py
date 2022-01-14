import Printer
import Bresenham
import Curve
from tkinter import *

points = Bresenham.Bresenham.Poliline([(0,0),(30,10),(0,20)])
Bresenham.Bresenham.Draw(points, poli=True)
Printer.CriarTemplate()
mainloop()