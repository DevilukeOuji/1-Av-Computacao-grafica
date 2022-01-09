import Printer
import Line
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
        print(points)
        for r in range(1,n):
            for i in range(n-r):
                x = np.array(points[i]) * (1-t)
                y = np.array(points[i+1]) * t
                points[i] =  (x,y) #np.dot(x,y)
        return points[0]
    
    def draw(self,):
        numLines = round(len(self.controlPt) / 2 + 2)
        for i in range(1, numLines):
            t = (1.0 / numLines) * i
            self.finalPoint = Curve.DeCasteljau(self, t)
            Line.Line.Line(self.initialPoint, self.finalPoint)

            self.initialPoint = self.finalPoint

c = Curve((2,4),(12,9),[2,4,7,8])
c.draw()