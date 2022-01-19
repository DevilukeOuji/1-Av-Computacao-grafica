from math import sin, cos
from Bresenham import Bresenham
import Printer
from tkinter import *
def Translation(polygon, x,y):
    new_polygon = []
    for point in polygon:
        new_x = point[0] + x 
        new_y = point[1] + y
        new_polygon.append([new_x,new_y])
    return new_polygon

def Scale(polygon, x_scalar, y_scalar):
    new_polygon = []
    if y_scalar == 0: y_scalar = 1
    if x_scalar == 0: x_scalar = 1
    for point in polygon:
        new_x = point[0] * x_scalar 
        new_y = point[1] * y_scalar
        new_polygon.append([new_x,new_y])
    return new_polygon

def Rotation(polygon, angle):
    polygon = Translation(polygon,-40,-40)
    new_polygon = []
    for point in polygon:
        new_x = point[0] * cos(angle) - point[1] * sin(angle)
        new_y = point[0] *sin(angle) + point[1]* cos(angle)
        new_polygon.append([new_x,new_y])
    return new_polygon

rect = [[10,10],[10,40],[40,40],[40,10]]
points = Bresenham.Poliline(rect)
flat_list = [item for sublist in points for item in sublist]
translated_rect = Rotation(flat_list, 60)
Bresenham.Draw(points, poli=True)

print(flat_list == translated_rect)
Bresenham.Draw(points = translated_rect, color = Printer.violet)
Printer.CriarTemplate()
mainloop()