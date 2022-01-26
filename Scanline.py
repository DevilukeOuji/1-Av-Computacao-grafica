from Bresenham import Bresenham
import Printer
from tkinter import *
class Scanline:

    def __init__(self, edges) -> None:
        self.edges = edges
        self.critical_points = []
        
    def InvSlope(self, aux, point):
        return (1.0 * aux[0] - point[0]) / (1.0 * aux[1] - point[1])


    def GetMax(self, Y_list):
        Ymin, Ymax = min(Y_list), max(Y_list)
        return Ymin,Ymax

    def BoundBox(self):
        Y_list = []
        edges = self.edges
        edges_length = len(self.edges)
        for i in range(edges_length):
            aux = edges[(i+1) % edges_length]
            x, y = edges[i][0], edges[i][1]

            if y < aux[1]:
                self.critical_points += [{ "index": i,
                "dir": 1,
                "xIntersection": x,
                "invSlope": Scanline.InvSlope(self, aux, edges[i])}]

            aux = edges[(i-1 + edges_length)% edges_length]

            if y < aux[1]:
                self.critical_points += [{ "index": i,
                "dir": -1,
                "xIntersection": x,
                "invSlope": Scanline.InvSlope(self, aux, edges[i])}]
            Y_list.append(y)
        return Y_list

    def Scanline(self):
        active_critical_points = []
        Y_list = Scanline.BoundBox(self)
        Ymin,Ymax = Scanline.GetMax(self, Y_list)
        scanline_points = []
        for y in range(Ymin, Ymax):
            for i in range(len(active_critical_points)):
                point = active_critical_points[i]
                point['xIntersection'] = point['invSlope']
                active_critical_points[i] = point

            for j in range(len(self.critical_points)):
                point = self.critical_points[j]
                if(self.edges[point['index']][1] == y): 
                    active_critical_points += [point]

            active_critical_points = sorted(active_critical_points, key = lambda x: x['xIntersection'])

            for i in range(len(active_critical_points)-1): #linhas entre intersecções encontradas para um y
                if i % 2 == 0:
                    new_points = Bresenham([active_critical_points[i]['xIntersection'],y], [active_critical_points[i+1]['xIntersection'],y])
                    scanline_points += [new_points]
        return scanline_points