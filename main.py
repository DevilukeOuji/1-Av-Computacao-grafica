import Printer
import Bresenham
import Curve
import Scanline
from tkinter import *
polygon = [(0,5),(0,30),(10,20),(25,30),(25,0)]

points = Bresenham.Bresenham.Poliline(polygon)
Bresenham.Bresenham.Draw(points, poli=True)
scanline = Scanline.Scanline(polygon)
scanline.Scanline(points)


Printer.CriarTemplate()
mainloop()