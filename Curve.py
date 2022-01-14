import Printer
import Bresenham
import numpy as np
class Curve:

    def __init__(self,initial_point,final_point, controlPt:list):
        self.initialPoint = initial_point
        self.finalPoint = final_point
        self.controlPt = controlPt

    def DeCasteljau(self, t:float):
        points = []
        n = len(self.controlPt)
        for i in range(n):
            points += [[self.controlPt[i]]]
        for r in range(1,n):
            for i in range(n-r):
                x = np.array(points[i]) * (1-t)
                y = np.array(points[i+1]) * t
                if r == 1 and i == 0:
                    points[i] = (x,y) 
                else:
                    point = np.dot(x,y)
                    point_flatten = point.flatten()
                    points[i] = point_flatten
        return points[0]
    
    def draw(self,):
        conj = []
        numLines = round(len(self.controlPt) / 2 + 2)
        b = Bresenham.Bresenham
        for i in range(1, numLines):
            t = (1.0 / numLines) * i
            self.finalPoint = Curve.DeCasteljau(self, t)
            
            conj += b.Bresenham(self.initialPoint, self.finalPoint)
            b.draw(conj)
            self.initialPoint = self.finalPoint