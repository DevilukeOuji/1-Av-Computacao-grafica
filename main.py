'''import Printer as Printer
import Bresenham
import Curve
import Scanline
from tkinter import *
polygon = [[0,5],[0,30],[10,20],[25,28],[25,0]]

points = Bresenham.Bresenham.Poliline(polygon)
Bresenham.Bresenham.Draw(points, poli=True)
flat_list = [item for sublist in points for item in sublist]
scanline = Scanline.Scanline(flat_list)
scanline_points = scanline.Scanline()
Bresenham.Bresenham.Draw(scanline_points, poli=True)

Printer.CriarTemplate()
mainloop()'''