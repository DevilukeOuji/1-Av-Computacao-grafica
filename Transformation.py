from math import sin, cos
from Bresenham import Poliline
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
    polygon = Translation(polygon,0, 0)
    new_polygon = []
    for point in polygon:
        new_x = point[0] * cos(angle) - point[1] * sin(angle)
        new_y = point[0] *sin(angle) + point[1]* cos(angle)
        new_polygon.append([new_x,new_y])
    return new_polygon
